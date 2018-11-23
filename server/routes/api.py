from server import app, db
from flask import request, jsonify
from peewee import IntegrityError
from server.models import Users
import bcrypt


@app.route("/api/hello", methods=["GET", "POST", "PUT"])
def test():
    print(request.user["id"])
    return ("Hello", 204)
