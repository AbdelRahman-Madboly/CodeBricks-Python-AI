"""
01_model_card.py — Solution
──────────────────────────────
Topic  : Classes and Objects
Solution: 1 of 3 — Easy
"""


class ModelCard:
    def __init__(self, name: str, version: str, accuracy: float, size_mb: int, framework: str):
        self.name      = name
        self.version   = version
        self.accuracy  = accuracy
        self.size_mb   = size_mb
        self.framework = framework

    def __str__(self) -> str:
        # The version is included in the name field in the expected output.
        return (
            f"{self.name} {self.version} | accuracy={self.accuracy:.4f} | "
            f"size={self.size_mb}MB | framework={self.framework}"
        )

    def is_production_ready(self) -> bool:
        # Both conditions must hold — no point deploying a huge inaccurate model.
        return self.accuracy >= 0.90 and self.size_mb <= 500


resnet = ModelCard("ResNet-50", "v2", accuracy=0.934, size_mb=120, framework="PyTorch")
vit    = ModelCard("ViT-Base",  "v1", accuracy=0.8721, size_mb=340, framework="JAX")

print(resnet)
print(vit)
print(f"Production ready: {resnet.is_production_ready()}")
print(f"Production ready: {vit.is_production_ready()}")


# ── Why this works ─────────────────────────────────────────────────────────────
# __init__ stores everything on self so every method can access it.
# __str__ uses f-string formatting to produce exact output — :.4f gives four
# decimal places regardless of how many the input has.
# is_production_ready() reads two instance variables and returns a bool expression
# directly — no need for an explicit if/return True/return False.
