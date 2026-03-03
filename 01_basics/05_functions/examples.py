"""
Functions — Examples

Covers function definition, return values, default parameters,
*args/**kwargs, type hints, and scope through realistic scenarios.
"""


# ---------------------------------------------------------------------------
# Example 1 — Basic function with type hints and docstring
# Scenario: normalizing a pixel value for a neural network input
# ---------------------------------------------------------------------------

def normalize_pixel(pixel_value: int, min_val: int = 0, max_val: int = 255) -> float:
    """
    Normalize a pixel value to the range [0.0, 1.0].

    Args:
        pixel_value: Raw pixel intensity (typically 0-255).
        min_val: Minimum of the input range.
        max_val: Maximum of the input range.

    Returns:
        Normalized float in [0.0, 1.0].
    """
    return (pixel_value - min_val) / (max_val - min_val)


print(normalize_pixel(128))           # 0.5019...
print(normalize_pixel(255))           # 1.0
print(normalize_pixel(0))             # 0.0
print(normalize_pixel(200, 100, 300)) # 0.5 — custom range via keyword args


# ---------------------------------------------------------------------------
# Example 2 — *args and **kwargs
# Scenario: a flexible logging function for a training pipeline
# ---------------------------------------------------------------------------

def log_event(level: str, *messages: str, **metadata) -> None:
    """
    Log a structured event with optional extra context.

    Args:
        level: Severity level (INFO, WARNING, ERROR).
        *messages: One or more message strings to join.
        **metadata: Optional key-value context (epoch, loss, etc.).
    """
    combined_message = " ".join(messages)
    meta_str = " ".join(f"{k}={v}" for k, v in metadata.items())
    output = f"[{level}] {combined_message}"
    if meta_str:
        output += f" | {meta_str}"
    print(output)


log_event("INFO", "Training started")
log_event("INFO", "Epoch", "complete", epoch=5, loss=0.042)
log_event("WARNING", "Low GPU memory", device="cuda:0", free_mb=312)


# ---------------------------------------------------------------------------
# Example 3 — Mutable default trap and scope
# Scenario: building a batch collector that must not share state between calls
# ---------------------------------------------------------------------------

# WRONG — the list is created once and reused across all calls
def add_to_batch_wrong(sample: str, batch: list = []) -> list:
    batch.append(sample)
    return batch

# RIGHT — create a fresh list each call when none is provided
def add_to_batch(sample: str, batch: list | None = None) -> list:
    """
    Add a sample to a batch, creating a new batch if none is provided.

    Args:
        sample: The sample identifier to add.
        batch: Existing batch to append to, or None to start fresh.

    Returns:
        The updated batch list.
    """
    if batch is None:
        batch = []
    batch.append(sample)
    return batch


# Demonstrates the wrong version sharing state
print(add_to_batch_wrong("img_001"))   # ['img_001']
print(add_to_batch_wrong("img_002"))   # ['img_001', 'img_002'] — bug!

# Correct version starts fresh each time
print(add_to_batch("img_001"))         # ['img_001']
print(add_to_batch("img_002"))         # ['img_002'] — correct

# Passing an existing batch explicitly still works
existing = ["img_000"]
print(add_to_batch("img_001", existing))  # ['img_000', 'img_001']
