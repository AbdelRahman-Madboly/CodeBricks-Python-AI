"""
examples/03_comprehensions.py
──────────────────────────────
Topic  : Lists
Example: 3 of 3 — List comprehensions, key-based sorting, the shallow copy trap

Context
-------
Detection pipelines filter and transform large lists of results.
Model evaluation ranks checkpoints. Data prep builds label arrays.
All of this is cleaner with list comprehensions and sorted() with key=.

This example also shows the shallow copy trap — a bug that bites
everyone working with nested lists (images as 2D arrays, batch matrices).

Covers:
  - List comprehension: [expr for item in iterable if condition]
  - Filter, transform, filter+transform
  - Comprehension from range()
  - Nested comprehension to flatten
  - sorted() with key= and lambda
  - The * shallow copy trap with nested lists
  - Safe nested list creation with comprehension

Run this file. Predict each output before you see it.
"""

# ── Basic comprehensions ──────────────────────────────────────────────────────

print("=== Basic comprehensions ===")

raw_scores = [0.92, 0.45, 0.88, 0.31, 0.76, 0.95, 0.60]

# Filter only
high = [s for s in raw_scores if s >= 0.75]
print(f"High scores     : {high}")

# Transform only
pct = [f"{s:.0%}" for s in raw_scores]
print(f"As percentages  : {pct}")

# Filter + transform
high_pct = [f"{s:.0%}" for s in raw_scores if s >= 0.75]
print(f"High as pct     : {high_pct}")

# From range
squares = [i ** 2 for i in range(1, 6)]
print(f"Squares 1-5     : {squares}")

# Build label array
predictions = [0.9, 0.3, 0.8, 0.2, 0.7]
labels = [1 if p >= 0.5 else 0 for p in predictions]
print(f"Predicted labels: {labels}")

# ── Nested comprehension — flatten ───────────────────────────────────────────

print()
print("=== Flatten batches ===")

# A list of batches — each batch is a list of frame confidence scores
batches = [
    [0.91, 0.83, 0.72],
    [0.65, 0.88],
    [0.77, 0.93, 0.55, 0.81],
]

# Flatten: visit each batch, yield each score
all_scores = [score for batch in batches for score in batch]
print(f"All scores      : {all_scores}")
print(f"Total frames    : {len(all_scores)}")

# ── sorted() with key= ────────────────────────────────────────────────────────

print()
print("=== sorted() with key= ===")

checkpoints = [
    {"name": "epoch_05.pt", "val_acc": 0.82, "val_loss": 0.43},
    {"name": "epoch_15.pt", "val_acc": 0.91, "val_loss": 0.21},
    {"name": "epoch_10.pt", "val_acc": 0.88, "val_loss": 0.29},
    {"name": "epoch_20.pt", "val_acc": 0.89, "val_loss": 0.27},
]

# Sort by val_acc descending — best first
by_acc = sorted(checkpoints, key=lambda c: c["val_acc"], reverse=True)
print("By accuracy (best first):")
for rank, ckpt in enumerate(by_acc, start=1):
    print(f"  {rank}. {ckpt['name']}  acc={ckpt['val_acc']:.2%}  loss={ckpt['val_loss']:.3f}")

# Sort by val_loss ascending — lowest loss first
by_loss = sorted(checkpoints, key=lambda c: c["val_loss"])
print(f"\nBest by loss: {by_loss[0]['name']}")

# ── The shallow copy trap ─────────────────────────────────────────────────────

print()
print("=== Shallow copy trap ===")

# Trying to create a 3x3 matrix of zeros using * repetition
matrix_bad = [[0] * 3] * 3   # looks like 3 separate rows
print(f"Before          : {matrix_bad}")

matrix_bad[0][0] = 99        # modify ONE cell in ONE row
print(f"After [0][0]=99 : {matrix_bad}")   # ALL rows changed — bug!

# Why: [[0]*3]*3 creates 3 references to the SAME inner list
# Modifying one is modifying all of them

print()
# Correct way — comprehension creates 3 SEPARATE inner lists
matrix_good = [[0] * 3 for _ in range(3)]
print(f"Before (good)   : {matrix_good}")

matrix_good[0][0] = 99
print(f"After [0][0]=99 : {matrix_good}")  # only row 0 changed — correct

# ── What to notice ────────────────────────────────────────────────────────────
#
# 1. Comprehension syntax: [expression for variable in iterable if condition]
#    The 'if condition' is optional. The 'expression' can be any Python expression.
#
# 2. Nested comprehension reads inside out:
#    [score for batch in batches for score in batch]
#    Read: "for each batch in batches, for each score in batch, yield score"
#    The outer loop comes first in the comprehension.
#
# 3. lambda c: c["val_acc"] is an anonymous function used as the sort key.
#    It takes a checkpoint dict and returns the value to sort by.
#    You'll learn lambda properly in topic 16 (Advanced Functions).
#    For now, read it as: "sort each item by this attribute".
#
# 4. The * copy trap is one of the most common Python bugs with nested lists.
#    [[0] * 3] * 3 → one list object, 3 references to it.
#    [[0] * 3 for _ in range(3)] → 3 independent list objects.
#    This matters whenever you work with matrices, image arrays, or any 2D data.
#
# 5. _ as a loop variable means "I don't care about the value, just the count".
#    for _ in range(3) is Python idiom for "do this 3 times".