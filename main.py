import discord
from discord.ext import commands
import os
import requests
import json
import http.client
import urllib.parse
import random
from replit import db

from keepalive import keep_alive
import kekreply

#client = discord.Client()
bot = commands.Bot(command_prefix='$')

#Kek Replies Word lists
kek_words = kekreply.kek_words
kek_replies = kekreply.starter_kek_replies

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return quote

def get_8ball(question):
  conn = http.client.HTTPSConnection("8ball.delegator.com")
  conn.request('GET', '/magic/JSON/' + question)
  response = conn.getresponse()
  answer = json.loads(response.read())
  return answer

@bot.event
async def on_ready():
  print("We have logged in as {0.user}".format(bot))
  
@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  msg = message.content
 
  # Kek Reply Code: This checks whether the message is sent in the Bot CMDS, Media or Shitpost channels and then send the reply.
  if any(word in msg for word in kek_words):
    if (message.channel.id == kekreply.botcmdsId):
      await message.channel.send(random.choice(kek_replies))
    elif (message.channel.id == kekreply.spamId):
      await message.channel.send(random.choice(kek_replies))
    elif (message.channel.id == kekreply.shitpostId):
      await message.channel.send(random.choice(kek_replies))

  # $KekReply new <reply> - Lets users add new Kek Replies, resets after every reboot, WORK ON DATABASE
  if msg.startswith("$KekReply new"):
    new_reply = msg.split("$KekReply new ", 1)[1]
    kekreply.update_kek_replies(kek_replies ,new_reply)
    await message.channel.send("New laugh reply added!")
  
  await bot.process_commands(message)

@bot.command(name='hello')
async def hello(ctx):
  await ctx.send('Hello! I\'m the 2024 bot UwU')

@bot.command(name='quote')
async def quote(ctx):
  quote = get_quote()
  await ctx.send(quote)

@bot.command(name='KekReply', pass_context=True)
async def kekReply_cmds(ctx, cmd):
  if cmd == 'wordslist': # $KekReply wordslist - Sends a list of the trigger words, list in kekreply.py
    await ctx.send(kek_words)
  elif cmd == 'replylist': # $KekReply replylist - Sends a list of the replies, list in kekreply.py
    await ctx.send(kek_replies)
  elif cmd == 'db-delete': # $KekReply database delete - Clears database, temporary(?)
    del db["kekreplies"]
    await ctx.send("Replit database emptied!")

@bot.command(name='8ball', pass_context=True)
async def answer_ball(ctx, ques):
  question = urllib.parse.quote(ques)
  answers = get_8ball(question)
  await ctx.send(answers.get('magic', {}).get('answer'))

keep_alive()
bot.run(os.environ['TOKEN'])