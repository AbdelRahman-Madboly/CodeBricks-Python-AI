"""
Modules and Packages — Exercises
"""

# ---------------------------------------------------------------------------
# Exercise 1 (Easy) — Import and use standard library modules
#
# Problem:
#   Using only standard library imports (no pip installs), write a script that:
#     a) Prints today's date formatted as: "Run date: 15 Jan 2024"
#     b) Prints the absolute path of the current working directory
#     c) Generates and prints 5 random floats between 0.5 and 1.0,
#        each rounded to 3 decimal places, on one line separated by spaces
#
#   Expected output (values will differ each run):
#   Run date: 15 Jan 2024
#   Working dir: /home/user/codebricks
#   Scores: 0.731 0.892 0.654 0.978 0.812
#
# Your solution below:
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Exercise 2 (Medium) — The __name__ guard
#
# Problem:
#   Write a module-style file that:
#     - Defines a function called normalise_scores(scores, min_val, max_val)
#       that normalises a list of floats to [0, 1] using min-max scaling
#     - At module level (outside the function), prints "Module loaded: normalise"
#     - Under __name__ == "__main__", runs a self-test that prints:
#         Testing normalise_scores...
#         [0.0, 0.5, 1.0]
#         All tests passed.
#
#   If this file is imported, only "Module loaded: normalise" should print.
#   The test block must NOT run on import.
#
# Your solution below:
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Exercise 3 (Hard) — Path manipulation with pathlib
#
# Problem:
#   Write a function scan_checkpoint_dir() that:
#     - Takes a directory path (as a string or Path)
#     - Returns a dict with:
#         "found":  list of .pt filenames sorted alphabetically
#         "latest": the filename with the highest number in its name
#                   (e.g. "epoch_15.pt" beats "epoch_10.pt")
#         "count":  total number of .pt files found
#     - If the directory doesn't exist or has no .pt files,
#       return {"found": [], "latest": None, "count": 0}
#
#   You don't need real files — write the logic and test with a mock
#   using pathlib.Path and a mocked list of filenames.
#
# Hint: you can test path logic without real files using:
#   from unittest.mock import patch, MagicMock
# Or simply test the sorting/extraction logic with plain strings.
#
# Expected behaviour:
#   Given filenames: ["epoch_05.pt", "epoch_15.pt", "epoch_10.pt"]
#   Output: {'found': ['epoch_05.pt', 'epoch_10.pt', 'epoch_15.pt'],
#            'latest': 'epoch_15.pt', 'count': 3}
#
from pathlib import Path


def scan_checkpoint_dir(directory: str | Path) -> dict:
    """
    Scan a directory for model checkpoint files.

    Args:
        directory: Path to the checkpoint directory.

    Returns:
        Dict with 'found', 'latest', and 'count' keys.
    """
    # TODO: implement
    pass


# Test with a temporary directory containing dummy files
import tempfile, os

def test_scan():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create dummy checkpoint files
        for name in ["epoch_05.pt", "epoch_15.pt", "epoch_10.pt"]:
            Path(tmpdir, name).touch()
        # Also add a non-.pt file that should be ignored
        Path(tmpdir, "config.yaml").touch()

        result = scan_checkpoint_dir(tmpdir)
        print(result)

test_scan()
