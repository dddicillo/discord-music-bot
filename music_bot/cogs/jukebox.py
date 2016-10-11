from discord.ext import commands
from music_bot.youtube_search import youtube

class Jukebox:
  """Commands used to control the jukebox"""

  def __init__(self, bot):
    self.bot = bot

  @commands.command(description='Search for a song to add to the playlist')
  async def play(self, query : str):
    """Search for a song to add to the playlist"""
    videos = youtube.search(query)
    if len(videos) > 0:
      await self.bot.say('Please choose one of the options below:')
      for idx, video in enumerate(videos):
        await self.bot.say('%d: %s' % (idx+1, video.title))

def setup(bot):
  bot.add_cog(Jukebox(bot))
