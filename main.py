import discord
import os
from discord.ext import commands 
from discord import Intents
intents = discord.Intents.default()

client = commands.Bot(command_prefix=".",intents=intents)

@client.event
async def on_ready():
  print("Bot is ready to rock as {0.user}".format(client))
  
my_secret = os.environ['TOKEN']
client.run(my_secret)