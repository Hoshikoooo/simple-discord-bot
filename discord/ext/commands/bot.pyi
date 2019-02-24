import discord
import asyncio
import aiohttp

from .core import GroupMixin, Command
from .context import Context
from .formatter import HelpFormatter
from .cog import Cog

from typing import Any, Optional, Union, Callable, Coroutine, List, Tuple, Dict, Set, TypeVar, Type, overload


CommandPrefix = Union[
    str,
    Callable[[Bot, discord.Message], Union[str, Coroutine[Any, Any, str]]]]


def when_mentioned(bot: Bot, msg: discord.Message) -> List[str]: ...


def when_mentioned_or(*prefixes: str) -> Callable[[Bot, discord.Message], List[str]]: ...

CT = TypeVar('CT', bound=Context)
_OT = TypeVar('_OT', bound=Context)

_CoroType = Callable[..., Coroutine[Any, Any, Any]]
_C = TypeVar('_C', bound=_CoroType)


class BotBase(GroupMixin[CT]):
    command_prefix: CommandPrefix
    cogs: Dict[str, Cog[CT]]
    extra_events: Dict[str, List[Callable[..., Coroutine[Any, Any, None]]]]
    extensions: Dict[str, Any]
    case_insensitive: bool
    description: str
    formatter: HelpFormatter  # noqa
    pm_help: bool
    help_attrs: Dict[str, Any]
    command_not_found: str
    command_has_no_subcommands: str
    owner_id: Optional[int]

    def __init__(self, command_prefix: CommandPrefix, formatter: Optional[HelpFormatter] = ...,
                 description: Optional[str] = ..., pm_help: bool = ..., **options: Any) -> None: ...

    def dispatch(self, event: str, *args: Any, **kwargs: Any) -> None: ...

    async def close(self) -> None: ...

    async def on_command_error(self, context: Any, exception: Exception) -> None: ...

    def check(self, func: _C) -> _C: ...

    def add_check(self, func: _CoroType, *, call_once: bool = ...) -> None: ...

    def remove_check(self, func: _CoroType, *, call_once: bool = ...) -> None: ...

    def check_once(self, func: _C) -> _C: ...

    async def can_run(self, ctx: CT, *, call_once: bool = ...) -> None: ...

    async def is_owner(self, user: Union[discord.User, discord.Member]) -> bool: ...

    def before_invoke(self, coro: _C) -> _C: ...

    def after_invoke(self, coro: _C) -> _C: ...

    def add_listener(self, func: _CoroType, name: Optional[str] = ...) -> None: ...

    def remove_listener(self, func: _CoroType, name: Optional[str] = ...) -> None: ...

    def listen(self, name: Optional[str] = ...) -> Callable[[_C], _C]: ...

    def add_cog(self, cog: Cog[CT]) -> None: ...

    def get_cog(self, name: str) -> Cog[CT]: ...

    def remove_cog(self, name: str) -> None: ...

    def load_extension(self, name: str) -> None: ...

    def unload_extension(self, name: str) -> None: ...

    async def get_prefix(self, message: discord.Message) -> Union[List[str], str]: ...

    @overload
    async def get_context(self, message: discord.Message) -> CT: ...

    @overload
    async def get_context(self, message: discord.Message, *, cls: Type[_OT]) -> _OT: ...

    async def invoke(self, ctx: CT) -> None: ...

    async def process_commands(self, message: discord.Message) -> None: ...

    async def on_message(self, message: discord.Message) -> None: ...


class Bot(BotBase[CT], discord.Client):
    def __init__(self, command_prefix: CommandPrefix, formatter: Optional[HelpFormatter] = ...,
                 description: Optional[str] = ..., pm_help: bool = ..., *,
                 case_insensitive: bool = ..., loop: Optional[asyncio.AbstractEventLoop] = ...,
                 shard_id: Optional[int] = ..., shard_count: Optional[int] = ...,
                 connector: aiohttp.BaseConnector = ..., proxy: Optional[str] = ...,
                 proxy_auth: Optional[aiohttp.BasicAuth] = ..., max_messages: Optional[int] = ...,
                 fetch_offline_members: bool = ..., status: Optional[discord.Status] = ...,
                 activity: Optional[Union[discord.Activity, discord.Game, discord.Streaming]] = ...,
                 heartbeat_timeout: float = ..., **options: Any) -> None: ...


class AutoShardedBot(BotBase[CT], discord.AutoShardedClient):
    def __init__(self, command_prefix: CommandPrefix, formatter: Optional[HelpFormatter] = ...,
                 description: Optional[str] = ..., pm_help: bool = ..., *,
                 case_insensitive: bool = ..., loop: Optional[asyncio.AbstractEventLoop] = ...,
                 shard_ids: Optional[Union[List[int], Tuple[int]]] = ..., shard_count: Optional[int] = ...,
                 connector: aiohttp.BaseConnector = ..., proxy: Optional[str] = ...,
                 proxy_auth: Optional[aiohttp.BasicAuth] = ..., max_messages: Optional[int] = ...,
                 fetch_offline_members: bool = ..., status: Optional[discord.Status] = ...,
                 activity: Optional[Union[discord.Activity, discord.Game, discord.Streaming]] = ...,
                 heartbeat_timeout: float = ..., **options: Any) -> None: ...
