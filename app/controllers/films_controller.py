from app.services.swampi_service import (
    get_films,
    get_film_by_id,
    get_characters_from_film
)
from app.utils.filters import (
    filter_characters,
    filter_films
)
from app.utils.sort import sort_results
from app.utils.validators import (
    validate_order,
    validate_order_by
)

ALLOWED_FILMS_FIELDS = {"title", "episode_id", "release_date"}
ALLOWED_CHARACTERS_FIELDS = {"name", "height", "mass"}


def list_films(query_params):
    films = get_films()
    filtered_films = filter_films(films, query_params)

    order_by = validate_order_by(
        query_params.get("order_by"),
        ALLOWED_FILMS_FIELDS
    )
    order = validate_order(
        query_params.get("order")
    )

    sorted_films = sort_results(
        filtered_films,
        order_by=order_by,
        order=order
    )

    return {
        "count": len(sorted_films),
        "results": sorted_films
    }


def list_film_characters(film_id, query_params):
    film = get_film_by_id(film_id)

    character_urls = film.get("characters", [])
    characters = get_characters_from_film(character_urls)

    filtered_characters = filter_characters(characters, query_params)

    order_by = validate_order_by(
        query_params.get("order_by"),
        ALLOWED_CHARACTERS_FIELDS
    )
    order = validate_order(
        query_params.get("order")
    )

    sorted_characters = sort_results(
        filtered_characters,
        order_by=order_by,
        order=order
    )

    return {
        "film": film["title"],
        "release_date": film["release_date"],
        "total_characters": len(sorted_characters),
        "characters": sorted_characters
    }