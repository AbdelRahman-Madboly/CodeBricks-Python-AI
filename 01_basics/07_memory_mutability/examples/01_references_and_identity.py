"""
examples/01_references_and_identity.py
───────────────────────────────────────
Topic  : Memory and Mutability
Example: 1 of 3 — Easy
Concept: id(), variables as labels, mutable vs immutable types, is vs ==

Context
-------
Two training runs share what looks like separate configs — but a subtle
aliasing bug means changing one silently changes the other. Before fixing
it, you need to understand how Python actually stores variables in memory.
Variables are not boxes. They are labels stuck on objects.

Covers:
  - id() — the memory address of an object
  - Variables as labels (references), not containers
  - Mutable types: list, dict, set — can change in place
  - Immutable types: int, float, str, tuple — cannot change
  - is vs == — identity vs equality

Run this file. Predict each output before you see it.
"""

# ── Variables are labels, not boxes ──────────────────────────────────────────

print("=== Variables as labels ===")

# Think of objects as living in memory. Variables are sticky notes
# attached to those objects. Multiple notes can point to the same object.

lr = 0.001
print(f"id(lr)       : {id(lr)}")

backup = lr               # backup is ANOTHER label on the same float object
print(f"id(backup)   : {id(backup)}")
print(f"lr is backup : {lr is backup}")   # True — same object

# Reassigning lr creates a NEW float object and moves the label
lr = 0.01
print(f"\nAfter lr = 0.01:")
print(f"lr           : {lr}")
print(f"backup       : {backup}")   # still 0.001 — label didn't move
print(f"lr is backup : {lr is backup}")   # False — different objects now

# ── Mutable vs immutable ──────────────────────────────────────────────────────

print()
print("=== Mutable vs Immutable ===")

# IMMUTABLE — ints, floats, strings, tuples
# Python cannot change the object in place.
# "Changing" a variable just moves the label to a new object.

epochs = 10
print(f"id(epochs) before : {id(epochs)}")
epochs = 20                              # new int object created
print(f"id(epochs) after  : {id(epochs)}")   # different address

name = "ResNet"
# name[0] = "r"   # TypeError — strings can't be modified in place

# MUTABLE — lists, dicts, sets
# Python CAN change the object in place. The label stays on the same object.

pipeline = ["load", "train", "save"]
print(f"\nid(pipeline) before : {id(pipeline)}")
pipeline.append("log")                  # same object, new content
print(f"id(pipeline) after  : {id(pipeline)}")   # SAME address — object mutated

# ── is vs == ─────────────────────────────────────────────────────────────────

print()
print("=== is vs == ===")

# == checks VALUE equality — do both sides have the same content?
# is checks IDENTITY — are both sides the same object in memory?

a = [1, 2, 3]
b = [1, 2, 3]    # same content, different object

print(f"a == b : {a == b}")   # True  — same content
print(f"a is b : {a is b}")   # False — different objects

c = a             # c is ANOTHER label on the same list
print(f"a is c : {a is c}")   # True  — same object

# The small-integer cache: CPython reuses objects for small ints
x = 5
y = 5
print(f"\nx is y (small int) : {x is y}")   # True — CPython caches -5 to 256

# But don't rely on this! Use == for value comparison.
# is is for: "is this None?", "is this the same object I passed in?"

score = None
print(f"score is None : {score is None}")   # Correct way to check for None
print(f"score == None : {score == None}")   # Works but is is preferred for None

# ── What to notice ────────────────────────────────────────────────────────────
#
# 1. id() returns the memory address. Two variables with the same id() are the
#    same object — there is literally one thing in memory with two labels on it.
#
# 2. Reassigning an immutable variable (lr = 0.01) never changes the old object.
#    It creates a new object and moves the label. Other labels pointing to the
#    old object are unaffected.
#
# 3. Mutating a mutable variable (pipeline.append()) changes the object IN PLACE.
#    All labels pointing to that object see the change — that's the aliasing risk.
#
# 4. Use == to compare values. Use is only for identity checks — most commonly
#    "x is None" and "x is not None". Never write x is "string" or x is 5.
#
# 5. The small-integer cache is an implementation detail of CPython.
#    Code that relies on it will break in other Python implementations.