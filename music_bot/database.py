from playhouse.sqlite_ext import SqliteExtDatabase
from .properties import properties

class Database(SqliteExtDatabase):

  def __init__(self):
    super(Database, self).__init__(properties.get_db_name())

  def create_schema(self):
    from .model.youtube_video import YoutubeVideo
    if not YoutubeVideo.table_exists():
      super(Database, self).create_table(YoutubeVideo)

db = Database()
