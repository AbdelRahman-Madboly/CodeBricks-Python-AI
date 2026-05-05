"""
solutions/01_model_leaderboard.py
──────────────────────────────────
Topic    : Dictionaries and Sets
Solution : Exercise 1 — Model leaderboard
"""

model_names = ["ResNet-50", "EfficientNet-B4", "MobileNet-V3", "ViT-Base"]
accuracies  = [0.881, 0.942, 0.855, 0.920]

# ── Task A ────────────────────────────────────────────────────────────────────

# zip() pairs each name with its score — dict() builds the mapping
model_scores = dict(zip(model_names, accuracies))

for name, acc in model_scores.items():
    print(f"{name:<16} : {acc:.1%}")

# ── Task B ────────────────────────────────────────────────────────────────────

best_name = None
best_acc  = float("-inf")

for name, acc in model_scores.items():
    if acc > best_acc:
        best_acc  = acc
        best_name = name

print(f"\nBest model: {best_name} ({best_acc:.1%})")

# ── Task C ────────────────────────────────────────────────────────────────────

above_90 = [name for name, acc in model_scores.items() if acc >= 0.90]
print(f"Above 90%: {above_90}")

# ── Why this works ────────────────────────────────────────────────────────────
#
# Task A — dict(zip(names, values))
#   zip() pairs corresponding elements from two lists into tuples.
#   dict() turns a list of (key, value) tuples into a dict.
#   This is the idiomatic one-liner for building a dict from two parallel lists.
#   The loop version is: for name, acc in zip(model_names, accuracies): d[name] = acc
#
# Task B — running max with float("-inf")
#   Starting best_acc at negative infinity guarantees the first real value
#   always replaces it — no special case needed for the first iteration.
#   This same pattern works for find_min (start at float("inf")) and
#   for any "find the extreme value" problem.
#
# Task C — list comprehension as a filter over .items()
#   .items() yields (key, value) pairs, which you unpack directly in the for clause.
#   The condition filters inline — no intermediate variable needed.
#   This is the dict equivalent of [x for x in lst if condition(x)].