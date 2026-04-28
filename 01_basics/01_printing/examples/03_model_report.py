"""
examples/03_model_report.py
───────────────────────────
Topic  : Printing
Example: 3 of 3 — Model evaluation report

Context
-------
After training a classifier, you compare how different models
performed on a test dataset. The results need to be presented
as a clean, aligned table — not a mess of floating-point numbers.

This is the exact output pattern you'll write in Phase 7 when
you evaluate scikit-learn and PyTorch models.

This example covers:
  - f-string column alignment (:<  :>  :.xf)
  - Printing table headers and separators
  - Looping through structured data to build rows
  - Computing totals and summary lines

Run this file and predict the output before you see it.
"""

# ── Evaluation results ───────────────────────────────────────────────────────
# (model_name, accuracy, f1_score, inference_time_ms)

results = [
    ("Logistic Regression", 0.8712, 0.8650, 12.4),
    ("Random Forest",       0.9134, 0.9101, 87.2),
    ("BERT-base (frozen)",  0.9441, 0.9438, 342.1),
    ("DistilBERT",          0.9389, 0.9371, 198.7),
    ("GPT-2 (fine-tuned)",  0.9502, 0.9498, 891.3),
]

# ── Print the report ─────────────────────────────────────────────────────────

title = "Text Classification — Evaluation Report"
print()
print(f"  {title}")
print("  " + "─" * len(title))
print()

# Header row
# :<22  left-aligns in 22 characters
# :>10  right-aligns in 10 characters
print(f"  {'Model':<22} {'Accuracy':>10} {'F1 Score':>10} {'Time (ms)':>10}")
print("  " + "─" * 56)

# Data rows
for model_name, accuracy, f1, time_ms in results:
    # :.4f  — 4 decimal places for accuracy/f1
    # :.1f  — 1 decimal place for time
    print(f"  {model_name:<22} {accuracy:>10.4f} {f1:>10.4f} {time_ms:>10.1f}")

print("  " + "─" * 56)

# Best model summary
best = max(results, key=lambda r: r[1])   # highest accuracy
print(f"\n  Best model : {best[0]}")
print(f"  Accuracy   : {best[1]:.2%}")    # .2% formats as percentage
print(f"  F1 Score   : {best[2]:.4f}")
print()

# ── What to notice ───────────────────────────────────────────────────────────
#
# 1. Column alignment
#    :<22  means: left-align in a field 22 characters wide
#    :>10  means: right-align in a field 10 characters wide
#    Numbers should be right-aligned so their decimal points line up.
#    Text labels should be left-aligned.
#
# 2. :.4f and :.2%
#    :.4f  → 4 decimal places  (0.9441)
#    :.2%  → multiply by 100, show 2 decimal places, add %  (94.41%)
#    Same value, different format — choose what reads better in context.
#
# 3. len(title) for the separator
#    Instead of hardcoding a number, len() measures the string.
#    Change the title and the separator adjusts automatically.
#
# 4. max(..., key=lambda r: r[1])
#    This finds the row with the highest accuracy.
#    lambda is an anonymous function — you'll learn it in topic 16.
#    For now, read it as: "find the result where position [1] is largest".
#
# 5. Why does this matter?
#    This exact output pattern — header, aligned rows, summary — is what
#    you'll write every time you run model comparisons in Phase 7.
#    Learn the formatting here so it's automatic by then.