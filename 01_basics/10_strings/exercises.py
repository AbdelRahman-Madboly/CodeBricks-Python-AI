"""
Strings — Exercises
"""


# ---------------------------------------------------------------------------
# Exercise 1 (Easy) — String methods and formatting
#
# Problem:
#   Given the raw filename below, produce the expected cleaned output
#   using string methods only (no regex, no imports).
#
#   raw:      "  Train_DeepFake_Dataset__V2.CSV  "
#   Expected: "train-deepfake-dataset-v2.csv"
#
#   Steps: strip → lowercase → replace double underscores with single dash
#          → replace remaining underscores with dashes
#
raw_filename = "  Train_DeepFake_Dataset__V2.CSV  "
#
# Your solution (one expression or a few chained method calls):
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Exercise 2 (Medium) — Parse a structured string
#
# Problem:
#   Each line in a model registry file has this format:
#   "model_name::version::accuracy::dataset"
#
#   Write a function parse_registry_line() that takes one such line and
#   returns a dict with keys: model, version, accuracy (float), dataset.
#
#   Expected output:
#   {'model': 'EfficientNet-B4', 'version': 'v2.1', 'accuracy': 0.942, 'dataset': 'deepfake-v2'}
#   {'model': 'ResNet-50', 'version': 'v1.0', 'accuracy': 0.881, 'dataset': 'deepfake-v1'}
#
registry_lines = [
    "EfficientNet-B4::v2.1::0.942::deepfake-v2",
    "ResNet-50::v1.0::0.881::deepfake-v1",
]
#
# Your solution below:
# ---------------------------------------------------------------------------

# Uncomment to test:
# for line in registry_lines:
#     print(parse_registry_line(line))


# ---------------------------------------------------------------------------
# Exercise 3 (Hard) — String analysis without imports
#
# Problem:
#   Write a function analyze_label_sequence() that takes a string of
#   comma-separated labels and returns a summary dict containing:
#     - total: total number of labels
#     - unique: number of unique labels
#     - most_common: the label that appears most often
#     - formatted: labels joined with " | " and title-cased
#
#   Expected output:
#   {
#     'total': 8,
#     'unique': 3,
#     'most_common': 'fake',
#     'formatted': 'Real | Fake | Fake | Real | Uncertain | Fake | Real | Fake'
#   }
#
label_string = "real,fake,fake,real,uncertain,fake,real,fake"
#
# Constraints:
#   - No imports (no Counter, no collections)
#   - Use only string methods, lists, and dicts
#
# Your solution below:
# ---------------------------------------------------------------------------

# Uncomment to test:
# print(analyze_label_sequence(label_string))
