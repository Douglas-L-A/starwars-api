def validate_order_by(order_by, allowed_fields):
    if not order_by:
        return None

    if order_by not in allowed_fields:
        return None

    return order_by


def validate_order(order):
    if order and order.lower() in ("asc", "desc"):
        return order.lower()
    return "asc"
