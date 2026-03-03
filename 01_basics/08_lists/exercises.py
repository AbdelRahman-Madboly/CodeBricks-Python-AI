"""
Lists — Exercises
"""


# ---------------------------------------------------------------------------
# Exercise 1 (Easy) — Slicing and indexing
#
# Problem:
#   Using only slicing and indexing (no loops), extract the following
#   from the frames list below:
#     a) The first 3 frames
#     b) The last 2 frames
#     c) Every other frame starting from index 0
#     d) The list in reverse order
#
#   Expected output:
#   First 3   : [1, 2, 3]
#   Last 2    : [9, 10]
#   Every other: [1, 3, 5, 7, 9]
#   Reversed  : [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#
frames = list(range(1, 11))   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# Your solution below:
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Exercise 2 (Medium) — List comprehension pipeline
#
# Problem:
#   Given the detection records below, use list comprehensions to:
#     a) Extract only the records where confidence > 0.80 AND label == "face"
#     b) From those filtered records, build a list of strings in the format:
#        "img_001: face @ 94%"
#
#   Expected output:
#   Filtered count: 2
#   ['img_001: face @ 94%', 'img_004: face @ 91%']
#
detections = [
    {"image": "img_001", "label": "face",       "confidence": 0.94},
    {"image": "img_002", "label": "background", "confidence": 0.87},
    {"image": "img_003", "label": "face",       "confidence": 0.73},
    {"image": "img_004", "label": "face",       "confidence": 0.91},
    {"image": "img_005", "label": "hand",       "confidence": 0.85},
]
#
# Your solution below:
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Exercise 3 (Hard) — Implement without built-in sort or max
#
# Problem:
#   Implement the function find_top_k() that returns the top-k highest values
#   from a list, in descending order, without using sorted(), max(), or min().
#
#   Expected output:
#   [0.97, 0.95, 0.92]
#
# Constraints:
#   - No sorted(), max(), min(), or heapq
#   - You may use any list methods (append, pop, etc.)
#   - Must work correctly for any k <= len(scores)
#
scores = [0.72, 0.95, 0.61, 0.97, 0.88, 0.92, 0.45]


def find_top_k(values: list[float], k: int) -> list[float]:
    """
    Return the k highest values from the list in descending order.

    Args:
        values: List of float scores.
        k: Number of top values to return.

    Returns:
        List of k highest values, highest first.
    """
    # TODO: implement without sorted/max/min
    pass


print(find_top_k(scores, 3))   # [0.97, 0.95, 0.92]
