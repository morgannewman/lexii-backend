import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.getenv("SECRET_KEY") or "NOT_A_REAL_SECRET"
    DATABASE_URL = os.getenv("DATABASE_URL") or "postgresql://dev:@localhost/lexii"

