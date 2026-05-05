"""
exercises/02_batch_processor.py
─────────────────────────────────
Topic    : Exceptions
Exercise : 2 of 3 — Medium
Concept  : Multiple except blocks, specific exception types, catch order

Context
-------
A batch processor reads detection records from a list, parses their
fields, and computes a normalised score. Each step can fail in a
different way — and the recovery strategy differs for each failure type.

─────────────────────────────────────────────────────────────────
Task A — parse_score()
─────────────────────────────────────────────────────────────────
Write a function that:
  1. Reads record["confidence"] — raises KeyError if missing
  2. Converts it to float — raises ValueError if not numeric
  3. Divides by record["scale"] — raises ZeroDivisionError if scale=0
  4. Returns the normalised score (rounded to 4 decimal places)

Each exception type should print a specific message and return None.

Signature:
  def parse_score(record: dict, index: int) -> float | None

Expected output (given the records list below):
  record 0: 0.94
  record 1: scale=0 — returning raw score: 0.88
  record 2: bad value for confidence: could not convert string to float: 'high'
  record 3: missing field: 'confidence'
  record 4: 0.38

─────────────────────────────────────────────────────────────────
Task B — process_batch()
─────────────────────────────────────────────────────────────────
Write a function that calls parse_score() for each record in the list
and returns only the non-None results.

Signature:
  def process_batch(records: list[dict]) -> list[float]

Expected output:
  Valid scores: [0.94, 0.88, 0.38]
─────────────────────────────────────────────────────────────────
"""

records = [
    {"confidence": 0.94, "scale": 1.0},     # happy path
    {"confidence": 0.88, "scale": 0},        # ZeroDivisionError
    {"confidence": "high", "scale": 1.0},    # ValueError
    {"scale": 1.0},                          # KeyError
    {"confidence": 0.76, "scale": 2.0},     # happy path → 0.38
]


# ── Task A ────────────────────────────────────────────────────────────────────

def parse_score(record: dict, index: int) -> float | None:
    """
    Parse and normalise the confidence score from a record.
    Returns None on any error, printing a specific message per error type.
    """
    # TODO: implement
    pass


# ── Task B ────────────────────────────────────────────────────────────────────

def process_batch(records: list[dict]) -> list[float]:
    """Run parse_score on each record, return only valid results."""
    # TODO: implement
    pass


# ── Run ───────────────────────────────────────────────────────────────────────

valid = process_batch(records)
print(f"\nValid scores: {valid}")