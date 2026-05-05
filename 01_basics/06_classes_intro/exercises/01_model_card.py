"""
01_model_card.py
──────────────────────────────
Topic  : Classes and Objects
Exercise: 1 of 3 — Easy
Concept: __init__, instance variables, __str__, a simple method

Task
----
Build a ModelCard class that holds metadata about a trained model.
This is the kind of object you'd use in a model registry or experiment tracker.

Rules
-----
- Use __init__ to set all instance variables
- Write __str__ to produce the exact output shown below
- Write a method is_production_ready() that returns True if
  accuracy >= 0.90 and size_mb <= 500

Expected output (exact):
    ResNet-50 v2 | accuracy=0.9340 | size=120MB | framework=PyTorch
    ViT-Base | accuracy=0.8721 | size=340MB | framework=JAX
    Production ready: True
    Production ready: False

Attempt before opening solutions.
"""


class ModelCard:
    def __init__(self, name: str, version: str, accuracy: float, size_mb: int, framework: str):
        pass  # your code here

    def __str__(self) -> str:
        pass  # your code here

    def is_production_ready(self) -> bool:
        pass  # your code here


# ── Test it ───────────────────────────────────────────────────────────────────

resnet = ModelCard("ResNet-50", "v2", accuracy=0.934, size_mb=120, framework="PyTorch")
vit    = ModelCard("ViT-Base",  "v1", accuracy=0.8721, size_mb=340, framework="JAX")

print(resnet)
print(vit)
print(f"Production ready: {resnet.is_production_ready()}")
print(f"Production ready: {vit.is_production_ready()}")
