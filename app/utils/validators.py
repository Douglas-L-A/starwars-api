ALLOWED_ORDER_FIELDS = {"name", "height"}
ALLOWED_ORDER = {"asc", "desc"}

def validate_order_params(order_by, order):
    if order_by and order_by not in ALLOWED_ORDER_FIELDS:
        raise ValueError(f"order_by inválido. Use: {ALLOWED_ORDER_FIELDS}")
    
    if order and order not in ALLOWED_ORDER:
        raise ValueError(f"order inválido. Use: {ALLOWED_ORDER}")