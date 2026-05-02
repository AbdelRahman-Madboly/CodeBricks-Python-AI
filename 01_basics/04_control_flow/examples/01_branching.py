"""
examples/01_branching.py
─────────────────────────
Topic  : Control Flow
Example: 1 of 3 — if/elif/else, ternary, guard clauses

Context
-------
After a model produces a confidence score, you need to route that output
to one of several outcomes: auto-accept, send to review, flag for attention,
or reject outright. This is one of the most common decision patterns in
deployed AI systems.

Covers:
  - if / elif / else — multiple branches
  - Only one branch runs — order matters
  - Ternary expression: value_if_true if condition else value_if_false
  - Guard clause pattern — exit early on bad conditions
  - Boolean conditions with 'and', 'or', 'not'

Run this file. Predict each output before you see it.
"""

# ── Part 1: if / elif / else — confidence router ──────────────────────────────

def route_prediction(confidence: float, label: str) -> str:
    """Route a model prediction to an outcome tier based on confidence."""
    if confidence >= 0.95:
        return f"AUTO-ACCEPT  [{label}]  ({confidence:.0%})"
    elif confidence >= 0.75:
        return f"REVIEW       [{label}]  ({confidence:.0%})"
    elif confidence >= 0.50:
        return f"FLAG         [{label}]  ({confidence:.0%})"
    else:
        return f"REJECT       [{label}]  ({confidence:.0%})"


predictions = [
    (0.97, "real"),
    (0.82, "fake"),
    (0.61, "real"),
    (0.43, "fake"),
]

print("=== Prediction Router ===")
for conf, label in predictions:
    print(" ", route_prediction(conf, label))

# ── Part 2: ternary expression — one-line if/else ────────────────────────────

print()
print("=== Ternary expressions ===")

score = 0.78

# Full if/else
if score >= 0.5:
    result = "positive"
else:
    result = "negative"
print(f"Full form   : {result}")

# Ternary — same logic, one line
result = "positive" if score >= 0.5 else "negative"
print(f"Ternary     : {result}")

# Common uses in AI output formatting
status_icon = "✓" if score >= 0.5 else "✗"
class_label = "REAL" if score >= 0.5 else "FAKE"
print(f"Icon        : {status_icon}  Label: {class_label}")

# ── Part 3: guard clauses — exit early on bad conditions ─────────────────────

print()
print("=== Guard clauses ===")

def validate_and_score(confidence: float, resolution: int,
                       is_labeled: bool) -> str:
    """
    Validate a sample before scoring. Exit early if any check fails.
    This is cleaner than a deeply nested if/elif/else tree.
    """
    # Guards — each one exits immediately if violated
    if not 0.0 <= confidence <= 1.0:
        return "ERROR: confidence out of range"
    if resolution < 360:
        return "SKIP: resolution too low"
    if not is_labeled:
        return "SKIP: not labeled"

    # If we reach here, all checks passed
    tier = "high" if confidence >= 0.8 else "low"
    return f"OK: {tier} confidence at {resolution}p"


samples = [
    (1.5,  1080, True),    # bad confidence
    (0.9,   240, True),    # bad resolution
    (0.9,  1080, False),   # not labeled
    (0.9,  1080, True),    # all good
    (0.4,   720, True),    # all good, low confidence
]

for conf, res, labeled in samples:
    print(f"  {validate_and_score(conf, res, labeled)}")

# ── What to notice ────────────────────────────────────────────────────────────
#
# 1. Only ONE branch runs in if/elif/else.
#    Python checks top to bottom and stops at the first True condition.
#    The order of conditions matters: put the most specific first.
#    In route_prediction, confidence=0.97 hits the '>= 0.95' branch and stops —
#    the '>= 0.75' branch is never evaluated.
#
# 2. Ternary: value_if_true if condition else value_if_false
#    Read it left to right: "what do I want if True, what condition, what if False".
#    Use it for single-value choices. Don't nest ternaries — use full if/else.
#
# 3. Guard clauses — early returns that handle bad cases first.
#    This keeps the "happy path" (the main logic) un-indented and clean.
#    Compare: without guards, the valid case would be nested 3 ifs deep.
#    With guards, the valid case is at the same level as the top of the function.
#
# 4. not 0.0 <= confidence <= 1.0
#    Python evaluates the chained comparison first: (0.0 <= confidence <= 1.0)
#    Then 'not' inverts it. Parentheses make it readable without changing meaning.