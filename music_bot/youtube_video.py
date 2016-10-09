class YoutubeVideo():

  def __init__(self, video_info):
    self.title = video_info['snippet']['title']
    self.url = 'https://www.youtube.com/watch?v=%s' % (video_info['id']['videoId'])
