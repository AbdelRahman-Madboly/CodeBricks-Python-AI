"""
exercises/01_predict_the_output.py
────────────────────────────────────
Topic    : Memory and Mutability
Exercise : 1 of 3 — Easy
Concept  : References, aliasing, is vs ==, shallow copy

Context
-------
Before you can fix aliasing bugs, you need to predict them.
Each snippet below comes from real mistakes made in ML pipelines.
For each one: predict the output, then run and verify.

─────────────────────────────────────────────────────────────────
Rules
─────────────────────────────────────────────────────────────────
- Write your prediction as a comment BEFORE uncommenting the print
- Do not run any snippet until you have written ALL predictions
- After running, write a one-sentence explanation for any that
  surprised you
─────────────────────────────────────────────────────────────────

Attempt before opening solutions.
"""

# ── Snippet 1 ─────────────────────────────────────────────────────────────────

config_a = {"lr": 0.001, "epochs": 30}
config_b = config_a
config_b["epochs"] = 100

# Prediction:
# print(config_a["epochs"]) →

print(config_a["epochs"])


# ── Snippet 2 ─────────────────────────────────────────────────────────────────

config_c = {"lr": 0.001, "epochs": 30}
config_d = config_c.copy()
config_d["epochs"] = 100

# Prediction:
# print(config_c["epochs"]) →

print(config_c["epochs"])


# ── Snippet 3 ─────────────────────────────────────────────────────────────────

tags_a = ["baseline", "v1"]
tags_b = tags_a[:]
tags_b.append("exp")

# Prediction:
# print(tags_a) →

print(tags_a)


# ── Snippet 4 ─────────────────────────────────────────────────────────────────

config_e = {"tags": ["baseline"]}
config_f = config_e.copy()
config_f["tags"].append("exp")

# Prediction:
# print(config_e["tags"]) →

print(config_e["tags"])


# ── Snippet 5 ─────────────────────────────────────────────────────────────────

a = [0.91, 0.74, 0.58]
b = a
b += [0.47]

# Prediction:
# print(a) →
# print(a is b) →

print(a)
print(a is b)


# ── Snippet 6 ─────────────────────────────────────────────────────────────────

x = 10
y = x
y += 5

# Prediction:
# print(x) →
# print(x is y) →

print(x)
print(x is y)