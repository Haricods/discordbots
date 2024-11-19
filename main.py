import discord
import os
from discord.ext import commands
from discord import Intents, message

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=intents)


@client.event
async def on_ready():
  print("Bot is ready to rock as {0.user}".format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith("!hello"):
    await message.channel.send("Hello Friend!")


my_secret = os.environ['TOKEN']
client.run(my_secret)
