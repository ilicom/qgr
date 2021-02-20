import discord # pip3 install discord.py
import time
from discord.ext import commands
import random

TOKEN = 'TOKEN'

# Префикс
client = commands.Bot( command_prefix = '!' )


@client.event
async def on_ready():
	print("Huibot Bot is ready")


@client.event
async def on_message( message ):
   user = message.author
   msg = message.content.lower()


   if not user.bot:
      await message.channel.send("хуй" + msg[-3:])


# Run
client.run(TOKEN)