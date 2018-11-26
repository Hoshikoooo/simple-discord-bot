import discord.abc
import datetime

from .activity import Activity, Game, Streaming, Spotify
from .enums import Status, DefaultAvatar
from .colour import Colour
from .message import Message
from .role import Role
from .permissions import Permissions
from .channel import VoiceChannel, GroupChannel, DMChannel
from .guild import Guild
from .relationship import Relationship
from .user import Profile

from typing import Any, Optional, List, Union

class VoiceState:
    deaf: bool
    mute: bool
    self_mute: bool
    self_deaf: bool
    afk: bool
    channel: Optional[Union[GroupChannel, VoiceChannel]]
    session_id: str

    def __repr__(self) -> str: ...


class Member(discord.abc.Messageable, discord.abc.User):
    roles: List[Role]
    joined_at: datetime.datetime
    status: Status
    activity: Union[Activity, Game, Streaming, Spotify]
    nick: Optional[str]
    guild: Guild

    # From discord.user.BaseUser
    name: str
    id: int
    discriminator: str
    avatar: Optional[str]
    bot: bool

    @property
    def avatar_url(self) -> str: ...

    def is_avatar_animated(self) -> bool: ...

    def avatar_url_as(self, *, format: Optional[str] = ..., static_format: str = ...,
                      size: int = ...) -> str: ...
    @property
    def default_avatar(self) -> DefaultAvatar: ...

    @property
    def default_avatar_url(self) -> str: ...
    # End from discord.user.BaseUser

    # From discord.user.User
    @property
    def created_at(self) -> datetime.datetime: ...

    @property
    def dm_channel(self) -> Optional[DMChannel]: ...

    async def create_dm(self) -> DMChannel: ...

    @property
    def relationship(self) -> Optional[Relationship]: ...

    def is_friend(self) -> bool: ...

    def is_blocked(self) -> bool: ...

    async def block(self) -> None: ...

    async def unblock(self) -> None: ...

    async def remove_friend(self) -> None: ...

    async def send_friend_request(self) -> None: ...

    async def profile(self) -> Profile: ...
    # End from discord.user.User

    def __str__(self) -> str: ...

    def __repr__(self) -> str: ...

    def __eq__(self, other: Any) -> bool: ...

    def __ne__(self, other: Any) -> bool: ...

    def __hash__(self) -> int: ...

    @property
    def colour(self) -> Colour: ...

    color = colour

    @property
    def mention(self) -> str: ...

    @property
    def display_name(self) -> str: ...

    def mentioned_in(self, message: Message) -> bool: ...

    def permissions_in(self, channel: discord.abc.GuildChannel) -> Permissions: ...

    @property
    def top_role(self) -> Role: ...

    @property
    def guild_permissions(self) -> Permissions: ...

    @property
    def voice(self) -> Optional[VoiceState]: ...

    async def ban(self, *, reason: Optional[str] = ..., delete_message_days: int = ...) -> None: ...

    async def unban(self, *, reason: Optional[str] = ...) -> None: ...

    async def kick(self, *, reason: Optional[str] = ...) -> None: ...

    async def edit(self, *, reason: Optional[str] = ..., nick: Optional[str] = ..., mute: bool = ...,
                   deafen: bool = ..., roles: List[Role] = ..., voice_channel: VoiceChannel = ...) -> None: ...

    async def move_to(self, channel: VoiceChannel, *, reason: Optional[str] = ...) -> None: ...

    async def add_roles(self, *roles: discord.abc.Snowflake, reason: Optional[str] = ..., atomic: bool = ...) -> None: ...

    async def remove_roles(self, *roles: discord.abc.Snowflake, reason: Optional[str] = ..., atomic: bool = ...) -> None: ...
