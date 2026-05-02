"""
exercises/01_batch_calculator.py
─────────────────────────────────
Topic    : Operators
Exercise : 1 of 3 — Easy
Concept  : Arithmetic operators, in-place ops, scientific notation

Context
-------
Before training, you always calculate batch statistics to confirm the
data loader is configured correctly. These numbers also appear in the
training summary printed at the start of every run.

─────────────────────────────────────────────────────────────────
Task
─────────────────────────────────────────────────────────────────
Using only the variables provided below, compute each result
and print a summary that looks EXACTLY like this:

  === Training Setup ===
  Dataset       : 50,000 samples
  Batch size    : 64
  Full batches  : 781
  Last batch    : 16 samples
  Steps/epoch   : 782
  Total steps   : 3,910
  Initial LR    : 2e-05

Rules:
  - Full batches   = floor division of dataset by batch size
  - Last batch     = remainder (samples that don't fill a full batch)
  - Steps/epoch    = full batches + (1 if last batch > 0 else 0)
  - Total steps    = steps per epoch * epochs
  - Use comma formatting (:,) for large numbers
  - Initial LR must print as scientific notation — store it as 2e-5
─────────────────────────────────────────────────────────────────
"""

dataset_size = 50_000
batch_size   = 64
epochs       = 5
initial_lr   = 2e-5

# ── Your solution ─────────────────────────────────────────────────────────────