import configparser

class Properties(configparser.ConfigParser):

  def __init__(self):
    super(Properties, self).__init__()
    data = super(Properties, self).read('conf/music_bot.ini')
    if len(data) == 0:
      raise ValueError('Failed to load properties. Make sure you have added a \'music_bot.ini\' file')

  def get_discord_token(self):
    return self['Discord']['Token']

  def get_youtube_token(self):
    return self['Youtube']['Token']

  def get_youtube_max_results(self):
    return self['Youtube']['MaxResults']

# Create Singleton Instance
properties = None
try:
  properties = Properties()
except ValueError as err:
  print(err)
  sys.exit(1)


