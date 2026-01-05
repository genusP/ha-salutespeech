import task_pb2 as _task_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecognitionRequest(_message.Message):
    __slots__ = ("options", "audio_chunk")
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_CHUNK_FIELD_NUMBER: _ClassVar[int]
    options: RecognitionOptions
    audio_chunk: bytes
    def __init__(self, options: _Optional[_Union[RecognitionOptions, _Mapping]] = ..., audio_chunk: _Optional[bytes] = ...) -> None: ...

class RecognitionResponse(_message.Message):
    __slots__ = ("results", "eou", "emotions_result", "processed_audio_start", "processed_audio_end", "backend_info", "channel")
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    EOU_FIELD_NUMBER: _ClassVar[int]
    EMOTIONS_RESULT_FIELD_NUMBER: _ClassVar[int]
    PROCESSED_AUDIO_START_FIELD_NUMBER: _ClassVar[int]
    PROCESSED_AUDIO_END_FIELD_NUMBER: _ClassVar[int]
    BACKEND_INFO_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[Hypothesis]
    eou: bool
    emotions_result: Emotions
    processed_audio_start: _duration_pb2.Duration
    processed_audio_end: _duration_pb2.Duration
    backend_info: BackendInfo
    channel: int
    def __init__(self, results: _Optional[_Iterable[_Union[Hypothesis, _Mapping]]] = ..., eou: bool = ..., emotions_result: _Optional[_Union[Emotions, _Mapping]] = ..., processed_audio_start: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., processed_audio_end: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., backend_info: _Optional[_Union[BackendInfo, _Mapping]] = ..., channel: _Optional[int] = ...) -> None: ...

class AsyncRecognizeRequest(_message.Message):
    __slots__ = ("options", "request_file_id")
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    options: RecognitionOptions
    request_file_id: str
    def __init__(self, options: _Optional[_Union[RecognitionOptions, _Mapping]] = ..., request_file_id: _Optional[str] = ...) -> None: ...

class RecognitionOptions(_message.Message):
    __slots__ = ("audio_encoding", "sample_rate", "language", "model", "hypotheses_count", "hints", "enable_profanity_filter", "enable_multi_utterance", "enable_partial_results", "no_speech_timeout", "max_speech_timeout", "channels_count", "insight_models")
    class AudioEncoding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AUDIO_ENCODING_UNSPECIFIED: _ClassVar[RecognitionOptions.AudioEncoding]
        PCM_S16LE: _ClassVar[RecognitionOptions.AudioEncoding]
        OPUS: _ClassVar[RecognitionOptions.AudioEncoding]
        MP3: _ClassVar[RecognitionOptions.AudioEncoding]
        FLAC: _ClassVar[RecognitionOptions.AudioEncoding]
        ALAW: _ClassVar[RecognitionOptions.AudioEncoding]
        MULAW: _ClassVar[RecognitionOptions.AudioEncoding]
    AUDIO_ENCODING_UNSPECIFIED: RecognitionOptions.AudioEncoding
    PCM_S16LE: RecognitionOptions.AudioEncoding
    OPUS: RecognitionOptions.AudioEncoding
    MP3: RecognitionOptions.AudioEncoding
    FLAC: RecognitionOptions.AudioEncoding
    ALAW: RecognitionOptions.AudioEncoding
    MULAW: RecognitionOptions.AudioEncoding
    AUDIO_ENCODING_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    HYPOTHESES_COUNT_FIELD_NUMBER: _ClassVar[int]
    HINTS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PROFANITY_FILTER_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MULTI_UTTERANCE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PARTIAL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    NO_SPEECH_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    MAX_SPEECH_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_COUNT_FIELD_NUMBER: _ClassVar[int]
    INSIGHT_MODELS_FIELD_NUMBER: _ClassVar[int]
    audio_encoding: RecognitionOptions.AudioEncoding
    sample_rate: int
    language: str
    model: str
    hypotheses_count: int
    hints: Hints
    enable_profanity_filter: bool
    enable_multi_utterance: bool
    enable_partial_results: bool
    no_speech_timeout: _duration_pb2.Duration
    max_speech_timeout: _duration_pb2.Duration
    channels_count: int
    insight_models: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, audio_encoding: _Optional[_Union[RecognitionOptions.AudioEncoding, str]] = ..., sample_rate: _Optional[int] = ..., language: _Optional[str] = ..., model: _Optional[str] = ..., hypotheses_count: _Optional[int] = ..., hints: _Optional[_Union[Hints, _Mapping]] = ..., enable_profanity_filter: bool = ..., enable_multi_utterance: bool = ..., enable_partial_results: bool = ..., no_speech_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., max_speech_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., channels_count: _Optional[int] = ..., insight_models: _Optional[_Iterable[str]] = ...) -> None: ...

class Hints(_message.Message):
    __slots__ = ("words", "enable_letters", "eou_timeout")
    WORDS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_LETTERS_FIELD_NUMBER: _ClassVar[int]
    EOU_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    words: _containers.RepeatedScalarFieldContainer[str]
    enable_letters: bool
    eou_timeout: _duration_pb2.Duration
    def __init__(self, words: _Optional[_Iterable[str]] = ..., enable_letters: bool = ..., eou_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class Hypothesis(_message.Message):
    __slots__ = ("text", "normalized_text", "start", "end", "word_alignments")
    class WordAlignment(_message.Message):
        __slots__ = ("word", "start", "end")
        WORD_FIELD_NUMBER: _ClassVar[int]
        START_FIELD_NUMBER: _ClassVar[int]
        END_FIELD_NUMBER: _ClassVar[int]
        word: str
        start: _duration_pb2.Duration
        end: _duration_pb2.Duration
        def __init__(self, word: _Optional[str] = ..., start: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., end: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    TEXT_FIELD_NUMBER: _ClassVar[int]
    NORMALIZED_TEXT_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    WORD_ALIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    text: str
    normalized_text: str
    start: _duration_pb2.Duration
    end: _duration_pb2.Duration
    word_alignments: _containers.RepeatedCompositeFieldContainer[Hypothesis.WordAlignment]
    def __init__(self, text: _Optional[str] = ..., normalized_text: _Optional[str] = ..., start: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., end: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., word_alignments: _Optional[_Iterable[_Union[Hypothesis.WordAlignment, _Mapping]]] = ...) -> None: ...

class Emotions(_message.Message):
    __slots__ = ("positive", "neutral", "negative")
    POSITIVE_FIELD_NUMBER: _ClassVar[int]
    NEUTRAL_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_FIELD_NUMBER: _ClassVar[int]
    positive: float
    neutral: float
    negative: float
    def __init__(self, positive: _Optional[float] = ..., neutral: _Optional[float] = ..., negative: _Optional[float] = ...) -> None: ...

class BackendInfo(_message.Message):
    __slots__ = ("model_name", "model_version", "server_version")
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    MODEL_VERSION_FIELD_NUMBER: _ClassVar[int]
    SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    model_name: str
    model_version: str
    server_version: str
    def __init__(self, model_name: _Optional[str] = ..., model_version: _Optional[str] = ..., server_version: _Optional[str] = ...) -> None: ...
