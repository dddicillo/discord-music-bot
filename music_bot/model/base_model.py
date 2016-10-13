from peewee import Model
from music_bot.database import db

class BaseModel(Model):
  class Meta:
    database = db
