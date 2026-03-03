"""
Operators — Examples

Covers arithmetic, relational, logical, membership, and identity operators
with practical scenarios from data processing and system scripting.
"""


# ---------------------------------------------------------------------------
# Example 1 — Arithmetic operators
# Scenario: computing training statistics from raw numbers
# ---------------------------------------------------------------------------

total_samples = 10_000
batch_size = 32

# How many full batches fit in the dataset?
full_batches = total_samples // batch_size      # floor division → int
leftover_samples = total_samples % batch_size   # remainder

print(f"Full batches   : {full_batches}")        # 312
print(f"Leftover       : {leftover_samples}")    # 16

# / always returns float even when the result is whole
ratio = total_samples / batch_size
print(f"Exact ratio    : {ratio}")               # 312.5

# Exponentiation
learning_rate = 1e-3    # scientific notation = 0.001
decayed_rate = learning_rate ** 2
print(f"Decayed rate   : {decayed_rate}")        # 1e-06


# ---------------------------------------------------------------------------
# Example 2 — Relational and logical operators
# Scenario: filtering a sample based on quality thresholds
# ---------------------------------------------------------------------------

confidence_score = 0.91
resolution_width = 1280
is_labeled = True

# Relational operators return bool
above_threshold = confidence_score >= 0.90
high_resolution = resolution_width > 720

# Logical operators combine conditions
# 'and' requires both sides to be truthy
sample_is_usable = above_threshold and high_resolution and is_labeled
print(f"Sample usable  : {sample_is_usable}")    # True

# 'not' inverts
print(f"Should skip    : {not sample_is_usable}")  # False


# ---------------------------------------------------------------------------
# Example 3 — Short-circuit logic, membership, and identity
# Scenario: safe config loading with fallback defaults
# ---------------------------------------------------------------------------

config = {"model": "EfficientNet", "epochs": 0}

# Short-circuit with 'or' — returns first truthy value
# If epochs is 0 (falsy), fall back to 10
epochs = config.get("epochs") or 10
print(f"Epochs         : {epochs}")              # 10

# 'and' for safe attribute access
raw_label = config.get("label")
label = raw_label and raw_label.upper()          # only calls .upper() if not None/falsy
print(f"Label          : {label}")               # None

# Membership — checks if value exists in a collection
supported_models = ["ResNet", "EfficientNet", "ViT"]
print("EfficientNet" in supported_models)        # True
print("YOLO" not in supported_models)            # True

# Identity — checks if two names point to the same object
# Use 'is' for None checks, never ==
checkpoint = None
print(checkpoint is None)                        # True
print(checkpoint is not None)                    # False
