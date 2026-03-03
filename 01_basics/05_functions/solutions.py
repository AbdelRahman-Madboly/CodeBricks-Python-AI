"""
Functions — Solutions
"""


# ---------------------------------------------------------------------------
# Solution 1
# ---------------------------------------------------------------------------

def clamp(value: float, min_val: float = 0.0, max_val: float = 1.0) -> float:
    """
    Restrict a value to the range [min_val, max_val].

    Args:
        value: The number to clamp.
        min_val: Lower bound (default 0.0).
        max_val: Upper bound (default 1.0).

    Returns:
        value if within range, otherwise the nearest bound.
    """
    if value < min_val:
        return min_val
    if value > max_val:
        return max_val
    return value


print(clamp(-0.5))   # 0.0
print(clamp(0.75))   # 0.75
print(clamp(1.8))    # 1.0


# ---------------------------------------------------------------------------
# Solution 2
# ---------------------------------------------------------------------------

def build_report(title: str, *metric_names: str, **metric_values) -> str:
    """
    Build a formatted metrics report string.

    Args:
        title: Report heading.
        *metric_names: Names of metrics being tracked.
        **metric_values: Metric name → value pairs.

    Returns:
        Formatted multi-line report string.
    """
    lines = [
        f"=== {title} ===",
        f"Metrics tracked: {', '.join(metric_names)}",
    ]
    for key, value in metric_values.items():
        lines.append(f"{key:<8} : {value}")
    return "\n".join(lines)


report = build_report(
    "Training Report", "accuracy", "loss", "f1",
    accuracy=0.94, loss=0.042, f1=0.91
)
print(report)


# ---------------------------------------------------------------------------
# Solution 3
# ---------------------------------------------------------------------------

# Part A
def merge_configs(configs: list[dict]) -> dict:
    """
    Merge a list of config dicts into one. Later entries overwrite earlier ones.
    Input dicts are never modified.

    Args:
        configs: List of configuration dictionaries.

    Returns:
        A new merged dictionary.
    """
    result = {}
    for config in configs:
        result.update(config)   # update() copies into result, never touches config
    return result


configs = [
    {"model": "VGG", "epochs": 10},
    {"model": "ResNet", "lr": 0.001},
    {"epochs": 20, "device": "cuda"},
]
print(merge_configs(configs))

# Part B
# x inside modify() is a NEW local variable — it shadows the outer x.
# Assigning inside a function creates a local binding unless 'global' is declared.
# The outer x stays 10.

x = 10

def modify():
    x = 99
    print(f"inside: {x}")    # inside: 99

modify()
print(f"outside: {x}")       # outside: 10  ← outer x unchanged
