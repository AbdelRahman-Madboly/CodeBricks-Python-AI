"""
Dictionaries and Sets — Exercises
"""


# ---------------------------------------------------------------------------
# Exercise 1 (Easy) — Build and query a dict
#
# Problem:
#   Given the parallel lists below, build a dictionary mapping each model
#   name to its accuracy. Then:
#     a) Print each model and accuracy formatted as shown
#     b) Find and print the best model
#     c) Print all models with accuracy >= 0.90
#
#   Expected output:
#   ResNet-50      : 88.1%
#   EfficientNet-B4: 94.2%
#   MobileNet-V3   : 85.5%
#   ViT-Base       : 92.0%
#   Best model: EfficientNet-B4 (94.2%)
#   Above 90%: ['EfficientNet-B4', 'ViT-Base']
#
model_names = ["ResNet-50", "EfficientNet-B4", "MobileNet-V3", "ViT-Base"]
accuracies  = [0.881, 0.942, 0.855, 0.920]
#
# Your solution below:
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Exercise 2 (Medium) — Grouping with dicts
#
# Problem:
#   Given the list of detection records below, group them by label into a dict
#   where each key is a label and each value is the list of confidence scores
#   for that label. Then compute the average confidence per label.
#
#   Expected output:
#   face        : 3 samples | avg confidence: 0.913
#   background  : 2 samples | avg confidence: 0.770
#   hand        : 2 samples | avg confidence: 0.845
#
detections = [
    {"label": "face",       "confidence": 0.94},
    {"label": "background", "confidence": 0.82},
    {"label": "face",       "confidence": 0.91},
    {"label": "hand",       "confidence": 0.78},
    {"label": "background", "confidence": 0.72},
    {"label": "face",       "confidence": 0.89},
    {"label": "hand",       "confidence": 0.91},
]
#
# Your solution below:
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Exercise 3 (Hard) — Set-based pipeline validation
#
# Problem:
#   A data pipeline has a set of required fields that every record must contain.
#   Write a function validate_records() that:
#     - Takes a list of record dicts and a set of required field names
#     - Returns a dict with two keys:
#         "valid":   list of records that have ALL required fields
#         "invalid": list of dicts, each with the original record and a
#                    "missing_fields" key showing which fields are absent
#
#   Expected output:
#   Valid  : 2 records
#   Invalid: 2 records
#   img_003 missing: {'label'}
#   img_004 missing: {'confidence', 'width'}
#
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

    Args:
        records: List of record dicts.
        required: Set of field names every record must have.

    Returns:
        Dict with 'valid' and 'invalid' lists.
    """
    # TODO: implement
    pass


result = validate_records(records, required_fields)
print(f"Valid  : {len(result['valid'])} records")
print(f"Invalid: {len(result['invalid'])} records")
for item in result["invalid"]:
    print(f"{item['record'].get('filename', '???')} missing: {item['missing_fields']}")
