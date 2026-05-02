"""
exercises/03_checkpoint_search.py
──────────────────────────────────
Topic    : Control Flow
Exercise : 3 of 3 — Hard
Concept  : for/else, break, FizzBuzz variant, combined control flow

─────────────────────────────────────────────────────────────────
Task A — find_best_checkpoint()
─────────────────────────────────────────────────────────────────
Given a list of (filename, is_valid, loss) tuples, find the valid
checkpoint with the LOWEST loss. Use a for loop.

If no valid checkpoint exists, return None.
Use for/else to detect the "nothing found" case.

Signature:
  def find_best_checkpoint(
      checkpoints: list[tuple[str, bool, float]]
  ) -> str | None

─────────────────────────────────────────────────────────────────
Task B — batch_report()
─────────────────────────────────────────────────────────────────
Classic FizzBuzz — but framed as a batch report.
For batches 1 to n (inclusive), print:
  - "checkpoint" if the batch number is divisible by both 10 and 3
  - "validate"   if divisible by 10
  - "log"        if divisible by 3
  - the batch number otherwise

Signature:
  def batch_report(n: int) -> None

Expected output for n=30 (last 6 lines):
  25
  log
  validate
  28
  log
  checkpoint

─────────────────────────────────────────────────────────────────
Task C — Predict for/else behaviour (no code to write)
─────────────────────────────────────────────────────────────────
For each snippet, write a comment saying what prints. Then run it.
"""

# ── Your functions ────────────────────────────────────────────────────────────


# ── Task C — predictions ──────────────────────────────────────────────────────

# Snippet 1
for i in range(3):
    if i == 5:
        break
else:
    pass   # What prints here? Nothing? Something?
# Your prediction: ???

# Snippet 2
for i in range(6):
    if i == 3:
        break
else:
    pass
# Your prediction: does the else run? ???

# Snippet 3
items = []
for item in items:
    print("found:", item)
    break
else:
    pass  # empty list — does break ever fire? Does else run?
# Your prediction: ???


# ── Test data ─────────────────────────────────────────────────────────────────

checkpoints_a = [
    ("epoch_01.pt", True,  0.82),
    ("epoch_05.pt", False, 0.65),   # invalid
    ("epoch_10.pt", True,  0.58),   # best valid
    ("epoch_15.pt", True,  0.71),
]

checkpoints_no_valid = [
    ("epoch_01.pt", False, 0.82),
    ("epoch_05.pt", False, 0.65),
]

# ── Test calls (uncomment after writing your functions) ───────────────────────

# Task A
# print(find_best_checkpoint(checkpoints_a))          # epoch_10.pt
# print(find_best_checkpoint(checkpoints_no_valid))   # None

# Task B
# batch_report(30)