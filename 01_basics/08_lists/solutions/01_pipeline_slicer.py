"""
solutions/01_pipeline_slicer.py
────────────────────────────────
Topic    : Lists
Solution : Exercise 1 — Pipeline slicer
"""

pipeline = [
    "load_data", "normalize", "augment", "tokenize",
    "embed", "classify", "augment", "save_model",
]

print("  === Pipeline Inspector ===")
print(f"  First stage      : {pipeline[0]}")
print(f"  Last stage       : {pipeline[-1]}")
print(f"  Preprocessing    : {pipeline[1:3]}")
print(f"  Core stages      : {pipeline[3:6]}")
print(f"  Every other      : {pipeline[::2]}")
print(f"  Reversed         : {pipeline[::-1]}")

# ── Why this works ────────────────────────────────────────────────────────────
#
# pipeline[0]  → first item (index 0)
# pipeline[-1] → last item (negative index from end)
# pipeline[1:3] → indices 1 and 2 (stop=3 is exclusive): normalize, augment
# pipeline[3:6] → indices 3, 4, 5: tokenize, embed, classify
# pipeline[::2] → every 2nd item starting from 0: indices 0, 2, 4, 6
# pipeline[::-1] → step=-1 means go backwards through the whole list
#
# The duplicated "augment" at indices 2 and 6 is correctly preserved in the
# reversed output — your code doesn't need to do anything special about it.
# Slicing doesn't filter duplicates; it just copies the relevant elements.
#
# Why no loops?
# This exercise trains the "think in slices" mindset.
# In NumPy (Phase 6) and PyTorch (Phase 7), slicing is how you extract
# rows, columns, and sub-arrays from multi-dimensional tensors.
# The syntax is identical — learning it on plain lists is the foundation.