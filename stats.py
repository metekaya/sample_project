"""Statistics module."""


def mean(numbers: list) -> float:
    """Return the arithmetic mean of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot compute mean of empty list")
    return sum(numbers) / len(numbers)


def median(numbers: list) -> float:
    """Return the median of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot compute median of empty list")
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 1:
        return sorted_numbers[mid]
    return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2


def mode(numbers: list):
    """Return the most frequent element. If tie, return the smallest."""
    if not numbers:
        raise ValueError("Cannot compute mode of empty list")
    counts = {}
    for value in numbers:
        counts[value] = counts.get(value, 0) + 1
    max_count = max(counts.values())
    candidates = [value for value, count in counts.items() if count == max_count]
    return min(candidates)
