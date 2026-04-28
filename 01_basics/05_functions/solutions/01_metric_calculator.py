"""
solutions/01_metric_calculator.py
──────────────────────────────────
Topic    : Functions
Solution : Exercise 1 — Metric calculator

Open this only after a genuine attempt at the exercise.
"""


def accuracy(correct: int, total: int) -> float:
    """
    Calculate classification accuracy.

    Args:
        correct: Number of correct predictions.
        total: Total number of predictions.

    Returns:
        Accuracy as a float between 0.0 and 1.0.
    """
    return correct / total


def clamp(value: float, min_val: float = 0.0, max_val: float = 1.0) -> float:
    """
    Restrict a value to [min_val, max_val].

    Args:
        value: The number to clamp.
        min_val: Lower bound (default 0.0).
        max_val: Upper bound (default 1.0).

    Returns:
        value if within range, otherwise the nearest bound.
    """
    if value < min_val:
        return min_val
    if value > max_val:
        return max_val
    return value


def normalize(value: float, min_val: float, max_val: float) -> float:
    """
    Normalize value to [0.0, 1.0] using min-max scaling.

    Args:
        value: The raw value to normalize.
        min_val: Lower bound of the input range.
        max_val: Upper bound of the input range.

    Returns:
        Normalized float in [0.0, 1.0].
    """
    normalized = (value - min_val) / (max_val - min_val)
    return clamp(normalized)   # reuse clamp to guarantee the range


# ── Test output ───────────────────────────────────────────────────────────────

print(f"Accuracy: {accuracy(7, 8):.1%}")    # 87.5%
print(f"Accuracy: {accuracy(10, 10):.1%}")  # 100.0%
print(f"Accuracy: {accuracy(0, 5):.1%}")    # 0.0%

print(clamp(-0.5))   # 0.0
print(clamp(0.75))   # 0.75
print(clamp(1.8))    # 1.0

print(f"{normalize(0, 0, 255):.4f}")      # 0.0000
print(f"{normalize(128, 0, 255):.4f}")    # 0.5020
print(f"{normalize(255, 0, 255):.4f}")    # 1.0000
print(f"{normalize(150, 100, 200):.4f}")  # 0.5000

# ── Why this works ────────────────────────────────────────────────────────────
#
# accuracy(correct, total)
#   Single division. No need to multiply by 100 — store as a fraction,
#   format with :.1% when you need to display. This keeps the value
#   mathematically clean for further computation.
#
# clamp()
#   Two independent if statements, not if/elif/else.
#   Either condition can be true — no need to chain them.
#   Reading: "if too low, floor it. If too high, ceiling it. Otherwise keep it."
#
# normalize() calling clamp()
#   This is function composition — using one function inside another.
#   normalize() handles the math, clamp() handles the boundary guarantee.
#   If the input is outside the min/max range (e.g. a sensor spike),
#   clamp() prevents the result from going outside [0, 1].
#   Each function does ONE job. Together they do something useful.
#
# No print() inside any function.
#   These functions return values — they don't decide how to display them.
#   The caller decides the format (:.4f vs :.1% vs just the raw float).
#   This separation of concerns is what makes functions reusable.