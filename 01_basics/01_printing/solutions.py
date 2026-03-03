"""
Printing — Solutions

Open this only after genuinely attempting exercises.py.
"""


# ---------------------------------------------------------------------------
# Solution 1
# ---------------------------------------------------------------------------

python_version = "3.11"
platform = "linux"
debug_mode = False

print(f"[INFO] python v{python_version} | platform: {platform} | debug: {debug_mode}")


# ---------------------------------------------------------------------------
# Solution 2
# ---------------------------------------------------------------------------

sensor_data = [
    ("temperature", 98.60),
    ("humidity", 45.20),
    ("pressure", 1013.25),
]

print("=== Sensor Readings ===")
for name, value in sensor_data:
    print(f"{name:<12} {value:>8.2f}")
print("=" * 23)


# ---------------------------------------------------------------------------
# Solution 3
# ---------------------------------------------------------------------------

pipeline_steps = ["Loading", "preprocessing", "training", "evaluating", "saving"]

for i, step in enumerate(pipeline_steps):
    # Print each step — no newline, add arrow unless it's the last step
    if i < len(pipeline_steps) - 1:
        print(step, end=" -> ")
    else:
        # Last step: no arrow, space before DONE, newline at the end
        print(step, end=" ")

print("DONE")
