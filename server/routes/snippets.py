from server import app, db
from flask import request, jsonify
from peewee import IntegrityError
from server.models import Snippets
from server.helpers import required_fields


@app.route("/api/snippets", methods=["GET"])
def get_all_snippets():
    return jsonify({"GET": "test"})


@app.route("/api/snippets/<int:id>", methods=["GET"])
def get_snippet_by_id(id):
    return jsonify({"GET": id})


@app.route("/api/snippets", methods=["POST"])
def create_new_snippet():
    return jsonify({"POST": "test"})


@app.route("/api/snippets/<int:id>", methods=["PUT"])
def edit_snippet_by_id(id):
    return jsonify({"PUT": id})


@app.route("/api/snippets/<int:id>", methods=["DELETE"])
def delete_snippet_by_id(id):
    return jsonify({"DELETE": id})
