"""
Recursion — Exercises
"""

from functools import lru_cache


# ---------------------------------------------------------------------------
# Exercise 1 (Easy) — Sum and power
#
# Problem:
#   Implement both functions recursively. No loops allowed.
#
#   a) recursive_sum(numbers) — return the sum of a list of numbers
#   b) power(base, exp) — return base ** exp for non-negative integer exp
#
#   Expected output:
#   Sum: 15
#   2^10: 1024
#
numbers = [1, 2, 3, 4, 5]


def recursive_sum(numbers: list[float]) -> float:
    """Return the sum of all numbers in the list using recursion."""
    # TODO
    pass


def power(base: float, exp: int) -> float:
    """Return base raised to exp using recursion. exp >= 0."""
    # TODO
    pass


print(f"Sum: {recursive_sum(numbers)}")
print(f"2^10: {power(2, 10)}")


# ---------------------------------------------------------------------------
# Exercise 2 (Medium) — Recursive tree depth
#
# Problem:
#   A classification tree is represented as a nested dict.
#   Each node has a "label" and optionally "children" (a list of nodes).
#   Write max_depth(node) that returns the maximum depth of the tree.
#   A single node (no children) has depth 1.
#
#   Expected output:
#   Max depth: 4
#
tree = {
    "label": "root",
    "children": [
        {
            "label": "branch_A",
            "children": [
                {"label": "leaf_A1"},
                {
                    "label": "leaf_A2",
                    "children": [
                        {"label": "deep_leaf"},
                        {"label": "deep_leaf_2",
                         "children": [{"label": "deepest"}]}
                    ]
                },
            ],
        },
        {
            "label": "branch_B",
            "children": [{"label": "leaf_B1"}],
        },
    ],
}


def max_depth(node: dict) -> int:
    """
    Return the maximum depth of a nested tree structure.
    A leaf node (no children) has depth 1.

    Args:
        node: A dict with 'label' and optional 'children' list.

    Returns:
        Maximum depth as an integer.
    """
    # TODO
    pass


print(f"Max depth: {max_depth(tree)}")


# ---------------------------------------------------------------------------
# Exercise 3 (Hard) — Memoised path counting
#
# Problem:
#   A robot starts at position (0, 0) in a grid and wants to reach (rows-1, cols-1).
#   It can only move right or down.
#   Write count_paths(rows, cols) that returns the number of unique paths.
#   Use memoisation.
#
#   Expected output:
#   2x2 grid: 2
#   3x3 grid: 6
#   5x5 grid: 70
#   10x10 grid: 48620
#
# Hint: count_paths(r, c) = count_paths(r-1, c) + count_paths(r, c-1)
# Base case: any grid with 1 row or 1 column has exactly 1 path.
#

@lru_cache(maxsize=None)
def count_paths(rows: int, cols: int) -> int:
    """
    Count unique paths from top-left to bottom-right of a rows x cols grid.
    Only right and down moves are allowed.

    Args:
        rows: Number of rows.
        cols: Number of columns.

    Returns:
        Number of unique paths.
    """
    # TODO
    pass


print(f"2x2 grid: {count_paths(2, 2)}")
print(f"3x3 grid: {count_paths(3, 3)}")
print(f"5x5 grid: {count_paths(5, 5)}")
print(f"10x10 grid: {count_paths(10, 10)}")
