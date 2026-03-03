"""
Nested Lists — Examples

Covers 2D list creation, indexing, traversal, the * copy trap,
transpose, and neighbourhood operations used in grid-based problems.
"""


# ---------------------------------------------------------------------------
# Example 1 — Creating and indexing a 2D grid
# Scenario: a confusion matrix for a binary classifier
# ---------------------------------------------------------------------------

# Rows: actual class | Columns: predicted class
#               pred_real  pred_fake
confusion = [
    [850,  50],   # actual: real
    [ 30, 720],   # actual: fake
]

# Access: [row][col]
true_positives = confusion[1][1]   # actual fake, predicted fake
false_positives = confusion[0][1]  # actual real, predicted fake

print(f"True positives : {true_positives}")
print(f"False positives: {false_positives}")

precision = true_positives / (true_positives + false_positives)
print(f"Precision      : {precision:.3f}")


# ---------------------------------------------------------------------------
# Example 2 — Safe grid creation vs the * trap
# Scenario: initialising a blank grid for a dynamic programming table
# ---------------------------------------------------------------------------

rows, cols = 4, 5

# WRONG — all rows are the same list object
wrong_grid = [[0] * cols] * rows
wrong_grid[0][0] = 99
print("Wrong grid row 1:", wrong_grid[1])  # also 99! — shared reference

# CORRECT — each row is a new independent list
grid = [[0] * cols for _ in range(rows)]
grid[0][0] = 99
print("Correct grid row 1:", grid[1])      # still 0 — independent


# ---------------------------------------------------------------------------
# Example 3 — Traversal, transpose, and neighbourhood
# Scenario: image convolution prep — scanning pixel neighbourhoods
# ---------------------------------------------------------------------------

# 5x5 grayscale patch (pixel intensities 0-255)
patch = [
    [100, 120, 130, 115, 105],
    [110,  90,  85, 100, 120],
    [130,  80,  75,  95, 125],
    [120,  95,  88, 102, 118],
    [108, 115, 122, 110, 100],
]

# Compute the average of the entire patch
total = sum(cell for row in patch for cell in row)
average = total / (len(patch) * len(patch[0]))
print(f"\nPatch average: {average:.1f}")

# Transpose — swap rows and columns
transposed = [list(row) for row in zip(*patch)]
print(f"Original  [0]: {patch[0]}")
print(f"Transposed[0]: {transposed[0]}")   # first column of original

# Find the minimum value and its position
min_val = patch[0][0]
min_pos = (0, 0)
for r, row in enumerate(patch):
    for c, val in enumerate(row):
        if val < min_val:
            min_val = val
            min_pos = (r, c)

print(f"\nMin pixel: {min_val} at row={min_pos[0]}, col={min_pos[1]}")
