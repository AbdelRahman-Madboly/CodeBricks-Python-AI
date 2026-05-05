"""
solutions/02_fix_the_aliasing_bugs.py
───────────────────────────────────────
Topic    : Memory and Mutability
Solution : Exercise 2 — Fix the aliasing bugs
"""

import copy


# ── Bug 1 — add_regularisation() ─────────────────────────────────────────────
# Explanation: the function receives a reference to the caller's dict.
# config["weight_decay"] = weight_decay mutates the caller's object in place.
# Returning config returns the same object — not a new one.

def add_regularisation(config: dict, weight_decay: float) -> dict:
    config = config.copy()                  # new top-level dict — safe for flat configs
    config["weight_decay"] = weight_decay
    return config


base = {"lr": 0.001, "epochs": 30}
regularised = add_regularisation(base, 0.0001)
print("Bug 1:")
print(f"  base        : {base}")            # {"lr": 0.001, "epochs": 30}
print(f"  regularised : {regularised}")     # with weight_decay added
print()


# ── Bug 2 — append_stage() ───────────────────────────────────────────────────
# Explanation: list.append() mutates the list in place.
# The function receives a reference to the caller's list, appends to it,
# then returns that same list — the caller's original is permanently changed.

def append_stage(pipeline: list[str], stage: str) -> list[str]:
    pipeline = pipeline[:]      # shallow copy is sufficient — strings are immutable
    pipeline.append(stage)
    return pipeline


original_pipeline = ["load", "preprocess", "train"]
extended = append_stage(original_pipeline, "evaluate")
print("Bug 2:")
print(f"  original_pipeline : {original_pipeline}")   # unchanged
print(f"  extended          : {extended}")
print()


# ── Bug 3 — branch_config() ──────────────────────────────────────────────────
# Explanation: .copy() creates a new dict but the nested "augment" dict is
# still shared between base, exp_a, and exp_b. Modifying exp_a["augment"]["crop"]
# mutates the shared inner dict — visible through all three names.

def branch_config(base: dict) -> tuple[dict, dict]:
    exp_a = copy.deepcopy(base)   # fully independent — nested objects copied too
    exp_b = copy.deepcopy(base)
    return exp_a, exp_b


base_cfg = {
    "lr":      0.001,
    "augment": {"flip": True, "crop": 0.8},
}

exp_a, exp_b = branch_config(base_cfg)
exp_a["augment"]["crop"] = 0.5
exp_b["augment"]["flip"] = False
print("Bug 3:")
print(f"  base_cfg augment : {base_cfg['augment']}")   # {"flip": True, "crop": 0.8}
print(f"  exp_a augment    : {exp_a['augment']}")      # {"flip": True, "crop": 0.5}
print(f"  exp_b augment    : {exp_b['augment']}")      # {"flip": False, "crop": 0.8}

# ── Why this works ────────────────────────────────────────────────────────────
#
# Bug 1 — copy at the top of the function
#   config = config.copy() inside the function moves the LOCAL label config
#   to a new dict. The caller's original dict is unaffected.
#   A flat dict (no nested mutable values) only needs shallow copy.
#
# Bug 2 — same principle for lists
#   pipeline = pipeline[:] creates a new list. Appending to it doesn't touch
#   the caller's original. Strings inside are immutable — shallow copy is safe.
#
# Bug 3 — nested structures need deepcopy
#   .copy() on a dict creates a new container but the values (including nested
#   dicts and lists) are still shared references. Any mutation to a nested object
#   propagates through all copies that share it.
#   copy.deepcopy() recurses into every nested object and copies each one,
#   producing a completely independent tree of objects.