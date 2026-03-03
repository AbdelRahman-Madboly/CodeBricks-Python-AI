"""
Lists — Examples

Covers list creation, indexing, slicing, common methods,
list comprehensions, and performance-relevant patterns.
"""


# ---------------------------------------------------------------------------
# Example 1 — Core operations and slicing
# Scenario: managing a pipeline stage queue
# ---------------------------------------------------------------------------

stages = ["load", "validate", "preprocess", "augment", "infer", "postprocess", "save"]

print(stages[0])       # load   — first item
print(stages[-1])      # save   — last item
print(stages[2:5])     # ['preprocess', 'augment', 'infer']  — slice (stop exclusive)
print(stages[::2])     # every second stage
print(stages[::-1])    # reversed order

# Modifying
stages.append("log")           # add to end
stages.insert(1, "checksum")   # insert at index 1
removed = stages.pop(1)        # remove and return "checksum"
stages.remove("augment")       # remove by value (first occurrence)

print(f"\nFinal stages ({len(stages)} steps): {stages}")


# ---------------------------------------------------------------------------
# Example 2 — List comprehensions
# Scenario: filtering and transforming confidence scores
# ---------------------------------------------------------------------------

raw_scores = [0.92, 0.45, 0.88, 0.31, 0.76, 0.95, 0.60]

# Standard loop approach
high_scores_loop = []
for score in raw_scores:
    if score >= 0.75:
        high_scores_loop.append(round(score, 2))

# Comprehension — same result, more readable
high_scores = [round(score, 2) for score in raw_scores if score >= 0.75]

print(high_scores)   # [0.92, 0.88, 0.76, 0.95]

# Transform: convert to percentage strings
score_labels = [f"{score * 100:.0f}%" for score in high_scores]
print(score_labels)  # ['92%', '88%', '76%', '95%']

# Nested comprehension: flatten a batch of frame groups
frame_batches = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
all_frames = [frame for batch in frame_batches for frame in batch]
print(all_frames)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# ---------------------------------------------------------------------------
# Example 3 — Sorting and useful patterns
# Scenario: ranking model checkpoints by validation accuracy
# ---------------------------------------------------------------------------

checkpoints = [
    {"name": "epoch_05.pt", "val_accuracy": 0.82},
    {"name": "epoch_15.pt", "val_accuracy": 0.91},
    {"name": "epoch_10.pt", "val_accuracy": 0.88},
    {"name": "epoch_20.pt", "val_accuracy": 0.89},
]

# Sort by val_accuracy descending — sorted() returns a new list (non-destructive)
ranked = sorted(checkpoints, key=lambda ckpt: ckpt["val_accuracy"], reverse=True)

print("\nRanked checkpoints:")
for rank, ckpt in enumerate(ranked, start=1):
    print(f"  {rank}. {ckpt['name']} — {ckpt['val_accuracy']:.2%}")

# Best checkpoint
best = ranked[0]
print(f"\nBest: {best['name']}")

# Accumulate — running total without importing anything
losses = [0.9, 0.7, 0.5, 0.4, 0.35]
running_avg = []
for i, loss in enumerate(losses):
    window = losses[:i + 1]
    running_avg.append(round(sum(window) / len(window), 3))
print(f"\nRunning average loss: {running_avg}")
