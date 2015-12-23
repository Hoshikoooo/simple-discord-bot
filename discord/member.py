# -*- coding: utf-8 -*-

"""
The MIT License (MIT)

Copyright (c) 2015 Rapptz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from .user import User
from .utils import parse_time
from .game import Game

class Member(User):
    """Represents a Discord member to a :class:`Server`.

    This is a subclass of :class:`User` that extends more functionality
    that server members have such as roles and permissions.

    Instance attributes:

    .. attribute:: deaf

        A boolean that specifies if the member is currently deafened by the server.
    .. attribute:: mute

        A boolean that specifies if the member is currently muted by the server.
    .. attribute:: self_mute

        A boolean that specifies if the member is currently muted by their own accord.
    .. attribute:: self_deaf

        A boolean that specifies if the member is currently deafened by their own accord.
    .. attribute:: is_afk

        A boolean that specifies if the member is currently in the AFK channel in the server.
    .. attribute:: voice_channel

        A voice :class:`Channel` that the member is currently connected to. None if the member
        is not currently in a voice channel.
    .. attribute:: roles

        A list of :class:`Role` that the member belongs to. Note that the first element of this
        list is always the default '@everyone' role.
    .. attribute:: joined_at

        A datetime object that specifies the date and time in UTC that the member joined the server for
        the first time.
    .. attribute:: status

        A string that denotes the user's status. Can be 'online', 'offline' or 'idle'.
    .. attribute:: game

        A dictionary representing the game that the user is currently playing. None if no game is being played.
    .. attribute:: server

        The :class:`Server` that the member belongs to.
    """

    def __init__(self, deaf, joined_at, user, roles, mute, **kwargs):
        super(Member, self).__init__(**user)
        self.deaf = deaf
        self.mute = mute
        self.joined_at = parse_time(joined_at)
        self.roles = roles
        self.status = 'offline'
        game = kwargs.get('game', None)
        self.game = game and Game(**game)
        self.server = kwargs.get('server', None)
        self.update_voice_state(mute=mute, deaf=deaf)

    def update_voice_state(self, **kwargs):
        self.self_mute = kwargs.get('self_mute', False)
        self.self_deaf = kwargs.get('self_deaf', False)
        self.is_afk = kwargs.get('suppress', False)
        self.mute = kwargs.get('mute', False)
        self.deaf = kwargs.get('deaf', False)
        old_channel = getattr(self, 'voice_channel', None)
        self.voice_channel = kwargs.get('voice_channel')

        if old_channel is None and self.voice_channel is not None:
            # we joined a channel
            self.voice_channel.voice_members.append(self)
        elif old_channel is not None:
            try:
                # we either left a channel or we switched channels
                old_channel.voice_members.remove(self)
            except ValueError:
                pass
            finally:
                # we switched channels
                if self.voice_channel is not None:
                    self.voice_channel.voice_members.append(self)

