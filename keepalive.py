### How I keep the bot online 24/7 on repl.it

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return "Hello, I'm alive! 2024 Bot is currently active."

def run():
  app.run(host='0.0.0.0', port=8000)

def keep_alive():
  t = Thread(target=run)
  t.start()