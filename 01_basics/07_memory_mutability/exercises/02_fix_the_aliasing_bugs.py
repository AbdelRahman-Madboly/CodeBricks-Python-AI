"""
exercises/02_fix_the_aliasing_bugs.py
───────────────────────────────────────
Topic    : Memory and Mutability
Exercise : 2 of 3 — Medium
Concept  : Aliasing bugs in functions, shallow vs deep copy, safe mutation

Context
-------
Three functions in a model training pipeline have aliasing bugs.
Each function unintentionally mutates data it was given — causing
silent corruption that's hard to reproduce and painful to debug.
Find the bug in each, explain it in a comment, and fix it.

─────────────────────────────────────────────────────────────────
For each function:
  PART A — Run the broken version and observe the bug
  PART B — Write a one-sentence comment explaining why it happens
  PART C — Fix the function so the test calls pass
─────────────────────────────────────────────────────────────────

Attempt before opening solutions.
"""

import copy


# ── Bug 1 — add_regularisation() ─────────────────────────────────────────────
# Should return a NEW config with regularisation added.
# Must NOT modify the original config.

def add_regularisation(config: dict, weight_decay: float) -> dict:
    config["weight_decay"] = weight_decay    # ← bug
    return config


base = {"lr": 0.001, "epochs": 30}
regularised = add_regularisation(base, 0.0001)

# Expected:
# base        → {"lr": 0.001, "epochs": 30}           (unchanged)
# regularised → {"lr": 0.001, "epochs": 30, "weight_decay": 0.0001}
print("Bug 1:")
print(f"  base        : {base}")
print(f"  regularised : {regularised}")
print()

# PART B — explanation:

# PART C — fix add_regularisation above


# ── Bug 2 — append_stage() ───────────────────────────────────────────────────
# Should return a NEW pipeline list with the stage appended.
# Must NOT modify the original pipeline.

def append_stage(pipeline: list[str], stage: str) -> list[str]:
    pipeline.append(stage)    # ← bug
    return pipeline


original_pipeline = ["load", "preprocess", "train"]
extended = append_stage(original_pipeline, "evaluate")

# Expected:
# original_pipeline → ["load", "preprocess", "train"]    (unchanged)
# extended          → ["load", "preprocess", "train", "evaluate"]
print("Bug 2:")
print(f"  original_pipeline : {original_pipeline}")
print(f"  extended          : {extended}")
print()

# PART B — explanation:

# PART C — fix append_stage above


# ── Bug 3 — branch_config() ──────────────────────────────────────────────────
# Should create two independent experiment configs from a base config.
# Modifying one experiment must NOT affect the other or the base.
# The base config has a nested "augment" dict.

def branch_config(base: dict) -> tuple[dict, dict]:
    exp_a = base.copy()     # ← insufficient for nested objects
    exp_b = base.copy()
    return exp_a, exp_b


base_cfg = {
    "lr":      0.001,
    "augment": {"flip": True, "crop": 0.8},
}

exp_a, exp_b = branch_config(base_cfg)
exp_a["augment"]["crop"] = 0.5
exp_b["augment"]["flip"] = False

# Expected:
# base_cfg augment → {"flip": True,  "crop": 0.8}   (unchanged)
# exp_a augment    → {"flip": True,  "crop": 0.5}
# exp_b augment    → {"flip": False, "crop": 0.8}
print("Bug 3:")
print(f"  base_cfg augment : {base_cfg['augment']}")
print(f"  exp_a augment    : {exp_a['augment']}")
print(f"  exp_b augment    : {exp_b['augment']}")

# PART B — explanation:

# PART C — fix branch_config above