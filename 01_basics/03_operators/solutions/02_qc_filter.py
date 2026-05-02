"""
solutions/02_qc_filter.py
──────────────────────────
Topic    : Operators
Solution : Exercise 2 — QC filter
"""


def passes_qc(height: int, confidence: float,
              is_blurry: bool, codec: str) -> bool:
    return (
        height >= 720
        and confidence > 0.85
        and not is_blurry
        and codec in ("h264", "h265")
    )


def qc_reason(height: int, confidence: float,
              is_blurry: bool, codec: str) -> str:
    if height < 720:
        return "low resolution"
    if confidence <= 0.85:
        return "low confidence"
    if is_blurry:
        return "blurry"
    if codec not in ("h264", "h265"):
        return "bad codec"
    return "ok"


# Task C — short-circuit defaults
raw_model  = ""
raw_epochs = 0
raw_device = None
raw_tag    = "experiment-1"

default_model  = "resnet-50"
default_epochs = 30
default_device = "cuda"
default_tag    = "untagged"

model  = raw_model  or default_model
epochs = raw_epochs or default_epochs
device = raw_device or default_device
tag    = raw_tag    or default_tag

print(f"model  : {model}")
print(f"epochs : {epochs}")
print(f"device : {device}")
print(f"tag    : {tag}")

# ── Why this works ────────────────────────────────────────────────────────────
#
# passes_qc — multi-line 'and' expression
#   All four conditions must be True for the function to return True.
#   The parentheses allow spreading across lines for readability.
#   Python evaluates left to right and short-circuits:
#   if height < 720, the rest are never evaluated.
#
# codec in ("h264", "h265")
#   'in' checks membership in a tuple. This is cleaner than:
#   codec == "h264" or codec == "h265"
#   Both work — the 'in' form scales better as the list grows.
#
# qc_reason — guard clause pattern
#   Each early return is called a "guard clause" — it exits as soon as
#   a failure condition is found. This avoids deeply nested if/elif/else.
#   The function reads as a checklist: check each condition, return on first fail.
#
# raw_tag or default_tag → "experiment-1"
#   raw_tag = "experiment-1" is already truthy — the 'or' short-circuits
#   and returns "experiment-1" immediately. default_tag is never used.
#   This shows the 'or' pattern works correctly even when the raw value IS set.