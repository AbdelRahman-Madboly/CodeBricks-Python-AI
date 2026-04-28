"""
exercises/02_dataset_table.py
──────────────────────────────
Topic    : Printing
Exercise : 2 of 3 — Medium
Concept  : Column alignment, loops, formatted numbers

Context
-------
Before training any model, you summarize the dataset so you
(and anyone reading your logs) can confirm the data loaded
correctly and the class distribution looks reasonable.

This kind of summary is the first thing printed in every
serious training script.

─────────────────────────────────────────────────────────────────
Task
─────────────────────────────────────────────────────────────────
Print the dataset summary below as a formatted table that looks
EXACTLY like this:

  ══════════════════════════════════════════
    Dataset Summary — Sentiment Analysis
  ══════════════════════════════════════════
    Split        Samples    % of Total
    ──────────────────────────────────
    Train         12,000        70.0%
    Validation     2,571        15.0%
    Test           2,572        15.0%
    ──────────────────────────────────
    Total         17,143       100.0%
  ══════════════════════════════════════════

Rules:
  - Use the data dict below — don't hardcode totals or percentages
  - Calculate total and percentages with code
  - Split name: left-aligned, 12 chars wide
  - Samples: right-aligned, 9 chars wide, with comma formatting
  - Percentage: right-aligned, 12 chars wide, 1 decimal place, with %
  - The ══ and ── lines must be exactly 42 characters wide
─────────────────────────────────────────────────────────────────
"""

dataset_name = "Sentiment Analysis"

splits = {
    "Train":      12_000,
    "Validation":  2_571,
    "Test":        2_572,
}

# ── Your solution below ──────────────────────────────────────────────────────