"""
Operators — Exercises
"""


# ---------------------------------------------------------------------------
# Exercise 1 (Easy) — Arithmetic on dataset stats
#
# Problem:
#   Given the values below, compute and print each result.
#
#   Expected output:
#   Total pixels  : 921600
#   Full batches  : 281
#   Leftover      : 19
#   MB per sample : 0.9
#
# Variables provided:
width = 1280
height = 720
channels = 1
dataset_size = 9000
batch_size = 32
bytes_per_pixel = 1
mb = 1_048_576
#
# Your solution below:
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Exercise 2 (Medium) — Logical filtering
#
# Problem:
#   A video frame passes quality control only if ALL of the following are true:
#     - resolution is at least 720p (height >= 720)
#     - confidence score is above 0.85
#     - frame is not blurry
#     - codec is either "h264" or "h265"
#
#   Print whether the frame passes QC and a reason if it fails.
#
#   Expected output for the values below:
#   QC passed: False
#   Reason: low confidence
#
# Frame data — do not change:
frame_height = 1080
frame_confidence = 0.80
is_blurry = False
frame_codec = "h264"
#
# Your solution below:
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Exercise 3 (Hard) — Short-circuit defaults
#
# Problem:
#   Without using if-statements, use short-circuit operators to resolve
#   each value to a safe default if the raw value is falsy.
#   Then print the resolved configuration block.
#
#   Expected output:
#   model     : ResNet-50
#   epochs    : 20
#   device    : cpu
#   tag       : untagged
#
# Raw config (simulate missing/empty config values):
raw_model = ""
raw_epochs = 0
raw_device = None
raw_tag = "untagged"
#
# Defaults:
default_model = "ResNet-50"
default_epochs = 20
default_device = "cpu"
default_tag = "untagged"
#
# Your solution (no if-statements allowed):
# ---------------------------------------------------------------------------
