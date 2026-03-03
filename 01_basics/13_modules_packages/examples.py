"""
Modules and Packages — Examples

Demonstrates import styles, the __name__ guard, aliasing,
and how to structure reusable utility modules.

Note: some examples reference hypothetical sibling files to illustrate
package structure — the concepts apply directly to real projects.
"""

import os
import sys
import math
from pathlib import Path
from datetime import datetime


# ---------------------------------------------------------------------------
# Example 1 — Import styles and aliases
# ---------------------------------------------------------------------------

# Full module import — access everything via the namespace
print(math.pi)
print(math.sqrt(144))

# Selective import — bring a specific name into scope
from math import floor, ceil
print(floor(3.7))   # 3
print(ceil(3.2))    # 4

# Aliasing — standard convention for common libraries
import os.path as osp
print(osp.exists("/tmp"))   # True on Linux/Mac


# ---------------------------------------------------------------------------
# Example 2 — The __name__ guard
# Scenario: a utility file that can run standalone OR be imported
# ---------------------------------------------------------------------------

def compute_iou(box_a: tuple, box_b: tuple) -> float:
    """
    Compute Intersection over Union for two bounding boxes.

    Args:
        box_a: (x1, y1, x2, y2) for box A.
        box_b: (x1, y1, x2, y2) for box B.

    Returns:
        IoU score between 0.0 and 1.0.
    """
    ax1, ay1, ax2, ay2 = box_a
    bx1, by1, bx2, by2 = box_b

    inter_x1 = max(ax1, bx1)
    inter_y1 = max(ay1, by1)
    inter_x2 = min(ax2, bx2)
    inter_y2 = min(ay2, by2)

    inter_area = max(0, inter_x2 - inter_x1) * max(0, inter_y2 - inter_y1)
    area_a = (ax2 - ax1) * (ay2 - ay1)
    area_b = (bx2 - bx1) * (by2 - by1)
    union_area = area_a + area_b - inter_area

    return inter_area / union_area if union_area > 0 else 0.0


# This block runs only when you execute this file directly
# If another file imports this module, the block is skipped
if __name__ == "__main__":
    box1 = (0, 0, 100, 100)
    box2 = (50, 50, 150, 150)
    iou = compute_iou(box1, box2)
    print(f"IoU: {iou:.3f}")   # 0.143


# ---------------------------------------------------------------------------
# Example 3 — Using os and pathlib for filesystem operations
# Scenario: locating dataset files relative to the script's location
# ---------------------------------------------------------------------------

# __file__ is the path of the current script
script_dir = Path(__file__).parent
print(f"Script dir: {script_dir}")

# Build paths without hardcoding separators
data_dir = script_dir / "data"
checkpoint_path = script_dir / "checkpoints" / "epoch_10.pt"

print(f"Data dir    : {data_dir}")
print(f"Checkpoint  : {checkpoint_path}")
print(f"Exists?     : {checkpoint_path.exists()}")

# List all Python files in the current directory
py_files = list(script_dir.glob("*.py"))
print(f"Python files: {[f.name for f in py_files]}")

# Environment variable with fallback
log_level = os.environ.get("LOG_LEVEL", "INFO")
print(f"Log level   : {log_level}")
