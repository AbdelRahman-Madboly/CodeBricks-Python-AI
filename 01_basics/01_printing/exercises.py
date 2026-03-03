"""
Printing — Exercises

Work through each exercise before opening solutions.py.
The expected output is shown in each problem statement — match it exactly.
"""


# ---------------------------------------------------------------------------
# Exercise 1 (Easy) — Format a system info line
#
# Problem:
#   Given the variables below, print a single formatted line that looks
#   exactly like this (values must come from the variables, not be hardcoded):
#
#   [INFO] python v3.11 | platform: linux | debug: False
#
# Variables provided — do not change these:
python_version = "3.11"
platform = "linux"
debug_mode = False
#
# Your solution below:
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Exercise 2 (Medium) — Print a table with aligned columns
#
# Problem:
#   Print the following sensor readings as a neatly aligned table.
#   Column widths: name = 12 chars (left-aligned), value = 8 chars (right-aligned).
#
#   Expected output:
#   === Sensor Readings ===
#   temperature      98.60
#   humidity         45.20
#   pressure       1013.25
#   =======================
#
# Data provided — do not change these:
sensor_data = [
    ("temperature", 98.60),
    ("humidity", 45.20),
    ("pressure", 1013.25),
]
#
# Your solution below:
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Exercise 3 (Hard) — Build output without newlines, then terminate
#
# Problem:
#   Simulate a loading bar that prints steps on the same line, separated
#   by " -> ", with " DONE" at the end. Use only one print() per step
#   and control sep/end to achieve this.
#
#   Expected output (all on one line):
#   Loading -> preprocessing -> training -> evaluating -> saving DONE
#
# Steps provided — do not change this:
pipeline_steps = ["Loading", "preprocessing", "training", "evaluating", "saving"]
#
# Constraints:
#   - Do not build one big string and print it all at once
#   - Use a loop
#   - Control end= and/or sep= on each print() call
#
# Your solution below:
# ---------------------------------------------------------------------------
