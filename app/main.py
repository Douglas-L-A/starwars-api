from werkzeug.exceptions import BadRequest, NotFound, Unauthorized, InternalServerError
import json
from app.controllers.characters_controller import list_characters
from app.controllers.films_controller import (
    list_films,
    list_film_characters
)


def api_home():
    return (
        json.dumps({
            "message": "API is running...",
            "endpoints": {
                "films": "/films",
                "characters": "/characters",
                "film_characters": "/films/1/characters"
            }
        }),
        200,
        {"Content-Type": "application/json"}
    )


def error_response(message, status):
    return (
        json.dumps({
            "error": message,
            "status": status
        }),
        status,
        {"Content-Type": "application/json"}
    )


def main(request):
    path = request.path
    method = request.method

    endpoints = {
        "/characters": lambda: list_characters(request.args),
        "/films": lambda: list_films(request.args)
    }

    try:
        if method != "GET":
            return error_response("Method not allowed", 405)
        
        if path == "/":
            return api_home()
        
        # GET endpoints
        if path in endpoints:
            response = endpoints[path]()

            return (
                json.dumps(response),
                200,
                {"Content-Type": "application/json"}
            )

        # GET /films/<id>/characters
        if path.startswith("/films/") and path.endswith("/characters"):
            film_id = path.split("/")[2]

            if not film_id.isdigit():
                raise BadRequest("film_id must be a number")

            response = list_film_characters(
                film_id=film_id,
                query_params=request.args
            )

            return (
                json.dumps(response),
                200,
                {"Content-Type": "application/json"}
            )

        raise NotFound("Endpoint not found")
    
    except BadRequest as e:
        return error_response(str(e), 400)

    except Unauthorized as e:
        return error_response(str(e), 401)

    except NotFound as e:
        return error_response(str(e), 404)

    except InternalServerError as e:
        return error_response(str(e), 500)


