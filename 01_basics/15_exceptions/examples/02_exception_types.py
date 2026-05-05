"""
examples/02_exception_types.py
────────────────────────────────
Topic  : Exceptions
Example: 2 of 3 — Medium
Concept: Specific exception types, multiple except blocks, catch order, built-ins

Context
-------
A batch processor reads records from a list, parses numeric fields,
and divides by a normalisation factor. Each of these steps can fail
in a different way — and the recovery strategy differs for each.
Catching specific types lets you respond appropriately instead of
treating every error the same.

Covers:
  - Built-in exception types: ValueError, IndexError, ZeroDivisionError, TypeError, KeyError
  - Multiple except blocks — most specific first
  - Why order matters: general Exception catches everything below it
  - Checking exception type with isinstance()
  - Catching multiple types in one except clause

Run this file. Predict each output before you see it.
"""

# ── Built-in exception types ──────────────────────────────────────────────────

print("=== Common built-in exceptions ===")

# ValueError — right type, wrong value
try:
    score = float("not_a_number")
except ValueError as e:
    print(f"ValueError  : {e}")

# IndexError — list access out of range
try:
    batch = [0.91, 0.74, 0.58]
    print(batch[10])
except IndexError as e:
    print(f"IndexError  : {e}")

# ZeroDivisionError — divide by zero
try:
    normalised = 0.9 / 0
except ZeroDivisionError as e:
    print(f"ZeroDivErr  : {e}")

# TypeError — wrong type entirely
try:
    result = "score" + 0.91   # can't add str and float
except TypeError as e:
    print(f"TypeError   : {e}")

# KeyError — missing dict key
try:
    record = {"label": "real"}
    print(record["confidence"])
except KeyError as e:
    print(f"KeyError    : {e}")   # 'confidence'

# ── Multiple except blocks — order matters ────────────────────────────────────

print()
print("=== Multiple except blocks ===")

def parse_record(record: dict, index: int) -> float:
    """
    Extract and normalise the confidence score from a detection record.
    Different errors get different recovery paths.
    """
    try:
        raw = record["confidence"]           # KeyError if missing
        score = float(raw)                   # ValueError if not numeric
        normalised = score / record["scale"] # ZeroDivisionError if scale=0
        return round(normalised, 4)
    except KeyError as e:
        print(f"  [record {index}] missing field: {e} → skipping")
        return None
    except ValueError as e:
        print(f"  [record {index}] bad value: {e} → skipping")
        return None
    except ZeroDivisionError:
        print(f"  [record {index}] scale=0 — using raw score instead")
        return float(record["confidence"])
    except Exception as e:
        # Catch-all for anything unexpected — always last
        print(f"  [record {index}] unexpected error: {type(e).__name__}: {e}")
        return None


records = [
    {"confidence": 0.94, "scale": 1.0},    # happy path
    {"confidence": 0.88, "scale": 0},       # ZeroDivisionError
    {"confidence": "high", "scale": 1.0},   # ValueError
    {"scale": 1.0},                         # KeyError — missing confidence
    {"confidence": 0.76, "scale": 2.0},    # happy path
]

results = []
for i, rec in enumerate(records):
    result = parse_record(rec, i)
    if result is not None:
        results.append(result)

print(f"\nValid results: {results}")

# ── Why order matters ─────────────────────────────────────────────────────────

print()
print("=== Wrong order — general catches everything ===")

try:
    nums = [1, 2, 3]
    print(nums[10])
except Exception:
    print("  general Exception caught it")   # this runs
except IndexError:
    print("  IndexError caught it")          # NEVER reached — Exception above caught it

print()
print("=== Correct order — specific first ===")

try:
    nums = [1, 2, 3]
    print(nums[10])
except IndexError:
    print("  IndexError caught it")          # this runs — correct
except Exception:
    print("  general Exception (fallback)")  # only for other errors

# ── Catching multiple types in one clause ─────────────────────────────────────

print()
print("=== Catching multiple types at once ===")

def safe_parse(raw: str) -> float | None:
    """Parse a string to float, treating type and value errors the same."""
    try:
        return float(raw)
    except (ValueError, TypeError):
        return None


test_inputs = ["0.91", "high", None, "0.74", ""]
parsed = [safe_parse(x) for x in test_inputs]
print(f"Parsed: {parsed}")   # [0.91, None, None, 0.74, None]

# ── What to notice ────────────────────────────────────────────────────────────
#
# 1. Always put specific exception types before the general Exception fallback.
#    Python checks each except clause top-to-bottom and stops at the first match.
#    Exception matches everything — if it comes first, nothing below it ever runs.
#
# 2. The type of an exception is what matters for matching, not its message.
#    except ZeroDivisionError only catches ZeroDivisionError.
#    except Exception catches ZeroDivisionError AND everything else.
#    raise Exception("zero division") does NOT match except ZeroDivisionError —
#    even though the message says "zero division".
#
# 3. except (TypeError, ValueError) catches either type in one clause.
#    Use this when the recovery path is the same for both.
#
# 4. The catch-all except Exception at the end is good defensive practice
#    for production code — it prevents the program from crashing on truly
#    unexpected errors while still logging what happened.
#
# 5. isinstance(e, IndexError) inside a bare except lets you inspect the
#    type programmatically — useful when routing errors in a loop.