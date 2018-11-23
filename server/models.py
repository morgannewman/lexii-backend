import datetime
from peewee import DateTimeField, CharField, ForeignKeyField, TextField
from playhouse.postgres_ext import BinaryJSONField
from server import db_wrapper as db
from server.config import Config
import jwt

SECRET_KEY = Config.SECRET_KEY


class Users(db.Model):
    registered_on = DateTimeField(default=datetime.datetime.utcnow)
    email = CharField(max_length=255, unique=True)
    password = CharField(max_length=72)
    first_name = CharField(max_length=32)
    last_name = CharField(max_length=32)

    @staticmethod
    def encode_auth_token(user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                "exp": datetime.datetime.utcnow()
                + datetime.timedelta(days=7, seconds=0),
                "iat": datetime.datetime.utcnow(),
                "sub": user_id,
            }
            return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        except Exception as e:
            print("Failed to encode token", e)
            return e


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
