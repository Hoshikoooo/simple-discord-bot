import threading

from .voice_client import VoiceClient

from typing import Union, Optional, BinaryIO, ClassVar, overload


class AudioSource:
    def read(self) -> bytes: ...

    def is_opus(self) -> bool: ...

    def cleanup(self) -> None: ...

    def __del__(self) -> None: ...


class PCMAudio(AudioSource):
    stream: BinaryIO

    def __init__(self, stream: BinaryIO) -> None: ...

    def read(self) -> bytes: ...


class FFmpegPCMAudio(AudioSource):
    @overload
    def __init__(self, source: BinaryIO, *, executable: str = ..., pipe: bool,
                 stderr: Optional[BinaryIO] = ..., before_options: Optional[str] = ...,
                 options: Optional[str] = ...) -> None: ...
    @overload
    def __init__(self, source: str, *, executable: str = ..., stderr: Optional[BinaryIO] = ...,
                 before_options: Optional[str] = ..., options: Optional[str] = ...) -> None: ...

    def read(self) -> bytes: ...

    def cleanup(self) -> None: ...


class PCMVolumeTransformer(AudioSource):
    original: AudioSource
    volume: float

    def __init__(self, original: AudioSource, volume: float = ...) -> None: ...

    def cleanup(self) -> None: ...

    def read(self) -> bytes: ...

class AudioPlayer(threading.Thread):
    DELAY: ClassVar[float]

    source: AudioSource
    client: VoiceClient

    def run(self) -> None: ...

    def stop(self) -> None: ...

    def pause(self) -> None: ...

    def resume(self) -> None: ...

    def is_playing(self) -> bool: ...

    def is_paused(self) -> bool: ...
