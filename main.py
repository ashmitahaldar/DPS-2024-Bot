import discord
import os
import requests
import json
import random
from replit import db
from keepalive import keep_alive
import kekreply

client = discord.Client()

#Kek Replies Word lists
kek_words = kekreply.kek_words
kek_replies = kekreply.starter_kek_replies

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return quote

  
@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
    
  msg = message.content

  if message.content.startswith('$hello'):
    await message.channel.send('Hello! I\'m the 2024 bot UwU')

  if message.content.startswith('$quote'):
    quote = get_quote()
    await message.channel.send(quote)
  
  
  # Kek Reply Code
  # This checks whether the message is sent in the Bot CMDS, Media or Shitpost channels and then send the reply.
  if any(word in msg for word in kek_words):
    if (message.channel.id == kekreply.botcmdsId):
      await message.channel.send(random.choice(kek_replies))
    elif (message.channel.id == kekreply.mediaId):
      await message.channel.send(random.choice(kek_replies))
    elif (message.channel.id == kekreply.shitpostId):
      await message.channel.send(random.choice(kek_replies))

  # $KekReply words list - Sends a list of the trigger words, list in kekreply.py
  if msg.startswith("$KekReply words list"):
    await message.channel.send(kek_words)

  # $KekReply reply list - Sends a list of the replies, list in kekreply.py
  if msg.startswith("$KekReply reply list"):
    await message.channel.send(kek_replies)

  # $KekReply database delete - Clears database, temporary(?)
  if msg.startswith("$KekReply database delete"):
    del db["kekreplies"]
    await message.channel.send("Replit database emptied!")

  # $KekReply
  if msg.startswith("$KekReply new"):
    new_reply = msg.split("$KekReply new ", 1)[1]
    kekreply.update_kek_replies(kek_replies ,new_reply)
    await message.channel.send("New laugh reply added!")

keep_alive()
client.run(os.environ['TOKEN'])