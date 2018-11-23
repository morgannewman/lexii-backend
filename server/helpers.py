from flask import request, abort, jsonify
from functools import wraps


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
