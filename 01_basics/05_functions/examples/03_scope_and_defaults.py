"""
examples/03_scope_and_defaults.py
──────────────────────────────────
Topic  : Functions
Example: 3 of 3 — Scope, mutable default trap, main() entry point

Context
-------
Two of the most common sources of subtle bugs in Python functions:
scope confusion (does this variable come from inside or outside?) and
the mutable default trap (why does my list keep growing between calls?).

Understanding both saves hours of debugging later — especially in
training scripts where you're accumulating results across many calls.

Covers:
  - Local vs global scope
  - Why you can't reassign a global inside a function (without global keyword)
  - The mutable default argument trap — explained and fixed
  - The main() entry point pattern
  - Passing state in/out instead of using globals

Run this file. Predict each output before you see it.
"""


# ── Part 1: Scope ─────────────────────────────────────────────────────────────

# This variable lives in the global (module) scope
BATCH_SIZE = 32    # UPPER_CASE signals a constant — don't mutate this

def describe_batch() -> str:
    """Read a global but don't modify it."""
    # Functions CAN read global variables
    return f"Processing batches of {BATCH_SIZE} samples"

print(describe_batch())   # fine — reading globals is OK

# ─────────────────────────────────────────────────────────────
# What happens if we try to reassign inside a function?
epoch_count = 0

def try_increment():
    # This creates a NEW local variable called epoch_count
    # It does NOT touch the global one
    epoch_count = epoch_count + 1   # UnboundLocalError at runtime
    # Python sees the assignment → treats epoch_count as local
    # But 'local epoch_count' doesn't exist yet when we read it on the right

# Uncommenting the next line would crash:
# try_increment()

# ─────────────────────────────────────────────────────────────
# The right pattern: pass state in, return state out
def increment_epoch(current_epoch: int) -> int:
    """Return the next epoch number — no globals touched."""
    return current_epoch + 1

epoch = 0
epoch = increment_epoch(epoch)
epoch = increment_epoch(epoch)
print(f"Epoch: {epoch}")   # 2 — clean, no global state

# ── Part 2: The mutable default trap ──────────────────────────────────────────

print()

# WRONG — [] is created ONCE when Python reads the def line
# Every call that doesn't pass batch shares the same list object
def collect_sample_wrong(sample: str, batch: list = []) -> list:
    batch.append(sample)
    return batch

r1 = collect_sample_wrong("img_001")
r2 = collect_sample_wrong("img_002")   # should be fresh, but isn't
r3 = collect_sample_wrong("img_003")

print("Wrong version:")
print(f"  Call 1: {r1}")   # ['img_001', 'img_002', 'img_003'] ← all three!
print(f"  Call 2: {r2}")   # same object — it's been growing
print(f"  Call 3: {r3}")   # same object again
print(f"  Same object? r1 is r2: {r1 is r2}")  # True — they're all the same list

print()

# CORRECT — None as default, create fresh inside when needed
def collect_sample(sample: str, batch: list | None = None) -> list:
    """
    Add a sample to a batch.

    Args:
        sample: Sample identifier to add.
        batch: Existing batch to extend, or None to start a new one.

    Returns:
        Updated batch list.
    """
    if batch is None:
        batch = []          # new list created here — not at def time
    batch.append(sample)
    return batch

r1 = collect_sample("img_001")
r2 = collect_sample("img_002")   # completely fresh batch
r3 = collect_sample("img_003")

print("Correct version:")
print(f"  Call 1: {r1}")   # ['img_001']
print(f"  Call 2: {r2}")   # ['img_002']
print(f"  Call 3: {r3}")   # ['img_003']

# You can still pass an existing batch explicitly — that still works
existing_batch = ["img_000"]
result = collect_sample("img_001", existing_batch)
print(f"  Extended: {result}")   # ['img_000', 'img_001']

# ── Part 3: main() entry point ────────────────────────────────────────────────

print()

# Best practice: define all functions first, call at the bottom via main()
# This guarantees every function is defined before any of them is called

def load_data(path: str) -> list:
    """Simulate loading a dataset from a path."""
    return [f"sample_{i}" for i in range(3)]   # fake data

def run_pipeline(data: list, batch_size: int = 2) -> None:
    """Process data in batches and log each one."""
    for i in range(0, len(data), batch_size):
        batch = data[i : i + batch_size]
        print(f"  Processing batch: {batch}")

def main() -> None:
    """Entry point — calls everything in order."""
    print("Pipeline starting...")
    data = load_data("dataset/train.csv")
    run_pipeline(data, batch_size=2)
    print("Pipeline complete.")

main()   # ← called last, after all definitions

# ── What to notice ────────────────────────────────────────────────────────────
#
# 1. Local scope is created fresh on every function call and destroyed on return.
#    Variables inside a function don't exist before the call or after it.
#
# 2. Python decides at compile time whether a name is local or global.
#    If it sees an assignment to a name inside a function, that name is local
#    for the ENTIRE function — even lines before the assignment.
#    That's why 'epoch_count = epoch_count + 1' causes UnboundLocalError.
#
# 3. The fix for globals: don't use them. Pass values in, return new values out.
#    This makes functions pure — their output depends only on their inputs.
#    Pure functions are easier to test, debug, and reuse.
#
# 4. The mutable default trap:
#    Default values are evaluated ONCE when the def statement runs.
#    [] creates one list object. Every call that uses the default
#    gets the SAME list object, not a new one.
#    Rule: never use a mutable object (list, dict, set) as a default.
#    Always use None and create inside.
#
# 5. main() pattern:
#    Define all functions → call main() at the bottom.
#    main() orchestrates the others. Nothing runs at import time
#    (important when you start writing modules in topic 13).