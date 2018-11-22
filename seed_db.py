from datetime import datetime
from server import db
from server.models import User, Snippet
import json


db.drop_all()
db.create_all()


# User 1 - Snippets with odd IDs
# User 2 - Snippets with even IDs


u1 = User(
    email="test1@test.com",
    password="password",
    first_name="Morgan",
    last_name="Freeman",
)
u2 = User(
    email="test2@test.com",
    password="password",
    first_name="Morgan",
    last_name="Freeman",
)

db.session.bulk_save_objects([u1, u2])
db.session.commit()

u1 = User.query.get(1)
u2 = User.query.get(2)

s1 = Snippet(
    user=u1,
    title="This is a junk title",
    content="lorem lorem lorem lorem",
    keywords=[
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
    ],
)

s2 = Snippet(
    user=u2,
    title="This is a junk title",
    content="lorem lorem lorem lorem",
    keywords=[
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
    ],
)

s3 = Snippet(
    user=u1,
    title="This is a junk title",
    content="lorem lorem lorem lorem",
    keywords=[
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
    ],
)

s4 = Snippet(
    user=u2,
    title="This is a junk title",
    content="lorem lorem lorem lorem",
    keywords=[
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
    ],
)

s5 = Snippet(
    user=u1,
    title="This is a junk title",
    content="lorem lorem lorem lorem",
    keywords=[
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
    ],
)

s6 = Snippet(
    user=u2,
    title="This is a junk title",
    content="lorem lorem lorem lorem",
    keywords=[
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
    ],
)

s7 = Snippet(
    user=u1,
    title="This is a junk title",
    content="lorem lorem lorem lorem",
    keywords=[
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
    ],
)

s8 = Snippet(
    user=u2,
    title="This is a junk title",
    content="lorem lorem lorem lorem",
    keywords=[
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
        {"createdAt": str(datetime.utcnow()), "keyword": "test"},
    ],
)

db.session.add(s1)
db.session.add(s2)
db.session.add(s3)
db.session.add(s4)
db.session.add(s5)
db.session.add(s6)
db.session.add(s7)
db.session.add(s8)
db.session.commit()
