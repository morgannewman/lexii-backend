from server import app, db
from flask import request, json, jsonify, abort
from functools import wraps
from peewee import IntegrityError
from playhouse.flask_utils import get_object_or_404
from server import db
from server.models import Users
import jwt
import bcrypt


@app.route("/")
@app.route("/index")
def index():
    return "Hello, World!"


"""
EXPECT:
req to have all required fields (400)
TODO: req to have the correctly-formed params (400) => before DB
req email to be unique (403)
req to create a new user in DB (201)
-
DB password to be hashed
"""


@app.route("/auth/register", methods=["POST"])
def register():
    req = request.get_json()
    # Validate required fields
    required_fields = ("email", "password", "first_name", "last_name")
    for field in required_fields:
        if field not in req:
            err = jsonify({"message": "missing `{}` in request body".format(field)})
            err.status = "400"
            return err
    # TODO: add any additional verification checks (e.g. password length, email format)
    # insert into db
    try:
        with db.atomic():
            Users.create(
                email=req["email"],
                password=bcrypt.hashpw(
                    req["password"].encode("utf-8"), bcrypt.gensalt()
                ),
                first_name=req["first_name"],
                last_name=req["last_name"],
            )
        return ("", 201)

    except IntegrityError:
        return ("email already exists", 403)
    except AttributeError:
        return ("Invalid request values", 400)


"""
EXPECT:
req to have all required fields (400)
TODO: req to have the correctly-formed params (400) => before DB
req email to be unique (403)
req email to exist (404)
req password to match the user's password (404)
res to return a JWT
"""


@app.route("/auth/login", methods=["POST"])
def login():
    req = request.get_json()
    # EXPECT email / password
    required_fields = ("email", "password")
    for field in required_fields:
        if field not in req:
            err = jsonify({"message": "missing `{}` in request body".format(field)})
            err.status = "400"
            return err

    # find user
    user = Users.get(Users.email == req["email"])
    # validate password
    if bcrypt.checkpw(req["password"].encode("utf-8"), user.password.encode("utf-8")):
        # issue token
        token = Users.encode_auth_token(user.id)
        print("TOKEN ISSUED:", token)
        return jsonify({"token": str(token)})
    else:
        return ("Email or password not found", 404)


@app.route("/auth/refresh", methods=["POST"])
def refresh():
    req = request.get_json()
    if "token" not in req:
        res = jsonify({"message": "missing `token` in request body"})
        res.status = "400"
        return res
    # issue new token
    try:
        return jsonify(
            {
                "token": str(
                    Users.encode_auth_token(Users.decode_auth_token(req["token"]))
                )
            }
        )
    except:
        res = jsonify({"message": "Invalid token"})
        res.status = "400"
        return res
