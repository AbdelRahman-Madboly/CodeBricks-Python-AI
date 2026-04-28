"""
exercises/02_pipeline_builder.py
─────────────────────────────────
Topic    : Functions
Exercise : 2 of 3 — Medium
Concept  : *args, **kwargs, multiple return values, composing functions

Context
-------
You're building a configurable training pipeline. The pipeline needs a
flexible logger (unknown number of messages + metadata) and an evaluation
function that returns multiple metrics at once.

─────────────────────────────────────────────────────────────────
Task A — log_step()
─────────────────────────────────────────────────────────────────
Write a function that logs a pipeline step with optional metadata.

Signature:
  def log_step(step_name: str, *tags: str, **metrics) -> None

Expected output for the test calls below:
  [STEP] data_loading
  [STEP] preprocessing  |  tag: normalize  tag: augment
  [STEP] training  |  tag: gpu  epoch=5  loss=0.0421  acc=0.934
  [STEP] evaluation  |  epoch=10  f1=0.912

Rules:
  - step_name is always printed
  - tags (from *tags) are printed as "tag: <value>" each, if any exist
  - metrics (from **metrics) are printed as "key=value" each, if any exist
  - tags and metrics are separated from step_name by "  |  "
  - All tags come before all metrics in the output
  - Returns None

─────────────────────────────────────────────────────────────────
Task B — evaluate_epoch()
─────────────────────────────────────────────────────────────────
Write a function that computes three metrics from predictions and labels,
returning all three values at once.

Signature:
  def evaluate_epoch(
      predictions: list[int],
      labels: list[int],
  ) -> tuple[float, float, float]:

Returns (in this order):
  1. accuracy  — fraction of correct predictions
  2. error_rate — 1.0 - accuracy
  3. f1_score  — simplified: 2 * (precision * recall) / (precision + recall)
     where:
       precision = true_positives / (true_positives + false_positives)
       recall    = true_positives / (true_positives + false_negatives)
     For this exercise, treat class 1 as the positive class.
     If precision + recall is 0, return f1 = 0.0.

Expected output for the test call below:
  Accuracy   : 70.0%
  Error rate : 30.0%
  F1 score   : 0.7273
─────────────────────────────────────────────────────────────────
"""

# ── Your functions here ───────────────────────────────────────────────────────


# ── Test calls — do not change these ─────────────────────────────────────────

# Task A
# log_step("data_loading")
# log_step("preprocessing", "normalize", "augment")
# log_step("training", "gpu", epoch=5, loss=0.0421, acc=0.934)
# log_step("evaluation", epoch=10, f1=0.912)

# Task B
# preds  = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1]
# labels = [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]
# acc, err, f1 = evaluate_epoch(preds, labels)
# print(f"Accuracy   : {acc:.1%}")
# print(f"Error rate : {err:.1%}")
# print(f"F1 score   : {f1:.4f}")