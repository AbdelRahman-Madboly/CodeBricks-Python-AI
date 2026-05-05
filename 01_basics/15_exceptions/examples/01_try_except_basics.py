"""
examples/01_try_except_basics.py
──────────────────────────────────
Topic  : Exceptions
Example: 1 of 3 — Easy
Concept: try/except, raise, Exception as e, exceptions are not bugs

Context
-------
A model loader reads checkpoints from disk. Missing files, corrupt
weights, and bad paths are expected in production — they're not bugs.
The try/except pattern lets the pipeline recover gracefully instead
of crashing the entire training run.

Covers:
  - try/except — catching exceptions
  - except Exception as e — accessing the error message
  - raise — triggering your own exceptions
  - The rule: raise in the function, catch at the call site
  - Why exceptions are not bugs

Run this file. Predict each output before you see it.
"""

# ── Basic try/except ──────────────────────────────────────────────────────────

print("=== Basic try/except ===")

# Without protection — crashes the program
# result = 10 / 0   # ZeroDivisionError: division by zero

# With try/except — handles gracefully
try:
    result = 10 / 0
except Exception as e:
    print(f"Caught: {e}")       # Caught: division by zero

# The try block runs until an exception is raised or it completes.
# The except block runs ONLY if an exception was raised.
# If no exception is raised, the except block is skipped entirely.

try:
    result = 10 / 2    # no exception
    print(f"Result: {result}")  # 5.0 — this prints
except Exception as e:
    print("This never prints")  # skipped

# ── Accessing the exception ───────────────────────────────────────────────────

print()
print("=== Accessing exception data ===")

try:
    nums = [0.91, 0.74, 0.58]
    print(nums[10])    # IndexError — index 10 doesn't exist
except Exception as e:
    print(f"Type : {type(e).__name__}")   # IndexError
    print(f"Msg  : {e}")                  # list index out of range

# ── raise — triggering your own exceptions ────────────────────────────────────

print()
print("=== raise ===")

def load_checkpoint(path: str) -> dict:
    """
    Load a model checkpoint from a path.
    Raises ValueError if the path is empty or doesn't end in .pt
    """
    if not path:
        raise ValueError("checkpoint path cannot be empty")
    if not path.endswith(".pt"):
        raise ValueError(f"expected a .pt file, got: {path!r}")

    # In real code: torch.load(path) — simulated here
    return {"model": "ResNet-50", "epoch": 15, "val_acc": 0.91}


# Caller handles the exception — the function does NOT catch its own raise
try:
    ckpt = load_checkpoint("")
except ValueError as e:
    print(f"Bad checkpoint: {e}")   # Bad checkpoint: checkpoint path cannot be empty

try:
    ckpt = load_checkpoint("weights.pkl")
except ValueError as e:
    print(f"Bad checkpoint: {e}")   # Bad checkpoint: expected a .pt file...

# Happy path — no exception
try:
    ckpt = load_checkpoint("epoch_15.pt")
    print(f"Loaded: {ckpt}")
except ValueError as e:
    print(f"Bad checkpoint: {e}")   # skipped

# ── Exceptions are not bugs ───────────────────────────────────────────────────

print()
print("=== Exceptions are not bugs ===")

def safe_divide(a: float, b: float) -> float:
    """Divide a by b. Raises ZeroDivisionError if b is 0."""
    if b == 0:
        raise ZeroDivisionError("denominator cannot be zero")
    return a / b


# This is expected behaviour — not a bug
for numerator, denominator in [(10, 2), (5, 0), (9, 3)]:
    try:
        result = safe_divide(numerator, denominator)
        print(f"  {numerator} / {denominator} = {result:.2f}")
    except ZeroDivisionError as e:
        print(f"  {numerator} / {denominator} → skipped ({e})")

# ── What to notice ────────────────────────────────────────────────────────────
#
# 1. The except block only runs if an exception was raised in the try block.
#    If the try block completes without error, except is completely skipped.
#
# 2. except Exception as e gives you the exception object.
#    e is the exception instance. str(e) or print(e) gives the message.
#    type(e).__name__ gives the class name ("ValueError", "IndexError", etc.)
#
# 3. raise stops execution immediately — like return, but for errors.
#    Anything after raise in the same block never runs.
#
# 4. A function should raise exceptions; it should NOT catch its own raises.
#    The caller decides how to handle bad inputs — the function just signals them.
#    This separation of concerns keeps functions clean and testable.
#
# 5. Exceptions in production are normal. Network drops, missing files,
#    bad user input — all expected. A bug is when code behaves unexpectedly.
#    An exception you raise deliberately is a contract, not a failure.