"""
solutions/01_input_guards.py
──────────────────────────────
Topic    : Exceptions
Solution : Exercise 1 — Input guards
"""


def validate_threshold(threshold: float) -> float:
    if not 0.0 <= threshold <= 1.0:
        raise ValueError(
            f"threshold must be between 0.0 and 1.0, got {threshold}"
        )
    return threshold


def get_model_config(name: str) -> dict:
    registry = {
        "ResNet-50":       {"layers": 50,  "input_size": 224},
        "EfficientNet-B4": {"layers": 380, "input_size": 380},
        "ViT-Base":        {"layers": 12,  "input_size": 224},
    }
    if name not in registry:
        raise KeyError(f"unknown model: {name!r}")
    return registry[name]


# ── Task C ────────────────────────────────────────────────────────────────────

for t in [0.75, 1.5]:
    try:
        result = validate_threshold(t)
        print(f"threshold={result} → OK")
    except ValueError as e:
        print(f"threshold={t}  → ValueError: {e}")

for model in ["ResNet-50", "AlexNet"]:
    try:
        cfg = get_model_config(model)
        print(f"model={model:<18} → {cfg}")
    except KeyError as e:
        print(f"model={model:<18} → KeyError: {e}")

# ── Why this works ────────────────────────────────────────────────────────────
#
# validate_threshold — guard clause pattern
#   Check the precondition first. If it fails, raise immediately.
#   Nothing below the raise runs. The function communicates the contract:
#   "give me a float in [0, 1] or I won't proceed."
#   The caller wraps the call and decides what to do on failure.
#
# get_model_config — explicit KeyError instead of d[key]
#   We could write `return registry[name]` and let the dict raise KeyError.
#   But the message would be just the key: 'AlexNet' — not very helpful.
#   Raising our own KeyError with f"unknown model: {name!r}" gives the caller
#   context about WHAT was not found and WHERE to look.
#
# Task C — one try/except per call
#   Each call is in its own block so a failure in one doesn't skip the rest.
#   If both calls were in a single try, the second would never run if the first raised.