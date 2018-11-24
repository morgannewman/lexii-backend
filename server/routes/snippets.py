from flask import request, jsonify
from server import app, db
from peewee import IntegrityError
from server.models import Snippets
from server.helpers import required_fields

# from server.keyword_engine import generate_keywords, store_keywords


@app.route("/api/snippets", methods=["GET"])
def get_all_snippets():
    result = []
    for snippet in (
        Snippets.select()
        .where(Snippets.user == request.user["id"])
        .order_by(Snippets.updated_at)
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


# @required_fields(["title", "content"])
@app.route("/api/snippets", methods=["POST"])
def create_new_snippet():
    title = request.body["title"]
    content = request.body["content"]
    # TODO: Async add snippet to DB + generate_keywords
    # add to DB
    try:
        with db.atomic():
            snippet = Snippets.create(title=title, content=content)
            snippet = snippet.to_dict()
    except (IntegrityError, AttributeError):
        err = jsonify({"message": "Error adding snippet"})
        err.status = "500"
        return err
    # generate keywords using Google API
    raw_keywords = generate_keywords(title, content)
    # Await HERE
    # with new snippet_id, create keyword resource for each keyword
    final_keywords = store_keywords(snippet["id"], raw_keywords)
    snippet["keywords"] = final_keywords
    # respond with snippet + keywords
    res = jsonify(snippet)
    res.status = "201"
    return res


@app.route("/api/snippets/<int:id>", methods=["PUT"])
@required_fields(["id"])
def edit_snippet_by_id(id):
    return jsonify({"PUT": id})


@app.route("/api/snippets/<int:id>", methods=["DELETE"])
def delete_snippet_by_id(id):
    try:
        num_deleted = (
            Snippets.delete()
            .where(Snippets.user == request.user["id"], Snippets.id == id)
            .execute()
        )
        if num_deleted == 0:
            raise Snippets.DoesNotExist
        return ("", 204)
    except Snippets.DoesNotExist:
        err = jsonify({"message": "Snippet does not exist"})
        err.status = "404"
        return err
