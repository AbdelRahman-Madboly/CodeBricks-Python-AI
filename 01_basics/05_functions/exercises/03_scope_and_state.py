"""
exercises/03_scope_and_state.py
────────────────────────────────
Topic    : Functions
Exercise : 3 of 3 — Hard
Concept  : Scope reasoning, mutable default fix, state via return values

Context
-------
This exercise tests whether you understand what Python actually does
with variables — not just whether the code runs, but WHY it behaves
the way it does. These are real interview questions.

─────────────────────────────────────────────────────────────────
Part A — Scope predictions
─────────────────────────────────────────────────────────────────
For each block below, write your prediction as a comment BEFORE
running. Then run the file to check. No looking things up.

─────────────────────────────────────────────────────────────────
Part B — Fix the mutable default bug
─────────────────────────────────────────────────────────────────
The function below has a mutable default bug. Fix it so each call
without an explicit history gets a fresh empty list.

─────────────────────────────────────────────────────────────────
Part C — Rewrite with no global state
─────────────────────────────────────────────────────────────────
The training loop below uses a global variable to track the best
accuracy. Rewrite it so the functions take and return state instead.
"""

# ── Part A: Scope predictions ─────────────────────────────────────────────────

# Block 1
x = 10
def f1():
    x = 99
    print(f"inside f1: {x}")

f1()
print(f"after f1: {x}")
# Your prediction before running:
# inside f1: ???
# after f1:  ???


# Block 2
y = "global"
def f2():
    print(f"inside f2: {y}")   # does this read the global?

f2()
# Your prediction:
# inside f2: ???


# Block 3
results = []
def f3(item):
    results.append(item)   # mutating a global list — does this work?

f3("epoch_1")
f3("epoch_2")
print(f"results: {results}")
# Your prediction:
# results: ???


# Block 4 — the UnboundLocalError trap
z = 5
def f4():
    # z = z + 1   # what happens if you uncomment this line?
    print(f"inside f4: {z}")

f4()
# Your prediction if the assignment line is uncommented:
# ???

# ── Part B: Fix the mutable default bug ──────────────────────────────────────

print()

# This function is broken — fix it
def record_loss(loss: float, history: list = []) -> list:
    """
    Append a loss value to the training history.

    Args:
        loss: The loss value from this epoch.
        history: Running list of losses. Default starts fresh each call.

    Returns:
        Updated history list.
    """
    history.append(loss)
    return history

# These calls should each produce a fresh single-item list
# but currently they don't — fix record_loss() above
h1 = record_loss(0.842)
h2 = record_loss(0.731)
h3 = record_loss(0.614)

print("Loss histories (should each be length 1):")
print(f"  h1: {h1}")
print(f"  h2: {h2}")
print(f"  h3: {h3}")

# This call should extend an existing history — that must still work
shared_history = [0.9, 0.85]
h4 = record_loss(0.78, shared_history)
print(f"  h4 (extended): {h4}")

# ── Part C: Rewrite with no global state ─────────────────────────────────────

print()

# BROKEN — uses global state (bad practice)
best_accuracy = 0.0

def check_and_update(accuracy: float) -> None:
    global best_accuracy
    if accuracy > best_accuracy:
        best_accuracy = accuracy
        print(f"New best: {best_accuracy:.1%}")

check_and_update(0.72)
check_and_update(0.68)
check_and_update(0.89)
print(f"Final best: {best_accuracy:.1%}")

# ─────────────────────────────────────────────────────────────
# YOUR TASK: rewrite check_and_update so it takes current_best
# as a parameter and returns the new best — no global variable.
# Then rewrite the three call sites below to match.
#
# Signature:
#   def check_and_update_clean(accuracy: float, current_best: float) -> float:
#
# Expected output:
#   New best: 72.0%
#   New best: 89.0%
#   Final best: 89.0%
# ─────────────────────────────────────────────────────────────

# Your rewritten function:


# Your rewritten call sites: