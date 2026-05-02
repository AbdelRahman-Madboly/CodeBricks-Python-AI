"""
solutions/03_checkpoint_search.py
──────────────────────────────────
Topic    : Control Flow
Solution : Exercise 3 — Checkpoint search and batch report
"""


def find_best_checkpoint(checkpoints: list[tuple]) -> str | None:
    best_loss = float("inf")
    best_file = None

    for filename, is_valid, loss in checkpoints:
        if not is_valid:
            continue
        if loss < best_loss:
            best_loss = loss
            best_file = filename

    return best_file   # None if no valid checkpoint was ever found


def batch_report(n: int) -> None:
    for batch in range(1, n + 1):
        if batch % 30 == 0:       # divisible by both 10 and 3 (LCM = 30)
            print("checkpoint")
        elif batch % 10 == 0:
            print("validate")
        elif batch % 3 == 0:
            print("log")
        else:
            print(batch)


# ── Test output ───────────────────────────────────────────────────────────────

checkpoints_a = [
    ("epoch_01.pt", True,  0.82),
    ("epoch_05.pt", False, 0.65),
    ("epoch_10.pt", True,  0.58),
    ("epoch_15.pt", True,  0.71),
]
checkpoints_no_valid = [
    ("epoch_01.pt", False, 0.82),
    ("epoch_05.pt", False, 0.65),
]

print(find_best_checkpoint(checkpoints_a))          # epoch_10.pt
print(find_best_checkpoint(checkpoints_no_valid))   # None

print()
batch_report(30)

# ── Task C answers — for/else predictions ─────────────────────────────────────

# Snippet 1: range(3) → 0,1,2 — i never equals 5 → loop exhausts → else runs
# Snippet 2: range(6) → 0,1,2,3,... — i hits 3 → break fires → else does NOT run
# Snippet 3: items=[] → loop body never runs → break never fires → else DOES run

# ── Why this works ────────────────────────────────────────────────────────────
#
# find_best_checkpoint — tracking best with continue
#   We skip invalid checkpoints with continue and track the best loss seen.
#   Returning None implicitly happens when best_file is never assigned,
#   which occurs when all checkpoints are invalid (continue always fires).
#   This is cleaner than for/else for this problem because we're not just
#   looking for ANY valid checkpoint — we're looking for the BEST one.
#
# batch_report — check 30 before 10 and 3
#   Same logic as FizzBuzz: check the combined case (divisible by both) first.
#   If we checked % 10 first, batch=30 would print "validate" and never reach
#   the combined-case check. Most specific condition always goes first.
#   LCM(10, 3) = 30 — that's when both conditions are true simultaneously.
#
# for/else — the key insight (Task C)
#   The else clause runs when the loop EXHAUSTS its iterable.
#   It does NOT run when break exits the loop.
#   An empty iterable means the loop body never runs — but the loop still
#   "exhausts" (there was nothing to iterate), so else DOES run.
#   This surprises many developers — empty iterable → else runs.