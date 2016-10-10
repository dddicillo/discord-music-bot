from discord.ext import commands

class Jukebox:
  """Commands used to control the jukebox"""

  def __init__(self, bot):
    self.bot = bot

  @commands.command(description='Search for a song to add to the playlist')
  async def play(self):
    """Search for a song to add to the playlist"""
    print('Playing song')

def setup(bot):
  bot.add_cog(Jukebox(bot))
