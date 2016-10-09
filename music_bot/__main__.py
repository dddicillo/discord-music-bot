import discord
import sys
from .properties import properties

# Initialize Bot
print('Initializing...')
bot = discord.Client()

@bot.event
async def on_ready():
  print('Successfully logged in as \'%s\'' % (bot.user.name))

# Run Event Loop
bot.run(properties.get_discord_token())
