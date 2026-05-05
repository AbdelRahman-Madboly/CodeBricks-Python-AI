"""
solutions/03_pipeline_runner.py
─────────────────────────────────
Topic    : Exceptions
Solution : Exercise 3 — Pipeline runner
"""


# ── Task A — exception hierarchy ─────────────────────────────────────────────

class PipelineError(Exception):
    """Base class for all pipeline errors."""

class DataError(PipelineError):
    """Raised for bad or missing input data."""

class EpochError(PipelineError):
    """Raised for training failures."""


# ── Task B ────────────────────────────────────────────────────────────────────

def load_data(source: str) -> list[dict]:
    if source != "valid_source":
        raise DataError(f"source not found: {source!r}")
    return [
        {"label": "real", "confidence": 0.92},
        {"label": "fake", "confidence": 0.88},
        {"label": "real", "confidence": 0.95},
    ]


# ── Task C ────────────────────────────────────────────────────────────────────

def validate_records(records: list[dict]) -> int:
    if not records:
        raise DataError("empty dataset — nothing to train on")
    for rec in records:
        if "label" not in rec:
            raise DataError("record missing 'label' field")
    return len(records)


# ── Task D ────────────────────────────────────────────────────────────────────

def run_epoch(records: list[dict], epoch_num: int) -> dict:
    if epoch_num > 3:
        raise EpochError(f"out of memory at epoch {epoch_num}")
    return {"epoch": epoch_num, "loss": round(1.0 / epoch_num, 4)}


# ── Task E ────────────────────────────────────────────────────────────────────

def run_pipeline(source: str, epoch_num: int) -> dict | None:
    try:
        records = load_data(source)
        validate_records(records)
        result  = run_epoch(records, epoch_num)
    except DataError as e:
        print(f"DATA ERROR: {e}")
        return None
    except EpochError as e:
        print(f"EPOCH ERROR: {e}")
        return None
    else:
        print(f"Pipeline completed. Loss: {result['loss']}")
        return result
    finally:
        print("Pipeline teardown.")


run_pipeline("valid_source", 3)
print("---")
run_pipeline("missing_source", 3)
print("---")
run_pipeline("valid_source", 5)

# ── Why this works ────────────────────────────────────────────────────────────
#
# Exception hierarchy — PipelineError as base
#   DataError and EpochError both inherit from PipelineError.
#   This means:
#     except DataError    — catches only data problems
#     except EpochError   — catches only training problems
#     except PipelineError — catches either (useful at a higher level)
#     except Exception    — catches everything
#   The hierarchy gives callers a choice of how specific to be.
#
# run_pipeline — try/except/else/finally
#   try:     all three stages — if any raises, we jump to the matching except
#   except:  specific error types with specific messages — DataError vs EpochError
#   else:    only runs if ALL of try completed without exception
#            putting the success print here means it can never accidentally
#            catch an error from the print itself
#   finally: always runs — even if an exception propagated past all excepts
#            this is where you'd close files, release GPU memory, flush logs
#
# Why separate DataError and EpochError?
#   A caller at the orchestration level might want to:
#     - retry on EpochError (transient — maybe GPU memory frees up)
#     - alert the data team on DataError (permanent — the source is wrong)
#   Catching both as PipelineError and treating them the same loses that ability.
#   Custom exception types are how you preserve that information through the
#   call stack without passing extra flags or return codes.