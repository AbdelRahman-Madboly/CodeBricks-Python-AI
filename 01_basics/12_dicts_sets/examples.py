"""
Dictionaries and Sets — Examples

Covers dict creation, safe access, comprehensions, nested dicts,
set operations, and frequency counting patterns.
"""


# ---------------------------------------------------------------------------
# Example 1 — Dict fundamentals and safe access
# Scenario: managing model hyperparameter configs
# ---------------------------------------------------------------------------

config = {
    "model": "EfficientNet-B4",
    "epochs": 50,
    "learning_rate": 0.001,
    "optimizer": "Adam",
}

# Access — raises KeyError if missing
print(config["model"])

# Safe access — returns None (or a default) if key is absent
batch_size = config.get("batch_size")          # None
dropout = config.get("dropout", 0.5)           # 0.5 — explicit default
print(f"batch_size: {batch_size}, dropout: {dropout}")

# Iterating
for key, value in config.items():
    print(f"  {key}: {value}")

# Adding and updating
config["batch_size"] = 32
config["epochs"] = 100       # overwrite existing key
print(f"\nUpdated epochs: {config['epochs']}")

# Removing
removed = config.pop("optimizer", None)   # safe pop — no error if missing
print(f"Removed: {removed}")


# ---------------------------------------------------------------------------
# Example 2 — Frequency counting and dict comprehensions
# Scenario: counting label distribution in a dataset
# ---------------------------------------------------------------------------

raw_labels = ["real", "fake", "fake", "real", "uncertain", "fake", "real", "fake"]

# Manual frequency count — shows the pattern behind Counter
label_counts: dict[str, int] = {}
for label in raw_labels:
    label_counts[label] = label_counts.get(label, 0) + 1

print("\nLabel distribution:")
for label, count in sorted(label_counts.items(), key=lambda x: x[1], reverse=True):
    pct = count / len(raw_labels) * 100
    print(f"  {label:<12} {count:>3}  ({pct:.0f}%)")

# Dict comprehension — normalise scores to percentages
raw_scores = {"accuracy": 0.941, "precision": 0.928, "recall": 0.955, "f1": 0.941}
pct_scores = {metric: f"{val:.1%}" for metric, val in raw_scores.items()}
print(f"\nFormatted scores: {pct_scores}")


# ---------------------------------------------------------------------------
# Example 3 — Set operations
# Scenario: comparing which classes appear in train vs validation splits
# ---------------------------------------------------------------------------

train_labels = {"real", "fake", "uncertain", "blurry"}
val_labels   = {"real", "fake", "compressed"}

# What labels appear in both splits?
shared = train_labels & val_labels
print(f"\nShared labels      : {shared}")

# What labels are in train but not val? (coverage gap)
train_only = train_labels - val_labels
print(f"Train only         : {train_only}")

# All unique labels across both
all_labels = train_labels | val_labels
print(f"All labels         : {all_labels}")

# Labels in exactly one split (not both)
exclusive = train_labels ^ val_labels
print(f"Exclusive to one   : {exclusive}")

# Fast deduplication of a list while preserving order
seen: set[str] = set()
ordered_unique = []
for label in ["fake", "real", "fake", "uncertain", "real"]:
    if label not in seen:
        seen.add(label)
        ordered_unique.append(label)

print(f"\nDeduped (ordered)  : {ordered_unique}")
