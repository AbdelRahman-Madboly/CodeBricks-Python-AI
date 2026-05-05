"""
exercises/03_top_k.py
──────────────────────
Topic    : Lists
Exercise : 3 of 3 — Hard
Concept  : Manual search logic, shallow copy trap, running average

─────────────────────────────────────────────────────────────────
Task A — find_top_k()
─────────────────────────────────────────────────────────────────
Return the k highest values from a list, in descending order.
Do NOT use sorted(), sort(), max(), min(), or any import.

Hint: loop k times. Each pass, find the max index manually,
append its value to result, and pop it from a working copy.

Signature:
  def find_top_k(values: list[float], k: int) -> list[float]

Expected:
  find_top_k([0.72, 0.95, 0.61, 0.97, 0.88, 0.92, 0.45], 3)
  → [0.97, 0.95, 0.92]

─────────────────────────────────────────────────────────────────
Task B — running_average()
─────────────────────────────────────────────────────────────────
Return a list where each entry is the average of all values
up to and including that index.

Signature:
  def running_average(values: list[float]) -> list[float]

Expected:
  running_average([0.9, 0.7, 0.5, 0.4]) → [0.9, 0.8, 0.7, 0.625]

─────────────────────────────────────────────────────────────────
Task C — Shallow copy predictions (no code to write)
─────────────────────────────────────────────────────────────────
Write your prediction as a comment, then uncomment and run.
"""

# ── Your functions ────────────────────────────────────────────────────────────


# ── Task C ────────────────────────────────────────────────────────────────────

# Snippet 1 — what does grid look like after the assignment?
# grid = [[0] * 3] * 3
# grid[1][1] = 9
# print(grid)
# Prediction: ???

# Snippet 2
# grid = [[0] * 3 for _ in range(3)]
# grid[1][1] = 9
# print(grid)
# Prediction: ???

# Snippet 3 — alias vs copy
# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a)
# Prediction: ???

# Snippet 4
# a = [1, 2, 3]
# b = a[:]
# b.append(4)
# print(a)
# Prediction: ???


# ── Test calls (uncomment after writing your functions) ───────────────────────

# scores = [0.72, 0.95, 0.61, 0.97, 0.88, 0.92, 0.45]
# print(find_top_k(scores, 3))   # [0.97, 0.95, 0.92]
# print(find_top_k(scores, 1))   # [0.97]

# print(running_average([0.9, 0.7, 0.5, 0.4]))   # [0.9, 0.8, 0.7, 0.625]
# print(running_average([1.0]))                   # [1.0]