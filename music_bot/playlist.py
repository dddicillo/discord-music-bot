from .model.youtube_video import YoutubeVideo

class Playlist():

  def __init__(self):
    # Grab queue from last runtime
    self.__refreshLocalQueue()

  def enqueue(self, video):
    # Update votes if song exists in playlist
    query = (YoutubeVideo
      .select()
      .where(YoutubeVideo.youtube_id == video['youtube_id']))
    if query.count() > 0:
      (YoutubeVideo
        .update(votes=query[0].votes+1)
        .where(YoutubeVideo.youtube_id == video['youtube_id']))
      self.__refreshLocalQueue()
    else:
    # Add video to playlist
      video = YoutubeVideo.create(
        youtube_id=video['youtube_id'],
        title=video['title'],
        url=video['url'],
      )
      self.queue.append(video)

  def dequeue(self):
    # Refresh queue whenever data changes so we can do fast gets
    try:
      video = self.queue.pop(0)
      YoutubeVideo.delete().where(YoutubVideo.youtube_id == video.youtube_id)
      return video
    except IndexError:
      return None

  def string(self):
    playlist_string = []
    index = 1
    if len(self.queue) == 0:
        return 'There are currently no songs in the playlist'
    for song in self.queue:
        playlist_string.append('%d: %s' % (index, song))
    return playlist_string.join('\n')

  def __refreshLocalQueue(self):
    self.queue = []
    for video in YoutubeVideo.select().order_by(YoutubeVideo.votes.desc()):
      self.queue.append(video)

playlist = Playlist()
