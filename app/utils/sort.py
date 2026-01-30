def sort_results(results, order_by, order):
    if not order_by:
        return results
    
    reverse = order.lower() == "desc"

    def sort_key(item):
        value = item.get(order_by)

        if value is None or value == "unknown":
            return float("inf")
        
        if isinstance(value, str):
            value = value.replace(",", "")
        
        try:
            return float(value)
        except ValueError:
            return value.lower()
        
    return sorted(results, key=sort_key, reverse=reverse)