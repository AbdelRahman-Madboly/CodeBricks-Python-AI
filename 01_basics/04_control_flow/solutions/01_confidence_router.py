"""
solutions/01_confidence_router.py
──────────────────────────────────
Topic    : Control Flow
Solution : Exercise 1 — Confidence router
"""


def route_output(confidence: float) -> str:
    if confidence >= 0.95:
        return "auto_accept"
    elif confidence >= 0.75:
        return "human_review"
    elif confidence >= 0.50:
        return "flag"
    else:
        return "reject"


def format_result(confidence: float) -> str:
    return "REAL" if confidence >= 0.5 else "FAKE"


def should_alert(confidence: float, predicted_class: int,
                 is_high_risk_source: bool) -> bool:
    return confidence < 0.6 and predicted_class == 1 and is_high_risk_source


# ── Test output ───────────────────────────────────────────────────────────────

print(route_output(0.97))   # auto_accept
print(route_output(0.80))   # human_review
print(route_output(0.55))   # flag
print(route_output(0.30))   # reject

print(format_result(0.82))  # REAL
print(format_result(0.34))  # FAKE
print(format_result(0.50))  # REAL

print(should_alert(0.55, 1, True))   # True
print(should_alert(0.55, 0, True))   # False
print(should_alert(0.75, 1, True))   # False

# ── Why this works ────────────────────────────────────────────────────────────
#
# route_output — order matters
#   We check >= 0.95 before >= 0.75. If we reversed them, a confidence of 0.97
#   would match >= 0.75 first and return "human_review" — wrong.
#   Always order conditions from most specific (highest threshold) to least.
#
# format_result — ternary
#   "REAL" if confidence >= 0.5 else "FAKE"
#   Read: give me "REAL" if the condition is True, "FAKE" if False.
#   Equivalent to a 2-line if/else but appropriate here since it's one value.
#
# should_alert — single 'and' expression
#   All three conditions must be True simultaneously.
#   'and' short-circuits: if confidence >= 0.6, the other two are never checked.
#   Returning the boolean expression directly (not wrapping in if/return True/return False)
#   is cleaner and more Pythonic.