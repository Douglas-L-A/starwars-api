def apply_limit(results, limit):
    if not limit:
        return results
    
    try:
        limit = int(limit)
    except ValueError:
        return results
    
    return results[: min(limit, 50)]