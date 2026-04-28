"""
examples/01_normalize_and_hints.py
───────────────────────────────────
Topic  : Functions
Example: 1 of 3 — def, return, type hints, docstring, default parameters

Context
-------
Before any image passes through a neural network, pixel values (0–255)
get normalized to [0.0, 1.0]. This is one of the first preprocessing
functions you'll write in any computer vision project.

It's a perfect first function: one clear job, one input, one output,
a natural default range, and a result you can actually verify by hand.

Covers:
  - def keyword, parameters, return
  - Type hints on parameters and return value
  - Google-style docstring
  - Default parameter values
  - Calling with positional vs keyword arguments
  - print vs return — the function produces a value, not output

Run this file. Predict each output before you see it.
"""


# ── The function ──────────────────────────────────────────────────────────────

def normalize_pixel(
    pixel_value: int,
    min_val: int = 0,
    max_val: int = 255,
) -> float:
    """
    Normalize a pixel intensity to the range [0.0, 1.0].

    Args:
        pixel_value: Raw pixel intensity.
        min_val: Lower bound of the input range (default 0).
        max_val: Upper bound of the input range (default 255).

    Returns:
        Float in [0.0, 1.0] representing the normalized value.
    """
    return (pixel_value - min_val) / (max_val - min_val)


# ── Calling it ────────────────────────────────────────────────────────────────

# Positional arguments — order matters
print(normalize_pixel(0))     # 0.0   — black pixel
print(normalize_pixel(128))   # 0.5019...
print(normalize_pixel(255))   # 1.0   — white pixel

# Keyword arguments — any order, self-documenting
print(normalize_pixel(pixel_value=200, min_val=100, max_val=300))  # 0.5

# Default parameters let you skip arguments you don't need to override
# normalize_pixel(128) uses min_val=0, max_val=255 automatically

# ── Storing and reusing the result ───────────────────────────────────────────

raw_pixels = [0, 64, 128, 192, 255]

print("\nNormalized image row:")
for px in raw_pixels:
    normalized = normalize_pixel(px)   # result captured in a variable
    print(f"  {px:>3}  →  {normalized:.4f}")

# ── What to notice ────────────────────────────────────────────────────────────
#
# 1. def + indentation
#    The colon after def starts the function block.
#    Everything indented under it is the function body.
#    Python uses indentation — not {} braces — to define the block.
#
# 2. Type hints: pixel_value: int, -> float
#    These are annotations, not enforcement. Python won't crash if you
#    pass a float — but your IDE will warn you, and mypy will flag it.
#    In Phase 5 you'll enforce these with mypy + ruff.
#
# 3. return vs print
#    The function returns a float — it doesn't print anything.
#    The print() calls are outside the function, using the returned value.
#    A function that prints instead of returning can't be composed:
#      result = normalize_pixel(128)   # works — result is 0.5019
#      result = print_pixel(128)       # result is None — useless
#
# 4. Default parameters
#    min_val=0, max_val=255 are the sensible defaults for 8-bit images.
#    You can override them for 16-bit images (0–65535) or custom ranges.
#    Required parameters (no default) must come BEFORE optional ones.
#
# 5. Google-style docstring
#    Args: lists each parameter with its type and description.
#    Returns: describes what the function produces.
#    This format is read by IDEs, documentation generators, and other devs.
#    Get in the habit now — it costs 30 seconds and pays back constantly.