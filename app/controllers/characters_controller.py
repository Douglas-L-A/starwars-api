from app.services.swampi_service import get_characters
from app.utils.filters import filter_characters
from app.utils.sort import sort_results
from app.utils.pagination import apply_limit
from app.utils.validators import validate_order_params

def list_characters(request):
    characters = get_characters()

    filters = {
        "name": request.args.get("name"),
        "gender": request.args.get("gender")
    }

    order_by = request.args.get("order_by")
    order = request.args.get("order", "asc")
    limit = request.args.get("limit")

    validate_order_params(order_by, order)

    characters = filter_characters(characters, filters)
    characters = sort_results(characters, order_by, order)
    characters = apply_limit(characters, limit)

    return {
        "count": len(characters),
        "results": characters
    }