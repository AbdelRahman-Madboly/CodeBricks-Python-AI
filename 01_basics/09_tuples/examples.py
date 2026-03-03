"""
Tuples — Examples

Covers tuple creation, unpacking, extended unpacking, using tuples
as dict keys, and returning multiple values from functions.
"""


# ---------------------------------------------------------------------------
# Example 1 — Tuple basics and unpacking
# Scenario: representing image dimensions and bounding box coordinates
# ---------------------------------------------------------------------------

# Fixed structure — dimensions never change for a given image spec
image_size = (1920, 1080)
width, height = image_size   # unpacking — clean and readable
print(f"Width: {width}, Height: {height}")

# Bounding box: (x, y, w, h) — tuple communicates "these belong together"
bbox = (120, 45, 200, 160)
x, y, box_w, box_h = bbox
print(f"Box at ({x},{y}) size {box_w}x{box_h}")

# Extended unpacking — grab the first, ignore the rest
first_stage, *remaining_stages = ("load", "preprocess", "infer", "save")
print(f"First: {first_stage}")
print(f"Rest : {remaining_stages}")   # list, not tuple


# ---------------------------------------------------------------------------
# Example 2 — Returning multiple values from a function
# Scenario: a function that computes both mean and standard deviation
# ---------------------------------------------------------------------------

def compute_stats(scores: list[float]) -> tuple[float, float]:
    """
    Compute mean and standard deviation of a list of scores.

    Args:
        scores: List of float values.

    Returns:
        A tuple of (mean, std_dev).
    """
    mean = sum(scores) / len(scores)
    variance = sum((s - mean) ** 2 for s in scores) / len(scores)
    std_dev = variance ** 0.5
    return mean, std_dev   # Python packs this as a tuple automatically


confidence_scores = [0.92, 0.75, 0.88, 0.61, 0.95, 0.70]

mean, std = compute_stats(confidence_scores)
print(f"\nMean : {mean:.3f}")
print(f"Std  : {std:.3f}")

# You can also keep it as a tuple and access by index
stats = compute_stats(confidence_scores)
print(f"Compact: mean={stats[0]:.3f}, std={stats[1]:.3f}")


# ---------------------------------------------------------------------------
# Example 3 — Tuples as dictionary keys
# Scenario: caching results indexed by (model, dataset) pairs
# ---------------------------------------------------------------------------

# Lists cannot be dict keys — they are mutable and therefore not hashable
# Tuples are hashable — perfect for composite keys

evaluation_cache: dict[tuple[str, str], float] = {}

# Simulate caching evaluation results
results = [
    ("ResNet-50", "deepfake-v1", 0.91),
    ("EfficientNet", "deepfake-v1", 0.94),
    ("ResNet-50", "deepfake-v2", 0.88),
]

for model, dataset, accuracy in results:
    key = (model, dataset)   # tuple as dict key
    evaluation_cache[key] = accuracy

# Lookup
query = ("EfficientNet", "deepfake-v1")
print(f"\nCached accuracy for {query}: {evaluation_cache[query]:.2%}")

# Iterate over all cached results
print("\nAll cached evaluations:")
for (model, dataset), acc in evaluation_cache.items():
    print(f"  {model:<15} on {dataset:<14} → {acc:.2%}")
