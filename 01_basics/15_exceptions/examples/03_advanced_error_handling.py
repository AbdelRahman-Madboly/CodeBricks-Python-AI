"""
examples/03_advanced_error_handling.py
────────────────────────────────────────
Topic  : Exceptions
Example: 3 of 3 — Advanced
Concept: else clause, finally clause, custom exception classes, re-raise

Context
-------
A training pipeline loads a dataset, validates it, runs an epoch, and
saves the checkpoint — even if something fails. The else clause runs
post-success logic cleanly. finally ensures cleanup always happens.
Custom exceptions make error taxonomy explicit across a large codebase.

Covers:
  - try/except/else — else runs only when no exception was raised
  - try/except/finally — finally always runs (cleanup, resource release)
  - try/except/else/finally — full form
  - Custom exception classes (inheriting from Exception)
  - raise ... from ... — chaining exceptions
  - re-raise with bare raise

Run this file. Predict each output before you see it.
"""

# ── else clause ───────────────────────────────────────────────────────────────

print("=== try/except/else ===")

def load_batch(batch_id: int) -> list[float]:
    if batch_id < 0:
        raise ValueError(f"batch_id must be non-negative, got {batch_id}")
    return [0.91, 0.74, 0.58, 0.47]


for bid in [2, -1, 5]:
    try:
        batch = load_batch(bid)
    except ValueError as e:
        print(f"  batch {bid}: FAILED  — {e}")
    else:
        # Only runs if NO exception was raised
        avg = sum(batch) / len(batch)
        print(f"  batch {bid}: OK      — avg={avg:.3f}, n={len(batch)}")

# The else clause avoids nesting success logic inside the try block.
# Without else you'd put the avg calculation inside try — making it
# harder to tell which line triggered the exception if one is added later.

# ── finally clause ────────────────────────────────────────────────────────────

print()
print("=== try/except/finally ===")

def process_file(filename: str, should_fail: bool = False) -> None:
    """Simulate opening a file, processing it, and always closing it."""
    print(f"  Opening {filename}")
    try:
        if should_fail:
            raise RuntimeError("corrupt data in file")
        print(f"  Processing {filename} — success")
    except RuntimeError as e:
        print(f"  Error during processing: {e}")
    finally:
        # Runs whether or not an exception was raised — guaranteed cleanup
        print(f"  Closing {filename}")


process_file("batch_001.bin")
print()
process_file("batch_002.bin", should_fail=True)

# In real code, finally is where you release resources:
# close file handles, database connections, GPU memory, etc.
# Python's `with` statement automates this pattern — topic 03_pythonic.

# ── Full form: try/except/else/finally ───────────────────────────────────────

print()
print("=== Full form ===")

def run_epoch(epoch: int, fail_at: int | None = None) -> dict | None:
    """Run one training epoch with full error handling."""
    print(f"  [epoch {epoch}] starting")
    try:
        if epoch == fail_at:
            raise RuntimeError(f"GPU out of memory at epoch {epoch}")
        loss = round(1.0 / (epoch + 1), 4)   # fake decreasing loss
    except RuntimeError as e:
        print(f"  [epoch {epoch}] FAILED: {e}")
        return None
    else:
        print(f"  [epoch {epoch}] loss={loss}")
        return {"epoch": epoch, "loss": loss}
    finally:
        print(f"  [epoch {epoch}] cleanup done")   # always runs


run_epoch(1)
print()
run_epoch(2, fail_at=2)

# ── Custom exception classes ──────────────────────────────────────────────────

print()
print("=== Custom exceptions ===")

class PipelineError(Exception):
    """Base class for all pipeline errors in this project."""

class ValidationError(PipelineError):
    """Raised when a data record fails validation."""

class CheckpointError(PipelineError):
    """Raised when a checkpoint cannot be loaded or saved."""


def validate_record(record: dict) -> None:
    """Validate a detection record. Raises ValidationError on bad data."""
    if "confidence" not in record:
        raise ValidationError(f"missing 'confidence' in record: {record}")
    if not 0.0 <= record["confidence"] <= 1.0:
        raise ValidationError(
            f"confidence {record['confidence']} is out of range [0, 1]"
        )


test_records = [
    {"label": "real",  "confidence": 0.92},   # valid
    {"label": "fake"},                          # missing field
    {"label": "real",  "confidence": 1.5},     # out of range
]

for rec in test_records:
    try:
        validate_record(rec)
        print(f"  {rec['label']:<6} conf={rec.get('confidence', '?')} → VALID")
    except ValidationError as e:
        print(f"  INVALID: {e}")
    except PipelineError as e:
        # Catches any other pipeline-level error
        print(f"  PIPELINE ERROR: {e}")

# Custom exceptions let callers catch errors at the right level of specificity:
#   except ValidationError — only data validation problems
#   except PipelineError   — any pipeline problem
#   except Exception       — anything at all

# ── re-raise ──────────────────────────────────────────────────────────────────

print()
print("=== re-raise ===")

def load_weights(path: str) -> dict:
    """Load weights. Re-raises after logging so the caller also sees the error."""
    try:
        if path == "corrupt.pt":
            raise CheckpointError(f"file {path!r} is corrupt")
        return {"weights": "..."}
    except CheckpointError as e:
        print(f"  [load_weights] logging error: {e}")
        raise   # bare raise — re-raises the same exception


try:
    load_weights("corrupt.pt")
except CheckpointError as e:
    print(f"  [caller] caught re-raised error: {e}")

# ── What to notice ────────────────────────────────────────────────────────────
#
# 1. else runs only when no exception was raised in try.
#    Use it for "success path" logic that shouldn't be inside try,
#    because you don't want to accidentally catch errors from that logic.
#
# 2. finally always runs — even if an exception was raised AND not caught,
#    even if there's a return inside try or except.
#    Use it for cleanup that must happen regardless of outcome.
#
# 3. Custom exceptions inherit from Exception (or a project base class).
#    They make your error taxonomy explicit:
#      except ValidationError  — I know what went wrong and can recover
#      except PipelineError    — something in the pipeline failed
#      except Exception        — something completely unexpected
#
# 4. Bare raise (no argument) re-raises the current exception unchanged.
#    Use it when you want to log or partially handle an error, but still
#    let it propagate up to the caller.
#
# 5. The full form — try/except/else/finally — is uncommon but clean.
#    In practice, you'll mostly use try/except or try/finally (via `with`).