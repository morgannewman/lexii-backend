from server import app, db
from flask import request, jsonify
from peewee import IntegrityError
from server.models import Users
import bcrypt


@app.route("/")
@app.route("/index")
def index():
    return "Hello, World!"


@app.route("/auth/register", methods=["POST"])
def register():
    """
    EXPECT:
    req to have all required fields (400)
    TODO: req to have the correctly-formed params (400) => before DB
    req email to be unique (403)
    req to create a new user in DB (201)
    -
    DB password to be hashed
    """
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


@app.route("/auth/login", methods=["POST"])
def login():
    """
    EXPECT:
    req to have all required fields (400)
    TODO: req to have the correctly-formed params (400) => before DB
    req email to be unique (403)
    req email to exist (404)
    req password to match the user's password (404)
    res to issue a new token (200)
    """
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
    try:
        if bcrypt.checkpw(
            req["password"].encode("utf-8"), user.password.encode("utf-8")
        ):
            # issue token
            token = Users.encode_auth_token(user.id)
            print("TOKEN ISSUED:", token)
            return jsonify({"token": str(token)})
        else:
            return ("Incorrect email or password", 404)
    # TODO: Handle malformed requests more idiomatically
    except:
        return ("Incorrect email or password", 404)


@app.route("/auth/refresh", methods=["POST"])
def refresh():
    """
    EXPECT:
    req to have all required fields (400)
    req to contain a valid token (400)
    res to issue a new token (200)
    """
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
    # TODO: Handle malformed tokens idiomatically
    except:
        res = jsonify({"message": "Invalid token"})
        res.status = "400"
        return res
