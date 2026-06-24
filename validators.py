"""
Input validation helpers for the Flask API endpoints.
Each validator raises ValueError with a descriptive message on failure.
"""
from config import MAX_LIST_SIZE, MAX_STRING_LEN, CLAMP_RANGE_LIMIT


def validate_number(value, name: str = "value") -> float:
    """Accept int or float; reject anything else."""
    if not isinstance(value, (int, float)):
        raise ValueError(f"'{name}' must be a number, got {type(value).__name__}")
    if value != value:  # NaN check
        raise ValueError(f"'{name}' must not be NaN")
    return float(value)


def validate_number_list(items, name: str = "numbers") -> list:
    """Validate a list of numbers. Returns a clean list of floats."""
    if not isinstance(items, list):
        raise ValueError(f"'{name}' must be a list")
    if len(items) == 0:
        raise ValueError(f"'{name}' must not be empty")
    if len(items) > MAX_LIST_SIZE:
        raise ValueError(f"'{name}' exceeds maximum size of {MAX_LIST_SIZE}")
    result = []
    for i, item in enumerate(items):
        if not isinstance(item, (int, float)):
            raise ValueError(f"'{name}[{i}]' must be a number, got {type(item).__name__}")
        result.append(float(item))
    return result


def validate_string(value, name: str = "text") -> str:
    """Validate a non-empty string within length limits."""
    if not isinstance(value, str):
        raise ValueError(f"'{name}' must be a string")
    if len(value) == 0:
        raise ValueError(f"'{name}' must not be empty")
    if len(value) > MAX_STRING_LEN:
        raise ValueError(f"'{name}' exceeds maximum length of {MAX_STRING_LEN}")
    return value


def validate_clamp_args(value, min_val, max_val) -> tuple:
    """Validate clamp inputs and check min <= max."""
    value   = validate_number(value, "value")
    min_val = validate_number(min_val, "min")
    max_val = validate_number(max_val, "max")
    if min_val > max_val:
        raise ValueError(f"'min' ({min_val}) must be <= 'max' ({max_val})")
    if abs(min_val) > CLAMP_RANGE_LIMIT or abs(max_val) > CLAMP_RANGE_LIMIT:
        raise ValueError(f"Clamp bounds exceed limit of {CLAMP_RANGE_LIMIT}")
    return value, min_val, max_val


def validate_nested_list(items, name: str = "nested") -> list:
    """Validate a potentially nested list (no depth limit, but total elements capped)."""
    if not isinstance(items, list):
        raise ValueError(f"'{name}' must be a list")

    def _count(lst):
        total = 0
        for item in lst:
            if isinstance(item, list):
                total += _count(item)
            else:
                total += 1
        return total

    if _count(items) > MAX_LIST_SIZE:
        raise ValueError(f"'{name}' total element count exceeds {MAX_LIST_SIZE}")
    return items
