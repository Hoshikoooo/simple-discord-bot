import datetime
import abc

from typing import Any, Optional, Union, List, overload

from .colour import Colour
from .enums import ActivityType
from .types import RawActivityDict, RawTimestampsDict, RawActivityAssetsDict, RawActivityPartyDict, RawSpotifyActivityDict

class _ActivityTag:
    ...

class Activity(_ActivityTag):
    application_id: str
    name: str
    url: str
    type: ActivityType
    state: str
    details: str
    timestamps: RawTimestampsDict
    assets: RawActivityAssetsDict
    party: RawActivityPartyDict
    flags: int
    sync_id: Optional[str]
    session_id: Optional[str]

    def __init__(self, *, state: Optional[str] = ..., details: Optional[str] = ...,
                 timestamps: RawTimestampsDict = ..., assets: RawActivityAssetsDict = ...,
                 party: RawActivityPartyDict = ...,
                 application_id: Optional[str] = ..., name: Optional[str] = ...,
                 url: Optional[str] = ..., flags: int = ..., sync_id: Optional[str] = ...,
                 session_id: Optional[str] = ..., type: ActivityType = ...) -> None: ...

    def to_dict(self) -> RawActivityDict: ...

    @property
    def start(self) -> Optional[datetime.datetime]: ...

    @property
    def end(self) -> Optional[datetime.datetime]: ...

    @property
    def large_image_url(self) -> Optional[str]: ...

    @property
    def small_image_url(self) -> Optional[str]: ...

    @property
    def large_image_text(self) -> Optional[str]: ...

    @property
    def small_image_text(self) -> Optional[str]: ...

class Game(_ActivityTag):
    name: str
    _start: int
    _end: int

    @overload
    def __init__(self, name: str, *, timestamps: RawTimestampsDict) -> None: ...

    @overload
    def __init__(self, name: str, *, start: Optional[datetime.datetime] = ..., end: Optional[datetime.datetime] = ...) -> None: ...

    @property
    def type(self) -> ActivityType: ...

    @property
    def start(self) -> Optional[datetime.datetime]: ...

    @property
    def end(self) -> Optional[datetime.datetime]: ...

    def __str__(self) -> str: ...

    def __repr__(self) -> str: ...

    def to_dict(self) -> RawActivityDict: ...

    def __eq__(self, other: Any) -> bool: ...

    def __ne__(self, other: Any) -> bool: ...

    def __hash__(self) -> int: ...

class Streaming(_ActivityTag):
    name: str
    url: str
    details: Optional[str]
    assets: RawActivityAssetsDict

    def __init__(self, *, name: str, url: str, details: Optional[str] = ..., assets: RawActivityAssetsDict = ...) -> None: ...

    @property
    def type(self) -> ActivityType: ...

    def __str__(self) -> str: ...

    def __repr__(self) -> str: ...

    @property
    def twitch_name(self) -> Optional[str]: ...

    def to_dict(self) -> RawActivityDict: ...

    def __eq__(self, other: Any) -> bool: ...

    def __ne__(self, other: Any) -> bool: ...

    def __hash__(self) -> int: ...

class Spotify:
    _state: Optional[str]
    _details: Optional[str]
    _timestamps: RawTimestampsDict
    _assets: RawActivityAssetsDict
    _party: RawActivityPartyDict
    _sync_id: str
    _session_id: str

    @property
    def type(self) -> ActivityType: ...

    @property
    def colour(self) -> Colour: ...

    @property
    def color(self) -> Colour: ...

    def to_dict(self) -> RawSpotifyActivityDict: ...

    @property
    def name(self) -> str: ...

    def __eq__(self, other: Any) -> bool: ...

    def __ne__(self, other: Any) -> bool: ...

    def __hash__(self) -> int: ...

    def __str__(self) -> str: ...

    def __repr__(self) -> str: ...

    @property
    def title(self) -> Optional[str]: ...

    @property
    def artists(self) -> List[str]: ...

    @property
    def artist(self) -> str: ...

    @property
    def album(self) -> str: ...

    @property
    def album_cover_url(self) -> str: ...

    @property
    def track_id(self) -> str: ...

    @property
    def start(self) -> datetime.datetime: ...

    @property
    def end(self) -> datetime.datetime: ...

    @property
    def duration(self) -> datetime.timedelta: ...

    @property
    def party_id(self) -> str: ...

def create_activity(data: Optional[RawActivityDict]) -> Optional[Union[Activity, Game, Streaming, Spotify]]: ...
