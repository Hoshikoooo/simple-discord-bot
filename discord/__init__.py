# -*- coding: utf-8 -*-

"""
Discord API Wrapper
~~~~~~~~~~~~~~~~~~~

A basic wrapper for the Discord API.

:copyright: (c) 2015 Rapptz
:license: MIT, see LICENSE for more details.

"""

__title__ = 'discord'
__author__ = 'Rapptz'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015 Rapptz'
__version__ = '0.9.1'
__build__ = 0x009010

from .client import Client
from .user import User
from .game import Game
from .channel import Channel, PrivateChannel
from .server import Server
from .member import Member
from .message import Message
from .errors import *
from .permissions import Permissions
from .role import Role
from .colour import Color, Colour
from .invite import Invite
from .object import Object
from . import utils

import logging

try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
