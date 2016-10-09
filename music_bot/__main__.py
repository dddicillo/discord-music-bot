import discord
import sys
from .properties import Properties

# Load Properties
props = None
try:
  props = Properties()
except ValueError as err:
  print(err)
  sys.exit(1)

# Initialize Bot
print('Initializing...')
bot = discord.Client()

@bot.event
async def on_ready():
  print('Successfully logged in as \'%s\'' % (bot.user.name))

# Run Event Loop
bot.run(props.get_discord_token())
