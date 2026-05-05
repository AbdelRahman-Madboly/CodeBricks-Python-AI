"""
examples/02_frequency_and_grouping.py
───────────────────────────────────────
Topic  : Dictionaries and Sets
Example: 2 of 3 — Medium
Concept: Frequency counting, .get() accumulation, .setdefault(), dict comprehensions

Context
-------
Before training, you audit your dataset: how many samples per class,
which classes are underrepresented, and how each model's metrics compare.
All three tasks collapse into the same pattern — building and querying
dicts from raw sequences.

Covers:
  - Frequency counting with .get(key, 0) + 1
  - Grouping with .setdefault(key, []).append(value)
  - Dict comprehensions: {k: expr for k, v in ...}
  - Sorting a dict's items by value
  - Nested dicts: d[outer][inner]

Run this file. Predict each output before you see it.
"""

# ── Frequency counting ────────────────────────────────────────────────────────

print("=== Label frequency ===")

raw_labels = [
    "real", "fake", "fake", "real", "uncertain",
    "fake", "real", "fake", "real", "real",
]

# Pattern: counts[label] = counts.get(label, 0) + 1
# If the key is absent, .get returns 0 — so first occurrence sets it to 1.
counts: dict[str, int] = {}
for label in raw_labels:
    counts[label] = counts.get(label, 0) + 1

print("Raw counts:", counts)

# Sort by count descending
for label, n in sorted(counts.items(), key=lambda x: x[1], reverse=True):
    pct = n / len(raw_labels) * 100
    bar = "█" * n
    print(f"  {label:<12} {n:>3}  ({pct:.0f}%)  {bar}")

# ── Grouping with .setdefault() ───────────────────────────────────────────────

print()
print("=== Group detections by label ===")

detections = [
    {"label": "face",       "confidence": 0.94},
    {"label": "background", "confidence": 0.82},
    {"label": "face",       "confidence": 0.91},
    {"label": "hand",       "confidence": 0.78},
    {"label": "background", "confidence": 0.72},
    {"label": "face",       "confidence": 0.89},
    {"label": "hand",       "confidence": 0.91},
]

# .setdefault(key, []) returns the existing list for key, or inserts []
# and returns it — so .append() always works in one line
grouped: dict[str, list[float]] = {}
for det in detections:
    grouped.setdefault(det["label"], []).append(det["confidence"])

print("Grouped scores:")
for label, scores in grouped.items():
    avg = sum(scores) / len(scores)
    print(f"  {label:<12} samples={len(scores)}  avg={avg:.3f}  scores={scores}")

# ── Dict comprehensions ───────────────────────────────────────────────────────

print()
print("=== Dict comprehensions ===")

raw_metrics = {
    "accuracy":  0.941,
    "precision": 0.928,
    "recall":    0.955,
    "f1":        0.941,
}

# Transform values — format as percentages
formatted = {metric: f"{val:.1%}" for metric, val in raw_metrics.items()}
print("Formatted:", formatted)

# Filter — keep only metrics above 0.93
high = {k: v for k, v in raw_metrics.items() if v >= 0.93}
print("Above 93%:", high)

# Invert a dict — swap keys and values (only safe when values are unique)
model_ids = {"ResNet-50": "r50", "EfficientNet-B4": "eb4", "ViT-Base": "vit"}
id_to_name = {v: k for k, v in model_ids.items()}
print("ID → name:", id_to_name)

# ── Nested dicts ──────────────────────────────────────────────────────────────

print()
print("=== Nested dicts — run registry ===")

runs = {
    "run_001": {"model": "ResNet-50",        "val_acc": 0.881, "status": "done"},
    "run_002": {"model": "EfficientNet-B4",  "val_acc": 0.942, "status": "done"},
    "run_003": {"model": "ViT-Base",         "val_acc": 0.920, "status": "running"},
}

# Access nested value — chain the keys
print(f"run_002 model    : {runs['run_002']['model']}")
print(f"run_003 status   : {runs['run_003']['status']}")

# Find best completed run
best_run = None
best_acc  = float("-inf")
for run_id, info in runs.items():
    if info["status"] == "done" and info["val_acc"] > best_acc:
        best_acc = info["val_acc"]
        best_run = run_id

print(f"\nBest completed   : {best_run}  ({best_acc:.1%})")

# ── What to notice ────────────────────────────────────────────────────────────
#
# 1. counts.get(label, 0) + 1 is the canonical frequency-counting pattern.
#    You'll see this in every codebase. Memorise it.
#    The stdlib version is collections.Counter(raw_labels) — same result,
#    but understanding the manual version shows you what Counter does.
#
# 2. .setdefault(key, []) is cleaner than writing:
#      if key not in d: d[key] = []
#      d[key].append(value)
#    Both do the same thing. .setdefault() is preferred in production.
#
# 3. Dict comprehensions follow the same structure as list comprehensions:
#    {key_expr: val_expr for item in iterable if condition}
#    The key and value expressions can be any Python expression.
#
# 4. Chained access d[outer][inner] works because d[outer] returns a dict.
#    If outer is missing, you get KeyError on the first lookup.
#    Use d.get(outer, {}).get(inner, default) for safe nested access.
#
# 5. float("-inf") as a starting "best so far" value ensures the first
#    real value always beats it — no special-case needed for the first iteration.