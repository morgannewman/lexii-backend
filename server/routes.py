from server import app, db
from flask import request, json, jsonify, abort
from functools import wraps
from peewee import IntegrityError
from server import db
from server.models import Users
import bcrypt


@app.route("/")
@app.route("/index")
def index():
    return "Hello, World!"


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
