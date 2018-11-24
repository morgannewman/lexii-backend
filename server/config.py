import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.getenv("SECRET_KEY") or "NOT_A_REAL_SECRET"
    DATABASE_URL = os.getenv("DATABASE_URL") or "postgresql://dev:@localhost/lexii"
    UNSPLASH_CLIENT_ID = (
        "38d91223e00315d4c6926c55580e4e8c2ea513672893c1bdda4b3cbca4a09f31"
    )
    UNSPLASH_CLIENT_SECRET = (
        "64efe5a0ee03d7bb161c111c6fc7e18b5d73e184d7ffe4294f09b3dbc099374b"
    )

