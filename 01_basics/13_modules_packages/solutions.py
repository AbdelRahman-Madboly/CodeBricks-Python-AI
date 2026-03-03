"""
Modules and Packages — Solutions
"""

import os
import random
import tempfile
from datetime import datetime
from pathlib import Path


# ---------------------------------------------------------------------------
# Solution 1
# ---------------------------------------------------------------------------

today = datetime.today()
print(f"Run date: {today.strftime('%d %b %Y')}")
print(f"Working dir: {os.getcwd()}")

scores = [round(random.uniform(0.5, 1.0), 3) for _ in range(5)]
print("Scores:", " ".join(str(s) for s in scores))


# ---------------------------------------------------------------------------
# Solution 2
# ---------------------------------------------------------------------------

print("Module loaded: normalise")


def normalise_scores(scores: list[float], min_val: float, max_val: float) -> list[float]:
    """
    Apply min-max normalisation to scale scores to [0, 1].

    Args:
        scores: List of raw float values.
        min_val: Minimum of the input range.
        max_val: Maximum of the input range.

    Returns:
        List of normalised floats in [0.0, 1.0].
    """
    span = max_val - min_val
    if span == 0:
        return [0.0] * len(scores)
    return [(s - min_val) / span for s in scores]


if __name__ == "__main__":
    print("Testing normalise_scores...")
    result = normalise_scores([0.0, 0.5, 1.0], 0.0, 1.0)
    print(result)
    assert result == [0.0, 0.5, 1.0], "Test failed"
    print("All tests passed.")


# ---------------------------------------------------------------------------
# Solution 3
# ---------------------------------------------------------------------------

def scan_checkpoint_dir(directory: str | Path) -> dict:
    """
    Scan a directory for model checkpoint (.pt) files.
    """
    path = Path(directory)

    empty_result: dict = {"found": [], "latest": None, "count": 0}

    if not path.exists() or not path.is_dir():
        return empty_result

    pt_files = sorted(f.name for f in path.glob("*.pt"))

    if not pt_files:
        return empty_result

    def extract_number(filename: str) -> int:
        # Extract the first sequence of digits found in the filename
        digits = "".join(ch for ch in filename if ch.isdigit())
        return int(digits) if digits else 0

    latest = max(pt_files, key=extract_number)

    return {"found": pt_files, "latest": latest, "count": len(pt_files)}


def test_scan():
    with tempfile.TemporaryDirectory() as tmpdir:
        for name in ["epoch_05.pt", "epoch_15.pt", "epoch_10.pt"]:
            Path(tmpdir, name).touch()
        Path(tmpdir, "config.yaml").touch()   # should be ignored

        result = scan_checkpoint_dir(tmpdir)
        print(result)


test_scan()
