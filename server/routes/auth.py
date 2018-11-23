from server import app, db
from flask import request, jsonify
from peewee import IntegrityError
from server.models import Users
import bcrypt
from server.helpers import required_fields


@app.route("/auth/register", methods=["POST"])
@required_fields(["email", "password", "first_name", "last_name"])
def register_user():
    """
    EXPECT:
    req to have all required fields (400)
    TODO: req to have the correctly-formed params (400) => before DB
    req email to be unique (403)
    req to create a new user in DB (201)
    -
    DB password to be hashed
    """
    # TODO: add any additional verification checks (e.g. password length, email format)
    # insert into db
    try:
        with db.atomic():
            Users.create(
                email=request.body["email"],
                password=bcrypt.hashpw(
                    request.body["password"].encode("utf-8"), bcrypt.gensalt()
                ),
                first_name=request.body["first_name"],
                last_name=request.body["last_name"],
            )
        return ("", 201)

    except IntegrityError:
        return ("email already exists", 403)
    except AttributeError:
        return ("Invalid request values", 400)


@app.route("/auth/login", methods=["POST"])
@required_fields(["email", "password"])
def login():
    """
    EXPECT:
    req to have all required fields (400)
    TODO: req to have the correctly-formed params (400) => before DB
    req email to exist (403)
    req password to match the user's password (403)
    res to issue a new token (200)
    """
    # TODO: validate inputs before DB
    # find user
    user = Users.get(Users.email == request.body["email"])
    user_object = {
        "id": user.id,
        "registered_on": user.registered_on,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
    }
    try:
        # validate password
        if bcrypt.checkpw(
            request.body["password"].encode("utf-8"), user.password.encode("utf-8")
        ):
            # issue token
            token = Users.encode_auth_token(user_object)
            return jsonify({"token": str(token)})
        else:
            return ("Incorrect email or password", 403)
    except Exception:
        return ("Incorrect email or password", 403)


@app.route("/auth/refresh", methods=["POST"])
@required_fields(["token"])
def refresh_token():
    """
    EXPECT:
    req to have all required fields (400)
    req to contain a valid token (400)
    res to issue a new token (200)
    """
    # issue new token
    try:
        return jsonify(
            {
                "token": str(
                    Users.encode_auth_token(
                        Users.decode_auth_token(request.body["token"])
                    )
                )
            }
        )
    except Exception:
        err = jsonify({"message": "Invalid token"})
        err.status = "400"
        return err
