"""
exercises/03_top_k.py
──────────────────────
Topic    : Lists
Exercise : 3 of 3 — Hard
Concept  : Manual search/sort logic, list methods, no built-in sort

Context
-------
In evaluation you often need the top-K model predictions by confidence
score. This exercise makes you implement it manually — which builds
understanding of what sorted() actually does under the hood.

─────────────────────────────────────────────────────────────────
Task A — find_top_k()
─────────────────────────────────────────────────────────────────
Return the k highest values from a list, in descending order.
Do NOT use sorted(), sort(), max(), min(), or any import.

Signature:
  def find_top_k(values: list[float], k: int) -> list[float]

Expected:
  find_top_k([0.72, 0.95, 0.61, 0.97, 0.88, 0.92, 0.45], 3)
  → [0.97, 0.95, 0.92]

Hint: loop k times. Each time, find the index of the current
maximum manually, append it to the result, and remove it from
a working copy so you don't pick the same value twice.

─────────────────────────────────────────────────────────────────
Task B — running_average()
─────────────────────────────────────────────────────────────────
Given a list of loss values, return a new list where each entry
is the average of all values up to and including that index.

Signature:
  def running_average(values: list[float]) -> list[float]

Expected:
  running_average([0.9, 0.7, 0.5, 0.4])
  → [0.9, 0.8, 0.7, 0.625]

─────────────────────────────────────────────────────────────────
Task C — Shallow copy trap (no code to write)
─────────────────────────────────────────────────────────────────
Predict what each snippet prints. Then uncomment and run to verify.
─────────────────────────────────────────────────────────────────
"""

# ── Your functions ────────────────────────────────────────────────────────────


# ── Task C — predictions ──────────────────────────────────────────────────────

# Snippet 1 — what prints?
# grid = [[0] * 3] * 3
# grid[1][1] = 9
# print(grid)
# Your prediction: ???

# Snippet 2 — what prints?
# grid = [[0] * 3 for _ in range(3)]
# grid[1][1] = 9
# print(grid)
# Your prediction: ???

# Snippet 3 — what is result?
# a = [1, 2, 3]
# b = a           # assignment — not a copy
# b.append(4)
# print(a)        # ???
# Your prediction: ???

# Snippet 4 — what is result?
# a = [1, 2, 3]
# b = a[:]        # slice copy — creates a new list
# b.append(4)
# print(a)        # ???
# Your prediction: ???


# ── Test calls (uncomment after writing your functions) ───────────────────────

# Task A
# scores = [0.72, 0.95, 0.61, 0.97, 0.88, 0.92, 0.45]
# print(find_top_k(scores, 3))   # [0.97, 0.95, 0.92]
# print(find_top_k(scores, 1))   # [0.97]
# print(find_top_k(scores, 7))   # all 7 values in descending order

# Task B
# print(running_average([0.9, 0.7, 0.5, 0.4]))    # [0.9, 0.8, 0.7, 0.625]
# print(running_average([1.0]))                    # [1.0]
# print(running_average([0.5, 0.5, 0.5]))          # [0.5, 0.5, 0.5]