import discord, json, locale
from discord.ext import commands
from datetime import datetime, timedelta
from asyncio import *
from sound import setup
from boot import access
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
#locale.setlocale(locale.LC_TIME, 'ru_RU')
bot = commands.Bot(command_prefix="~", intents=intents, help_command=None)
t=access()["bro"]
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    return
    print("Started without errors!")
setup(bot)
bot.run(t)