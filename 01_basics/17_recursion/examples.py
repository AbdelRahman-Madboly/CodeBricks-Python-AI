"""
Recursion — Examples

Covers the base-case/recursive-case pattern, memoisation with lru_cache,
and recursion over nested structures (trees, dicts) which appear constantly
in real AI/ML configuration and data handling.
"""

from functools import lru_cache


# ---------------------------------------------------------------------------
# Example 1 — Classic recursion: factorial and Fibonacci
# Demonstrates base case, recursive case, and the memoisation speedup
# ---------------------------------------------------------------------------

def factorial(n: int) -> int:
    """
    Compute n! recursively.

    Args:
        n: Non-negative integer.

    Returns:
        n factorial.
    """
    if n == 0:          # base case
        return 1
    return n * factorial(n - 1)   # recursive case


print(factorial(6))    # 720


# Without memoisation — recomputes the same subproblems exponentially
def fib_slow(n: int) -> int:
    """Fibonacci — exponential time without caching."""
    if n <= 1:
        return n
    return fib_slow(n - 1) + fib_slow(n - 2)


# With memoisation — each value computed exactly once
@lru_cache(maxsize=None)
def fib(n: int) -> int:
    """
    Compute the nth Fibonacci number with memoisation.

    Args:
        n: Position in the sequence (0-indexed).

    Returns:
        The nth Fibonacci number.
    """
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


print([fib(i) for i in range(10)])   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# ---------------------------------------------------------------------------
# Example 2 — Recursion over nested structures
# Scenario: flattening a nested model config dict into dot-notation keys
# ---------------------------------------------------------------------------

def flatten_config(config: dict, prefix: str = "") -> dict[str, any]:
    """
    Recursively flatten a nested dict into a flat dict with dot-notation keys.

    Args:
        config: Possibly nested dictionary.
        prefix: Key prefix accumulated from parent calls.

    Returns:
        Flat dict with keys like "training.optimizer.lr".
    """
    flat: dict = {}
    for key, value in config.items():
        full_key = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict):
            # Recurse into nested dicts
            flat.update(flatten_config(value, prefix=full_key))
        else:
            flat[full_key] = value
    return flat


nested_config = {
    "model": "EfficientNet-B4",
    "training": {
        "epochs": 50,
        "optimizer": {
            "name": "Adam",
            "lr": 0.001,
        },
    },
    "data": {
        "input_size": [224, 224],
        "augment": True,
    },
}

flat = flatten_config(nested_config)
print("\nFlattened config:")
for key, value in flat.items():
    print(f"  {key}: {value}")


# ---------------------------------------------------------------------------
# Example 3 — Binary search (recursive)
# Scenario: finding a confidence threshold in a sorted list
# ---------------------------------------------------------------------------

def binary_search(
    sorted_values: list[float],
    target: float,
    low: int = 0,
    high: int | None = None,
) -> int:
    """
    Search for target in a sorted list using recursion.

    Args:
        sorted_values: Sorted list of floats.
        target: Value to find.
        low: Lower bound index (inclusive).
        high: Upper bound index (inclusive).

    Returns:
        Index of target, or -1 if not found.
    """
    if high is None:
        high = len(sorted_values) - 1

    if low > high:          # base case: search space exhausted
        return -1

    mid = (low + high) // 2

    if sorted_values[mid] == target:
        return mid
    elif sorted_values[mid] < target:
        return binary_search(sorted_values, target, mid + 1, high)
    else:
        return binary_search(sorted_values, target, low, mid - 1)


thresholds = [0.50, 0.60, 0.70, 0.80, 0.90, 0.95]
print(f"\nIndex of 0.80: {binary_search(thresholds, 0.80)}")  # 3
print(f"Index of 0.75: {binary_search(thresholds, 0.75)}")   # -1
