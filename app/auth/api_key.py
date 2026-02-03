from werkzeug.exceptions import Unauthorized, InternalServerError
import os
from functools import wraps
from flask import request


def require_api_key(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        api_key = request.headers.get("X-API-KEY")
        expected_key = os.getenv("API_KEY")

        if not expected_key:
            raise InternalServerError("API key not configured")

        if not api_key or api_key != expected_key:
            raise Unauthorized("Invalid or missing API key")

        return func(*args, **kwargs)

    return wrapper
