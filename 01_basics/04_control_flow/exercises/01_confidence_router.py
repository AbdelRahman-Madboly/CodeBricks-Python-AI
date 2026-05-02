"""
exercises/01_confidence_router.py
──────────────────────────────────
Topic    : Control Flow
Exercise : 1 of 3 — Easy
Concept  : if/elif/else, ternary, boolean conditions

Context
-------
A deployed model produces a confidence score and a predicted class.
Before any prediction reaches a user, it passes through a decision
router that classifies the action to take.

─────────────────────────────────────────────────────────────────
Task A — route_output()
─────────────────────────────────────────────────────────────────
Write a function that returns an action string based on confidence:

  >= 0.95  → "auto_accept"
  >= 0.75  → "human_review"
  >= 0.50  → "flag"
  < 0.50   → "reject"

Signature:
  def route_output(confidence: float) -> str

─────────────────────────────────────────────────────────────────
Task B — format_result()
─────────────────────────────────────────────────────────────────
Write a function using a ternary expression that returns:
  "REAL" if confidence >= 0.5, otherwise "FAKE"

Signature:
  def format_result(confidence: float) -> str

─────────────────────────────────────────────────────────────────
Task C — should_alert()
─────────────────────────────────────────────────────────────────
Write a function that returns True only if ALL of:
  - confidence < 0.6         (low confidence)
  - predicted_class == 1     (predicted positive/real)
  - is_high_risk_source      (came from a flagged source)

Signature:
  def should_alert(confidence: float, predicted_class: int,
                   is_high_risk_source: bool) -> bool
─────────────────────────────────────────────────────────────────
"""

# ── Your functions ────────────────────────────────────────────────────────────


# ── Test calls (uncomment after writing your functions) ───────────────────────

# Task A
# print(route_output(0.97))   # auto_accept
# print(route_output(0.80))   # human_review
# print(route_output(0.55))   # flag
# print(route_output(0.30))   # reject

# Task B
# print(format_result(0.82))  # REAL
# print(format_result(0.34))  # FAKE
# print(format_result(0.50))  # REAL (>= 0.5)

# Task C
# print(should_alert(0.55, 1, True))   # True  — all three
# print(should_alert(0.55, 0, True))   # False — wrong class
# print(should_alert(0.55, 1, False))  # False — not high risk
# print(should_alert(0.75, 1, True))   # False — confidence too high