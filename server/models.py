from server import db
from sqlalchemy.dialects.postgresql import JSON


class Snippet(db.Model):
    __tablename__ = 'snippets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String())

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return '<content {}>'.format(self.content)


class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
