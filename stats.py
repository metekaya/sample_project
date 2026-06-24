"""
Statistics module — intentionally incomplete.
mean() is implemented but has an off-by-one bug.
median() and mode() are stubs that raise NotImplementedError.
"""


def mean(numbers: list) -> float:
    """Return the arithmetic mean of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot compute mean of empty list")
    # bug: divides by len-1 instead of len
    return sum(numbers) / (len(numbers) - 1)


def median(numbers: list) -> float:
    """Return the median of a list of numbers."""
    raise NotImplementedError("median() is not implemented yet")


def mode(numbers: list):
    """Return the most frequent element. If tie, return the smallest."""
    raise NotImplementedError("mode() is not implemented yet")
