import datetime
from mongoengine import *


class Doc(Document):
    title = StringField(required=True, min_length=3)
    date_modified = DateTimeField(default=datetime.datetime.utcnow)
