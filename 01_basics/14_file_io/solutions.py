"""
File I/O — Solutions
"""

import json
import tempfile
from pathlib import Path


# ---------------------------------------------------------------------------
# Solution 1
# ---------------------------------------------------------------------------

model_names = ["ResNet-50", "EfficientNet-B4", "MobileNet-V3", "ViT-Base"]

with tempfile.NamedTemporaryFile(mode="w", suffix=".txt",
                                  delete=False, encoding="utf-8") as f:
    tmp_path = f.name
    for name in model_names:
        f.write(name + "\n")

with open(tmp_path, encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}. {line.rstrip()}")


# ---------------------------------------------------------------------------
# Solution 2
# ---------------------------------------------------------------------------

log_content = """# Training run: 2024-01-15
epoch=1 loss=0.921 accuracy=0.610
epoch=2 loss=0.734 accuracy=0.720

epoch=3 loss=0.512 accuracy=0.830
epoch=4 loss=0.388 accuracy=0.890
epoch=5 loss=0.291 accuracy=0.920
"""


def parse_training_log(file_path: str) -> list[dict]:
    """
    Parse a training log file into a list of epoch records.

    Args:
        file_path: Path to the log file.

    Returns:
        List of dicts with epoch, loss, and accuracy keys.
    """
    entries = []
    with open(file_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = dict(pair.split("=") for pair in line.split())
            entries.append({
                "epoch":    int(parts["epoch"]),
                "loss":     float(parts["loss"]),
                "accuracy": float(parts["accuracy"]),
            })
    return entries


with tempfile.NamedTemporaryFile(mode="w", suffix=".log",
                                  delete=False, encoding="utf-8") as lf:
    lf.write(log_content)
    log_path = lf.name

epochs = parse_training_log(log_path)

best = min(epochs, key=lambda e: e["loss"])
print(f"Best epoch: {best['epoch']} (loss={best['loss']})")

threshold = 0.85
above = [e["epoch"] for e in epochs if e["accuracy"] > threshold]
print(f"Above 85% accuracy: {above}")


# ---------------------------------------------------------------------------
# Solution 3
# ---------------------------------------------------------------------------

required_keys = {"model", "epochs", "lr", "device"}


def load_and_merge_configs(file_paths: list[str], required: set[str]) -> dict:
    """
    Load and merge multiple JSON config files.
    Later files overwrite earlier keys.
    Raises ValueError if required keys are missing after merging.
    """
    merged: dict = {}

    for path in file_paths:
        with open(path, encoding="utf-8") as f:
            config = json.load(f)
        merged.update(config)

    missing = required - set(merged.keys())
    if missing:
        raise ValueError(f"Missing required config keys: {missing}")

    return merged


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

    incomplete = {"model": "ResNet"}
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json",
                                      delete=False, encoding="utf-8") as f3:
        json.dump(incomplete, f3)
        path3 = f3.name

    try:
        load_and_merge_configs([path3], required_keys)
    except ValueError as e:
        print(f"Missing keys test passed. Error: {e}")


run_test()
