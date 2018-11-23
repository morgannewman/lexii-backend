from server.config import Config
from flask import Flask, request, abort, jsonify
from playhouse.flask_utils import FlaskDB


# Init app
app = Flask(__name__)
# Default to production environment for security
app.config.from_object(Config)
# Init db
db_wrapper = FlaskDB(app)
db = db_wrapper.database


from server.models import Users, Snippets


@app.before_request
def _protect_api_root_JWT_strategy():
    """
    Protects all /api endpoints with JWT strategy.
    Decorates request with `request.user` object.
    """
    if request.path[1:4] == "api":
        # Extract auth header from request
        try:
            token = request.headers["Authorization"][7:]
        except Exception:
            err = jsonify({"message": "missing `Authorization` header in request"})
            err.status = "400"
            abort(err)
        # Decode token to user object
        try:
            user = Users.decode_auth_token(token)
        except Exception:
            err = jsonify({"message": "Invalid token"})
            err.status = "400"
            abort(err)
        # Append user object to request object
        request.user = user


@app.before_request
def _require_json_in_req_body():
    """
    Ensures that all request bodies include JSON data.
    Decorates request with `request.body` object.
    """
    if request.method in ["POST", "PUT", "PATCH"]:
        if request.is_json:
            request.body = request.get_json()
        else:
            err = jsonify(
                {"message": "request body must be of type `application/json`."}
            )
            err.status = 400
            abort(err)


@app.before_request
def _db_connect():
    """
    Open DB connection before valid requests are routed.
    """
    if db.is_closed():
        db.connect()


@app.teardown_request
def _db_close(exp):
    """
    Close DB connection at end of a request's lifecycle.
    """
    if not db.is_closed():
        db.close()


import server.routes
