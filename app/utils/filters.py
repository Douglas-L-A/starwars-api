def filter_characters(characters, filters):
    result = characters

    # Filtro por nome
    if filters.get("name"):
        result = [
            c for c in result
            if filters["name"].lower() in c.get("name", "").lower()
        ]

    # Filtro por gênero
    if filters.get("gender"):
        result = [
            c for c in result
            if c.get("gender", "").lower() == filters["gender"].lower()
        ]

    return result


def filter_films(films, filters):
    result = films

    # Filtro por título
    if filters.get("title"):
        result = [
            f for f in result
            if filters["title"].lower() in f.get("title", "").lower()
        ]

    return result