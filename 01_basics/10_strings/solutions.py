"""
Strings — Solutions
"""


# ---------------------------------------------------------------------------
# Solution 1
# ---------------------------------------------------------------------------

raw_filename = "  Train_DeepFake_Dataset__V2.CSV  "

cleaned = raw_filename.strip().lower().replace("__", "-").replace("_", "-")
print(cleaned)   # train-deepfake-dataset-v2.csv


# ---------------------------------------------------------------------------
# Solution 2
# ---------------------------------------------------------------------------

def parse_registry_line(line: str) -> dict:
    """
    Parse a model registry line into a structured dictionary.

    Args:
        line: A string in the format "model::version::accuracy::dataset".

    Returns:
        Dict with keys: model, version, accuracy (float), dataset.
    """
    model, version, accuracy, dataset = line.split("::")
    return {
        "model": model,
        "version": version,
        "accuracy": float(accuracy),
        "dataset": dataset,
    }


registry_lines = [
    "EfficientNet-B4::v2.1::0.942::deepfake-v2",
    "ResNet-50::v1.0::0.881::deepfake-v1",
]

for line in registry_lines:
    print(parse_registry_line(line))


# ---------------------------------------------------------------------------
# Solution 3
# ---------------------------------------------------------------------------

def analyze_label_sequence(label_string: str) -> dict:
    """
    Analyze a comma-separated label string and return summary statistics.

    Args:
        label_string: Comma-separated labels e.g. "real,fake,fake,real".

    Returns:
        Dict with total, unique, most_common, and formatted keys.
    """
    labels = label_string.split(",")

    # Count occurrences manually — no Counter
    counts: dict[str, int] = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1

    # Find most common — manual loop over dict
    most_common = ""
    top_count = 0
    for label, count in counts.items():
        if count > top_count:
            top_count = count
            most_common = label

    return {
        "total": len(labels),
        "unique": len(counts),
        "most_common": most_common,
        "formatted": " | ".join(label.title() for label in labels),
    }


label_string = "real,fake,fake,real,uncertain,fake,real,fake"
print(analyze_label_sequence(label_string))
