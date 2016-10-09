import configparser

class Properties(configparser.ConfigParser):

  def __init__(self):
    super(Properties, self).__init__()
    data = super(Properties, self).read('conf/music_bot.ini')
    if len(data) == 0:
      raise ValueError('Failed to load properties. Make sure you have added a \'music_bot.ini\' file')

  def get_discord_token(self):
    return self['Discord']['Token']
