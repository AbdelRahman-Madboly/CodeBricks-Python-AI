"""
solutions/01_batch_calculator.py
─────────────────────────────────
Topic    : Operators
Solution : Exercise 1 — Batch calculator
"""

dataset_size = 50_000
batch_size   = 64
epochs       = 5
initial_lr   = 2e-5

full_batches  = dataset_size // batch_size
last_batch    = dataset_size % batch_size
steps_epoch   = full_batches + (1 if last_batch > 0 else 0)
total_steps   = steps_epoch * epochs

print("  === Training Setup ===")
print(f"  Dataset       : {dataset_size:,} samples")
print(f"  Batch size    : {batch_size}")
print(f"  Full batches  : {full_batches}")
print(f"  Last batch    : {last_batch} samples")
print(f"  Steps/epoch   : {steps_epoch}")
print(f"  Total steps   : {total_steps:,}")
print(f"  Initial LR    : {initial_lr}")

# ── Why this works ────────────────────────────────────────────────────────────
#
# full_batches = dataset_size // batch_size
#   Floor division gives the count of complete batches.
#   50,000 // 64 = 781 (not 781.25 — the floor is taken).
#
# last_batch = dataset_size % batch_size
#   Modulo gives the remainder — 50,000 - (781 * 64) = 16.
#   If this is 0, the dataset divides evenly and there's no partial batch.
#
# steps_epoch = full_batches + (1 if last_batch > 0 else 0)
#   If there are leftover samples, we need one extra step to process them.
#   This is the ternary expression (one-line if/else) — covered fully in topic 04.
#   Read it as: "add 1 if last_batch is non-zero, otherwise add 0".
#
# {initial_lr} prints as 2e-05
#   Python uses scientific notation automatically for very small floats.
#   2e-5 = 0.00002 — the interpreter chooses the clearest representation.
#
# Why use // instead of int(dataset_size / batch_size)?
#   Both give the same result here, but // is the semantically correct choice:
#   "how many full batches?" is a floor division question, not a cast.
#   int() truncates toward zero; // floors toward negative infinity.
#   For positive numbers they agree — for negative numbers they don't.