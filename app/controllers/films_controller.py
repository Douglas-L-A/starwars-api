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
from app.utils.cache import get_cache, set_cache
from app.auth.api_key import require_api_key


ALLOWED_FILMS_FIELDS = {
    "order_by": {"title", "episode_id", "release_date"},
    "filters": {"title"}
}

ALLOWED_CHARACTERS_FIELDS = {
    "order_by": {"name", "height", "mass"},
    "filters": {"name", "gender"}
}


def list_films(query_params):
    films = get_resource("films")

    data_list = list_resource(
        data=films,
        query_params=query_params,
        filter_fn=filter_films,
        allowed_fields=ALLOWED_FILMS_FIELDS
    )

    return {
        "count": len(data_list),
        "results": data_list
    }


@require_api_key
def list_film_characters(film_id, query_params):
    cache_key = f"film:{film_id}:characters"
    cached = get_cache(cache_key)

    if cached:
        film = cached["film"]
        characters = cached["characters"]
    else:
        film_data = get_film_by_id(film_id)

        film = {
            "title": film_data["title"],
            "release_date": film_data["release_date"]
        }

        characters = get_resources_from_urls(
            film_data.get("characters", [])
        )

        set_cache(cache_key, {
            "film": film,
            "characters": characters
        }, ttl=300)

    data_list = list_resource(
        data=characters,
        query_params=query_params,
        filter_fn=filter_characters,
        allowed_fields=ALLOWED_CHARACTERS_FIELDS
    )

    return {
        "film": film["title"],
        "release_date": film["release_date"],
        "total_characters": len(data_list),
        "characters": data_list
    }
