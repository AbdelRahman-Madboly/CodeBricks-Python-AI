"""
solutions/03_top_k.py
──────────────────────
Topic    : Lists
Solution : Exercise 3 — Top-k and running average
"""


def find_top_k(values: list[float], k: int) -> list[float]:
    """
    Return the k highest values from the list in descending order.
    Uses selection-sort logic — no sorted/max/min.
    """
    remaining = values[:]   # copy — don't mutate the caller's list
    result = []

    for _ in range(k):
        # Find the index of the maximum in 'remaining' manually
        max_idx = 0
        for i in range(1, len(remaining)):
            if remaining[i] > remaining[max_idx]:
                max_idx = i
        result.append(remaining.pop(max_idx))   # pop removes it from remaining

    return result


def running_average(values: list[float]) -> list[float]:
    """Return a list of running averages up to each index."""
    result = []
    total  = 0.0

    for i, v in enumerate(values):
        total += v
        result.append(round(total / (i + 1), 10))   # i+1 = count so far

    return result


# ── Test output ───────────────────────────────────────────────────────────────

scores = [0.72, 0.95, 0.61, 0.97, 0.88, 0.92, 0.45]
print(find_top_k(scores, 3))   # [0.97, 0.95, 0.92]
print(find_top_k(scores, 1))   # [0.97]

print(running_average([0.9, 0.7, 0.5, 0.4]))   # [0.9, 0.8, 0.7, 0.625]

# ── Task C — answers ──────────────────────────────────────────────────────────

# Snippet 1: [[9, 0, 0], [9, 0, 0], [9, 0, 0]] — all rows changed
# Snippet 2: [[0, 0, 0], [0, 9, 0], [0, 0, 0]] — only row 1 changed
# Snippet 3: [1, 2, 3, 4] — b = a is an alias, not a copy; appending to b affects a
# Snippet 4: [1, 2, 3]    — b = a[:] creates a new list; a is untouched

# ── Why this works ────────────────────────────────────────────────────────────
#
# find_top_k — selection sort for k iterations
#   We loop k times. Each time, we scan the remaining values to find the
#   current maximum's index, pop it (which removes it from remaining),
#   and add it to result. After k iterations, result holds the top k values.
#   This is O(n*k) — acceptable for small k, inefficient for large k.
#   The real-world version uses heapq.nlargest(k, values) which is O(n log k).
#   You'll learn heapq in Phase 4 (standard library).
#
# remaining = values[:] — why copy?
#   .pop() modifies the list. Without the copy, we'd be mutating the caller's
#   list — a side effect the caller doesn't expect.
#   a[:] is a SHALLOW copy — creates a new list with the same elements.
#   For a flat list of floats this is fine. For nested lists, use copy.deepcopy().
#
# running_average — accumulate with a counter
#   i + 1 gives the count of values seen so far (enumerate is 0-based).
#   total / (i + 1) is the running mean at each step.
#   round(..., 10) avoids floating-point noise in the output.
#
# Snippet 3 vs 4 — alias vs copy
#   b = a → b and a are the SAME list object. Mutating one mutates both.
#   b = a[:] → b is a NEW list. Mutating b leaves a untouched.
#   This is the same issue as the mutable default trap in functions (topic 05).