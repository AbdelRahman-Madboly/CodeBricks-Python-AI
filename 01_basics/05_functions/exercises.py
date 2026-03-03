"""
Functions — Exercises
"""


# ---------------------------------------------------------------------------
# Exercise 1 (Easy) — Write a function with type hints and default args
#
# Problem:
#   Write a function called clamp() that restricts a value to a given range.
#   If the value is below min_val, return min_val.
#   If the value is above max_val, return max_val.
#   Otherwise return the value unchanged.
#
#   Expected output:
#   0.0
#   0.75
#   1.0
#
# Requirements:
#   - Type hints on all parameters and return value
#   - Docstring
#   - Default min_val=0.0, max_val=1.0
#
# Your solution below:
# ---------------------------------------------------------------------------

# Uncomment to test after writing your function:
# print(clamp(-0.5))      # 0.0
# print(clamp(0.75))      # 0.75
# print(clamp(1.8))       # 1.0


# ---------------------------------------------------------------------------
# Exercise 2 (Medium) — Use *args and **kwargs
#
# Problem:
#   Write a function called build_report() that:
#     - Takes a required title (str)
#     - Accepts any number of metric names as positional args
#     - Accepts any number of metric values as keyword args
#     - Returns a formatted report string
#
#   Expected output from the test call below:
#   === Training Report ===
#   Metrics tracked: accuracy, loss, f1
#   accuracy : 0.94
#   loss     : 0.042
#   f1       : 0.91
#
# Test call (do not change):
# report = build_report("Training Report", "accuracy", "loss", "f1",
#                        accuracy=0.94, loss=0.042, f1=0.91)
# print(report)
#
# Your solution below:
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Exercise 3 (Hard) — Avoid the mutable default trap + scope reasoning
#
# Problem Part A:
#   Write a function called merge_configs() that merges a list of config dicts
#   into one dict. Later keys overwrite earlier ones.
#   The function must NOT modify any of the input dicts.
#
#   Expected output:
#   {'model': 'ResNet', 'epochs': 20, 'lr': 0.001, 'device': 'cuda'}
#
# configs to merge (do not change):
configs = [
    {"model": "VGG", "epochs": 10},
    {"model": "ResNet", "lr": 0.001},
    {"epochs": 20, "device": "cuda"},
]
#
# Problem Part B:
#   What is printed by the code below? Write your answer as a comment
#   before running it, then verify.
#
x = 10

def modify():
    x = 99          # does this change the outer x?
    print(f"inside: {x}")

modify()
print(f"outside: {x}")   # what prints here?
#
# Your answer (comment):
# outside x will be: ???
#
# Your solution below:
# ---------------------------------------------------------------------------
