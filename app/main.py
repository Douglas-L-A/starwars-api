import json
from app.controllers.characters_controller import list_characters
from app.controllers.films_controller import (
    list_films,
    list_film_characters
)


def main(request):
    print("PATH RECEBIDO:", request.path)
    print("METHOD:", request.method)

    path = request.path
    method = request.method

    # GET /characters
    if path == "/characters" and method == "GET":
        response = list_characters(request)

        return (
            json.dumps(response),
            200,
            {"Content-Type": "application/json"}
        )
    
    # GET /films
    if path == "/films" and method == "GET":
        response = list_films(request.args)

        return (
            json.dumps(response),
            200,
            {"Content-Type": "application/json"}
        )
    

    # GET /films/<id>/characters
    if path.startswith("/films/") and path.endswith("/characters") and method == "GET":
        film_id = path.split("/")[2]

        response = list_film_characters(
            film_id=film_id,
            query_params=request.args
        )

        return (
            json.dumps(response),
            200,
            {"Content-Type": "application/json"}
        )
    
    # Retorno padrão
    return (
        json.dumps({"message": "Star Wars API is running 🚀"}),
        200,
        {"Content-Type": "application/json"}
    )

