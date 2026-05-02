"""
examples/02_logical_and_compare.py
────────────────────────────────────
Topic  : Operators
Example: 2 of 3 — Logical operators, comparison, and short-circuit evaluation

Context
-------
Every AI pipeline makes decisions: is this sample good enough to train on?
Has the model improved enough to save a checkpoint? Is this confidence score
above the threshold?

All of those decisions come down to comparisons and logical operators.
Understanding short-circuit evaluation is the difference between clean,
idiomatic Python and verbose, fragile conditionals.

Covers:
  - Comparison operators: ==, !=, <, >, <=, >=
  - Chained comparisons: 0.0 <= x <= 1.0
  - Logical: and, or, not
  - Short-circuit evaluation — what 'and' and 'or' actually return
  - The 'or' default pattern for safe config loading
  - 'is' vs '==' — when to use each

Run this file. Predict each output before you see it.
"""

# ── Comparison operators ──────────────────────────────────────────────────────

confidence = 0.87
threshold  = 0.90

print("=== Comparisons ===")
print(f"confidence > threshold   : {confidence > threshold}")   # False
print(f"confidence >= 0.85       : {confidence >= 0.85}")       # True
print(f"confidence == 0.87       : {confidence == 0.87}")       # True
print(f"confidence != 1.0        : {confidence != 1.0}")        # True

# Chained comparisons — Python supports this natively
# Read: "is confidence between 0.0 and 1.0?"
is_valid_prob = 0.0 <= confidence <= 1.0
print(f"0.0 <= confidence <= 1.0 : {is_valid_prob}")            # True

# In most other languages you'd write: confidence >= 0.0 and confidence <= 1.0
# Python's chained form is cleaner and reads like math notation

# ── Logical operators — what they actually return ─────────────────────────────

print()
print("=== What and/or actually return ===")

# 'and' returns the first FALSY operand, or the last operand if all are truthy
print(0 and "hello")        # 0       — stopped at 0 (falsy)
print("hi" and "hello")     # hello   — both truthy, returns last
print("hi" and 0 and "bye") # 0       — stopped at 0

# 'or' returns the first TRUTHY operand, or the last operand if all are falsy
print(0 or "default")       # default — 0 is falsy, returns "default"
print("hi" or "default")    # hi      — "hi" is truthy, returns it
print(0 or "" or None)      # None    — all falsy, returns last

# 'not' always returns a bool
print(not 0)                # True
print(not "hello")          # False
print(not None)             # True

# ── Short-circuit evaluation ──────────────────────────────────────────────────

print()
print("=== Short-circuit evaluation ===")

# 'and': if the left side is falsy, the right side is NEVER evaluated
# This prevents errors when the right side depends on the left side being valid
items = []
# items[0].upper() would crash on an empty list — but it's never called
result = items and items[0].upper()
print(f"Safe access: {result}")   # [] — stopped at items (falsy empty list)

items = ["bert"]
result = items and items[0].upper()
print(f"Safe access: {result}")   # BERT — items is truthy, evaluates items[0]

# 'or': if the left side is truthy, the right side is NEVER evaluated
# This enables the default-value pattern
print()
print("=== or as default pattern ===")

raw_model  = ""       # empty string from a broken config — falsy
raw_epochs = 0        # zero from a broken config — falsy
raw_device = None     # not set — falsy

model  = raw_model  or "bert-base"  # falls back to default
epochs = raw_epochs or 20           # falls back to default
device = raw_device or "cpu"        # falls back to default

print(f"model  : {model}")    # bert-base
print(f"epochs : {epochs}")   # 20
print(f"device : {device}")   # cpu

# ── 'is' vs '==' ─────────────────────────────────────────────────────────────

print()
print("=== is vs == ===")

checkpoint = None

# 'is None' checks identity — there is only one None object
print(f"checkpoint is None     : {checkpoint is None}")    # True  — correct
print(f"checkpoint == None     : {checkpoint == None}")    # True  — works but wrong style

# 'is' is wrong for value comparison
a = 1000
b = 1000
print(f"a is b (large int)     : {a is b}")   # False — separate objects
print(f"a == b                 : {a == b}")   # True  — same value

# Use 'is' ONLY for: None, True, False
# Use '==' for everything else

# ── What to notice ────────────────────────────────────────────────────────────
#
# 1. Python's chained comparisons (0.0 <= x <= 1.0) are unique.
#    In C++/JavaScript you must write: x >= 0.0 && x <= 1.0
#    Python evaluates it as: (0.0 <= x) and (x <= 1.0) — cleaner.
#
# 2. 'and'/'or' don't return True/False — they return one of their operands.
#    This is intentional and enables the default-value pattern:
#    value = raw or default
#    It's idiomatic Python — you'll see it everywhere.
#
# 3. Short-circuit prevents unnecessary computation AND prevents errors.
#    'items and items[0]' is safe even when items is empty.
#    This is a common pattern for safe attribute/index access.
#
# 4. Always use 'is' for None checks, '==' for value checks.
#    This is a PEP 8 rule enforced by ruff/flake8 in real codebases.