"""
exercises/02_training_loop.py
──────────────────────────────
Topic    : Control Flow
Exercise : 2 of 3 — Medium
Concept  : for, while, range, enumerate, continue, break, early stopping

─────────────────────────────────────────────────────────────────
Task A — log_epochs()
─────────────────────────────────────────────────────────────────
Using a for loop with range(), print each epoch's stats.
Use enumerate() to get a 1-based epoch number alongside each loss.

Signature:
  def log_epochs(losses: list[float]) -> None

Expected output for losses = [0.91, 0.74, 0.58, 0.47, 0.39]:
  Epoch  1 | loss=0.9100
  Epoch  2 | loss=0.7400
  Epoch  3 | loss=0.5800
  Epoch  4 | loss=0.4700
  Epoch  5 | loss=0.3900

─────────────────────────────────────────────────────────────────
Task B — filter_valid_batches()
─────────────────────────────────────────────────────────────────
Given a list of (batch_id, loss, is_corrupted) tuples, return a
list of batch_ids where is_corrupted is False AND loss < 2.0.
Use continue to skip bad batches inside the loop.

Signature:
  def filter_valid_batches(batches: list[tuple]) -> list[int]

Expected for batches below:
  [1, 3, 5]

─────────────────────────────────────────────────────────────────
Task C — early_stopping_loop()
─────────────────────────────────────────────────────────────────
Simulate a training loop with early stopping.
Use a while loop. Stop when:
  - all epochs are done, OR
  - loss hasn't improved for 'patience' consecutive epochs

Return the epoch where training stopped and the best loss seen.

Signature:
  def early_stopping_loop(losses: list[float], patience: int) -> tuple[int, float]
─────────────────────────────────────────────────────────────────
"""

# ── Your functions ────────────────────────────────────────────────────────────


# ── Test data ─────────────────────────────────────────────────────────────────

losses_a = [0.91, 0.74, 0.58, 0.47, 0.39]

batches_b = [
    (1, 0.54, False),
    (2, 0.81, True),    # corrupted — skip
    (3, 1.20, False),
    (4, 2.50, False),   # loss too high — skip
    (5, 0.33, False),
    (6, 0.90, True),    # corrupted — skip
]

losses_c = [0.90, 0.75, 0.80, 0.82, 0.84, 0.60, 0.55]
# Best loss: 0.55 at epoch 7
# patience=2: loss gets worse at epochs 3,4,5 but patience=2 so stops after 2 no-improvement

# ── Test calls (uncomment after writing your functions) ───────────────────────

# Task A
# log_epochs(losses_a)

# Task B
# print(filter_valid_batches(batches_b))  # [1, 3, 5]

# Task C
# epoch, best = early_stopping_loop(losses_c, patience=2)
# print(f"Stopped at epoch {epoch}, best loss: {best}")