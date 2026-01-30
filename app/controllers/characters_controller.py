from app.services.swampi_service import get_characters
from app.utils.filters import filter_characters
from app.utils.sort import sort_results
from app.utils.pagination import apply_limit
from app.utils.validators import (
    validate_order,
    validate_order_by
)

ALLOWED_CHARACTERS_FIELDS = {"name", "height", "mass"}

def list_characters(query_params):
    characters = get_characters()
    filtered_characters = filter_characters(characters, query_params)

    order_by = validate_order_by(
        query_params.get("order_by"),
        ALLOWED_CHARACTERS_FIELDS
    )
    order = validate_order(
        query_params.get("order")
    )
    
    #limit = request.args.get("limit")

    sorted_characters = sort_results(
        filtered_characters,
        order_by=order_by,
        order = order
    )

    return {
        "count": len(sorted_characters),
        "results": sorted_characters
    }