import discord
import asyncio
from discord.ext import commands

description = """Example bot to show the use of hybrid commands.
These can be used as both application (slash) and message (prefix) commands
"""
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="?", intents=intents, description=description)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")


@bot.hybrid_command()
@bot.is_owner()
async def synctree(ctx: commands.Context, *guild_ids: int):
    """
    Sync the application commands tree
    This must also be done with hybrid commands, to ensure that the application commands also work
    """
    if not guild_ids:
        await bot.tree.sync()  # sync global commands
    else:
        for g in guild_ids:
            await bot.tree.sync(guild=discord.Object(id=g))


@bot.hybrid_command()
async def hello(ctx: commands.Context) -> None:
    """Says hello"""
    if ctx.interaction is not None:  # check if application commands are being used
        await ctx.send("Hello from slash commands!")
    else:
        await ctx.send("Hello from prefix commands!")


@bot.hybrid_command(aliases=["say", "repeat"])
async def say(ctx: commands.Context, *, msg: str) -> None:
    """Repeat the given message"""
    await ctx.send(msg)


@bot.hybrid_command()
async def dice(ctx: commands.Context, fmt: str = "1d6") -> None:
    """
    Rolls a dice in NdN format
    Example of optional arguments (fmt defaults to 1d6)
    """
    try:
        rolls, limit = map(int, fmt.lower().split("d"))
    except Exception:
        await ctx.send("Format has to be in NdN!")
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


# IMPORTANT: You mustn't hard code your token in a production bot
# Treat it like a password - if someone gets hold of it, they can use it to access your bot and do potentially harmful things with it
# It's recommended to either use a .env file (python-dotenv) or a config.json file under .gitignore
TOKEN = "..."


async def main() -> None:
    async with bot:
        await bot.start(TOKEN)


if __name__ == "__main__":
    asyncio.run(main())
