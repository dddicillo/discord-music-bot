import discord
from discord.ext import commands
from .properties import properties
from .database import db

extensions = [
  'jukebox'
]

# Initialize DB
db.connect()
db.create_schema()

# Initialize Bot
print('Initializing...')
bot = commands.Bot(command_prefix=properties.get_discord_command_prefix())

@bot.event
async def on_ready():
  print('Successfully logged in as \'%s\'' % (bot.user.name))

for extension in extensions:
  bot.load_extension('music_bot.cogs.%s' % (extension))

# Run Event Loop
bot.run(properties.get_discord_token())
