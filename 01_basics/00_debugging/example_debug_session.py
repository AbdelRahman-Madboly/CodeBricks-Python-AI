"""
example_debug_session.py
─────────────────────────
Topic  : Debugging
Type   : Walkthrough — run this file step by step

Context
-------
You're building a function to evaluate a batch of model predictions.
The function is broken in several ways — we'll find and fix each bug
using the same workflow you'll use every day as a developer:
  add print → run → read output → fix → remove print → repeat.

This file is meant to be read and run section by section.
Uncomment one section at a time, run it, then re-comment it
before moving to the next.

The final version at the bottom is the clean, working function.
"""

# =============================================================================
# Stage 0 — The broken function
# Run it. Read the error. Don't fix anything yet — just understand it.
# =============================================================================

# def evaluate_batch(predictions, labels, threshold=0.5):
#     n_correct = 0
#     for i in range(len(predictions)):
#         if predictions[i] >= threshold:
#             predicted_class = 1
#         else
#             predicted_class = 0
#         if predicted_class == labels[i]:
#             n_correct =+ 1
#     accuracy = n_correct / len(labels)
#     return accuracy, n_correct
#
# preds  = [0.9, 0.3, 0.7, 0.1, 0.8]
# labels = [1,   0,   1,   0,   1  ]
# acc, n = evaluate_batch(preds, labels)
# print(f"Accuracy: {acc:.1%}  Correct: {n}")

# What error do you get? Where is it? What does it mean?
# Answer: SyntaxError on the 'else' line — missing colon: else:


# =============================================================================
# Stage 1 — Fix the SyntaxError. Now does it run?
# =============================================================================

# def evaluate_batch(predictions, labels, threshold=0.5):
#     n_correct = 0
#     for i in range(len(predictions)):
#         if predictions[i] >= threshold:
#             predicted_class = 1
#         else:                            # ← fixed: added colon
#             predicted_class = 0
#         if predicted_class == labels[i]:
#             n_correct =+ 1
#     accuracy = n_correct / len(labels)
#     return accuracy, n_correct
#
# preds  = [0.9, 0.3, 0.7, 0.1, 0.8]
# labels = [1,   0,   1,   0,   1  ]
# acc, n = evaluate_batch(preds, labels)
# print(f"Accuracy: {acc:.1%}  Correct: {n}")

# It runs! But the output is wrong.
# acc = 20.0%, n = 1 — should be 100%, 5 (all predictions are correct)
# There's a logic bug somewhere. Time to add print() statements.


# =============================================================================
# Stage 2 — Add prints to trace what's happening inside the loop
# =============================================================================

# def evaluate_batch(predictions, labels, threshold=0.5):
#     n_correct = 0
#     for i in range(len(predictions)):
#         if predictions[i] >= threshold:
#             predicted_class = 1
#         else:
#             predicted_class = 0
#
#         print(f"DEBUG i={i}  pred={predictions[i]:.1f}  "
#               f"class={predicted_class}  label={labels[i]}")
#
#         if predicted_class == labels[i]:
#             n_correct =+ 1
#             print(f"DEBUG   → correct! n_correct={n_correct}")
#
#     accuracy = n_correct / len(labels)
#     return accuracy, n_correct
#
# preds  = [0.9, 0.3, 0.7, 0.1, 0.8]
# labels = [1,   0,   1,   0,   1  ]
# acc, n = evaluate_batch(preds, labels)
# print(f"Accuracy: {acc:.1%}  Correct: {n}")

# Read the output carefully.
# predicted_class and label match every time — the comparison is right.
# But n_correct never gets above 1 even though "→ correct!" prints 5 times.
# The bug must be in the accumulation line: n_correct =+ 1
# Look carefully: =+ is assignment then positive. It means n_correct = (+1)
# We want +=  not  =+
# n_correct += 1  is "add 1 to n_correct"
# n_correct =+ 1  is "assign positive 1 to n_correct" → always resets to 1


# =============================================================================
# Stage 3 — Fix the logic bug. Remove debug prints. Verify.
# =============================================================================

def evaluate_batch(predictions: list[float], labels: list[int],
                   threshold: float = 0.5) -> tuple[float, int]:
    """
    Evaluate a batch of model predictions against ground-truth labels.

    Args:
        predictions: List of confidence scores in [0.0, 1.0].
        labels: List of ground-truth class labels (0 or 1).
        threshold: Decision boundary — scores >= threshold → class 1.

    Returns:
        Tuple of (accuracy, n_correct).
    """
    n_correct = 0
    for i in range(len(predictions)):
        predicted_class = 1 if predictions[i] >= threshold else 0
        if predicted_class == labels[i]:
            n_correct += 1   # ← fixed: += not =+

    accuracy = n_correct / len(labels)
    return accuracy, n_correct


# Test it
preds  = [0.9, 0.3, 0.7, 0.1, 0.8]
labels = [1,   0,   1,   0,   1  ]
acc, n = evaluate_batch(preds, labels)
print(f"Accuracy: {acc:.1%}  Correct: {n} / {len(labels)}")
# Expected: Accuracy: 100.0%  Correct: 5 / 5

# Test with a harder case
preds2  = [0.9, 0.6, 0.3, 0.4, 0.8]
labels2 = [1,   0,   1,   0,   1  ]
acc2, n2 = evaluate_batch(preds2, labels2)
print(f"Accuracy: {acc2:.1%}  Correct: {n2} / {len(labels2)}")
# Expected: Accuracy: 60.0%  Correct: 3 / 5
# (pred=0.6 misclassified as 1, pred=0.3 misclassified as 0)

# Test edge case — custom threshold
acc3, n3 = evaluate_batch(preds2, labels2, threshold=0.7)
print(f"Threshold 0.7 — Accuracy: {acc3:.1%}  Correct: {n3} / {len(labels2)}")

# =============================================================================
# Summary of bugs found and fixed
# =============================================================================
#
# Bug 1 — SyntaxError: missing colon on else clause
#   else         →  else:
#   Caught by: Python interpreter before any code ran
#
# Bug 2 — Logic error: =+ instead of +=
#   n_correct =+ 1  →  n_correct += 1
#   Caught by: adding print() statements and reading intermediate values
#   The key: the loop ran correctly (5 "→ correct!" messages) but the
#   accumulator kept resetting. Tracing n_correct after each update
#   made the problem obvious immediately.
#
# Lesson: SyntaxErrors are caught automatically. Logic bugs are silent —
# the code runs, produces output, and you have to think about whether
# the output is actually correct. Print-driven debugging is how you find them.