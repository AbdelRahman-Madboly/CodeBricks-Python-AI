"""
exercises/01_metric_calculator.py
──────────────────────────────────
Topic    : Functions
Exercise : 1 of 3 — Easy
Concept  : def, return, type hints, docstring, default parameters

Context
-------
After a training epoch you need to compute evaluation metrics.
Write the three functions below. Each one takes numbers in,
does one clear calculation, and returns a result — no printing inside.

─────────────────────────────────────────────────────────────────
Task A — accuracy()
─────────────────────────────────────────────────────────────────
Write a function that calculates classification accuracy.

Signature:
  def accuracy(correct: int, total: int) -> float

Expected output when called with the test calls below:
  Accuracy: 87.5%
  Accuracy: 100.0%
  Accuracy: 0.0%

─────────────────────────────────────────────────────────────────
Task B — clamp()
─────────────────────────────────────────────────────────────────
Write a function that clamps (clips) a value to a given range.
If the value is below min_val, return min_val.
If it's above max_val, return max_val.
Otherwise return it unchanged.

Signature (with defaults):
  def clamp(value: float, min_val: float = 0.0, max_val: float = 1.0) -> float

Expected output:
  0.0
  0.75
  1.0

─────────────────────────────────────────────────────────────────
Task C — normalize()
─────────────────────────────────────────────────────────────────
Write a function that normalizes a value to [0.0, 1.0] given a range.
Uses the formula: (value - min_val) / (max_val - min_val)
Use clamp() inside normalize() to ensure the result never goes outside [0, 1].

Signature:
  def normalize(value: float, min_val: float, max_val: float) -> float

Expected output:
  0.0000
  0.5020
  1.0000
  0.5000

Rules for all three:
  - Type hints on all parameters and return value
  - Google-style docstring (Args + Returns)
  - No print() inside any function — only return
─────────────────────────────────────────────────────────────────
"""

# ── Your functions here ───────────────────────────────────────────────────────


# ── Test calls — do not change these ─────────────────────────────────────────

# Task A
# print(f"Accuracy: {accuracy(7, 8):.1%}")
# print(f"Accuracy: {accuracy(10, 10):.1%}")
# print(f"Accuracy: {accuracy(0, 5):.1%}")

# Task B
# print(clamp(-0.5))    # 0.0
# print(clamp(0.75))    # 0.75
# print(clamp(1.8))     # 1.0

# Task C
# print(f"{normalize(0, 0, 255):.4f}")     # 0.0000
# print(f"{normalize(128, 0, 255):.4f}")   # 0.5020
# print(f"{normalize(255, 0, 255):.4f}")   # 1.0000
# print(f"{normalize(150, 100, 200):.4f}") # 0.5000