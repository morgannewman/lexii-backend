import bcrypt


users = [
    {
        "email": "test1@test.com",
        "password": bcrypt.hashpw("password".encode("utf-8"), bcrypt.gensalt()),
        "first_name": "Morgan",
        "last_name": "Freeman",
    },
    {
        "email": "test2@test.com",
        "password": bcrypt.hashpw("password".encode("utf-8"), bcrypt.gensalt()),
        "first_name": "Morgan",
        "last_name": "NotFreeman",
    },
]

snippets = [
    {"user": 1, "title": "This is a junk title", "content": "lorem lorem lorem lorem"},
    {"user": 2, "title": "This is a junk title", "content": "lorem lorem lorem lorem"},
    {"user": 1, "title": "This is a junk title", "content": "lorem lorem lorem lorem"},
    {"user": 2, "title": "This is a junk title", "content": "lorem lorem lorem lorem"},
    {"user": 1, "title": "This is a junk title", "content": "lorem lorem lorem lorem"},
    {"user": 2, "title": "This is a junk title", "content": "lorem lorem lorem lorem"},
    {"user": 1, "title": "This is a junk title", "content": "lorem lorem lorem lorem"},
    {"user": 2, "title": "This is a junk title", "content": "lorem lorem lorem lorem"},
]

keywords = [
    {
        "keyword": "Keyword 1",
        "images": ["images", "arbitrary", {"json": "item"}],
        "images_meta": ["images_meta", "arbitrary", {"json": "item"}],
    },
    {
        "keyword": "Keyword 2?¿",
        "images": ["some more", "arbitrary", {"json": "items"}],
        "images_meta": ["another", "arbitrary", {"json": "item"}],
    },
    {
        "keyword": "Keyword 3",
        "images": ["some more", "arbitrary", {"json": "items"}],
        "images_meta": ["another", "arbitrary", {"json": "item"}],
    },
    {
        "keyword": "Keyword 4?¿",
        "images": ["some more", "arbitrary", {"json": "items"}],
        "images_meta": ["another", "arbitrary", {"json": "item"}],
    },
    {
        "keyword": "Keyword 5",
        "images": ["some more", "arbitrary", {"json": "items"}],
        "images_meta": ["another", "arbitrary", {"json": "item"}],
    },
]

snippets_keywords = [
    {"snippet": 1, "keyword": 1},
    {"snippet": 2, "keyword": 2},
    {"snippet": 1, "keyword": 3},
    {"snippet": 2, "keyword": 4},
    {"snippet": 1, "keyword": 5},
]
