"""
Exceptions — Examples

Covers try/except/else/finally, specific exception types,
custom exception classes, and exception chaining.
"""


# ---------------------------------------------------------------------------
# Example 1 — try/except/else/finally
# Scenario: loading a model config file that might not exist
# ---------------------------------------------------------------------------

import json
import tempfile

def load_config(file_path: str) -> dict:
    """
    Load a JSON config file safely.

    Args:
        file_path: Path to the JSON config file.

    Returns:
        Parsed config dict.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file content is not valid JSON.
    """
    try:
        with open(file_path, encoding="utf-8") as f:
            config = json.load(f)
    except FileNotFoundError:
        # Specific, actionable message — not a raw traceback
        raise FileNotFoundError(f"Config file not found: {file_path}")
    except json.JSONDecodeError as e:
        # Chain the original error so the traceback includes both
        raise ValueError(f"Invalid JSON in {file_path}: {e}") from e
    else:
        # Only runs if no exception was raised
        print(f"Config loaded successfully: {len(config)} keys")
        return config
    finally:
        # Always runs — useful for logging or cleanup
        print(f"load_config({file_path!r}) completed")


# Test with a valid file
with tempfile.NamedTemporaryFile(mode="w", suffix=".json",
                                  delete=False, encoding="utf-8") as f:
    json.dump({"model": "ResNet", "epochs": 10}, f)
    valid_path = f.name

config = load_config(valid_path)
print(f"Model: {config['model']}\n")

# Test with a missing file
try:
    load_config("/nonexistent/config.json")
except FileNotFoundError as e:
    print(f"Caught: {e}\n")


# ---------------------------------------------------------------------------
# Example 2 — Custom exception hierarchy
# Scenario: a data pipeline with domain-specific error types
# ---------------------------------------------------------------------------

class PipelineError(Exception):
    """Base class for all pipeline errors."""

class InsufficientDataError(PipelineError):
    """Raised when a dataset has too few samples to proceed."""
    def __init__(self, found: int, required: int) -> None:
        self.found = found
        self.required = required
        super().__init__(f"Need {required} samples, found {found}")

class InvalidLabelError(PipelineError):
    """Raised when a sample contains an unrecognised label."""
    def __init__(self, label: str, valid_labels: set[str]) -> None:
        self.label = label
        super().__init__(f"Unknown label {label!r}. Valid: {valid_labels}")


def validate_dataset(samples: list[dict], min_samples: int = 100) -> None:
    """
    Validate a dataset before training.

    Raises:
        InsufficientDataError: If sample count is below the minimum.
        InvalidLabelError: If any sample has an unrecognised label.
    """
    valid_labels = {"real", "fake"}

    if len(samples) < min_samples:
        raise InsufficientDataError(found=len(samples), required=min_samples)

    for sample in samples:
        if sample["label"] not in valid_labels:
            raise InvalidLabelError(sample["label"], valid_labels)


# Test the custom exceptions
small_dataset = [{"label": "real"}, {"label": "fake"}]

try:
    validate_dataset(small_dataset, min_samples=100)
except InsufficientDataError as e:
    print(f"Data error: {e}")
    print(f"  Found {e.found}, need {e.required} more samples")

bad_label_dataset = [{"label": "unknown"}] * 200
try:
    validate_dataset(bad_label_dataset, min_samples=10)
except InvalidLabelError as e:
    print(f"Label error: {e}")
