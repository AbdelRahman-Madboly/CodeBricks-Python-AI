"""
Variables and Data Types — Exercises

Attempt every exercise before opening solutions.py.
"""


# ---------------------------------------------------------------------------
# Exercise 1 (Easy) — Type inspection
#
# Problem:
#   Given the five variables below, print each variable's value AND its type
#   on one line per variable using an f-string.
#
#   Expected output:
#   10000 -> <class 'int'>
#   0.92 -> <class 'float'>
#   ResNet -> <class 'str'>
#   True -> <class 'bool'>
#   None -> <class 'NoneType'>
#
# Variables provided — do not change these:
batch_size = 10000
confidence = 0.92
architecture = "ResNet"
is_pretrained = True
checkpoint = None
#
# Your solution below:
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Exercise 2 (Medium) — Type conversion pipeline
#
# Problem:
#   You receive raw sensor data as strings (as you would from a CSV or API).
#   Convert each value to the appropriate type, then print a formatted summary.
#
#   Expected output:
#   Device  : camera-01
#   Frames  : 1200
#   FPS     : 29.97
#   Active  : True
#   Missing : None
#
# Raw data — do not change these:
raw_device_id = "camera-01"
raw_frame_count = "1200"
raw_fps = "29.97"
raw_active = "True"
raw_missing = "None"
#
# Hints:
#   - int("1200") works
#   - float("29.97") works
#   - bool("True") does NOT work the way you expect — think about why,
#     then find a one-line workaround
#   - "None" as a string is not None — convert it manually
#
# Your solution below:
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Exercise 3 (Hard) — Floating point and identity
#
# Problem:
#   Answer each question by assigning True or False to the variable,
#   then verify by running the file. Do not look anything up — reason it out.
#
# Your predictions (replace each None with True or False):
# ---------------------------------------------------------------------------

# Q1: Does 0.1 + 0.2 equal 0.3 in Python?
q1_prediction = None

# Q2: Is bool a subclass of int?
q2_prediction = None

# Q3: Does True == 1 evaluate to True?
q3_prediction = None

# Q4: Is None == False?
q4_prediction = None

# Q5: After: a = 1000; b = 1000 — does a is b return True?
#     (Hint: think about CPython's integer caching range: -5 to 256)
q5_prediction = None

# Verification — run this block after filling in your predictions:
print("--- Your Predictions vs Reality ---")
print(f"Q1 float equality   | predicted: {q1_prediction} | actual: {0.1 + 0.2 == 0.3}")
print(f"Q2 bool subclass    | predicted: {q2_prediction} | actual: {issubclass(bool, int)}")
print(f"Q3 True == 1        | predicted: {q3_prediction} | actual: {True == 1}")
print(f"Q4 None == False    | predicted: {q4_prediction} | actual: {None == False}")
a = 1000
b = 1000
print(f"Q5 large int is     | predicted: {q5_prediction} | actual: {a is b}")
