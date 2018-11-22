import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = "NOT_A_REAL_SECRET"
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL") or "postgresql://dev:@localhost/lexii"