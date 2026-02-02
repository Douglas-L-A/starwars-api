from app.utils.sort import sort_results
from app.utils.validators import validate_order, validate_order_by, validate_filters
from app.utils.pagination import apply_limit

def list_resource(
    *,
    data,
    query_params,
    filter_fn,
    allowed_fields
):
    validate_filters(
        query_params,
        allowed_fields.get("filters")
    )
    
    filtered = filter_fn(data, query_params)

    order_by = validate_order_by(
        query_params.get("order_by"),
        allowed_fields.get("order_by")
    )

    order = validate_order(
        query_params.get("order")
    )

    sorted_results = sort_results(
        filtered,
        order_by=order_by,
        order=order
    )

    limited_results = apply_limit(
        sorted_results,
        query_params.get("limit")
    )

    return limited_results
