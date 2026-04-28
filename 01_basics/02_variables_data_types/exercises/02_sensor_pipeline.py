"""
exercises/02_sensor_pipeline.py
────────────────────────────────
Topic    : Variables and Data Types
Exercise : 2 of 3 — Medium
Concept  : Type conversion, the bool("False") trap, None handling

Context
-------
A data pipeline reads config and sensor data from a CSV file.
Everything arrives as a string — your job is to convert each
value to the correct Python type before passing it to the model.

This is one of the most common tasks in real AI/data work.

─────────────────────────────────────────────────────────────────
Task
─────────────────────────────────────────────────────────────────
Convert each raw string value to the correct type, then print
a summary that looks EXACTLY like this:

  === Camera Pipeline — Parsed Config ===
  device_id      : camera-03         (str)
  frame_count    : 4800              (int)
  sample_rate    : 29.97             (float)
  active         : False             (bool)
  last_error     : None              (NoneType)
  === Validation ===
  frame_count is int     : True
  sample_rate is float   : True
  active is bool         : False   ← bool("False") trap — fix this!
  last_error is None     : True

The last line of the Validation block should say True, not False.
Read the hints in the code carefully.

─────────────────────────────────────────────────────────────────
"""

# Raw data from a CSV file — everything is a string
raw_device_id   = "camera-03"
raw_frame_count = "4800"
raw_sample_rate = "29.97"
raw_active      = "False"    # ← this is the string "False", not the bool False
raw_last_error  = "None"     # ← this is the string "None", not None itself

# ── Convert each value to the correct type ────────────────────────────────────
# Hint: int() and float() work on numeric strings
# Hint: bool("False") returns True — DON'T use bool() for this
# Hint: "None" == "None" is True, but that's still a string — convert manually

device_id   = None   # already a str — just assign it
frame_count = None   # replace None with the correct conversion
sample_rate = None   # replace None with the correct conversion
active      = None   # replace None with the correct conversion — avoid bool()!
last_error  = None   # replace None — should become actual None, not the string

# ── Print the summary ─────────────────────────────────────────────────────────
# (write your print statements here)