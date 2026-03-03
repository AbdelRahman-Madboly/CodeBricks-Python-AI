"""
Nested Lists — Exercises
"""


# ---------------------------------------------------------------------------
# Exercise 1 (Easy) — Row and column operations
#
# Problem:
#   Given the score matrix below (rows = models, cols = datasets),
#   compute and print:
#     a) The average score for each model (row average)
#     b) The best score across all models and datasets, and its position
#
#   Expected output:
#   ResNet-50      avg: 0.873
#   EfficientNet   avg: 0.920
#   MobileNet      avg: 0.848
#   Best score: 0.95 at model=EfficientNet, dataset=deepfake-v2
#
model_names = ["ResNet-50", "EfficientNet", "MobileNet"]
dataset_names = ["deepfake-v1", "deepfake-v2", "celeb-df"]

scores = [
    [0.88, 0.91, 0.83],   # ResNet-50
    [0.90, 0.95, 0.92],   # EfficientNet
    [0.85, 0.87, 0.82],   # MobileNet
]
#
# Your solution below:
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Exercise 2 (Medium) — Build and populate a grid
#
# Problem:
#   Build a multiplication table as a 2D list where table[i][j] = i * j,
#   for i and j from 1 to 5 inclusive.
#   Then print it as a formatted grid.
#
#   Expected output:
#    1  2  3  4  5
#    2  4  6  8 10
#    3  6  9 12 15
#    4  8 12 16 20
#    5 10 15 20 25
#
# Constraint: build the table using a list comprehension (no append loops)
#
# Your solution below:
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Exercise 3 (Hard) — Neighbourhood search
#
# Problem:
#   Given the 2D grid of detection confidence values below, find all cells
#   where the value is above the threshold AND at least one of its direct
#   neighbours (up, down, left, right) is BELOW the threshold.
#   These are "edge" detections — high confidence surrounded by uncertainty.
#
#   Return a list of (row, col) tuples for such cells.
#
#   Expected output:
#   Edge detections: [(0, 2), (1, 0), (1, 3), (2, 1), (2, 3), (3, 2)]
#
threshold = 0.80

confidence_grid = [
    [0.60, 0.72, 0.91, 0.65],
    [0.88, 0.75, 0.70, 0.93],
    [0.55, 0.95, 0.68, 0.90],
    [0.71, 0.66, 0.87, 0.74],
]


def find_edge_detections(grid: list[list[float]], threshold: float) -> list[tuple[int, int]]:
    """
    Find cells above the threshold that border at least one cell below it.

    Args:
        grid: 2D list of float confidence values.
        threshold: Minimum value to be considered a detection.

    Returns:
        List of (row, col) positions of edge detections.
    """
    # TODO: implement
    pass


print("Edge detections:", find_edge_detections(confidence_grid, threshold))
