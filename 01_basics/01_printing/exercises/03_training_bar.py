"""
exercises/03_training_bar.py
─────────────────────────────
Topic    : Printing
Exercise : 3 of 3 — Hard
Concept  : end=, sep=, loop control, conditional formatting

Context
-------
During model training, you want to print each epoch's metrics
on a single line as training progresses — not a wall of text,
not separate lines per metric.

The format should look like a timeline: each epoch's result
flows into the next, separated by arrows, so you can scan
the trend at a glance.

─────────────────────────────────────────────────────────────────
Task
─────────────────────────────────────────────────────────────────
Using the training log below, print all epochs on ONE LINE
that looks EXACTLY like this:

  Training: E1(loss=0.8821,acc=61.2%) → E2(loss=0.6134,acc=74.5%) → E3(loss=0.4502,acc=81.3%) → E4(loss=0.3211,acc=86.7%) → E5(loss=0.2498,acc=90.1%) ✓ done

Rules:
  - Use a loop — no copy-pasting print calls per epoch
  - Each epoch block: E{n}(loss={:.4f},acc={:.1f}%)
  - Epochs are separated by " → " — no trailing arrow after the last one
  - After the last epoch print " ✓ done" on the same line, then a newline
  - Do NOT build one big string and print it at the end
    (use end= to control line behaviour per print call)
─────────────────────────────────────────────────────────────────
"""

training_log = [
    (1, 0.8821, 0.6123),   # (epoch, loss, accuracy)
    (2, 0.6134, 0.7452),
    (3, 0.4502, 0.8134),
    (4, 0.3211, 0.8671),
    (5, 0.2498, 0.9012),
]

# ── Your solution below ──────────────────────────────────────────────────────