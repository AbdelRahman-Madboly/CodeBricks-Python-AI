"""
Tuples — Solutions
"""


# ---------------------------------------------------------------------------
# Solution 1
# ---------------------------------------------------------------------------

camera_spec = ("front", 1920, 1080)
tag_sequence = ("deepfake", "real", "uncertain", "blurry")
rgb_color = (255, 128, 0)

camera_position, res_width, res_height = camera_spec
print(f"Camera: {camera_position}, Resolution: {res_width}x{res_height}")

first_tag, *remaining_tags = tag_sequence
print(f"First tag: {first_tag}, Remaining: {remaining_tags}")

red, green, blue = rgb_color
print(f"Red={red}, Green={green}, Blue={blue}")


# ---------------------------------------------------------------------------
# Solution 2
# ---------------------------------------------------------------------------

def split_dataset(sample_ids: list[str], ratio: float) -> tuple[list[str], list[str]]:
    """
    Split a list of sample IDs into training and validation sets.

    Args:
        sample_ids: Ordered list of sample identifiers.
        ratio: Fraction of samples to use for training (0.0 to 1.0).

    Returns:
        A tuple of (train_samples, val_samples).
    """
    split_index = int(len(sample_ids) * ratio)
    return sample_ids[:split_index], sample_ids[split_index:]


samples = ["s01", "s02", "s03", "s04", "s05", "s06", "s07", "s08", "s09", "s10"]
train, val = split_dataset(samples, 0.8)
print(f"Train ({len(train)}): {train}")
print(f"Val   ({len(val)}): {val}")


# ---------------------------------------------------------------------------
# Solution 3
# ---------------------------------------------------------------------------

evaluation_runs = [
    ("EfficientNet", "deepfake-v1", 0.94),
    ("ResNet-50",    "deepfake-v1", 0.91),
    ("EfficientNet", "deepfake-v1", 0.92),
    ("ResNet-50",    "deepfake-v1", 0.86),
    ("ResNet-50",    "deepfake-v2", 0.88),
]

# First pass: accumulate all scores per (model, dataset) key
accumulated: dict[tuple[str, str], list[float]] = {}
for model, dataset, accuracy in evaluation_runs:
    key = (model, dataset)
    if key not in accumulated:
        accumulated[key] = []
    accumulated[key].append(accuracy)

# Second pass: compute averages
averages: dict[tuple[str, str], float] = {
    key: round(sum(scores) / len(scores), 3)
    for key, scores in accumulated.items()
}

for key, avg in sorted(averages.items(), key=lambda item: item[1], reverse=True):
    print(f"{str(key):<35} → {avg:.3f}")
