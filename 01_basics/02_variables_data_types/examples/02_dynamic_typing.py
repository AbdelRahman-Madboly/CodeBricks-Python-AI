"""
examples/02_dynamic_typing.py
──────────────────────────────
Topic  : Variables and Data Types
Example: 2 of 3 — Dynamic typing and the label mental model

Context
-------
Python is dynamically typed — the type of a variable is determined
by what you assign to it, not by how you declared it.

This is very different from C++, where you write:
    int epochs = 10;    // type is locked at declaration

In Python you just write:
    epochs = 10         # Python figures out it's an int

This example shows what this means in practice, where it's useful,
and where it leads you into trouble.

Covers:
  - Dynamic typing — the same name can hold different types
  - The label/object mental model (id() to see memory address)
  - Variable reassignment — what actually happens in memory
  - Why changing a variable's type is a bad idea
  - None as a "not yet set" placeholder

Run this file. Predict each line's output before you see it.
"""

# ── The label mental model — id() shows memory address ───────────────────────

print("=== Labels and memory addresses ===")

accuracy = 0.94
print(f"accuracy = {accuracy}  |  id: {id(accuracy)}")

accuracy = 0.97
print(f"accuracy = {accuracy}  |  id: {id(accuracy)}")
# The id changed — a new object was created, the label moved to it

# Two labels can point to the same object:
a = 42
b = a
print(f"a id: {id(a)}  |  b id: {id(b)}")  # same id — same object
# This is why mutating shared objects causes bugs — but that's topic 07.

# ── Dynamic typing in practice ────────────────────────────────────────────────

print()
print("=== Dynamic typing ===")

# This is valid Python — the type changes each assignment
config_value = "auto"
print(f"Stage 1 | config_value = {config_value!r}  ({type(config_value).__name__})")
# !r adds repr() formatting — shows the quotes around strings

config_value = 0.001
print(f"Stage 2 | config_value = {config_value}  ({type(config_value).__name__})")

config_value = True
print(f"Stage 3 | config_value = {config_value}  ({type(config_value).__name__})")

# Python never complains — but this is hard to read and debug.

# ── The right way — descriptive names, one type per name ─────────────────────

print()
print("=== The right way ===")

# Bad: same name, type changes mid-script
lr = "auto"        # placeholder
lr = 0.001         # overwrites — what was the original value?

# Good: separate names, clear purpose
lr_config_raw = "auto"      # what was read from config file (str)
lr = 0.001                  # the resolved value used for training (float)

print(f"Raw config : {lr_config_raw!r}")
print(f"Resolved   : {lr}")

# ── None as a placeholder ─────────────────────────────────────────────────────

print()
print("=== None as placeholder ===")

# Common pattern: set to None until the value is determined
best_model   = None
best_accuracy = None

# ... training would happen here ...
# For now, simulate that training finished:
best_model    = "distilbert-epoch-3"
best_accuracy = 0.9312

# Check before using:
if best_model is None:
    print("No model trained yet.")
else:
    print(f"Best model    : {best_model}")
    print(f"Best accuracy : {best_accuracy:.2%}")

# Always use 'is None' not '== None'
# 'is' checks identity (same object), '==' checks value equality
# None should be compared by identity — there is only one None object
result = None
print(f"result is None : {result is None}")   # True  — correct
print(f"result == None : {result == None}")   # True  — works but wrong style

# ── What to notice ────────────────────────────────────────────────────────────
#
# 1. id() returns the memory address of the object a variable points to.
#    When you reassign, the id changes — a new object was created.
#    This proves that variables are labels, not boxes.
#
# 2. !r in f-strings calls repr() on the value.
#    repr() gives you a developer-friendly view: strings get quotes,
#    None appears as None rather than an empty string.
#    Use !r when logging values for debugging.
#
# 3. Dynamic typing is not the same as "no types".
#    Every object in Python has a type — you just don't declare it upfront.
#    The type is determined when the object is created, not when the
#    variable name is declared.
#
# 4. In Phase 5 (typing_quality), you'll write:
#    lr: float = 0.001
#    This is a type hint — it doesn't change runtime behaviour,
#    but tools like mypy will warn you if you assign the wrong type.