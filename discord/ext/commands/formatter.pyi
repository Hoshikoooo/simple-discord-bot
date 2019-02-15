from .bot import Bot
from .core import Command
from .context import Context

from typing import Any, Union, List, Iterable, Tuple

class Paginator:
    prefix: str
    suffix: str
    max_size: int

    def __init__(self, prefix: str = ..., suffix: str = ..., max_size: int = ...) -> None: ...

    def add_line(self, line: str = ..., *, empty: bool = ...) -> None: ...

    def close_page(self) -> None: ...

    @property
    def pages(self) -> List[str]: ...

    def __repr__(self) -> str: ...


class HelpFormatter:
    show_hidden: bool
    show_check_failure: bool
    width: int
    commands_heading: str
    no_category: str
    context: Context
    command: Union[Command, Bot]

    def __init__(self, show_hidden: bool = ..., show_check_failure: bool = ..., width: int = ...,
                 commands_heading: str = ..., no_category: str = ...) -> None: ...

    def has_subcommands(self) -> bool: ...

    def is_bot(self) -> bool: ...

    def is_cog(self) -> bool: ...

    def shorten(self, text: str) -> str: ...

    @property
    def max_name_size(self) -> int: ...

    @property
    def clean_prefix(self) -> str: ...

    def get_command_signature(self) -> str: ...

    def get_ending_note(self) -> str: ...

    async def filter_command_list(self) -> Iterable[Tuple[str, Command]]: ...

    async def format_help_for(self, ctx: Context, command_or_bot: Union[Command, Bot]) -> List[Any]: ...

    async def format(self) -> List[Any]: ...
