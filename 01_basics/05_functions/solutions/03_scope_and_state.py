"""
solutions/03_scope_and_state.py
────────────────────────────────
Topic    : Functions
Solution : Exercise 3 — Scope and state

Open this only after filling in your own predictions and attempting the fixes.
"""


# ── Part A: Scope answers ─────────────────────────────────────────────────────

x = 10
def f1():
    x = 99           # creates a NEW local variable — does not touch global x
    print(f"inside f1: {x}")

f1()
print(f"after f1: {x}")
# inside f1: 99     ← local x
# after f1:  10     ← global x unchanged

print()

y = "global"
def f2():
    print(f"inside f2: {y}")   # no assignment in f2 → y is read from global scope

f2()
# inside f2: global

print()

results = []
def f3(item):
    results.append(item)   # .append() MUTATES the existing list — no assignment
                           # so Python reads results from global scope just fine

f3("epoch_1")
f3("epoch_2")
print(f"results: {results}")
# results: ['epoch_1', 'epoch_2']
# Mutation of a global mutable object works — but it's risky.
# Prefer passing the list in and returning it.

print()

# Block 4 — uncommenting 'z = z + 1' would cause UnboundLocalError
# Because Python sees the assignment → marks z as local for the WHOLE function
# Then tries to read z before it's been assigned locally → crash
z = 5
def f4():
    # z = z + 1   # UnboundLocalError if uncommented
    print(f"inside f4: {z}")

f4()
# inside f4: 5

# ── Part B: Fixed mutable default ────────────────────────────────────────────

print()

def record_loss(loss: float, history: list | None = None) -> list:
    """
    Append a loss value to the training history.

    Args:
        loss: The loss value from this epoch.
        history: Running list of losses. Creates a new list if None.

    Returns:
        Updated history list.
    """
    if history is None:
        history = []    # new list created here, not at def time
    history.append(loss)
    return history


h1 = record_loss(0.842)
h2 = record_loss(0.731)
h3 = record_loss(0.614)

print("Loss histories (each length 1):")
print(f"  h1: {h1}")   # [0.842]
print(f"  h2: {h2}")   # [0.731]
print(f"  h3: {h3}")   # [0.614]

shared_history = [0.9, 0.85]
h4 = record_loss(0.78, shared_history)
print(f"  h4 (extended): {h4}")   # [0.9, 0.85, 0.78]

# ── Part C: No global state ───────────────────────────────────────────────────

print()

def check_and_update_clean(accuracy: float, current_best: float) -> float:
    """
    Return the new best accuracy, printing a message if it improved.

    Args:
        accuracy: Accuracy from this epoch.
        current_best: The best accuracy seen so far.

    Returns:
        The new best accuracy (unchanged if this epoch didn't improve).
    """
    if accuracy > current_best:
        print(f"New best: {accuracy:.1%}")
        return accuracy
    return current_best


best = 0.0
best = check_and_update_clean(0.72, best)
best = check_and_update_clean(0.68, best)
best = check_and_update_clean(0.89, best)
print(f"Final best: {best:.1%}")

# Expected output:
# New best: 72.0%
# New best: 89.0%
# Final best: 89.0%

# ── Why this works ────────────────────────────────────────────────────────────
#
# Part A — the key rules:
#   - Assignment inside a function → local variable for the ENTIRE function
#   - Reading (no assignment) → Python walks up the scope chain to global
#   - Mutation (.append, .update) → not an assignment → reads global fine
#   - This is why f3() works but f4()'s z = z + 1 would crash:
#     f3 reads and mutates, f4 would try to read before its own local assignment
#
# Part B — the None pattern:
#   if history is None: history = []
#   This creates a fresh list on EVERY call that doesn't pass one.
#   The [] is no longer in the function signature — no shared state.
#   Passing an explicit list still works because the if-branch is skipped.
#
# Part C — state via return:
#   best = check_and_update_clean(acc, best)
#   The function takes the current best IN and returns the new best OUT.
#   No global needed. The caller is responsible for tracking the state.
#   This makes the function:
#     - Pure: output depends only on inputs
#     - Testable: check_and_update_clean(0.9, 0.8) always returns 0.9
#     - Reusable: works in any context, not just this specific script