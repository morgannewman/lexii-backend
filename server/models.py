from datetime import datetime

from server import db
from sqlalchemy.dialects.postgresql import JSONB


class User(db.Model):
    """ User Model for storing user related details """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(32), nullable=False)
    last_name = db.Column(db.String(32), nullable=False)
    snippets = db.relationship("Snippet", backref="user", lazy=True)

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        return "<User {}>".format(self.id)


class Snippet(db.Model):
    __tablename__ = "snippets"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id"), nullable=False, index=True
    )
    title = db.Column(db.String(125))
    content = db.Column(db.Text)
    keywords = db.Column(JSONB)

    def __init__(self, user, title, content, keywords):
        self.user = user
        self.title = title
        self.content = content
        self.keywords = keywords

    def __repr__(self):
        return "<content {}>".format(self.content)
