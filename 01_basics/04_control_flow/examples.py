"""
Control Flow — Examples

Covers if/elif/else, while loops, for loops, break/continue,
and the for/else pattern through practical data-processing scenarios.
"""


# ---------------------------------------------------------------------------
# Example 1 — if / elif / else
# Scenario: classifying a model's confidence score into a decision tier
# ---------------------------------------------------------------------------

confidence = 0.76

if confidence >= 0.90:
    decision = "accept"
elif confidence >= 0.70:
    decision = "review"
elif confidence >= 0.50:
    decision = "flag"
else:
    decision = "reject"

print(f"Confidence {confidence:.2f} → {decision}")   # review


# ---------------------------------------------------------------------------
# Example 2 — while loop with break and continue
# Scenario: reading frames from a video stream until a stop signal
# ---------------------------------------------------------------------------

import random
random.seed(42)

frame_index = 0
processed = 0
max_frames = 10

while frame_index < max_frames:
    frame_index += 1

    # Simulate a corrupted frame — skip it
    if random.random() < 0.2:
        print(f"  Frame {frame_index:02d}: corrupted — skipping")
        continue

    # Simulate a stop signal mid-stream
    if frame_index == 8:
        print(f"  Frame {frame_index:02d}: stop signal received")
        break

    processed += 1
    print(f"  Frame {frame_index:02d}: processed")

print(f"Total processed: {processed}")


# ---------------------------------------------------------------------------
# Example 3 — for loop patterns: enumerate, range, for/else
# Scenario: searching a list of checkpoints for a valid one
# ---------------------------------------------------------------------------

checkpoints = [
    ("epoch_01.pt", False),
    ("epoch_05.pt", False),
    ("epoch_10.pt", True),
    ("epoch_15.pt", True),
]

# enumerate gives index and value together — avoids manual counter
print("\nCheckpoint log:")
for index, (filename, is_valid) in enumerate(checkpoints):
    status = "✓" if is_valid else "✗"
    print(f"  [{index}] {status} {filename}")

# for/else — else runs only if break was never hit
target = "epoch_05.pt"
print(f"\nSearching for {target}:")

for filename, is_valid in checkpoints:
    if filename == target:
        if is_valid:
            print(f"  Found and valid: {filename}")
        else:
            print(f"  Found but invalid: {filename}")
        break
else:
    # This runs only if we exhausted the list without breaking
    print(f"  Not found: {target}")
