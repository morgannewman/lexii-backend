from flask import request, jsonify
from functools import wraps
import datetime
import re


def required_fields(required_fields_list):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            for field in required_fields_list:
                if field not in request.body:
                    err = jsonify(
                        {"message": "missing `{}` in request body".format(field)}
                    )
                    err.status = "400"
                    return err
            return fn(*args, **kwargs)

        return wrapper

    return decorator


def ensure_email_is_valid(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        is_valid_email = re.fullmatch(
            "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", request.body["email"]
        )
        if is_valid_email:
            return fn(*args, **kwargs)
        else:
            err = jsonify({"message": "Malformed `email` in request body."})
            err.status = "400"
            return err

    return wrapper


def generate_utcnow():
    return datetime.datetime.now(datetime.timezone.utc)


def generate_utcnow_str():
    return str(datetime.datetime.now(datetime.timezone.utc))
