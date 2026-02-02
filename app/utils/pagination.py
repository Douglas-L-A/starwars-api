def apply_limit(results, limit, max_limit=50):
    if limit is None:
        return results
    
    try:
        limit = int(limit)
    except (TypeError, ValueError):
        return results
    
    if limit < 1:
        return results
    
    return results[: min(limit, max_limit)]