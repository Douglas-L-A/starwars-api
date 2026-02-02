from werkzeug.exceptions import BadRequest

def validate_order_by(order_by, allowed_fields):
    if not order_by:
        return None

    if order_by not in allowed_fields:
        raise BadRequest(
            f"Invalid value for order_by. Allowed values: {', '.join((allowed_fields))}"
        )

    return order_by


def validate_order(order):
    if not order:
        return "asc"
    
    order = order.lower()

    if order not in ("asc", "desc"):
        raise BadRequest("Invalid value for order. Allowed values: 'asc' or 'desc'")
    
    return order


def validate_filters(query_params, allowed_fields):
    for param in query_params.keys():
        # ignora params técnicos
        if param in ("order", "order_by", "limit"):
            continue

        if param not in allowed_fields:
            raise BadRequest(
                f"Invalid filter '{param}'. Allowed filters: "
                f"{', '.join(sorted(allowed_fields))}"
            )