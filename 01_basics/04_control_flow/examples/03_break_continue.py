"""
examples/03_break_continue.py
──────────────────────────────
Topic  : Control Flow
Example: 3 of 3 — break, continue, for/else, search patterns

Context
-------
A real video processing pipeline skips corrupted frames (continue),
stops when a termination signal arrives (break), and reports whether
a valid checkpoint was found or not (for/else). These three constructs
work together to give you precise control over loop execution.

Covers:
  - continue — skip the rest of this iteration
  - break — exit the loop entirely
  - for/else — else runs only if break never fired
  - The search pattern: find + break, report if not found
  - Combining break and continue in one loop

Run this file. Predict each output before you see it.
"""

import random
random.seed(42)

# ── Part 1: continue — skip bad items ────────────────────────────────────────

print("=== continue — skip corrupted frames ===")

frames = [
    {"id": 1, "corrupted": False, "confidence": 0.91},
    {"id": 2, "corrupted": True,  "confidence": 0.00},
    {"id": 3, "corrupted": False, "confidence": 0.45},
    {"id": 4, "corrupted": True,  "confidence": 0.00},
    {"id": 5, "corrupted": False, "confidence": 0.87},
]

processed = 0
for frame in frames:
    if frame["corrupted"]:
        print(f"  Frame {frame['id']}: SKIP (corrupted)")
        continue   # jumps back to the top of the loop — skips code below

    # Only reaches here for non-corrupted frames
    processed += 1
    status = "✓ accept" if frame["confidence"] >= 0.5 else "✗ reject"
    print(f"  Frame {frame['id']}: {status}  conf={frame['confidence']:.2f}")

print(f"Processed: {processed}/{len(frames)} frames")

# ── Part 2: break — stop on a signal ─────────────────────────────────────────

print()
print("=== break — stop on end-of-stream ===")

stream = [
    ("frame_001", False),
    ("frame_002", False),
    ("frame_003", False),
    ("END_SIGNAL", True),    # stop flag
    ("frame_004", False),    # these are never seen
    ("frame_005", False),
]

seen = 0
for frame_id, is_stop in stream:
    if is_stop:
        print(f"  Stop signal received at: {frame_id}")
        break   # exits the loop — frame_004 and frame_005 never processed

    seen += 1
    print(f"  Processing: {frame_id}")

print(f"Total processed before stop: {seen}")

# ── Part 3: for/else — the search pattern ────────────────────────────────────

print()
print("=== for/else — checkpoint search ===")

checkpoints = [
    ("epoch_01.pt", False),   # invalid
    ("epoch_05.pt", False),   # invalid
    ("epoch_10.pt", True),    # valid ← this one will be found
    ("epoch_15.pt", True),
]

# Search for the FIRST valid checkpoint
for filename, is_valid in checkpoints:
    if is_valid:
        print(f"  Loaded checkpoint: {filename}")
        break   # found it — stop searching
else:
    # Only runs if the loop finished without ever hitting break
    print("  No valid checkpoint found — starting from scratch")

print()

# Same pattern but with NO valid checkpoints
empty_run = [
    ("epoch_01.pt", False),
    ("epoch_05.pt", False),
]

for filename, is_valid in empty_run:
    if is_valid:
        print(f"  Loaded: {filename}")
        break
else:
    print("  No valid checkpoint — starting from scratch")  # this runs

# ── Part 4: break + continue together ────────────────────────────────────────

print()
print("=== break + continue together ===")

# Process frames: skip low-confidence, stop on error, report results
frame_data = [
    (0.91, "ok"),
    (0.32, "ok"),       # low confidence — skip
    (0.85, "ok"),
    (0.78, "error"),    # error — stop
    (0.95, "ok"),       # never reached
]

accepted = []
for confidence, status in frame_data:
    if status == "error":
        print(f"  ERROR at confidence={confidence:.2f} — stopping pipeline")
        break

    if confidence < 0.5:
        print(f"  SKIP  confidence={confidence:.2f} (below threshold)")
        continue

    accepted.append(confidence)
    print(f"  OK    confidence={confidence:.2f}")

print(f"Accepted {len(accepted)} frames: {accepted}")

# ── What to notice ────────────────────────────────────────────────────────────
#
# 1. continue skips the REST of the current iteration — code BELOW continue
#    in the loop body is not executed. The loop continues with the next item.
#
# 2. break exits the ENTIRE loop — code after the loop runs next.
#    Nothing else in the loop (or after it in the loop body) runs.
#
# 3. for/else — the else belongs to the for statement, not to an if inside it.
#    It runs when the loop exhausts its iterable WITHOUT hitting break.
#    It does NOT run if break was hit.
#
# 4. The search pattern: for + if + break + else
#    This is the idiomatic Python way to say: "find the first X, or report failure".
#    Without for/else, you'd need a boolean flag (found = False before the loop,
#    check after). for/else is cleaner and removes the flag entirely.
#
# 5. break and continue work in while loops too — same rules apply.