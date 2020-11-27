"""Uses a messages to add and remove roles through reactions."""

import discord
from discord.ext import commands

# This bot requires the members and reactions intensions.
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), intents=intents)

role_message_id = 0  # ID of message that can be reacted to to add role
emoji_to_role = {
    "👍": 0,  # ID of role associated with thumbs up emoji
    "test": 0  # ID of role associated with custom emoji 'test'
}

@bot.event
async def on_raw_reaction_add(payload):
    """Gives a role based on a reaction emoji."""
    # Make sure that the message the user is reacting to is the one we care about
    if payload.message_id != role_message_id:
        return

    try:
        role_id = emoji_to_role[str(payload.emoji)]
    except KeyError:
        # If the emoji isn't the one we care about then exit as well.
        return

    guild = bot.get_guild(payload.guild_id)
    if guild is None:
        # Check if we're still in the guild and it's cached.
        return

    role = guild.get_role(role_id)
    if role is None:
        # Make sure the role still exists and is valid.
        return

    try:
        # Finally add the role
        await payload.member.add_roles(role)
    except discord.HTTPException:
        # If we want to do something in case of errors we'd do it here.
        pass

@bot.event
async def on_raw_reaction_remove(payload):
    """Removes a role based on a reaction emoji."""
    # Make sure that the message the user is reacting to is the one we care about
    if payload.message_id == role_message_id:
        return

    try:
        role_id = emoji_to_role[str(payload.emoji)]
    except KeyError:
        # If the emoji isn't the one we care about then exit as well.
        return

    guild = bot.get_guild(payload.guild_id)
    if guild is None:
        # Check if we're still in the guild and it's cached.
        return

    role = guild.get_role(role_id)
    if role is None:
        # Make sure the role still exists and is valid.
        return

    member = guild.get_member(payload.user_id)
    if member is None:
        # Makes sure the member still exists and is valid
        return

    try:
        # Finally, remove the role
        await member.remove_roles(role)
    except discord.HTTPException:
        # If we want to do something in case of errors we'd do it here.
        pass

bot.run("token")
