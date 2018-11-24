import bcrypt
from datetime import datetime
from server import db
from server.models import Users, Snippets
from server.helpers import generate_utcnow_str

MODELS = [Users, Snippets]
db.bind(MODELS, bind_refs=False, bind_backrefs=False)
db.connect()

db.drop_tables(MODELS)
db.create_tables([Users, Snippets])


# Users 1 - Snippetss with odd IDs
# Users 2 - Snippetss with even IDs


u1 = Users(
    email="test1@test.com",
    password=bcrypt.hashpw("password".encode("utf-8"), bcrypt.gensalt()),
    first_name="Morgan",
    last_name="Freeman",
)

u2 = Users(
    email="test2@test.com",
    password=bcrypt.hashpw("password".encode("utf-8"), bcrypt.gensalt()),
    first_name="Morgan",
    last_name="NotFreeman",
)

u1.save()
u2.save()

# Users.insert_many([u1, u2]).execute()


s1 = {
    "user": 1,
    "title": "This is a junk title",
    "content": "lorem lorem lorem lorem",
    "keywords": [
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
    ],
}

s2 = {
    "user": 2,
    "title": "This is a junk title",
    "content": "lorem lorem lorem lorem",
    "keywords": [
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
    ],
}

s3 = {
    "user": 1,
    "title": "This is a junk title",
    "content": "lorem lorem lorem lorem",
    "keywords": [
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
    ],
}

s4 = {
    "user": 2,
    "title": "This is a junk title",
    "content": "lorem lorem lorem lorem",
    "keywords": [
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
    ],
}

s5 = {
    "user": 1,
    "title": "This is a junk title",
    "content": "lorem lorem lorem lorem",
    "keywords": [
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
    ],
}

s6 = {
    "user": 2,
    "title": "This is a junk title",
    "content": "lorem lorem lorem lorem",
    "keywords": [
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
    ],
}

s7 = {
    "user": 1,
    "title": "This is a junk title",
    "content": "lorem lorem lorem lorem",
    "keywords": [
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
    ],
}

s8 = {
    "user": 2,
    "title": "This is a junk title",
    "content": "lorem lorem lorem lorem",
    "keywords": [
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
        {"createdAt": generate_utcnow_str(), "keyword": "test"},
    ],
}

Snippets.insert_many([s1, s2, s3, s4, s5, s6, s7, s8]).execute()

db.close()
