import os
# Import Flask and deps
from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# Init app
app = Flask(__name__)
# Default to production environment for security
app.config.from_object(os.getenv("APP_SETTINGS") or "config.ProductionConfig")
# Init db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *

# Set CORS permissions
CORS(app, resources={r"/*": {"origins": "*"}}, send_wildcard=True)


# POST /search endpoint
@app.route("/search", methods=["POST"])
def request_handler():
    if request.method == "POST":
        data = (request.get_json())["content"]
        # INSERT MAGIC FUNCTION TO DO MAGIC THINGS HERE
        images = {"placeholder": "text"}
        response = jsonify(images)
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response, 201
    else:
        return jsonify({"Error": "does not exist"}, 404)


@app.route("/")
def hello():
    return "Nothing to see here ;)"


# Spin up server
if __name__ == "__main__":
    app.run()
