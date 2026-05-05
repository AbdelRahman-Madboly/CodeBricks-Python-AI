"""
examples/02_methods_and_loops.py
─────────────────────────────────
Topic  : Lists
Example: 2 of 3 — Iterating with loops, enumerate, zip, accumulation

Context
-------
After each training epoch, you collect loss values, compare predictions
against labels, and compute running statistics. All of this is built on
iterating lists — with and without indices, over one list or two at once.

Covers:
  - for loop over a list (direct iteration)
  - enumerate() — index + value together
  - zip() — two lists in parallel
  - Accumulating with += (sum, count, running total)
  - while loop over a list with a condition
  - sum(), min(), max(), len() on lists
  - sorted() vs .sort()

Run this file. Predict each output before you see it.
"""

# ── Direct iteration ──────────────────────────────────────────────────────────

epoch_losses = [0.91, 0.74, 0.58, 0.47, 0.39]

print("=== Training log ===")
for loss in epoch_losses:
    bar = "█" * int(loss * 20)   # visual bar scaled to loss
    print(f"  loss={loss:.2f}  {bar}")

# ── Accumulation with a loop ──────────────────────────────────────────────────

print()
print("=== Accumulation ===")

# Manual sum (same as sum(epoch_losses) — but shows the pattern)
total = 0
for loss in epoch_losses:
    total += loss
avg = total / len(epoch_losses)
print(f"Manual avg  : {avg:.4f}")
print(f"Built-in    : {sum(epoch_losses) / len(epoch_losses):.4f}")   # same

# Running total — loss at each step
running_total = 0
print("Running totals:")
for i, loss in enumerate(epoch_losses, start=1):
    running_total += loss
    print(f"  After epoch {i}: cumulative={running_total:.2f}  running_avg={running_total/i:.4f}")

# ── enumerate — index + value ────────────────────────────────────────────────

print()
print("=== enumerate ===")

checkpoints = ["epoch_01.pt", "epoch_05.pt", "epoch_10.pt", "epoch_15.pt"]

# enumerate gives (index, value) pairs
for idx, name in enumerate(checkpoints):
    print(f"  [{idx}] {name}")

print()
# 1-based indexing with start=
for rank, name in enumerate(checkpoints, start=1):
    print(f"  Checkpoint #{rank}: {name}")

# ── zip — two lists in parallel ───────────────────────────────────────────────

print()
print("=== zip — predictions vs labels ===")

predictions  = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1]
true_labels  = [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]

correct = 0
for pred, label in zip(predictions, true_labels):
    match = "✓" if pred == label else "✗"
    if pred == label:
        correct += 1
    print(f"  pred={pred}  label={label}  {match}", end="")

print(f"\n\nAccuracy: {correct}/{len(predictions)} = {correct/len(predictions):.0%}")

# ── sorted() vs .sort() ───────────────────────────────────────────────────────

print()
print("=== sorted() vs .sort() ===")

val_losses = [0.58, 0.39, 0.91, 0.47, 0.74]

# sorted() returns a NEW list — original unchanged
ascending = sorted(val_losses)
print(f"Original    : {val_losses}")    # unchanged
print(f"Ascending   : {ascending}")

# reverse=True for descending
descending = sorted(val_losses, reverse=True)
print(f"Descending  : {descending}")

# .sort() modifies IN PLACE and returns None
val_losses.sort()
print(f"After .sort(): {val_losses}")   # now sorted

# ── while loop with a condition ───────────────────────────────────────────────

print()
print("=== while loop — drain queue ===")

# Simulate processing a queue of frames until empty or error
frame_queue = [0.91, 0.83, 0.76, 0.62, 0.45]
processed   = []

while frame_queue and frame_queue[0] >= 0.70:
    conf = frame_queue.pop(0)    # take from front
    processed.append(conf)
    print(f"  Processed: {conf:.2f}")

print(f"Remaining in queue : {frame_queue}")
print(f"Processed          : {processed}")

# ── What to notice ────────────────────────────────────────────────────────────
#
# 1. Direct iteration (for item in lst) is cleaner than range(len(lst)).
#    Use range(len(lst)) only when you need to modify the list IN PLACE
#    using the index — otherwise always iterate directly.
#
# 2. enumerate() is always better than a manual counter variable.
#    The counter can't get out of sync and the code reads more clearly.
#
# 3. zip() stops at the shortest list. If predictions has 12 items and
#    true_labels has 10, zip gives you 10 pairs — no error.
#    Use itertools.zip_longest() if you need to handle unequal lengths.
#
# 4. sorted() is non-destructive — it's safe to call on data you still need.
#    .sort() is destructive — it modifies the list in place and returns None.
#    result = lst.sort() gives you None, not a sorted list — common mistake.
#
# 5. frame_queue.pop(0) is O(n) — removes the first item and shifts everything.
#    For a real queue, use collections.deque and .popleft() which is O(1).