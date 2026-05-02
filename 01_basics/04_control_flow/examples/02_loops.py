"""
examples/02_loops.py
─────────────────────
Topic  : Control Flow
Example: 2 of 3 — for, while, range, enumerate, zip

Context
-------
Training a model for N epochs, processing a dataset batch by batch,
comparing predictions with labels side by side — all of these are loops.
Python's for loop works on any iterable, which is why it fits AI work
so naturally.

Covers:
  - for with a list, range(), and string
  - range(start, stop, step) — all three arguments
  - enumerate() — index + value together
  - zip() — two collections in parallel
  - while loop with a counter and a condition
  - Avoiding manual index tracking

Run this file. Predict each output before you see it.
"""

# ── Part 1: for with range ────────────────────────────────────────────────────

print("=== range() variants ===")

# range(stop) — 0 to stop-1
print("Epochs:", end=" ")
for epoch in range(5):
    print(epoch, end=" ")   # 0 1 2 3 4
print()

# range(start, stop) — start to stop-1
print("Epochs 1-based:", end=" ")
for epoch in range(1, 6):
    print(epoch, end=" ")   # 1 2 3 4 5
print()

# range(start, stop, step) — every 'step' values
print("Log every 10:", end=" ")
for step in range(0, 51, 10):
    print(step, end=" ")    # 0 10 20 30 40 50
print()

# ── Part 2: enumerate — index + value ────────────────────────────────────────

print()
print("=== enumerate() ===")

checkpoints = ["epoch_01.pt", "epoch_05.pt", "epoch_10.pt", "epoch_15.pt"]

# Without enumerate — manual counter (avoid this)
i = 0
for ckpt in checkpoints:
    print(f"  [{i}] {ckpt}")
    i += 1

print()

# With enumerate — cleaner, less error-prone
for idx, ckpt in enumerate(checkpoints):
    print(f"  [{idx}] {ckpt}")

print()

# enumerate with a custom start value
for idx, ckpt in enumerate(checkpoints, start=1):
    print(f"  Checkpoint {idx}: {ckpt}")

# ── Part 3: zip — two collections in parallel ─────────────────────────────────

print()
print("=== zip() ===")

predictions = [0.92, 0.31, 0.78, 0.15, 0.88]
labels      = [1,    0,    1,    0,    1   ]

correct = 0
print("Predictions vs labels:")
for pred, label in zip(predictions, labels):
    predicted_class = 1 if pred >= 0.5 else 0
    match = "✓" if predicted_class == label else "✗"
    print(f"  pred={pred:.2f}  label={label}  {match}")
    if predicted_class == label:
        correct += 1

print(f"Accuracy: {correct}/{len(labels)} = {correct/len(labels):.0%}")

# ── Part 4: while loop — training with patience ───────────────────────────────

print()
print("=== while loop — simulated training ===")

import random
random.seed(7)

epoch      = 0
best_loss  = float("inf")
patience   = 0
max_epochs = 10
max_patience = 3

while epoch < max_epochs:
    epoch += 1
    # Simulate loss — generally decreasing with some noise
    loss = round(1.0 / epoch + random.uniform(-0.05, 0.05), 4)

    if loss < best_loss:
        best_loss = loss
        patience  = 0
        saved = " ← saved"
    else:
        patience += 1
        saved = f"  (patience {patience}/{max_patience})"

    print(f"  Epoch {epoch:>2} | loss={loss:.4f}{saved}")

    if patience >= max_patience:
        print(f"  Early stopping at epoch {epoch}")
        break

print(f"Best loss: {best_loss:.4f}")

# ── What to notice ────────────────────────────────────────────────────────────
#
# 1. range(stop) is 0-indexed and exclusive: range(5) → 0,1,2,3,4
#    range(1, 6) → 1,2,3,4,5 — use when you want 1-indexed output.
#
# 2. enumerate() is always better than a manual counter variable.
#    The counter never gets out of sync, and you can't forget to increment.
#    enumerate(items, start=1) if you want 1-based numbering.
#
# 3. zip() stops at the shortest iterable.
#    If predictions has 10 items and labels has 8, zip gives you 8 pairs.
#    This is usually what you want — use itertools.zip_longest() if not.
#
# 4. while epoch < max_epochs — the condition is checked BEFORE each iteration.
#    If epoch starts at 0 and max_epochs is 0, the loop never runs.
#    The early stopping pattern (break when patience exceeded) is standard in ML.
#
# 5. float("inf") as initial best_loss — any real loss will be less than infinity,
#    so the first epoch always "improves" and saves a checkpoint. Common pattern.