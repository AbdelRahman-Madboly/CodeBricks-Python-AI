"""
exercises/01_model_leaderboard.py
──────────────────────────────────
Topic    : Dictionaries and Sets
Exercise : 1 of 3 — Easy
Concept  : Dict creation, .get(), iteration, filtering

Context
-------
You're managing a model evaluation leaderboard. Given parallel lists of
model names and accuracy scores, build a dict and answer three queries
about it — without using sorted() or max() for the best-model task.

─────────────────────────────────────────────────────────────────
Tasks
─────────────────────────────────────────────────────────────────

Task A — Build and print
  Build a dict mapping each model name to its accuracy.
  Print each entry formatted exactly like this (left-align names in 16 chars):

  ResNet-50        : 88.1%
  EfficientNet-B4  : 94.2%
  MobileNet-V3     : 85.5%
  ViT-Base         : 92.0%

Task B — Find the best model (no max(), no sorted())
  Iterate over the dict and track the best model manually.
  Print:

  Best model: EfficientNet-B4 (94.2%)

Task C — Filter
  Print all model names where accuracy >= 0.90, as a plain list.

  Above 90%: ['EfficientNet-B4', 'ViT-Base']

Rules:
  - Task B must use a loop with a running-max variable (float("-inf") hint)
  - No max(), no sorted() anywhere in this exercise
─────────────────────────────────────────────────────────────────
"""

model_names = ["ResNet-50", "EfficientNet-B4", "MobileNet-V3", "ViT-Base"]
accuracies  = [0.881, 0.942, 0.855, 0.920]

# ── Task A ────────────────────────────────────────────────────────────────────


# ── Task B ────────────────────────────────────────────────────────────────────


# ── Task C ────────────────────────────────────────────────────────────────────