from datetime import datetime
from server import db
from server.models import Users, Snippets

MODELS = [Users, Snippets]
db.bind(MODELS, bind_refs=False, bind_backrefs=False)
db.connect()

db.drop_tables(MODELS)
db.create_tables([Users, Snippets])


# Users 1 - Snippetss with odd IDs
# Users 2 - Snippetss with even IDs


u1 = {
    "email": "test1@test.com",
    "password": "password",
    "first_name": "Morgan",
    "last_name": "Freeman",
}

u2 = {
    "email": "test2@test.com",
    "password": "password",
    "first_name": "Morgan",
    "last_name": "NotFreeman",
}

Users.insert_many([u1, u2]).execute()


s1 = {
    "user": 1,
    "title": "This is a junk title",
    "content": "lorem lorem lorem lorem",
    "keywords": [
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
    ],
}

s2 = {
    "user": 2,
    "title": "This is a junk title",
    "content": "lorem lorem lorem lorem",
    "keywords": [
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
    ],
}

s3 = {
    "user": 1,
    "title": "This is a junk title",
    "content": "lorem lorem lorem lorem",
    "keywords": [
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
    ],
}

s4 = {
    "user": 2,
    "title": "This is a junk title",
    "content": "lorem lorem lorem lorem",
    "keywords": [
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
    ],
}

s5 = {
    "user": 1,
    "title": "This is a junk title",
    "content": "lorem lorem lorem lorem",
    "keywords": [
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
    ],
}

s6 = {
    "user": 2,
    "title": "This is a junk title",
    "content": "lorem lorem lorem lorem",
    "keywords": [
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
    ],
}

s7 = {
    "user": 1,
    "title": "This is a junk title",
    "content": "lorem lorem lorem lorem",
    "keywords": [
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
    ],
}

s8 = {
    "user": 2,
    "title": "This is a junk title",
    "content": "lorem lorem lorem lorem",
    "keywords": [
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
    ],
}

Snippets.insert_many([s1, s2, s3, s4, s5, s6, s7, s8]).execute()

db.close()
