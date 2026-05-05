"""
exercises/03_pipeline_validator.py
────────────────────────────────────
Topic    : Dictionaries and Sets
Exercise : 3 of 3 — Hard
Concept  : Set operations on dict keys, validation logic, structured return values

Context
-------
A data pipeline ingests records from multiple sources. Before training,
every record must pass a field validation check. Some records are missing
required fields — you need to split them into valid and invalid, report
exactly which fields are missing per record, and summarise the gaps across
the entire batch so the data team knows what to fix.

─────────────────────────────────────────────────────────────────
Task A — validate_records()
─────────────────────────────────────────────────────────────────
Write a function that splits a list of records into valid and invalid.

Signature:
  def validate_records(
      records: list[dict], required: set[str]
  ) -> dict[str, list]:

Returns a dict with two keys:
  "valid"   — list of records that contain ALL required fields
  "invalid" — list of dicts, each with:
                 "record"         : the original record
                 "missing_fields" : set of field names that are absent

Expected output:
  Valid  : 2 records
  Invalid: 2 records
  img_003 missing: {'label'}
  img_004 missing: {'confidence', 'width'}

Hint: use set difference — required - set(record.keys())

─────────────────────────────────────────────────────────────────
Task B — field_gap_report()
─────────────────────────────────────────────────────────────────
Write a function that takes the invalid list from Task A and returns
a dict mapping each missing field name to the count of records that
are missing it. This tells the data team which fields need the most
attention.

Signature:
  def field_gap_report(invalid: list[dict]) -> dict[str, int]:

Expected output:
  Field gap report:
    label      : 1 record(s) missing
    confidence : 1 record(s) missing
    width      : 1 record(s) missing
─────────────────────────────────────────────────────────────────
"""

required_fields = {"filename", "label", "confidence", "width", "height"}

records = [
    {"filename": "img_001", "label": "real",  "confidence": 0.92, "width": 1280, "height": 720},
    {"filename": "img_002", "label": "fake",  "confidence": 0.88, "width": 1920, "height": 1080},
    {"filename": "img_003", "confidence": 0.75, "width": 640, "height": 480},           # missing: label
    {"filename": "img_004", "label": "real",  "height": 720},                            # missing: confidence, width
]


# ── Task A ────────────────────────────────────────────────────────────────────

def validate_records(
    records: list[dict], required: set[str]
) -> dict[str, list]:
    """
    Split records into valid and invalid based on required fields.

    Args:
        records: List of record dicts.
        required: Set of field names every record must have.

    Returns:
        Dict with 'valid' (list of records) and
        'invalid' (list of {record, missing_fields} dicts).
    """
    # TODO: implement
    pass


# ── Task B ────────────────────────────────────────────────────────────────────

def field_gap_report(invalid: list[dict]) -> dict[str, int]:
    """
    Count how many records are missing each field.

    Args:
        invalid: The 'invalid' list from validate_records().

    Returns:
        Dict mapping field name to missing-record count.
    """
    # TODO: implement
    pass


# ── Run and print ─────────────────────────────────────────────────────────────

result = validate_records(records, required_fields)
print(f"Valid  : {len(result['valid'])} records")
print(f"Invalid: {len(result['invalid'])} records")
for item in result["invalid"]:
    print(f"  {item['record'].get('filename', '???')} missing: {item['missing_fields']}")

print()
print("Field gap report:")
gaps = field_gap_report(result["invalid"])
for field, count in gaps.items():
    print(f"  {field:<12}: {count} record(s) missing")