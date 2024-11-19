import discord
import os
from discord.ext import commands
from discord import Intents, message
import requests
import json

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=intents)


@client.event
async def on_ready():
  print("Bot is ready to rock as {0.user}".format(client))

async def Tell_joke():
  jokes = requests.get("https://official-joke-api.appspot.com/random_joke")
  json_data = json.loads(jokes.text)
  ques = json_data["setup"]
  ans = json_data["punchline"]

  return (ques +" "+ " -" + ans )


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith("!hello"):
    await message.channel.send("Hello Friend!")
  joking = await Tell_joke()
  if message.content.startswith("!joke"):
    await message.channel.send(joking)


  

my_secret = os.environ['TOKEN']
client.run(my_secret)
