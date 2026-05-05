"""
solutions/02_detection_grouper.py
──────────────────────────────────
Topic    : Dictionaries and Sets
Solution : Exercise 2 — Detection grouper
"""

detections = [
    {"id": "det_001", "label": "face",       "confidence": 0.94},
    {"id": "det_002", "label": "background", "confidence": 0.82},
    {"id": "det_003", "label": "face",       "confidence": 0.91},
    {"id": "det_004", "label": "hand",       "confidence": 0.78},
    {"id": "det_002", "label": "background", "confidence": 0.72},
    {"id": "det_005", "label": "face",       "confidence": 0.89},
    {"id": "det_005", "label": "hand",       "confidence": 0.91},
]

# ── Task A ────────────────────────────────────────────────────────────────────

grouped: dict[str, list[float]] = {}
for det in detections:
    grouped.setdefault(det["label"], []).append(det["confidence"])

for label, scores in grouped.items():
    avg = sum(scores) / len(scores)
    print(f"{label:<12}: {len(scores)} samples | avg confidence: {avg:.3f}")

# ── Task B ────────────────────────────────────────────────────────────────────

print()
label_counts: dict[str, int] = {}
for det in detections:
    label_counts[det["label"]] = label_counts.get(det["label"], 0) + 1

total = len(detections)
for label, count in label_counts.items():
    print(f"{label:<12}: {count}")

for label, count in label_counts.items():
    share = count / total
    if share < 0.30:
        print(f"WARNING: {label} is underrepresented ({share:.1%})")

# ── Task C ────────────────────────────────────────────────────────────────────

print()
id_counts: dict[str, int] = {}
for det in detections:
    id_counts[det["id"]] = id_counts.get(det["id"], 0) + 1

for det_id, count in id_counts.items():
    if count > 1:
        print(f"DUPLICATE: {det_id} appears {count} times")

# ── Why this works ────────────────────────────────────────────────────────────
#
# Task A — .setdefault(key, []).append(value)
#   .setdefault() returns the existing list for the key if present, or
#   inserts [] and returns it if absent. Either way, .append() works on
#   the return value. This collapses the common "check then initialise" pattern:
#     if label not in grouped: grouped[label] = []
#     grouped[label].append(score)
#   into one readable line.
#
# Task B — frequency counting with .get(key, 0) + 1
#   The canonical pattern. On first encounter: .get returns 0, adds 1 → sets to 1.
#   On subsequent encounters: .get returns the current count, adds 1.
#   The share check (count / total < threshold) then filters underrepresented classes.
#
# Task C — same frequency count, different field
#   Counting IDs is identical to counting labels — same pattern, different key.
#   The duplicate check is just filtering where count > 1.
#   This is how you'd detect duplicate rows in a DataFrame before you learn Pandas.