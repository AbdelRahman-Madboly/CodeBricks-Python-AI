"""
exercises/02_detection_filter.py
─────────────────────────────────
Topic    : Lists
Exercise : 2 of 3 — Medium
Concept  : List comprehensions, enumerate, zip, accumulation

─────────────────────────────────────────────────────────────────
Task A — Comprehension filter + transform
─────────────────────────────────────────────────────────────────
From `detections`, use a single list comprehension to build a list
of formatted strings for all face detections with confidence > 0.80.

Expected output:
  ['img_001: face @ 94%', 'img_004: face @ 91%']

─────────────────────────────────────────────────────────────────
Task B — Accumulation with enumerate
─────────────────────────────────────────────────────────────────
Print each epoch with a trend arrow: ↓ if loss fell, ↑ if rose,
→ for the first epoch (no comparison).

Expected output:
  Epoch  1 | loss=0.9100  →
  Epoch  2 | loss=0.7400  ↓
  Epoch  3 | loss=0.8200  ↑
  Epoch  4 | loss=0.5800  ↓
  Epoch  5 | loss=0.3900  ↓

─────────────────────────────────────────────────────────────────
Task C — zip comparison + accuracy
─────────────────────────────────────────────────────────────────
Using zip(), count correct predictions and print:

Expected output:
  Correct: 7/10  Accuracy: 70%
─────────────────────────────────────────────────────────────────
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

# ── Your solutions ────────────────────────────────────────────────────────────

# Task A:


# Task B:


# Task C: