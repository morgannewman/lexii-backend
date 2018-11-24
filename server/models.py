import datetime
from peewee import DateTimeField, CharField, ForeignKeyField, TextField
from playhouse.postgres_ext import BinaryJSONField
from playhouse.shortcuts import model_to_dict
from flask import json
from server import db_wrapper as db
from server.config import Config
from server.helpers import generate_utcnow, generate_utcnow_str
import jwt

SECRET_KEY = Config.SECRET_KEY


class Users(db.Model):
    registered_on = DateTimeField(default=generate_utcnow_str)
    email = CharField(max_length=255, unique=True)
    password = CharField(max_length=72)
    first_name = CharField(max_length=32)
    last_name = CharField(max_length=32)

    @staticmethod
    def encode_auth_token(user):
        """
        Generates the Auth Token
        :return: string
        """
        payload = {
            # 7 day life
            "exp": generate_utcnow() + datetime.timedelta(days=7, seconds=0),
            "iat": generate_utcnow(),
            "sub": json.dumps(user),
        }
        return jwt.encode(payload, SECRET_KEY, algorithm="HS256").decode("utf-8")

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Validates the auth token
        :param auth_token:
        :return: integer|string
        """
        payload = jwt.decode(auth_token, SECRET_KEY)
        """
        is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
        if is_blacklisted_token:
            return 'Token blacklisted. Please log in again.'
        else:
        """
        return json.loads(payload["sub"])

    def to_dict(self):
        result = model_to_dict(self)
        del result["password"]
        del result["user"]
        result["registered_on"] = str(result["registered_on"]) + "+00:00"
        return result


class Snippets(db.Model):
    user = ForeignKeyField(Users, backref="snippets", index=True)
    title = CharField(max_length=128)
    content = TextField()
    created_at = DateTimeField(default=generate_utcnow_str)
    updated_at = DateTimeField(default=generate_utcnow_str)

    def to_dict(self):
        result = model_to_dict(self, recurse=False)
        del result["user"]
        result["created_at"] = str(result["created_at"]) + "+00:00"
        result["updated_at"] = str(result["updated_at"]) + "+00:00"
        return result


class Keywords(db.Model):
    keyword = CharField(max_length=48, unique=True)
    images = BinaryJSONField()
    images_meta = BinaryJSONField()
    updated_at = DateTimeField(default=generate_utcnow_str)

    def to_dict(self):
        result = model_to_dict(self, recurse=False)
        result["updated_at"] = str(result["updated_at"]) + "+00:00"
        return result


class Snippets_Keywords(db.Model):
    snippet = ForeignKeyField(Snippets)
    keyword = ForeignKeyField(Keywords)
    favorite_images = BinaryJSONField(null=True)

    # class Meta:
    #     primary_key = CompositeKey("snippet", "keyword")
