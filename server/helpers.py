from flask import request, jsonify
from functools import wraps
import re


def required_fields(required_fields_list):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            for field in required_fields_list:
                print(field)
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
            "([a-zA-Z0-9])+@([a-zA-Z0-9])+\.([a-z])+", request.body["email"]
        )
        if is_valid_email:
            return fn(*args, **kwargs)
        else:
            err = jsonify({"message": "Malformed `email` in request body."})
            err.status = "400"
            return err

    return wrapper