"""
solutions/02_sensor_pipeline.py
────────────────────────────────
Topic    : Variables and Data Types
Solution : Exercise 2 — Sensor pipeline type conversion

Open this only after a genuine attempt at the exercise.
"""

# Raw data from a CSV file — everything is a string
raw_device_id   = "camera-03"
raw_frame_count = "4800"
raw_sample_rate = "29.97"
raw_active      = "False"
raw_last_error  = "None"

# ── Conversions ───────────────────────────────────────────────────────────────

device_id   = raw_device_id                      # already str — no conversion needed
frame_count = int(raw_frame_count)               # "4800" → 4800
sample_rate = float(raw_sample_rate)             # "29.97" → 29.97
active      = raw_active == "True"               # "False" == "True" → False
last_error  = None if raw_last_error == "None" else raw_last_error

# ── Summary ───────────────────────────────────────────────────────────────────

print("  === Camera Pipeline — Parsed Config ===")
print(f"  {'device_id':<15}: {device_id:<18} ({type(device_id).__name__})")
print(f"  {'frame_count':<15}: {frame_count:<18} ({type(frame_count).__name__})")
print(f"  {'sample_rate':<15}: {sample_rate:<18} ({type(sample_rate).__name__})")
print(f"  {'active':<15}: {str(active):<18} ({type(active).__name__})")
print(f"  {'last_error':<15}: {str(last_error):<18} ({type(last_error).__name__})")

print("  === Validation ===")
print(f"  frame_count is int     : {isinstance(frame_count, int)}")
print(f"  sample_rate is float   : {isinstance(sample_rate, float)}")
print(f"  active is bool         : {isinstance(active, bool)}")
print(f"  last_error is None     : {last_error is None}")

# ── Why this works ────────────────────────────────────────────────────────────
#
# active = raw_active == "True"
#   This compares the string to "True" and returns a real bool.
#   "False" == "True" evaluates to False — which is exactly what we want.
#   "True" == "True" evaluates to True.
#   This works correctly for both cases.
#
#   Why NOT bool(raw_active)?
#   bool() on any non-empty string returns True — always.
#   bool("False") → True, bool("0") → True, bool("no") → True.
#   It doesn't parse the string content, it checks if the string exists.
#
# last_error = None if raw_last_error == "None" else raw_last_error
#   This is a ternary expression (one-line if/else).
#   Read it as: "set to None if the string is 'None', otherwise keep the string"
#   You'll learn ternary expressions formally in topic 04 (Control Flow).
#
# isinstance(active, bool) → True
#   Because active = raw_active == "True" returns a genuine bool value.
#   The == comparison always returns True or False — the bool type.
#
# last_error is None → True
#   We converted the string "None" to the actual None object.
#   'is None' checks object identity — there is only one None in Python.