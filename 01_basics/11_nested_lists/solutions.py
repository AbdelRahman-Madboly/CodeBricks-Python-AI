"""
Nested Lists — Solutions
"""


# ---------------------------------------------------------------------------
# Solution 1
# ---------------------------------------------------------------------------

model_names = ["ResNet-50", "EfficientNet", "MobileNet"]
dataset_names = ["deepfake-v1", "deepfake-v2", "celeb-df"]

scores = [
    [0.88, 0.91, 0.83],
    [0.90, 0.95, 0.92],
    [0.85, 0.87, 0.82],
]

for name, row in zip(model_names, scores):
    avg = sum(row) / len(row)
    print(f"{name:<14} avg: {avg:.3f}")

best_val = scores[0][0]
best_model_idx = 0
best_dataset_idx = 0

for r, row in enumerate(scores):
    for c, val in enumerate(row):
        if val > best_val:
            best_val = val
            best_model_idx = r
            best_dataset_idx = c

print(
    f"Best score: {best_val} at "
    f"model={model_names[best_model_idx]}, "
    f"dataset={dataset_names[best_dataset_idx]}"
)


# ---------------------------------------------------------------------------
# Solution 2
# ---------------------------------------------------------------------------

table = [[i * j for j in range(1, 6)] for i in range(1, 6)]

for row in table:
    print(" ".join(f"{val:2d}" for val in row))


# ---------------------------------------------------------------------------
# Solution 3
# ---------------------------------------------------------------------------

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
    """
    num_rows = len(grid)
    num_cols = len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    edge_cells = []

    for r in range(num_rows):
        for c in range(num_cols):
            if grid[r][c] <= threshold:
                continue  # only interested in high-confidence cells
            # Check if any neighbour is below threshold
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < num_rows and 0 <= nc < num_cols:
                    if grid[nr][nc] < threshold:
                        edge_cells.append((r, c))
                        break  # no need to check remaining neighbours

    return edge_cells


print("Edge detections:", find_edge_detections(confidence_grid, threshold))
