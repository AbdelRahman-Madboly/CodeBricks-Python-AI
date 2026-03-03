"""
File I/O — Exercises
"""

import json
import tempfile
from pathlib import Path


# ---------------------------------------------------------------------------
# Exercise 1 (Easy) — Write then read
#
# Problem:
#   Write a list of model names (one per line) to a temp file,
#   then read it back and print each name numbered from 1.
#
#   Expected output:
#   1. ResNet-50
#   2. EfficientNet-B4
#   3. MobileNet-V3
#   4. ViT-Base
#
model_names = ["ResNet-50", "EfficientNet-B4", "MobileNet-V3", "ViT-Base"]
#
# Your solution below:
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Exercise 2 (Medium) — Parse and filter a log file
#
# Problem:
#   Write a function parse_training_log() that:
#     - Reads a log file where each line is: "epoch=N loss=F accuracy=F"
#     - Returns a list of dicts with keys: epoch (int), loss (float), accuracy (float)
#     - Skips blank lines and lines that start with "#"
#
#   Then use it to find and print:
#     - The epoch with the lowest loss
#     - All epochs where accuracy > threshold
#
#   Expected output:
#   Best epoch: 5 (loss=0.291)
#   Above 85% accuracy: [3, 4, 5]
#
log_content = """# Training run: 2024-01-15
epoch=1 loss=0.921 accuracy=0.610
epoch=2 loss=0.734 accuracy=0.720

epoch=3 loss=0.512 accuracy=0.830
epoch=4 loss=0.388 accuracy=0.890
epoch=5 loss=0.291 accuracy=0.920
"""
#
# Your solution below:
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Exercise 3 (Hard) — JSON config with validation and merge
#
# Problem:
#   Write a function load_and_merge_configs() that:
#     - Takes a list of JSON file paths
#     - Loads each JSON file
#     - Merges them left to right (later files overwrite earlier keys)
#     - Validates that the final merged config contains all required keys
#     - Returns the merged dict, or raises ValueError listing missing keys
#
#   Expected output:
#   Merged config: {'model': 'ViT-Base', 'epochs': 100, 'lr': 0.0005, 'device': 'cuda'}
#   Missing keys test passed.
#
required_keys = {"model", "epochs", "lr", "device"}
#
# Your solution below:
# ---------------------------------------------------------------------------

def load_and_merge_configs(file_paths: list[str], required: set[str]) -> dict:
    """
    Load and merge multiple JSON config files.

    Args:
        file_paths: Ordered list of JSON file paths (later files win).
        required: Set of keys that must be present in the final config.

    Returns:
        Merged configuration dict.

    Raises:
        ValueError: If any required keys are missing after merging.
    """
    # TODO: implement
    pass


# Test setup — creates two temp JSON files
def run_test():
    base_config = {"model": "ResNet-50", "epochs": 50, "lr": 0.001}
    override_config = {"model": "ViT-Base", "epochs": 100, "lr": 0.0005, "device": "cuda"}

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json",
                                     delete=False, encoding="utf-8") as f1:
        json.dump(base_config, f1)
        path1 = f1.name

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json",
                                     delete=False, encoding="utf-8") as f2:
        json.dump(override_config, f2)
        path2 = f2.name

    merged = load_and_merge_configs([path1, path2], required_keys)
    print(f"Merged config: {merged}")

    # Test that missing keys raises ValueError
    incomplete = {"model": "ResNet"}
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json",
                                      delete=False, encoding="utf-8") as f3:
        json.dump(incomplete, f3)
        path3 = f3.name

    try:
        load_and_merge_configs([path3], required_keys)
        print("ERROR: should have raised ValueError")
    except ValueError as e:
        print(f"Missing keys test passed. Error: {e}")


run_test()
