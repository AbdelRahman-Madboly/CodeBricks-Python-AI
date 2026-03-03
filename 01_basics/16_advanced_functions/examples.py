"""
Advanced Functions — Examples

Covers first-class functions, closures, lambda, map/filter,
functools.partial, and higher-order function patterns.
"""

from functools import partial
from typing import Callable


# ---------------------------------------------------------------------------
# Example 1 — Functions as first-class objects
# Scenario: a pluggable metric system where the metric is passed as a function
# ---------------------------------------------------------------------------

def accuracy(predictions: list[int], labels: list[int]) -> float:
    """Fraction of predictions that match the true labels."""
    correct = sum(p == l for p, l in zip(predictions, labels))
    return correct / len(labels)


def false_positive_rate(predictions: list[int], labels: list[int]) -> float:
    """Fraction of negatives incorrectly classified as positive."""
    fp = sum(p == 1 and l == 0 for p, l in zip(predictions, labels))
    negatives = sum(l == 0 for l in labels)
    return fp / negatives if negatives else 0.0


def evaluate(
    predictions: list[int],
    labels: list[int],
    metrics: list[Callable],
) -> dict[str, float]:
    """
    Run a list of metric functions and return a results dict.

    Args:
        predictions: Model output labels.
        labels: Ground truth labels.
        metrics: List of metric functions (each takes preds, labels).

    Returns:
        Dict mapping metric function name to its value.
    """
    return {metric.__name__: metric(predictions, labels) for metric in metrics}


preds  = [1, 0, 1, 1, 0, 1, 0, 0]
labels = [1, 0, 0, 1, 0, 1, 1, 0]

results = evaluate(preds, labels, metrics=[accuracy, false_positive_rate])
for name, value in results.items():
    print(f"{name}: {value:.3f}")


# ---------------------------------------------------------------------------
# Example 2 — Closures and factory functions
# Scenario: creating configurable score filters without repeating code
# ---------------------------------------------------------------------------

def make_score_filter(threshold: float, label: str | None = None) -> Callable:
    """
    Create a filter function pre-configured with a threshold and optional label.

    Args:
        threshold: Minimum confidence score to pass the filter.
        label: If provided, also filter by this label.

    Returns:
        A function that takes a detection dict and returns True/False.
    """
    def filter_fn(detection: dict) -> bool:
        # Captures 'threshold' and 'label' from the enclosing scope
        passes_score = detection["confidence"] >= threshold
        passes_label = (label is None) or (detection["label"] == label)
        return passes_score and passes_label

    filter_fn.__name__ = f"filter_conf>={threshold}_label={label}"
    return filter_fn


detections = [
    {"label": "face", "confidence": 0.94},
    {"label": "face", "confidence": 0.71},
    {"label": "hand", "confidence": 0.88},
    {"label": "face", "confidence": 0.85},
]

high_confidence_faces = make_score_filter(threshold=0.80, label="face")
passed = list(filter(high_confidence_faces, detections))
print(f"\nHigh-confidence faces: {len(passed)}")


# ---------------------------------------------------------------------------
# Example 3 — functools.partial and lambda with map/filter
# Scenario: normalising a batch of scores with a pre-set range
# ---------------------------------------------------------------------------

def normalise(value: float, min_val: float, max_val: float) -> float:
    """Min-max normalise a value to [0, 1]."""
    return (value - min_val) / (max_val - min_val)


# partial fixes min_val and max_val, leaving value as the only free argument
normalise_0_to_1 = partial(normalise, min_val=0.0, max_val=1.0)
normalise_batch  = partial(normalise, min_val=0.5, max_val=1.0)

raw_scores = [0.60, 0.75, 0.88, 0.95, 0.50]

# map returns an iterator — wrap in list() to materialise
standard  = list(map(normalise_0_to_1, raw_scores))
rebased   = list(map(normalise_batch,  raw_scores))

print(f"\nStandard norm : {[round(s, 2) for s in standard]}")
print(f"Rebased norm  : {[round(s, 2) for s in rebased]}")

# lambda inline with sorted — sort by confidence descending
sorted_detections = sorted(detections, key=lambda d: d["confidence"], reverse=True)
print(f"\nTop detection: {sorted_detections[0]}")
