"""
Dictionaries and Sets — Solutions
"""


# ---------------------------------------------------------------------------
# Solution 1
# ---------------------------------------------------------------------------

model_names = ["ResNet-50", "EfficientNet-B4", "MobileNet-V3", "ViT-Base"]
accuracies  = [0.881, 0.942, 0.855, 0.920]

model_scores = dict(zip(model_names, accuracies))

for name, acc in model_scores.items():
    print(f"{name:<16}: {acc:.1%}")

best_model = max(model_scores, key=lambda m: model_scores[m])
print(f"Best model: {best_model} ({model_scores[best_model]:.1%})")

above_90 = [name for name, acc in model_scores.items() if acc >= 0.90]
print(f"Above 90%: {above_90}")


# ---------------------------------------------------------------------------
# Solution 2
# ---------------------------------------------------------------------------

detections = [
    {"label": "face",       "confidence": 0.94},
    {"label": "background", "confidence": 0.82},
    {"label": "face",       "confidence": 0.91},
    {"label": "hand",       "confidence": 0.78},
    {"label": "background", "confidence": 0.72},
    {"label": "face",       "confidence": 0.89},
    {"label": "hand",       "confidence": 0.91},
]

# Group scores by label
grouped: dict[str, list[float]] = {}
for det in detections:
    label = det["label"]
    grouped.setdefault(label, []).append(det["confidence"])

# Report averages
for label, scores in grouped.items():
    avg = sum(scores) / len(scores)
    print(f"{label:<12}: {len(scores)} samples | avg confidence: {avg:.3f}")


# ---------------------------------------------------------------------------
# Solution 3
# ---------------------------------------------------------------------------

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
    valid = []
    invalid = []

    for record in records:
        present_fields = set(record.keys())
        missing = required - present_fields   # set difference

        if missing:
            invalid.append({"record": record, "missing_fields": missing})
        else:
            valid.append(record)

    return {"valid": valid, "invalid": invalid}


result = validate_records(records, required_fields)
print(f"Valid  : {len(result['valid'])} records")
print(f"Invalid: {len(result['invalid'])} records")
for item in result["invalid"]:
    print(f"{item['record'].get('filename', '???')} missing: {item['missing_fields']}")
