"""
exercises/01_pipeline_slicer.py
────────────────────────────────
Topic    : Lists
Exercise : 1 of 3 — Easy
Concept  : Indexing, slicing, negative indices, basic methods

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
  Every other      : ['load_data', 'normalize', 'embed', 'save_model']
  Reversed         : ['save_model', 'augment', 'classify', 'embed', 'tokenize', 'normalize', 'augment', 'load_data']

Wait — that reversed output looks wrong. Look at the pipeline carefully.
One of the stage names is duplicated and that's intentional.
Your code should reflect the actual list — don't hardcode.

Rules:
  - No loops
  - No hardcoded values — all output must come from the list
  - Use only indexing `lst[i]` and slicing `lst[a:b:c]`
─────────────────────────────────────────────────────────────────
"""

pipeline = [
    "load_data",     # 0
    "normalize",     # 1
    "augment",       # 2
    "tokenize",      # 3
    "embed",         # 4
    "classify",      # 5
    "augment",       # 6  — post-processing augment (different role, same name)
    "save_model",    # 7
]

# ── Your solution ─────────────────────────────────────────────────────────────