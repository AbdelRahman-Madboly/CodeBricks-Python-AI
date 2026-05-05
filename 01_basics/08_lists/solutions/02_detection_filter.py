"""
solutions/02_detection_filter.py
─────────────────────────────────
Topic    : Lists
Solution : Exercise 2 — Detection filter
"""

detections = [
    {"image": "img_001", "label": "face",       "confidence": 0.94},
    {"image": "img_002", "label": "background", "confidence": 0.87},
    {"image": "img_003", "label": "face",       "confidence": 0.73},
    {"image": "img_004", "label": "face",       "confidence": 0.91},
    {"image": "img_005", "label": "hand",       "confidence": 0.85},
]

epoch_losses = [0.91, 0.74, 0.82, 0.58, 0.39]

predictions = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1]
true_labels = [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]

# ── Task A ────────────────────────────────────────────────────────────────────

result = [
    f"{d['image']}: {d['label']} @ {d['confidence']:.0%}"
    for d in detections
    if d["confidence"] > 0.80 and d["label"] == "face"
]
print(result)

# ── Task B ────────────────────────────────────────────────────────────────────

for i, loss in enumerate(epoch_losses, start=1):
    if i == 1:
        trend = "→"
    elif loss < epoch_losses[i - 2]:   # compare to previous (i-2 because enumerate starts at 1)
        trend = "↓"
    else:
        trend = "↑"
    print(f"  Epoch {i:>2} | loss={loss:.4f}  {trend}")

# ── Task C ────────────────────────────────────────────────────────────────────

correct = sum(1 for p, l in zip(predictions, true_labels) if p == l)
total   = len(predictions)
print(f"Correct: {correct}/{total}  Accuracy: {correct/total:.0%}")

# ── Why this works ────────────────────────────────────────────────────────────
#
# Task A — comprehension with two conditions
#   Both conditions must be True (and). The filter and the formatting
#   are combined in a single expression — no intermediate list needed.
#   f"{d['confidence']:.0%}" multiplies by 100 and adds %, rounds to 0 decimals.
#
# Task B — trend arrow using enumerate
#   enumerate starts at 1, so the previous loss is at epoch_losses[i-2]:
#   When i=2 (second epoch), i-2=0, which is epoch_losses[0] (first epoch). ✓
#   When i=1 (first epoch), we print "→" — no previous value to compare.
#
# Task C — sum with a generator expression
#   sum(1 for p, l in zip(...) if p == l) counts matching pairs.
#   This is a generator expression (like a comprehension, but lazy).
#   You'll learn generators formally in Phase 3 (topic: generators).
#   For now, read it as: "count 1 for each pair where pred equals label".