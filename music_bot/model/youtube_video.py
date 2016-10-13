from .base_model import BaseModel
from peewee import *
import datetime

class YoutubeVideo(BaseModel):
  id = PrimaryKeyField()
  youtube_id = CharField()
  title = CharField()
  url = CharField()
  votes = IntegerField(default=1)
  created = DateTimeField(default=datetime.datetime.now)
