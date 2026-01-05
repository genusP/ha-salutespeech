from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SynthesisRequest(_message.Message):
    __slots__ = ("text", "audio_encoding", "language", "content_type", "voice")
    class AudioEncoding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AUDIO_ENCODING_UNSPECIFIED: _ClassVar[SynthesisRequest.AudioEncoding]
        PCM_S16LE: _ClassVar[SynthesisRequest.AudioEncoding]
        OPUS: _ClassVar[SynthesisRequest.AudioEncoding]
        WAV: _ClassVar[SynthesisRequest.AudioEncoding]
    AUDIO_ENCODING_UNSPECIFIED: SynthesisRequest.AudioEncoding
    PCM_S16LE: SynthesisRequest.AudioEncoding
    OPUS: SynthesisRequest.AudioEncoding
    WAV: SynthesisRequest.AudioEncoding
    class ContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TEXT: _ClassVar[SynthesisRequest.ContentType]
        SSML: _ClassVar[SynthesisRequest.ContentType]
    TEXT: SynthesisRequest.ContentType
    SSML: SynthesisRequest.ContentType
    TEXT_FIELD_NUMBER: _ClassVar[int]
    AUDIO_ENCODING_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    VOICE_FIELD_NUMBER: _ClassVar[int]
    text: str
    audio_encoding: SynthesisRequest.AudioEncoding
    language: str
    content_type: SynthesisRequest.ContentType
    voice: str
    def __init__(self, text: _Optional[str] = ..., audio_encoding: _Optional[_Union[SynthesisRequest.AudioEncoding, str]] = ..., language: _Optional[str] = ..., content_type: _Optional[_Union[SynthesisRequest.ContentType, str]] = ..., voice: _Optional[str] = ...) -> None: ...

class SynthesisResponse(_message.Message):
    __slots__ = ("data", "audio_duration")
    DATA_FIELD_NUMBER: _ClassVar[int]
    AUDIO_DURATION_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    audio_duration: _duration_pb2.Duration
    def __init__(self, data: _Optional[bytes] = ..., audio_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
