from app.services.swampi_service import (
    get_resource,
    get_film_by_id,
    get_resources_from_urls
)
from app.utils.filters import (
    filter_films,
    filter_characters
)
from app.controllers.base_controller import list_resource

ALLOWED_FILMS_FIELDS = {"title", "episode_id", "release_date"}
ALLOWED_CHARACTERS_FIELDS = {"name", "height", "mass"}

def list_films(query_params):
    films = get_resource("films")

    data_list = list_resource(
        data=films,
        query_params=query_params,
        filter_fn=filter_films,
        allowed_order_fields=ALLOWED_FILMS_FIELDS
    )

    return {
        "count": len(data_list),
        "results": data_list
    }


def list_film_characters(film_id, query_params):
    film = get_film_by_id(film_id)

    characters = get_resources_from_urls(
        film.get("characters", [])
    )

    data_list = list_resource(
        data=characters,
        query_params=query_params,
        filter_fn=filter_characters,
        allowed_order_fields=ALLOWED_CHARACTERS_FIELDS
    )

    return {
        "film": film["title"],
        "release_date": film["release_date"],
        "total_characters": len(data_list),
        "characters": data_list
    }
