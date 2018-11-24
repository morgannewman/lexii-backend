from server import app, db
from flask import request, jsonify
from peewee import IntegrityError
from server.models import Snippets
from server.helpers import required_fields


@app.route("/api/snippets", methods=["GET"])
def get_all_snippets():
    result = []
    for snippet in (
        Snippets.select()
        .where(Snippets.user == request.user["id"])
        .order_by(Snippets.updatedAt)
    ):
        result.append(snippet.to_dict())
    return jsonify(result)


@app.route("/api/snippets/<int:id>", methods=["GET"])
def get_snippet_by_id(id):
    try:
        snippet = (
            Snippets.select()
            .where(Snippets.user == request.user["id"], Snippets.id == id)
            .get()
        )
        return jsonify(snippet.to_dict())
    except Snippets.DoesNotExist:
        err = jsonify({"message": "Snippet does not exist"})
        err.status = "404"
        return err


@app.route("/api/snippets", methods=["POST"])
def create_new_snippet():
    return jsonify({"POST": "test"})


@app.route("/api/snippets/<int:id>", methods=["PUT"])
def edit_snippet_by_id(id):
    return jsonify({"PUT": id})


@app.route("/api/snippets/<int:id>", methods=["DELETE"])
def delete_snippet_by_id(id):
    return jsonify({"DELETE": id})
