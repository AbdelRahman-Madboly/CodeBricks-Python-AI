"""
Control Flow — Exercises
"""


# ---------------------------------------------------------------------------
# Exercise 1 (Easy) — Grade classifier
#
# Problem:
#   Given a test score, print the grade according to this scale:
#     90-100 → A
#     80-89  → B
#     70-79  → C
#     60-69  → D
#     below 60 → F
#   Also print "Invalid score" for anything outside 0-100.
#
#   Expected output for score = 83:
#   Score: 83 → Grade: B
#
# Test with multiple values to verify all branches work.
#
score = 83
#
# Your solution below:
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Exercise 2 (Medium) — FizzBuzz (the real interview version)
#
# Problem:
#   Print numbers from 1 to 30. But:
#     - Multiples of 3 → print "Fizz" instead
#     - Multiples of 5 → print "Buzz" instead
#     - Multiples of both 3 and 5 → print "FizzBuzz" instead
#
#   Expected output (first 6 lines):
#   1
#   2
#   Fizz
#   4
#   Buzz
#   Fizz
#
# Constraint: use a single print() per number — no multiple prints per iteration.
#
# Your solution below:
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Exercise 3 (Hard) — Search with for/else
#
# Problem:
#   Given the list of model checkpoints below, find the LAST valid checkpoint
#   (highest epoch number that is valid) and print its filename.
#   If no valid checkpoint exists, print "No valid checkpoint found."
#
#   Expected output:
#   Best checkpoint: epoch_15.pt
#
# Data — do not change:
checkpoints = [
    ("epoch_01.pt", True),
    ("epoch_05.pt", False),
    ("epoch_10.pt", True),
    ("epoch_15.pt", True),
    ("epoch_20.pt", False),
]
#
# Constraints:
#   - Do not use any list/sorting functions — use only loops and conditions
#   - Must handle the case where no valid checkpoint exists
#
# Your solution below:
# ---------------------------------------------------------------------------
