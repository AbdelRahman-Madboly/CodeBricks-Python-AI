"""
examples/01_types_and_inspection.py
─────────────────────────────────────
Topic  : Variables and Data Types
Example: 1 of 3 — Core types and type inspection

Context
-------
The first thing any AI script does is set up its configuration:
what model to use, how many epochs to train, what the learning
rate is, whether to use a GPU. Each of these values has a specific
type — and getting that type wrong causes crashes downstream.

This example shows all five core Python types in one real scenario,
and introduces type() and isinstance() for inspecting them.

Covers:
  - str, int, float, bool, None
  - type() and type().__name__
  - isinstance() and why it's better than type() in real code
  - Underscore separators in large numbers (readability)
  - bool as a subclass of int (the surprise)

Run this file. Predict each line's output before you see it.
"""

# ── Model configuration — all five types in one block ────────────────────────

model_name     = "distilbert-base-uncased"   # str   — the model to load
max_epochs     = 10_000                       # int   — underscores for readability
dropout_rate   = 0.15                         # float — regularization strength
use_pretrained = True                         # bool  — load pretrained weights?
checkpoint     = None                         # None  — no checkpoint loaded yet

# ── type() — inspect what Python made ────────────────────────────────────────

print("=== type() inspection ===")
print(type(model_name))      # <class 'str'>
print(type(max_epochs))      # <class 'int'>
print(type(dropout_rate))    # <class 'float'>
print(type(use_pretrained))  # <class 'bool'>
print(type(checkpoint))      # <class 'NoneType'>

# type().__name__ gives just the name — cleaner for user-facing output
print()
print("=== type().__name__ — cleaner output ===")
print(f"model_name     : {type(model_name).__name__}")
print(f"max_epochs     : {type(max_epochs).__name__}")
print(f"dropout_rate   : {type(dropout_rate).__name__}")
print(f"use_pretrained : {type(use_pretrained).__name__}")
print(f"checkpoint     : {type(checkpoint).__name__}")

# ── isinstance() — the right tool for real code ───────────────────────────────

print()
print("=== isinstance() ===")

# isinstance checks whether a value IS a given type (or a subclass of it)
print(isinstance(max_epochs, int))      # True — it's an int
print(isinstance(dropout_rate, float))  # True — it's a float
print(isinstance(model_name, str))      # True — it's a str

# The bool/int surprise:
# bool is a subclass of int in Python. True is literally stored as 1.
print(isinstance(use_pretrained, bool))  # True  — it's a bool
print(isinstance(use_pretrained, int))   # True  — bool inherits from int!

# This means True == 1 and False == 0 in Python — for real:
print(True == 1)    # True
print(False == 0)   # True
print(True + 1)     # 2  — you can do arithmetic with bools (don't, but you can)

# None is its own type — NoneType
print(isinstance(checkpoint, type(None)))  # True

# ── What to notice ────────────────────────────────────────────────────────────
#
# 1. Underscores in numbers: 10_000 is the same as 10000
#    Python ignores them — they're just for human readability.
#    Use them whenever a number has 4+ digits: 1_500_000, 0.000_001
#
# 2. type() vs isinstance()
#    type(x) == int   →  False if x is a bool (because bool != int exactly)
#    isinstance(x, int) → True if x is a bool (because bool is a subclass)
#    In real code, isinstance is almost always what you want.
#
# 3. None is not False, not 0, not ""
#    It's its own type (NoneType) with exactly one value: None.
#    Use it for "this hasn't been set yet" — like checkpoint above.
#
# 4. Why does this matter for AI?
#    Type bugs in config values are silent at assignment time and
#    loud at runtime — often deep inside a library you didn't write.
#    Knowing what type each value should be prevents those crashes.