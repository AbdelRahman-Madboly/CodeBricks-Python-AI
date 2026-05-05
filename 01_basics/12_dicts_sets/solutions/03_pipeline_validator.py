"""
solutions/03_pipeline_validator.py
────────────────────────────────────
Topic    : Dictionaries and Sets
Solution : Exercise 3 — Pipeline validator
"""

required_fields = {"filename", "label", "confidence", "width", "height"}

records = [
    {"filename": "img_001", "label": "real",  "confidence": 0.92, "width": 1280, "height": 720},
    {"filename": "img_002", "label": "fake",  "confidence": 0.88, "width": 1920, "height": 1080},
    {"filename": "img_003", "confidence": 0.75, "width": 640, "height": 480},
    {"filename": "img_004", "label": "real",  "height": 720},
]


def validate_records(
    records: list[dict], required: set[str]
) -> dict[str, list]:
    """
    Split records into valid and invalid based on required fields.
    """
    valid   = []
    invalid = []

    for record in records:
        missing = required - set(record.keys())   # set difference
        if missing:
            invalid.append({"record": record, "missing_fields": missing})
        else:
            valid.append(record)

    return {"valid": valid, "invalid": invalid}


def field_gap_report(invalid: list[dict]) -> dict[str, int]:
    """
    Count how many records are missing each field.
    """
    gaps: dict[str, int] = {}
    for item in invalid:
        for field in item["missing_fields"]:
            gaps[field] = gaps.get(field, 0) + 1
    return gaps


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

# ── Why this works ────────────────────────────────────────────────────────────
#
# validate_records — set difference on dict keys
#   set(record.keys()) gives the set of fields this record has.
#   required - set(record.keys()) gives fields in required but NOT in the record.
#   This is the cleanest way to check for missing fields — one expression,
#   no loop over required, no if/in checks.
#   An empty set is falsy in Python, so "if missing:" is True only when
#   at least one required field is absent.
#
# field_gap_report — frequency count over sets
#   Each item["missing_fields"] is a set. Iterating over a set gives each
#   element once — so we count how many records have each missing field.
#   This is the same .get(field, 0) + 1 pattern from exercises 1 and 2,
#   applied one level deeper (iterating over a set inside a list of dicts).
#
# Why return {"valid": ..., "invalid": ...} instead of two separate lists?
#   Functions with multiple related outputs are cleaner as a single dict return
#   than as a tuple. The caller can unpack what they need by name:
#     result["valid"] or result["invalid"]
#   rather than remembering positional order.
#   In production code you'd use a dataclass or TypedDict for this pattern —
#   you'll learn those in Phase 5 (type hints and Pydantic).