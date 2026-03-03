"""
Advanced Functions — Solutions
"""

from typing import Callable


# ---------------------------------------------------------------------------
# Solution 1
# ---------------------------------------------------------------------------

scores = [0.72, 0.95, 0.61, 0.88, 0.43, 0.91]

percentages = list(map(lambda s: round(s * 100, 1), scores))
above_80    = list(filter(lambda s: s > 0.80, scores))

print(f"Percentages : {percentages}")
print(f"Above 0.80  : {above_80}")


# ---------------------------------------------------------------------------
# Solution 2
# ---------------------------------------------------------------------------

valid_labels = ["real", "fake", "uncertain"]
sample_records = [
    {"label": "real"},  {"label": "fake"},   {"label": "real"},
    {"label": "fake"},  {"label": "uncertain"},{"label": "fake"},
    {"label": "real"},  {"label": "fake"},
]


def make_label_counter(allowed_labels: list[str]) -> Callable:
    """
    Create a label counting function pre-configured with valid labels.

    Args:
        allowed_labels: Labels the counter will accept.

    Returns:
        A function that counts label occurrences in a list of records.
    """
    valid_set = set(allowed_labels)   # captured by the closure

    def count_labels(records: list[dict]) -> dict[str, int]:
        counts: dict[str, int] = {label: 0 for label in allowed_labels}
        for record in records:
            label = record["label"]
            if label not in valid_set:
                raise ValueError(f"Unknown label: {label!r}")
            counts[label] += 1
        return counts

    return count_labels


count_labels = make_label_counter(valid_labels)
print(count_labels(sample_records))


# ---------------------------------------------------------------------------
# Solution 3
# ---------------------------------------------------------------------------

raw_values = [-0.10, 0.94, 1.20, 0.753]


def compose_pipeline(*steps: Callable) -> Callable:
    """
    Compose multiple single-argument functions into one left-to-right pipeline.
    """
    def pipeline(value):
        result = value
        for step in steps:
            result = step(result)
        return result
    return pipeline


def clip_score(score: float) -> float:
    """Clip a score to the range [0.0, 1.0]."""
    return max(0.0, min(1.0, score))


def round_score(score: float) -> float:
    """Round a score to 2 decimal places."""
    return round(score, 2)


def to_percentage_str(score: float) -> str:
    """Convert a 0-1 float to a percentage string like '94.00%'."""
    return f"{score * 100:.2f}%"


process_score = compose_pipeline(clip_score, round_score, to_percentage_str)
results = [f"{v} → {process_score(v)}" for v in raw_values]
print(results)
