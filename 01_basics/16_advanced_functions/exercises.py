"""
Advanced Functions — Exercises
"""

from typing import Callable
from functools import partial


# ---------------------------------------------------------------------------
# Exercise 1 (Easy) — Higher-order functions
#
# Problem:
#   Using map() and filter() (no list comprehensions), produce:
#     a) A list of confidence scores converted to percentages (multiplied by 100,
#        rounded to 1 decimal place)
#     b) A list of only the scores above 0.80 from the originals
#
#   Expected output:
#   Percentages : [72.0, 95.0, 61.0, 88.0, 43.0, 91.0]
#   Above 0.80  : [0.95, 0.88, 0.91]
#
scores = [0.72, 0.95, 0.61, 0.88, 0.43, 0.91]
#
# Your solution below:
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Exercise 2 (Medium) — Closure factory
#
# Problem:
#   Write a function make_label_counter() that:
#     - Takes a list of valid labels
#     - Returns a function count_labels(records) that:
#         * Counts how many records have each valid label
#         * Raises ValueError for any record with an invalid label
#         * Returns a dict mapping label → count
#
#   Expected output:
#   {'real': 3, 'fake': 4, 'uncertain': 1}
#
valid_labels = ["real", "fake", "uncertain"]
sample_records = [
    {"label": "real"},  {"label": "fake"},   {"label": "real"},
    {"label": "fake"},  {"label": "uncertain"},{"label": "fake"},
    {"label": "real"},  {"label": "fake"},
]
#
# Your solution below:
# ---------------------------------------------------------------------------

# Uncomment to test:
# count_labels = make_label_counter(valid_labels)
# print(count_labels(sample_records))


# ---------------------------------------------------------------------------
# Exercise 3 (Hard) — Pipeline with composable functions
#
# Problem:
#   Write a function compose_pipeline(*steps) that takes any number of
#   single-argument functions and returns a new function that applies them
#   left to right (first step first).
#
#   Then build a detection score pipeline that:
#     1. Clips scores to [0.0, 1.0]
#     2. Rounds to 2 decimal places
#     3. Converts to a percentage string like "94.00%"
#
#   Expected output:
#   ['-0.10 → 0.00%', '0.94 → 94.00%', '1.20 → 100.00%', '0.753 → 75.00%']
#
raw_values = [-0.10, 0.94, 1.20, 0.753]


def compose_pipeline(*steps: Callable) -> Callable:
    """
    Compose multiple single-argument functions into one pipeline.
    Applies steps left to right: result = step_n(...step_2(step_1(value))).

    Args:
        *steps: Functions to chain.

    Returns:
        A single function that applies all steps in order.
    """
    # TODO: implement
    pass


# Define the individual steps:
def clip_score(score: float) -> float:
    """Clip a score to the range [0.0, 1.0]."""
    # TODO
    pass

def round_score(score: float) -> float:
    """Round a score to 2 decimal places."""
    # TODO
    pass

def to_percentage_str(score: float) -> str:
    """Convert a 0-1 float to a percentage string like '94.00%'."""
    # TODO
    pass


# Uncomment to test:
# process_score = compose_pipeline(clip_score, round_score, to_percentage_str)
# results = [f"{v} → {process_score(v)}" for v in raw_values]
# print(results)
