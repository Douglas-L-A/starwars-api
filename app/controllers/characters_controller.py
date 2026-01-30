from app.services.swampi_service import get_characters

def list_characters(request):
    characters = get_characters()

    name_filter = request.args.get("name")

    if name_filter:
        characters = [
            c for c in characters
            if name_filter.lower() in c["name"].lower()
        ]
    
    return {
        "count": len(characters),
        "results": characters
    }