import discord
import os
from discord.ext import commands
from discord import Intents, message
import requests
import json
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=intents)

comms = ["!hello", "!creator", "!joke", "!help", "!commands"]


@client.event
async def on_ready():
  print("Bot is ready to rock as {0.user}".format(client))


async def Tell_joke():
  jokes = requests.get("https://official-joke-api.appspot.com/random_joke")
  json_data = json.loads(jokes.text)
  ques = json_data["setup"]
  ans = json_data["punchline"]

  return (ques + " " + " -" + ans)


def comms_func():
  for comms in range(4):
    print(comms)


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith("!hello"):
    await message.channel.send("Hello Friend!")
  joking = await Tell_joke()
  if message.content.startswith("!joke"):
    await message.channel.send(joking)
  if message.content.startswith("!help"):
    await message.channel.send("I tell jokes -start typing '!joke'")
  if message.content.startswith("!bye"):
    await message.channel.send("Bye Friend!")
  if message.content.startswith("!creator"):
    await message.channel.send(
        "I have been created by 'Bean Bag' aka ' mighty8005 '")

keep_alive()
my_secret = os.environ['TOKEN']
client.run(my_secret)
