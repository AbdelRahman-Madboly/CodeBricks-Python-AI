"""
exercises/03_pipeline_runner.py
─────────────────────────────────
Topic    : Exceptions
Exercise : 3 of 3 — Hard
Concept  : Custom exceptions, else/finally, re-raise, exception hierarchy

Context
-------
A training pipeline has three stages: load data, validate records, run
epoch. Each stage has its own failure mode. Custom exceptions make the
error taxonomy explicit so callers can respond at exactly the right level.

─────────────────────────────────────────────────────────────────
Task A — Define the exception hierarchy
─────────────────────────────────────────────────────────────────
Define three custom exception classes:
  - PipelineError(Exception)          — base class for all pipeline errors
  - DataError(PipelineError)          — raised for bad input data
  - EpochError(PipelineError)         — raised for training failures

─────────────────────────────────────────────────────────────────
Task B — load_data()
─────────────────────────────────────────────────────────────────
Write load_data(source) that:
  - Returns a list of records if source is "valid_source"
  - Raises DataError("source not found: '<source>'") otherwise

─────────────────────────────────────────────────────────────────
Task C — validate_records()
─────────────────────────────────────────────────────────────────
Write validate_records(records) that:
  - Raises DataError("empty dataset — nothing to train on") if records is empty
  - Raises DataError("record missing 'label' field") if any record has no "label"
  - Returns the count of valid records otherwise

─────────────────────────────────────────────────────────────────
Task D — run_epoch()
─────────────────────────────────────────────────────────────────
Write run_epoch(records, epoch_num) that:
  - Raises EpochError("out of memory at epoch <N>") if epoch_num > 3
  - Returns {"epoch": epoch_num, "loss": round(1.0 / epoch_num, 4)} otherwise

─────────────────────────────────────────────────────────────────
Task E — run_pipeline()
─────────────────────────────────────────────────────────────────
Write run_pipeline(source, epoch_num) that calls all three functions
in sequence using try/except/else/finally:
  - try: load_data, validate_records, run_epoch
  - except DataError: print "DATA ERROR: <msg>", return None
  - except EpochError: print "EPOCH ERROR: <msg>", return None
  - else: print "Pipeline completed. Loss: <loss>", return the result dict
  - finally: print "Pipeline teardown."

Expected output for the test calls below:
  Pipeline teardown.
  Pipeline completed. Loss: 0.3333
  ---
  DATA ERROR: source not found: 'missing_source'
  Pipeline teardown.
  ---
  EPOCH ERROR: out of memory at epoch 5
  Pipeline teardown.
─────────────────────────────────────────────────────────────────
"""

# ── Task A — exception hierarchy ─────────────────────────────────────────────

# TODO: define PipelineError, DataError, EpochError


# ── Task B ────────────────────────────────────────────────────────────────────

def load_data(source: str) -> list[dict]:
    # TODO: implement
    pass


# ── Task C ────────────────────────────────────────────────────────────────────

def validate_records(records: list[dict]) -> int:
    # TODO: implement
    pass


# ── Task D ────────────────────────────────────────────────────────────────────

def run_epoch(records: list[dict], epoch_num: int) -> dict:
    # TODO: implement
    pass


# ── Task E ────────────────────────────────────────────────────────────────────

def run_pipeline(source: str, epoch_num: int) -> dict | None:
    # TODO: implement
    pass


# ── Test calls ────────────────────────────────────────────────────────────────

run_pipeline("valid_source", 3)
print("---")
run_pipeline("missing_source", 3)
print("---")
run_pipeline("valid_source", 5)