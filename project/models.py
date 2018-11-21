from app import db
from sqlalchemy.dialects.postgresql import JSON


class Snippet(db.Model):
    __tablename__ = 'snippets'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return '<content {}>'.format(self.content)