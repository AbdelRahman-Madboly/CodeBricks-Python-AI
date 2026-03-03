"""
File I/O — Examples

Covers reading and writing text files, CSV parsing without external libs,
JSON handling, and memory-efficient line-by-line processing.
"""

import json
import tempfile
from pathlib import Path


# All examples use temporary files so they run cleanly anywhere

# ---------------------------------------------------------------------------
# Example 1 — Writing and reading text files
# Scenario: saving and loading a training log
# ---------------------------------------------------------------------------

log_entries = [
    "epoch=01 loss=0.9210 accuracy=0.6100",
    "epoch=02 loss=0.7340 accuracy=0.7200",
    "epoch=03 loss=0.5120 accuracy=0.8300",
    "epoch=04 loss=0.3880 accuracy=0.8900",
    "epoch=05 loss=0.2910 accuracy=0.9200",
]

with tempfile.NamedTemporaryFile(mode="w", suffix=".log",
                                  delete=False, encoding="utf-8") as log_file:
    log_path = log_file.name
    for entry in log_entries:
        log_file.write(entry + "\n")   # write() does not add newlines

print(f"Wrote log to: {log_path}")

# Read back line by line — memory efficient for large files
print("\nTraining log:")
with open(log_path, encoding="utf-8") as f:
    for line in f:
        print(" ", line.rstrip())   # rstrip removes the trailing \n


# ---------------------------------------------------------------------------
# Example 2 — CSV parsing without the csv module
# Scenario: loading detection results from a simple CSV export
# ---------------------------------------------------------------------------

csv_content = """filename,label,confidence,width,height
img_001.jpg,real,0.94,1280,720
img_002.jpg,fake,0.88,1920,1080
img_003.jpg,uncertain,0.61,640,480
"""

with tempfile.NamedTemporaryFile(mode="w", suffix=".csv",
                                  delete=False, encoding="utf-8") as csv_file:
    csv_path = csv_file.name
    csv_file.write(csv_content)

records = []
with open(csv_path, encoding="utf-8") as f:
    header = f.readline().strip().split(",")   # first line is the header
    for line in f:
        if not line.strip():
            continue   # skip blank lines
        values = line.strip().split(",")
        record = dict(zip(header, values))
        record["confidence"] = float(record["confidence"])
        record["width"] = int(record["width"])
        record["height"] = int(record["height"])
        records.append(record)

print(f"\nLoaded {len(records)} records:")
for rec in records:
    print(f"  {rec['filename']:<16} {rec['label']:<12} conf={rec['confidence']:.2f}")


# ---------------------------------------------------------------------------
# Example 3 — JSON for structured config files
# Scenario: saving and loading a model configuration
# ---------------------------------------------------------------------------

model_config = {
    "model_name": "EfficientNet-B4",
    "input_size": [224, 224],
    "num_classes": 2,
    "class_names": ["real", "fake"],
    "training": {
        "epochs": 50,
        "learning_rate": 0.001,
        "batch_size": 32,
    },
}

with tempfile.NamedTemporaryFile(mode="w", suffix=".json",
                                  delete=False, encoding="utf-8") as json_file:
    json_path = json_file.name
    json.dump(model_config, json_file, indent=2)

print(f"\nSaved config to: {json_path}")

with open(json_path, encoding="utf-8") as f:
    loaded_config = json.load(f)

print(f"Model         : {loaded_config['model_name']}")
print(f"Learning rate : {loaded_config['training']['learning_rate']}")
print(f"Classes       : {loaded_config['class_names']}")
