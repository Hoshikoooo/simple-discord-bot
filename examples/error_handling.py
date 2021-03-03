import discord
from discord.ext import commands
from discord.ext.commands import BucketType
import traceback

description = '''
A basic bot featuring error handling for command errors
'''

# Here we are using regular intents, since they don't really matter for this example
intents = discord.Intents.default()

# Constructing the bot with a prefix, our above intents, and the description
bot = commands.Bot(command_prefix="!", intents=intents, description=description)

# Example command to showcase a potential error raised.
# The important ones to see are `MissingRequiredArgument` and `BadArgument`.
# `MissingRequiredArgument` will be raised when a required argument is not passed.
# Bad Argument will be raised in this case when the arg cannot be converted to an `int`.
@bot.command()
async def add(ctx, arg1: int, arg2: int):
    added = arg1 + arg2
    await ctx.send("{} + {} = {}".format(arg1, arg2, added))

# This command showcases the `is_owner` check, which will raise `commands.NotOwner` if the user doesn't own the bot.
@commands.is_owner()
@bot.command()
async def owner_check(ctx):
    await ctx.send("{} you do own this bot!".format(ctx.author.name))

# Here is a command with a cooldown.
# The syntax for cooldown is rate / per / type.
# Here we are doing 1 per 5 seconds per member.
@commands.cooldown(1, 5, BucketType.member)
@bot.command()
async def cooldown_example(ctx):
    await ctx.send("{}, you are not on cooldown!".format(ctx.author))

# Here we are **overriding** on_command_error.
# You can also use `bot.listen()` if you prefer not to override it, though there isn't a difference here.
# The event takes 2 args, `ctx` and `error`.
@bot.event
async def on_command_error(ctx, error):
    # Check if the command has a local handler.
    if ctx.command.has_error_handler():
        return

    # Check for ctx.cog and return if it has a local handler.
    elif ctx.cog:
        if ctx.cog.has_error_handler():
            return

    # The errors below are in a format that is readable, so we can just call `str` on them.
    readable_errors = (
        commands.BadArgument,
        commands.MissingRequiredArgument,
        commands.NotOwner
    )

    # The error may sometimes be wrapped in `CommandInvokeError`, which would cause our `isinstance` to fail,
    # to fix this, we unwrap the error.
    if isinstance(error, commands.CommandInvokeError):
        error = error.original

    # We use isinstance to check the type of error. 
    if isinstance(error, commands.CommandNotFound):
        # We don't really care if the command is not found, so we can just return.
        return
    
    # Checking for our readable errors and then calling `str` on them.
    elif isinstance(error, readable_errors):
        await ctx.send(str(error))

    # Here we send a custom error message if the user is on cooldown.
    # We also format the cooldown seconds to 2 digits.
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send("You are on cooldown! Please wait `{}` seconds".format(round(error.retry_after, 2)))

    # If the error isn't picked up by any of our other checks, then we should just print it.
    # **NOTE**: This error is *not* being raised. It is being printed.
    else:
        traceback.print_exc()

# Run the bot. You should really read the token from a configuration file.
bot.run("TOKEN HERE")