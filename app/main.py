import json
from app.controllers.characters_controller import list_characters

def main(request):
    path = request.path

    if path == "/characters" and request.method == "GET":
        response = list_characters(request)

        return (
            json.dumps(response),
            200,
            {"Content-Type": "application/json"}
        )
    
    return (
        json.dumps({"message": "Star Wars API is running 🚀"}),
        200,
        {"Content-Type": "application/json"}
    )

