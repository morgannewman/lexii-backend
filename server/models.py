from datetime import datetime
from peewee import DateTimeField, CharField, ForeignKeyField, TextField
from playhouse.postgres_ext import BinaryJSONField
from server import db_wrapper as db


class Users(db.Model):
    registered_on = DateTimeField(default=datetime.utcnow)
    email = CharField(max_length=255, unique=True)
    password = CharField(max_length=72)
    first_name = CharField(max_length=32)
    last_name = CharField(max_length=32)


class Snippets(db.Model):
    user = ForeignKeyField(Users, backref="snippets")
    title = CharField(max_length=128)
    content = TextField()
    keywords = BinaryJSONField()

    def __init__(self, user, title, content, keywords):
        self.user = user
        self.title = title
        self.content = content
        self.keywords = keywords
