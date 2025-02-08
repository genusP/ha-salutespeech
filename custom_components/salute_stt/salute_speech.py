import asyncio
from collections.abc import AsyncIterable
import datetime
from http import HTTPStatus
import json
import logging
import os
import uuid

import grpc

from . import recognition_pb2
from . import recognition_pb2_grpc
from . import synthesis_pb2
from . import synthesis_pb2_grpc

from .const import API_AUTH_ENDPOINT
from homeassistant.helpers.aiohttp_client import async_get_clientsession

CHUNK_SIZE = 2048
SLEEP_TIME = 0.1

_LOGGER = logging.getLogger(__name__)

async def generate_audio_chunks(options:recognition_pb2.RecognitionOptions, stream: AsyncIterable[bytes], chunk_size=CHUNK_SIZE, sleep_time=SLEEP_TIME):
    yield recognition_pb2.RecognitionRequest(options=options)
    audio=b''
    async for data in stream:
        audio += data
        if(len(audio) + len(data) > chunk_size):
            yield recognition_pb2.RecognitionRequest(audio_chunk=audio)
            audio=b''
            await asyncio.sleep(sleep_time)
    if len(audio) > 0:
        yield recognition_pb2.RecognitionRequest(audio_chunk=audio)

def get_cert():
    dir=os.path.dirname(os.path.abspath(__file__))
    path=os.path.join(dir, 'russian_trusted_sub_ca_pem.crt')
    _LOGGER.warn('cert path: '+ path)
    try:
      f = open(path, 'rb')
      return f.read()
    finally:
        f.close()

class SaluteSpeechCloud:
    def __init__(self, hass, auth_data):
        self._http_client = async_get_clientsession(hass, False)
        self._auth_data = auth_data
        self._expire_at = None
        self._channel = None
        self._current_token = None
        self._options = recognition_pb2.RecognitionOptions(
            audio_encoding=recognition_pb2.RecognitionOptions.PCM_S16LE, 
            sample_rate=16000)
        self._cert = None

    async def recognize(self, stream: AsyncIterable[bytes]) -> str:
        channel = await self.get_channel()
        stub = recognition_pb2_grpc.SmartSpeechStub(channel)

        con = stub.Recognize(generate_audio_chunks(self._options, stream))

        async for resp in con:
            if not resp.eou:
                _LOGGER.debug('Got partial result:')
            else:
                text = ''
                for i, hyp in enumerate(resp.results):
                    _LOGGER.warn(hyp)
                    if i == 0:
                        text = hyp.normalized_text
                _LOGGER.debug('Got end-of-utterance result:'+text)
                return text

    async def synthesis(self, text:str, voice:str, rate:str):
        is_ssml = text.find('<speak>') != -1

        if rate is None:
            rate='24000'
    
        opt = synthesis_pb2.SynthesisRequest(
            text=text,
            content_type= synthesis_pb2.SynthesisRequest.SSML if is_ssml else synthesis_pb2.SynthesisRequest.TEXT,
            voice='{}_{}'.format(voice, rate)
        )

        channel = await self.get_channel()
        stub = synthesis_pb2_grpc.SmartSpeechStub(channel)
        resp = stub.Synthesize(opt)
        audio=b''
        async for chunk in resp:
            audio+=chunk.data
        # _LOGGER.warn(resp)
        # audio = resp.data

        return 'wav', audio

    
    def disconnect(self):
        if self._channel is not None:
            self._channel.close()
            self._channel = None
    
    async def get_channel(self) -> grpc.aio.Channel:
        if self._channel is None or self.is_token_expired():
            if self._channel is not None:
                await self._channel.close()
            if self._cert is None:
                self._cert = get_cert()
            _LOGGER.warn('create channell')
            ssl_cred = grpc.ssl_channel_credentials(root_certificates=self._cert)
            token = await self.get_auth_token()
            token_cred = grpc.access_token_call_credentials(token)

            self._channel = grpc.aio.secure_channel(
                'smartspeech.sber.ru',
                grpc.composite_channel_credentials(ssl_cred, token_cred),
            )
        return self._channel

    def is_token_expired(self) -> bool:
        return self._expire_at is None or self._expire_at < datetime.datetime.now()
    
    async def get_auth_token(self) -> str | None:
        _LOGGER.warn('get token')
        if not self.is_token_expired():
            return self._current_token
        async with asyncio.timeout(10):
            response = await self._http_client.post(
                url=API_AUTH_ENDPOINT,
                headers={
                    'Authorization': 'Basic {}'.format(self._auth_data),
                    'RqUID': str(uuid.uuid4()),
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                data={
                    'scope': 'SALUTE_SPEECH_PERS',
                }
            )

            if response.status != HTTPStatus.OK:
                error = await response.read()
                _LOGGER.error('Error %d on load URL %s. Response %s' % (response.status, response.url, error))
                return None

            data = await response.json()
            _LOGGER.warn('auth response: '+ json.dumps( data))

            self._current_token = data.get('access_token')
            expire_at = float(data.get("expires_at"))/1000
            self._expire_at = datetime.datetime.fromtimestamp(expire_at) - datetime.timedelta(seconds=5)
            return self._current_token
