"""
solutions/02_pipeline_builder.py
─────────────────────────────────
Topic    : Functions
Solution : Exercise 2 — Pipeline builder

Open this only after a genuine attempt at the exercise.
"""


def log_step(step_name: str, *tags: str, **metrics) -> None:
    """
    Log a named pipeline step with optional tags and metrics.

    Args:
        step_name: Name of the pipeline step.
        *tags: Optional category tags for this step.
        **metrics: Optional key=value metrics to display.

    Returns:
        None.
    """
    parts = []
    for tag in tags:
        parts.append(f"tag: {tag}")
    for key, value in metrics.items():
        parts.append(f"{key}={value}")

    suffix = "  |  " + "  ".join(parts) if parts else ""
    print(f"[STEP] {step_name}{suffix}")


def evaluate_epoch(
    predictions: list[int],
    labels: list[int],
) -> tuple[float, float, float]:
    """
    Compute accuracy, error rate, and F1 score for one epoch.

    Args:
        predictions: Predicted class indices (0 or 1).
        labels: Ground-truth class indices (0 or 1).

    Returns:
        Tuple of (accuracy, error_rate, f1_score).
    """
    correct = sum(p == l for p, l in zip(predictions, labels))
    total = len(labels)
    acc = correct / total
    err = 1.0 - acc

    # F1 for the positive class (class 1)
    tp = sum(p == 1 and l == 1 for p, l in zip(predictions, labels))
    fp = sum(p == 1 and l == 0 for p, l in zip(predictions, labels))
    fn = sum(p == 0 and l == 1 for p, l in zip(predictions, labels))

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall    = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * precision * recall / (precision + recall) \
         if (precision + recall) > 0 else 0.0

    return acc, err, f1


# ── Test output ───────────────────────────────────────────────────────────────

log_step("data_loading")
log_step("preprocessing", "normalize", "augment")
log_step("training", "gpu", epoch=5, loss=0.0421, acc=0.934)
log_step("evaluation", epoch=10, f1=0.912)

print()

preds  = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1]
labels = [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]
acc, err, f1 = evaluate_epoch(preds, labels)
print(f"Accuracy   : {acc:.1%}")
print(f"Error rate : {err:.1%}")
print(f"F1 score   : {f1:.4f}")

# ── Why this works ────────────────────────────────────────────────────────────
#
# log_step — building parts then joining
#   Instead of building the string piece by piece with +=,
#   we collect parts into a list and join at the end.
#   This is more readable and handles zero-item cases cleanly.
#   "  |  ".join(parts) would also work — either approach is fine.
#
# *tags before **metrics in the signature
#   Python requires: regular params → *args → keyword-only → **kwargs.
#   You can't put **metrics before *tags — SyntaxError.
#
# evaluate_epoch — computing F1 properly
#   F1 requires tracking true positives, false positives, false negatives.
#   These are counts, not fractions — compute them first, then divide.
#   The guard (tp + fp) > 0 prevents ZeroDivisionError when there are
#   no positive predictions (a legitimate edge case in early training).
#
# Returning a tuple of three values
#   return acc, err, f1  is shorthand for  return (acc, err, f1).
#   The caller unpacks: acc, err, f1 = evaluate_epoch(...)
#   Order matters — match the return order in your variable names.
#
# Why separate functions?
#   log_step and evaluate_epoch do completely different jobs.
#   Keeping them separate means you can test each one independently,
#   reuse either in a different pipeline, and change one without touching the other.