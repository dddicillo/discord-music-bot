import copy

class Playlist():

  def __init__(self):
    self.queue = []

  def enqueue(self, video):
    heapq.heappush(self.queue, (1, video))

  def dequeue(self):
    heapq.heappop()[1]

  def toString(self):
    playlist_string = []
    index = 1
    queue_copy = copy.deepcopy(self.queue)
    while (len(queue_copy) > 0):
      video_title = heapq.heappop()[1]
      playlist_string.push('%d. %s' % (index, video_title))
    return playlist_string.join('\n')

playlist = Playlist()
