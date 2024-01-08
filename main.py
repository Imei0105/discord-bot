import discord
import os

from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print("The bot is ready, and online!")

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return
  if msg.content.startswith("$help"):
    await msg.channel.send("may I help you?")

try:
  keep_alive()
  client.run(os.environ.get('TOKEN'))
except Exception as err:
  raise err
