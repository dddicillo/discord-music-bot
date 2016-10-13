from apiclient.discovery import build
from .properties import properties
from .model.youtube_video import YoutubeVideo

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

class YoutubeSearch():

  def __init__(self):
    self.api = build(
      YOUTUBE_API_SERVICE_NAME,
      YOUTUBE_API_VERSION,
      developerKey=properties.get_youtube_token()
    )

  def search(self, term):
    response = self.api.search().list(
      q=term,
      part='snippet',
      type='video',
      maxResults=properties.get_youtube_max_results(),
      regionCode=properties.get_youtube_region_code(),
      videoCategoryId=properties.get_youtube_video_category_id()
    ).execute()
    return self.__search_results_to_video_array(response)

  def __search_results_to_video_array(self, search_results):
    videos = []
    for video in search_results.get('items'):
      videos.append({
        'title': video['snippet']['title'],
        'youtube_id': video['id']['videoId'],
        'url': 'https://www.youtube.com/watch?v=%s' % (video['id']['videoId'])
      })
    return videos

youtube = YoutubeSearch()
