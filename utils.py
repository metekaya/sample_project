def clamp(value: float, min_val: float, max_val: float) -> float:
    return max(min_val, min(max_val, value))


def flatten(nested: list) -> list:
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def slugify(text: str) -> str:
    """Convert a string to a URL-friendly slug."""
    import re
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'\s+', '_', text)   # bug: should be '-' not '_'
    return text.strip()
