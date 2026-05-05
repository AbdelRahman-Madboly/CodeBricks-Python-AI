"""
exercises/01_input_guards.py
──────────────────────────────
Topic    : Exceptions
Exercise : 1 of 3 — Easy
Concept  : raise, guard clauses, caller handles the exception

Context
-------
A model evaluation pipeline calls several utility functions with user-
supplied parameters. Each function must validate its inputs and raise
a meaningful exception before doing any work — the caller handles it.

─────────────────────────────────────────────────────────────────
Task A — validate_threshold()
─────────────────────────────────────────────────────────────────
Write a function that takes a confidence threshold and raises a
ValueError if it's outside [0.0, 1.0]. Otherwise return the value.

Signature:
  def validate_threshold(threshold: float) -> float

Expected behaviour:
  validate_threshold(0.75)   → 0.75
  validate_threshold(1.5)    → raises ValueError: "threshold must be between 0.0 and 1.0, got 1.5"
  validate_threshold(-0.1)   → raises ValueError: same message

─────────────────────────────────────────────────────────────────
Task B — get_model_config()
─────────────────────────────────────────────────────────────────
Write a function that takes a model name and returns its config dict.
If the model name is not in the registry, raise a KeyError with the
message: "unknown model: '<name>'"

Signature:
  def get_model_config(name: str) -> dict

Registry:
  "ResNet-50"       → {"layers": 50,  "input_size": 224}
  "EfficientNet-B4" → {"layers": 380, "input_size": 380}
  "ViT-Base"        → {"layers": 12,  "input_size": 224}

Expected behaviour:
  get_model_config("ResNet-50")    → {"layers": 50, "input_size": 224}
  get_model_config("AlexNet")      → raises KeyError: "unknown model: 'AlexNet'"

─────────────────────────────────────────────────────────────────
Task C — Wrap calls at the call site
─────────────────────────────────────────────────────────────────
Call each function below. Wrap each call in its own try/except block
and print the exception if one is raised.

Expected output:
  threshold=0.75 → OK
  threshold=1.5  → ValueError: threshold must be between 0.0 and 1.0, got 1.5
  model=ResNet-50       → {'layers': 50, 'input_size': 224}
  model=AlexNet         → KeyError: 'unknown model: 'AlexNet''
─────────────────────────────────────────────────────────────────
"""

# ── Task A ────────────────────────────────────────────────────────────────────

def validate_threshold(threshold: float) -> float:
    # TODO: implement
    pass


# ── Task B ────────────────────────────────────────────────────────────────────

def get_model_config(name: str) -> dict:
    # TODO: implement
    pass


# ── Task C ────────────────────────────────────────────────────────────────────

# threshold calls
for t in [0.75, 1.5]:
    pass   # TODO: wrap in try/except and print result or exception

# model config calls
for model in ["ResNet-50", "AlexNet"]:
    pass   # TODO: wrap in try/except and print result or exception