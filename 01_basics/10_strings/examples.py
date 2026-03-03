"""
Strings — Examples

Covers f-string formatting, common string methods, splitting/joining,
and performance-aware string building patterns.
"""


# ---------------------------------------------------------------------------
# Example 1 — F-string formatting options
# Scenario: formatting a training progress log line
# ---------------------------------------------------------------------------

epoch = 12
total_epochs = 50
loss = 0.04231
accuracy = 0.9187
elapsed_seconds = 142.5

# Basic embedding
print(f"Epoch {epoch}/{total_epochs}")

# Number formatting
print(f"Loss: {loss:.4f} | Accuracy: {accuracy:.2%}")

# Alignment and padding — useful for consistent tabular output
print(f"{'Epoch':<8} {'Loss':>10} {'Accuracy':>10}")
print(f"{epoch:<8} {loss:>10.4f} {accuracy:>10.2%}")

# Expression inside f-string
print(f"Progress: {epoch / total_epochs:.0%} ({elapsed_seconds:.0f}s elapsed)")

# repr conversion — adds quotes, useful for debug output
label = "deepfake"
print(f"Label is {label!r}")   # Label is 'deepfake'


# ---------------------------------------------------------------------------
# Example 2 — String methods for parsing and cleaning
# Scenario: cleaning raw data coming from a CSV or user input
# ---------------------------------------------------------------------------

raw_entries = [
    "  ResNet-50  ",
    "EFFICIENTNET_B4",
    "  vit_base_patch16  \n",
    "mobilenet-v3",
]

# Normalize each entry: strip whitespace, lowercase, replace separators
cleaned = [entry.strip().lower().replace("_", "-") for entry in raw_entries]
print(cleaned)
# ['resnet-50', 'efficientnet-b4', 'vit-base-patch16', 'mobilenet-v3']

# Parsing a structured line from a log file
log_line = "2024-01-15 14:32:01 | WARNING | low_memory | free_mb=512"
parts = log_line.split(" | ")
timestamp, level, event, context = parts
print(f"Level: {level}, Event: {event}")

# Extracting a value from a key=value string
key, value = context.split("=")
print(f"Key: {key}, Value: {value}")


# ---------------------------------------------------------------------------
# Example 3 — Join for efficient string building
# Scenario: generating a CSV row and an HTML-style tag list
# ---------------------------------------------------------------------------

# WRONG way — O(n²) due to string immutability
# result = ""
# for field in fields:
#     result += field + ","  # creates a new string object every iteration

headers = ["filename", "label", "confidence", "width", "height"]
values = ["img_042.jpg", "fake", "0.94", "1280", "720"]

# RIGHT way — join is O(n), only one string object created
csv_header = ",".join(headers)
csv_row = ",".join(values)
print(csv_header)
print(csv_row)

# Building a multi-line report from parts
report_lines = [
    "=== Evaluation Summary ===",
    f"Model     : EfficientNet-B4",
    f"Dataset   : deepfake-detection-v2",
    f"Accuracy  : 94.20%",
    f"F1 Score  : 0.939",
    "=" * 26,
]
print("\n".join(report_lines))
