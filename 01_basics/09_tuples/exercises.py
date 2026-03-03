"""
Tuples — Exercises
"""


# ---------------------------------------------------------------------------
# Exercise 1 (Easy) — Unpacking practice
#
# Problem:
#   Unpack each tuple using the appropriate unpacking style.
#   Do not use indexing (no t[0], t[1], etc.).
#
#   Expected output:
#   Camera: front, Resolution: 1920x1080
#   First tag: deepfake, Remaining: ['real', 'uncertain', 'blurry']
#   Red=255, Green=128, Blue=0
#
camera_spec = ("front", 1920, 1080)
tag_sequence = ("deepfake", "real", "uncertain", "blurry")
rgb_color = (255, 128, 0)
#
# Your solution below:
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Exercise 2 (Medium) — Function returning a tuple
#
# Problem:
#   Write a function called split_dataset() that takes a list of sample IDs
#   and a split ratio (float between 0 and 1), and returns a tuple of two lists:
#   (train_samples, val_samples).
#   The split should be based on the ratio without shuffling.
#
#   Expected output:
#   Train (8): ['s01', 's02', 's03', 's04', 's05', 's06', 's07', 's08']
#   Val   (2): ['s09', 's10']
#
samples = ["s01", "s02", "s03", "s04", "s05", "s06", "s07", "s08", "s09", "s10"]
#
# Your solution below:
# ---------------------------------------------------------------------------

# Uncomment to test:
# train, val = split_dataset(samples, 0.8)
# print(f"Train ({len(train)}): {train}")
# print(f"Val   ({len(val)}): {val}")


# ---------------------------------------------------------------------------
# Exercise 3 (Hard) — Tuple as dict key + aggregation
#
# Problem:
#   Given the list of evaluation records below, build a dictionary keyed by
#   (model, dataset) tuples that stores the AVERAGE accuracy across all runs
#   for that combination.
#
#   Expected output:
#   ('EfficientNet', 'deepfake-v1') → 0.930
#   ('ResNet-50', 'deepfake-v1')    → 0.885
#   ('ResNet-50', 'deepfake-v2')    → 0.880
#
evaluation_runs = [
    ("EfficientNet", "deepfake-v1", 0.94),
    ("ResNet-50",    "deepfake-v1", 0.91),
    ("EfficientNet", "deepfake-v1", 0.92),
    ("ResNet-50",    "deepfake-v1", 0.86),
    ("ResNet-50",    "deepfake-v2", 0.88),
]
#
# Constraints:
#   - Result dict keys must be tuples
#   - Values must be averaged floats rounded to 3 decimal places
#
# Your solution below:
# ---------------------------------------------------------------------------
