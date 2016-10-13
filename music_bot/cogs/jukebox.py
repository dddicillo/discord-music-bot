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
      await self.bot.say('Your search did not return any results')
      return
    await self.bot.say('Please choose one of the options below:')
    for idx, video in enumerate(videos):
      await self.bot.say('%d: %s' % (idx+1, video['title']))

    def isValidQueryResponse(message):
      try:
        value = int(message.content)
        return (1 <= value and value <= response_count)
      except ValueError as err:
        return False

    message = await self.bot.wait_for_message(timeout=5.0, author=ctx.message.author, check=isValidQueryResponse)
    if message is None:
      await self.bot.say('Sorry. You took too long')
      return
    playlist.enqueue(videos[int(message.content)-1])
    await self.bot.say('\'%s\' was added to the playlist' % (videos[int(message.content)-1]['title']))

  @commands.command(description='Display the playlist in chat')
  async def list(self):
    """Display the playlist in chat"""
    await self.bot.say(playlist.toString())

def setup(bot):
  bot.add_cog(Jukebox(bot))
