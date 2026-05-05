"""
exercises/02_detection_grouper.py
──────────────────────────────────
Topic    : Dictionaries and Sets
Exercise : 2 of 3 — Medium
Concept  : Grouping with dicts, .setdefault(), frequency counting, nested access

Context
-------
A detection model returns one record per frame. You need to group the
results by label, compute per-class statistics, and flag any frame that
has duplicate detection IDs — a sign of a pipeline bug.

─────────────────────────────────────────────────────────────────
Task A — Group by label
─────────────────────────────────────────────────────────────────
Group the detections by label into a dict where each value is a list
of confidence scores. Then print per-label stats.

Expected output:
  face        : 3 samples | avg confidence: 0.913
  background  : 2 samples | avg confidence: 0.770
  hand        : 2 samples | avg confidence: 0.845

─────────────────────────────────────────────────────────────────
Task B — Frequency count + class imbalance warning
─────────────────────────────────────────────────────────────────
Count how many times each label appears. Then print a warning for
any class whose share of total detections is below 20%.

Expected output:
  face        : 3
  background  : 2
  hand        : 2
  WARNING: background is underrepresented (28.6%)
  WARNING: hand is underrepresented (28.6%)

  (Note: 3/7 = 42.9%, 2/7 = 28.6% — both background and hand are below 30%,
   but adjust the threshold to 30% so both warnings appear as shown.)

─────────────────────────────────────────────────────────────────
Task C — Duplicate ID detection
─────────────────────────────────────────────────────────────────
Each detection has an "id" field. Find any IDs that appear more than once.
Print a warning for each duplicate.

Expected output:
  DUPLICATE: det_002 appears 2 times
  DUPLICATE: det_005 appears 2 times
─────────────────────────────────────────────────────────────────
"""

detections = [
    {"id": "det_001", "label": "face",       "confidence": 0.94},
    {"id": "det_002", "label": "background", "confidence": 0.82},
    {"id": "det_003", "label": "face",       "confidence": 0.91},
    {"id": "det_004", "label": "hand",       "confidence": 0.78},
    {"id": "det_002", "label": "background", "confidence": 0.72},   # duplicate id
    {"id": "det_005", "label": "face",       "confidence": 0.89},
    {"id": "det_005", "label": "hand",       "confidence": 0.91},   # duplicate id
]

# ── Task A ────────────────────────────────────────────────────────────────────


# ── Task B ────────────────────────────────────────────────────────────────────


# ── Task C ────────────────────────────────────────────────────────────────────