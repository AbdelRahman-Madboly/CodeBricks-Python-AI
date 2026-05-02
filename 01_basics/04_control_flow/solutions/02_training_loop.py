"""
solutions/02_training_loop.py
──────────────────────────────
Topic    : Control Flow
Solution : Exercise 2 — Training loop
"""


def log_epochs(losses: list[float]) -> None:
    for epoch, loss in enumerate(losses, start=1):
        print(f"  Epoch {epoch:>2} | loss={loss:.4f}")


def filter_valid_batches(batches: list[tuple]) -> list[int]:
    valid_ids = []
    for batch_id, loss, is_corrupted in batches:
        if is_corrupted:
            continue
        if loss >= 2.0:
            continue
        valid_ids.append(batch_id)
    return valid_ids


def early_stopping_loop(losses: list[float], patience: int) -> tuple[int, float]:
    best_loss     = float("inf")
    no_improve    = 0
    epoch         = 0

    while epoch < len(losses):
        current_loss = losses[epoch]
        epoch += 1

        if current_loss < best_loss:
            best_loss  = current_loss
            no_improve = 0
        else:
            no_improve += 1

        if no_improve >= patience:
            break

    return epoch, best_loss


# ── Test output ───────────────────────────────────────────────────────────────

losses_a = [0.91, 0.74, 0.58, 0.47, 0.39]
log_epochs(losses_a)

print()

batches_b = [
    (1, 0.54, False),
    (2, 0.81, True),
    (3, 1.20, False),
    (4, 2.50, False),
    (5, 0.33, False),
    (6, 0.90, True),
]
print(filter_valid_batches(batches_b))   # [1, 3, 5]

print()

losses_c = [0.90, 0.75, 0.80, 0.82, 0.84, 0.60, 0.55]
epoch, best = early_stopping_loop(losses_c, patience=2)
print(f"Stopped at epoch {epoch}, best loss: {best}")

# ── Why this works ────────────────────────────────────────────────────────────
#
# log_epochs — enumerate(losses, start=1)
#   start=1 gives 1-based epoch numbers without needing epoch+1 inside the loop.
#   The format spec {epoch:>2} right-aligns in 2 chars so single and double digits
#   line up neatly — same technique as the test report in topic 01.
#
# filter_valid_batches — two continue guards
#   Each continue skips the rest of the iteration independently.
#   This is cleaner than: if not is_corrupted and loss < 2.0: valid_ids.append(...)
#   because the conditions are separated and each one has a clear reason.
#
# early_stopping_loop — while + index tracking
#   We use epoch as both the index into losses[] and the epoch counter.
#   Incrementing BEFORE reading means epoch=1 after the first iteration,
#   which is the 1-based epoch number.
#   no_improve counts consecutive non-improvements. When it hits patience, break.
#   The function returns the epoch when training stopped — not the best epoch.