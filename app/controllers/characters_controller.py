from app.services.swampi_service import get_resource
from app.utils.filters import filter_characters
from app.controllers.base_controller import list_resource

ALLOWED_CHARACTERS_FIELDS = {"name", "height", "mass"}

def list_characters(query_params):
    characters = get_resource("people")

    list_char = list_resource(
        data=characters,
        query_params=query_params,
        filter_fn=filter_characters,
        allowed_order_fields=ALLOWED_CHARACTERS_FIELDS
    )

    return {
        "count": len(list_char),
        "results": list_char
    }
