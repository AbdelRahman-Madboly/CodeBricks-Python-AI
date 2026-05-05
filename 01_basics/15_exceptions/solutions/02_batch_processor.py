"""
solutions/02_batch_processor.py
─────────────────────────────────
Topic    : Exceptions
Solution : Exercise 2 — Batch processor
"""

records = [
    {"confidence": 0.94, "scale": 1.0},
    {"confidence": 0.88, "scale": 0},
    {"confidence": "high", "scale": 1.0},
    {"scale": 1.0},
    {"confidence": 0.76, "scale": 2.0},
]


def parse_score(record: dict, index: int) -> float | None:
    try:
        raw   = record["confidence"]          # KeyError if missing
        score = float(raw)                    # ValueError if not numeric
        norm  = score / record["scale"]       # ZeroDivisionError if scale=0
        return round(norm, 4)
    except KeyError as e:
        print(f"record {index}: missing field: {e}")
        return None
    except ValueError as e:
        print(f"record {index}: bad value for confidence: {e}")
        return None
    except ZeroDivisionError:
        print(f"record {index}: scale=0 — returning raw score: {record['confidence']}")
        return float(record["confidence"])


def process_batch(records: list[dict]) -> list[float]:
    results = []
    for i, rec in enumerate(records):
        score = parse_score(rec, i)
        if score is not None:
            results.append(score)
    return results


valid = process_batch(records)
print(f"\nValid scores: {valid}")

# ── Why this works ────────────────────────────────────────────────────────────
#
# parse_score — single try, multiple specific excepts
#   All three operations are inside one try block. Python raises the exception
#   at the first failing line and jumps to the matching except clause.
#   The order is: KeyError, ValueError, ZeroDivisionError — all specific,
#   no general Exception catch needed here because we know the possible errors.
#
# ZeroDivisionError recovery — partial handling
#   Instead of returning None, we return the raw score. This is deliberate:
#   scale=0 is unusual but the confidence value is still valid.
#   Different error types can have different recovery strategies.
#
# process_batch — filter on None
#   parse_score returns None on any error. The list comprehension approach
#   [parse_score(r, i) for i, r in enumerate(records) if parse_score(...) is not None]
#   would call parse_score twice per record — wasteful. Appending conditionally
#   in a loop calls it once and avoids duplicating the side-effect print.