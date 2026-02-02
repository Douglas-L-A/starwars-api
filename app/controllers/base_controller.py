from app.utils.sort import sort_results
from app.utils.validators import validate_order, validate_order_by

def list_resource(
    *,
    data,
    query_params,
    filter_fn,
    allowed_order_fields
):
    filtered = filter_fn(data, query_params)

    order_by = validate_order_by(
        query_params.get("order_by"),
        allowed_order_fields
    )
    order = validate_order(
        query_params.get("order")
    )

    sorted_results = sort_results(
        filtered,
        order_by=order_by,
        order=order
    )

    return sorted_results
