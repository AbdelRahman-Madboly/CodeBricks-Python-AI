"""
exercises/01_pipeline_slicer.py
────────────────────────────────
Topic    : Lists
Exercise : 1 of 3 — Easy
Concept  : Indexing, slicing, negative indices

Context
-------
You're inspecting a model training pipeline. Using only indexing and
slicing (no loops), extract the information you need from the stage list.

─────────────────────────────────────────────────────────────────
Task
─────────────────────────────────────────────────────────────────
Using only indexing and slicing on the `pipeline` list below,
print a summary that looks EXACTLY like this:

  === Pipeline Inspector ===
  First stage      : load_data
  Last stage       : save_model
  Preprocessing    : ['normalize', 'augment']
  Core stages      : ['tokenize', 'embed', 'classify']
  Every other      : ['load_data', 'augment', 'embed', 'augment']
  Reversed         : ['save_model', 'augment', 'classify', 'embed', 'tokenize', 'augment', 'normalize', 'load_data']

Rules:
  - No loops
  - No hardcoded values — all output must come from the list
  - Use only indexing lst[i] and slicing lst[a:b:c]
─────────────────────────────────────────────────────────────────
"""

pipeline = [
    "load_data",
    "normalize",
    "augment",
    "tokenize",
    "embed",
    "classify",
    "augment",
    "save_model",
]

# ── Your solution ─────────────────────────────────────────────────────────────