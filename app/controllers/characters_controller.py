from app.services.swampi_service import get_resource
from app.utils.filters import filter_characters
from app.controllers.base_controller import list_resource
from app.auth.api_key import require_api_key

ALLOWED_CHARACTERS_FIELDS = {
    "order_by": {"name", "height", "mass"},
    "filters": {"name", "gender"}
}


def list_characters(query_params):
    characters = get_resource("people")

    data_list = list_resource(
        data=characters,
        query_params=query_params,
        filter_fn=filter_characters,
        allowed_fields=ALLOWED_CHARACTERS_FIELDS
    )

    return {
        "count": len(data_list),
        "results": data_list
    }
