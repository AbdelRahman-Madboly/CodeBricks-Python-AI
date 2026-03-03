"""
Recursion — Solutions
"""

from functools import lru_cache


# ---------------------------------------------------------------------------
# Solution 1
# ---------------------------------------------------------------------------

def recursive_sum(numbers: list[float]) -> float:
    """Return the sum of all numbers in the list using recursion."""
    if not numbers:         # base case: empty list
        return 0
    return numbers[0] + recursive_sum(numbers[1:])


def power(base: float, exp: int) -> float:
    """Return base raised to exp using recursion."""
    if exp == 0:            # base case: anything to the power 0 is 1
        return 1
    return base * power(base, exp - 1)


numbers = [1, 2, 3, 4, 5]
print(f"Sum: {recursive_sum(numbers)}")   # 15
print(f"2^10: {power(2, 10)}")            # 1024


# ---------------------------------------------------------------------------
# Solution 2
# ---------------------------------------------------------------------------

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
    """Return the maximum depth of a nested tree structure."""
    children = node.get("children", [])
    if not children:        # base case: leaf node
        return 1
    # Depth = 1 (this node) + the deepest child
    return 1 + max(max_depth(child) for child in children)


print(f"Max depth: {max_depth(tree)}")    # 4


# ---------------------------------------------------------------------------
# Solution 3
# ---------------------------------------------------------------------------

@lru_cache(maxsize=None)
def count_paths(rows: int, cols: int) -> int:
    """
    Count unique paths from top-left to bottom-right.
    Only right and down moves allowed.
    """
    # Base case: a single row or single column has exactly one path
    if rows == 1 or cols == 1:
        return 1
    # Recursive case: paths = (paths from cell above) + (paths from cell to left)
    return count_paths(rows - 1, cols) + count_paths(rows, cols - 1)


print(f"2x2 grid: {count_paths(2, 2)}")    # 2
print(f"3x3 grid: {count_paths(3, 3)}")    # 6
print(f"5x5 grid: {count_paths(5, 5)}")    # 70
print(f"10x10 grid: {count_paths(10, 10)}") # 48620
