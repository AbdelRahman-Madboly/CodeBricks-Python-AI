"""
solutions/01_predict_the_output.py
────────────────────────────────────
Topic    : Memory and Mutability
Solution : Exercise 1 — Predict the output
"""

# ── Snippet 1 ─────────────────────────────────────────────────────────────────
# Prediction: 100
# config_b = config_a creates an alias — one dict, two labels.
# config_b["epochs"] = 100 mutates the dict in place.
# config_a sees the change because it points to the same object.

config_a = {"lr": 0.001, "epochs": 30}
config_b = config_a
config_b["epochs"] = 100
print(config_a["epochs"])   # 100

# ── Snippet 2 ─────────────────────────────────────────────────────────────────
# Prediction: 30
# .copy() creates a new dict — top-level keys are independent.
# config_d["epochs"] = 100 only modifies config_d's key.

config_c = {"lr": 0.001, "epochs": 30}
config_d = config_c.copy()
config_d["epochs"] = 100
print(config_c["epochs"])   # 30

# ── Snippet 3 ─────────────────────────────────────────────────────────────────
# Prediction: ['baseline', 'v1']
# tags_b = tags_a[:] creates a new list — shallow copy is sufficient here
# because the elements (strings) are immutable.
# tags_b.append("exp") only modifies tags_b's list.

tags_a = ["baseline", "v1"]
tags_b = tags_a[:]
tags_b.append("exp")
print(tags_a)   # ['baseline', 'v1']

# ── Snippet 4 ─────────────────────────────────────────────────────────────────
# Prediction: ['baseline', 'exp']
# config_f = config_e.copy() creates a new dict — but the VALUE for "tags"
# is still the SAME list object (shallow copy doesn't recurse).
# config_f["tags"].append("exp") mutates the shared inner list.
# config_e["tags"] points to the same list — so it sees the change.

config_e = {"tags": ["baseline"]}
config_f = config_e.copy()
config_f["tags"].append("exp")
print(config_e["tags"])   # ['baseline', 'exp']

# ── Snippet 5 ─────────────────────────────────────────────────────────────────
# Prediction: [0.91, 0.74, 0.58, 0.47]  /  True
# b = a — alias, one list.
# b += [0.47] on a list calls list.__iadd__ which extends IN PLACE.
# The label b stays on the same object. a and b are still the same list.

a = [0.91, 0.74, 0.58]
b = a
b += [0.47]
print(a)        # [0.91, 0.74, 0.58, 0.47]
print(a is b)   # True

# ── Snippet 6 ─────────────────────────────────────────────────────────────────
# Prediction: 10  /  False
# y = x — both labels point to the int 10.
# y += 5 on an int creates a NEW int object (15) and moves y's label to it.
# x still points to 10. Ints are immutable — += always creates a new object.

x = 10
y = x
y += 5
print(x)        # 10
print(x is y)   # False

# ── Why this works ────────────────────────────────────────────────────────────
#
# Snippets 1 and 4 show the aliasing bug — mutation through a shared reference.
# Snippet 2 shows shallow copy protecting a flat dict.
# Snippet 3 shows shallow copy being safe when contents are immutable strings.
# Snippet 4 shows shallow copy FAILING when contents are mutable lists.
# Snippet 5 shows += on a list mutating in place — id stays the same.
# Snippet 6 shows += on an int creating a new object — id changes.
#
# The core rule: mutable objects can be changed through any label that points
# to them. Immutable objects cannot be changed at all — "changing" them
# just moves the label to a new object.