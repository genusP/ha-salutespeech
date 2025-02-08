import logging
from collections.abc import AsyncIterable

from .salute_speech import SaluteSpeechCloud
import voluptuous as vol

from homeassistant.components import stt
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    async_add_entities([SaluteSTT(hass, config_entry)])

class SaluteSTT(stt.SpeechToTextEntity):
    _cloud: SaluteSpeechCloud

    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry) -> None:
        
        self.language: str = "ru"

        self._attr_name = "Salute STT"
        self._attr_unique_id = f"{config_entry.entry_id[:7]}-stt"
        self._cloud = config_entry.runtime_data


    @property
    def supported_languages(self) -> list[str]:
        return [self.language]

    @property
    def supported_formats(self) -> list[stt.AudioFormats]:
        return [stt.AudioFormats.WAV]

    @property
    def supported_codecs(self) -> list[stt.AudioCodecs]:
        return [stt.AudioCodecs.PCM]

    @property
    def supported_bit_rates(self) -> list[stt.AudioBitRates]:
        return [stt.AudioBitRates.BITRATE_16]

    @property
    def supported_sample_rates(self) -> list[stt.AudioSampleRates]:
        return [stt.AudioSampleRates.SAMPLERATE_16000]

    @property
    def supported_channels(self) -> list[stt.AudioChannels]:
        return [stt.AudioChannels.CHANNEL_MONO]

    async def async_process_audio_stream(
        self, metadata: stt.SpeechMetadata, stream: AsyncIterable[bytes]
    ) -> stt.SpeechResult:
        _LOGGER.debug("process_audio_stream start")

        # audio = b""
        # async for chunk in stream:
        #     audio += chunk

        # _LOGGER.debug(f"process_audio_stream transcribe: {len(audio)} bytes")

        # async with self.model_lock:
        #     segments, _info = self.model.transcribe(
        #         audio, beam_size=self.beam_size, language=self.language
        #     )

        text = await self._cloud.recognize(stream) # self.auth#" ".join(segment.text for segment in segments)

        _LOGGER.info(f"process_audio_stream end: {text}")

        return stt.SpeechResult(text, stt.SpeechResultState.SUCCESS)
