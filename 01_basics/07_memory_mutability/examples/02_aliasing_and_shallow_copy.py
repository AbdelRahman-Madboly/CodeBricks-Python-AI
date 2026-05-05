"""
examples/02_aliasing_and_shallow_copy.py
──────────────────────────────────────────
Topic  : Memory and Mutability
Example: 2 of 3 — Medium
Concept: Aliasing bug, shallow copy, mutation through function arguments

Context
-------
A pipeline stores the base training config and creates per-experiment
variants. A subtle aliasing bug means that "modifying" one experiment's
config silently mutates the base config and every other experiment.
This is one of the most common bugs in data science code — catching it
requires understanding how Python passes objects to functions.

Covers:
  - Aliasing: two names, one object
  - How the aliasing bug appears in real code
  - Shallow copy: list[:], list.copy(), dict.copy()
  - What shallow copy does NOT protect — nested mutable objects
  - Mutation through function arguments (pass-by-reference behaviour)

Run this file. Predict each output before you see it.
"""

# ── The aliasing bug ──────────────────────────────────────────────────────────

print("=== Aliasing bug ===")

base_config = {"lr": 0.001, "epochs": 30, "tags": ["baseline"]}

# A developer thinks they're making a copy for experiment B
experiment_b = base_config          # NOT a copy — same object, two labels

experiment_b["lr"] = 0.01          # intending to only change experiment B
experiment_b["tags"].append("exp-b")

print(f"base_config  : {base_config}")    # lr changed too — bug!
print(f"experiment_b : {experiment_b}")  # same object

print(f"\nSame object? {base_config is experiment_b}")   # True

# ── Shallow copy fixes the top level ─────────────────────────────────────────

print()
print("=== Shallow copy ===")

base_config = {"lr": 0.001, "epochs": 30, "tags": ["baseline"]}

# .copy() creates a new dict — new container, but the VALUES are still shared
experiment_c = base_config.copy()

experiment_c["lr"] = 0.01          # only changes experiment_c — top-level key
print(f"base lr     : {base_config['lr']}")     # 0.001 — protected
print(f"exp_c lr    : {experiment_c['lr']}")    # 0.01

# But the nested list IS still shared — shallow copy doesn't go deep
experiment_c["tags"].append("exp-c")
print(f"base tags   : {base_config['tags']}")   # ['baseline', 'exp-c'] — bug!
print(f"exp_c tags  : {experiment_c['tags']}")  # ['baseline', 'exp-c']

print(f"\nSame dict?  {base_config is experiment_c}")          # False — new dict
print(f"Same tags?  {base_config['tags'] is experiment_c['tags']}")  # True — shared list

# ── List shallow copy ─────────────────────────────────────────────────────────

print()
print("=== List shallow copy ===")

stages = ["load", "preprocess", "train"]

# Three equivalent ways to shallow copy a list
copy_a = stages[:]
copy_b = stages.copy()
copy_c = list(stages)

copy_a.append("save")
print(f"stages  : {stages}")    # unchanged — top-level append is safe
print(f"copy_a  : {copy_a}")    # ['load', 'preprocess', 'train', 'save']

# Nested list — shallow copy danger
batch = [[0.91, 0.74], [0.58, 0.47]]
batch_copy = batch[:]           # new outer list, shared inner lists

batch_copy[0].append(0.99)      # mutates the inner list — shared!
print(f"\nbatch      : {batch}")       # [[0.91, 0.74, 0.99], ...] — affected
print(f"batch_copy : {batch_copy}")   # same inner lists

# ── Mutation through function arguments ───────────────────────────────────────

print()
print("=== Function arguments ===")

# Python passes object references — not copies.
# If the function mutates the object, the caller sees the change.

def add_tag(config: dict, tag: str) -> None:
    """Intended to add a tag to a config — but mutates the caller's dict."""
    config["tags"].append(tag)   # mutates the object in place

run_config = {"lr": 0.001, "tags": ["v1"]}
add_tag(run_config, "experiment")
print(f"After add_tag: {run_config['tags']}")   # ['v1', 'experiment'] — mutated

# Reassigning the parameter inside the function does NOT affect the caller
def try_replace(config: dict) -> None:
    config = {"lr": 99}    # moves the LOCAL label — caller's label unchanged

run_config2 = {"lr": 0.001}
try_replace(run_config2)
print(f"After try_replace: {run_config2}")   # {'lr': 0.001} — unchanged

# ── What to notice ────────────────────────────────────────────────────────────
#
# 1. experiment_b = base_config creates an alias — one object, two names.
#    Any mutation through either name affects the same underlying object.
#    This is the source of most "why did my config change?" bugs.
#
# 2. Shallow copy (.copy(), [:]) protects top-level keys/elements.
#    It creates a new container but shares the nested objects inside.
#    Safe for flat structures. Unsafe for nested mutable objects.
#
# 3. Python passes references to functions — not copies.
#    Mutating the object inside a function (config["tags"].append(...)) changes
#    the caller's object. Reassigning the parameter (config = {...}) only moves
#    the local label and does NOT affect the caller.
#
# 4. The safe rule: if a function receives a mutable argument and you don't
#    want to mutate it, copy it at the top of the function:
#      config = config.copy()
#
# 5. Nested mutable objects always require deepcopy for full independence.
#    You'll see the fix in the next example.