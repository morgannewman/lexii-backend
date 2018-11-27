import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.getenv("SECRET_KEY") or "NOT_A_REAL_SECRET"
    DATABASE_URL = os.getenv("DATABASE_URL") or "postgresql://dev:@localhost/lexii"
    UNSPLASH_CLIENT_ID = os.getenv("UNSPLASH_CLIENT_ID")
    GOOGLE_CLOUD_API_KEY = os.getenv("GOOGLE_CLOUD_API_KEY")
