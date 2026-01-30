from app.services.swampi_service import (
    get_films,
    get_film_by_id,
    get_characters_from_film
)
from app.utils.filters import (
    filter_characters,
    filter_films
)


def list_films(query_params):
    films = get_films()
    filtered_films = filter_films(films, query_params)

    return {
        "total": len(filtered_films),
        "films": [
            {
                "id": f["url"].rstrip("/").split("/")[-1],
                "title": f["title"],
                "episode_id": f["episode_id"],
                "release_date": f["release_date"]
            }
            for f in filtered_films
        ]
    }


def list_film_characters(film_id, query_params):
    film = get_film_by_id(film_id)

    character_urls = film.get("characters", [])
    characters = get_characters_from_film(character_urls)

    filtered_characters = filter_characters(characters, query_params)

    return {
        "film": film["title"],
        "release_date": film["release_date"],
        "total_characters": len(filtered_characters),
        "characters": filtered_characters
    }