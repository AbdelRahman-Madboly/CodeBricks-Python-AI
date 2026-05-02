"""
exercises/02_qc_filter.py
──────────────────────────
Topic    : Operators
Exercise : 2 of 3 — Medium
Concept  : Logical operators, comparison, chaining, short-circuit defaults

Context
-------
Before any frame enters a training pipeline, it goes through quality control.
Frames that don't meet the standards get logged and discarded — bad training
data produces bad models.

─────────────────────────────────────────────────────────────────
Task A — Frame QC check
─────────────────────────────────────────────────────────────────
Write a function that returns True if ALL of these conditions hold:
  - resolution height is at least 720
  - confidence score is strictly above 0.85
  - frame is NOT blurry
  - codec is "h264" OR "h265"

Signature:
  def passes_qc(height: int, confidence: float,
                is_blurry: bool, codec: str) -> bool

─────────────────────────────────────────────────────────────────
Task B — First failure reason
─────────────────────────────────────────────────────────────────
Write a function that returns a string describing the FIRST reason
a frame fails QC, checked in this order:
  1. "low resolution"   if height < 720
  2. "low confidence"   if confidence <= 0.85
  3. "blurry"           if is_blurry
  4. "bad codec"        if codec not in ("h264", "h265")
  5. "ok"               if all checks pass

Signature:
  def qc_reason(height: int, confidence: float,
                is_blurry: bool, codec: str) -> str

─────────────────────────────────────────────────────────────────
Task C — Short-circuit config defaults (no if-statements allowed)
─────────────────────────────────────────────────────────────────
Use the 'or' operator to resolve each raw value to its default
if the raw value is falsy. Assign results to: model, epochs, device, tag

Expected output:
  model  : resnet-50
  epochs : 30
  device : cuda
  tag    : experiment-1
─────────────────────────────────────────────────────────────────
"""

# ── Task A & B — your functions ───────────────────────────────────────────────


# ── Task C — raw config values (do not change) ───────────────────────────────

raw_model  = ""
raw_epochs = 0
raw_device = None
raw_tag    = "experiment-1"   # this one is already set

default_model  = "resnet-50"
default_epochs = 30
default_device = "cuda"
default_tag    = "untagged"

# Your solution — no if-statements:


# ── Test calls (uncomment after writing your functions) ───────────────────────

# Task A
# print(passes_qc(1080, 0.92, False, "h264"))  # True
# print(passes_qc(480,  0.92, False, "h264"))  # False — low res
# print(passes_qc(1080, 0.80, False, "h264"))  # False — low confidence
# print(passes_qc(1080, 0.92, True,  "h264"))  # False — blurry
# print(passes_qc(1080, 0.92, False, "xvid"))  # False — bad codec

# Task B
# print(qc_reason(480,  0.80, True,  "xvid"))  # low resolution  (checked first)
# print(qc_reason(1080, 0.80, True,  "xvid"))  # low confidence
# print(qc_reason(1080, 0.92, True,  "xvid"))  # blurry
# print(qc_reason(1080, 0.92, False, "xvid"))  # bad codec
# print(qc_reason(1080, 0.92, False, "h265"))  # ok