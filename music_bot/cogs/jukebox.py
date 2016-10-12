from discord.ext import commands
from music_bot.youtube_search import youtube
from music_bot.playlist import playlist

class Jukebox:
  """Commands used to control the jukebox"""

  def __init__(self, bot):
    self.bot = bot

  @commands.command(pass_context=True, description='Search for a song to add to the playlist')
  async def play(self, ctx, query : str):
    """Search for a song to add to the playlist"""
    global response_count
    videos = youtube.search(query)
    response_count = len(videos)
    if response_count == 0:
      self.bot.say('Your search did not return any results')
      return
    await self.bot.say('Please choose one of the options below:')
    for idx, video in enumerate(videos):
      await self.bot.say('%d: %s' % (idx+1, video.title))

    def isValidQueryResponse(message):
      return (isinstance(message.content, int) and 1 <= message.content and response_count >= message.content)

    index = await self.bot.wait_for_message(timeout=5.0, author=ctx.message.author, check=isValidQueryResponse)
    # playlist.enqueue(videos[index])
    await self.bot.say('\'%s\' was added to the playlist' % (videos[index].title))

def setup(bot):
  bot.add_cog(Jukebox(bot))
