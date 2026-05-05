"""
01_model_config.py
──────────────────────────────
Topic  : Classes and Objects
Example: 1 of 3 — Easy
Concept: __init__, instance variables, __str__, __repr__, basic methods

Context
-------
Every ML training run starts from a configuration object: learning rate, batch size,
number of epochs, model architecture name. In production systems, these aren't kept
in loose variables — they're bundled in a config class so they can be validated,
logged, serialised, and passed around as a single unit.

Covers:
  - class definition and the __init__ constructor
  - self and instance variables
  - __str__ for human-readable output
  - __repr__ for developer-readable output
  - a simple getter method

Run this file. Predict each output before you see it.
"""


class ModelConfig:
    def __init__(self, name: str, lr: float, epochs: int, batch_size: int = 32):
        # Every parameter becomes an instance variable attached to self.
        # self.x = value is how you store data on the object.
        self.name = name
        self.lr = lr
        self.epochs = epochs
        self.batch_size = batch_size

    def __str__(self) -> str:
        # __str__ is called by print() and f"{}".
        # Write something a human would find useful in a log.
        return f"{self.name} | lr={self.lr} | epochs={self.epochs} | batch={self.batch_size}"

    def __repr__(self) -> str:
        # __repr__ is shown in the REPL and inside collections.
        # Convention: make it look like the call that would recreate the object.
        return (
            f"ModelConfig(name={self.name!r}, lr={self.lr}, "
            f"epochs={self.epochs}, batch_size={self.batch_size})"
        )

    def total_steps(self, dataset_size: int) -> int:
        # A getter method — computes a value from instance data without changing it.
        # Called as cfg.total_steps(50000), not ModelConfig.total_steps(cfg, 50000).
        return (dataset_size // self.batch_size) * self.epochs


# ── Creating instances ────────────────────────────────────────────────────────

resnet_cfg = ModelConfig("resnet50", lr=0.001, epochs=30, batch_size=64)
vit_cfg    = ModelConfig("vit-base", lr=0.0001, epochs=50)  # batch_size defaults to 32

# Each object is independent — changing one does not affect the other.
print(resnet_cfg)     # calls __str__
print(vit_cfg)

# __repr__ appears when you look at objects in a list or the REPL
print([resnet_cfg, vit_cfg])

# Calling a method — self is passed implicitly
steps = resnet_cfg.total_steps(50000)
print(f"ResNet training steps: {steps}")

# Mutating an instance variable directly
# (later you'll use @property to control this — topic 02_oop/02_properties_static)
resnet_cfg.epochs = 60
print(f"Updated epochs: {resnet_cfg.epochs}")
print(f"ViT epochs unchanged: {vit_cfg.epochs}")


# ── What to notice ────────────────────────────────────────────────────────────
# 1. self is always the first parameter but you never pass it — Python does that.
# 2. __str__ and __repr__ are just regular methods with special names.
#    Python calls them automatically in certain contexts.
# 3. batch_size=32 is a default — works exactly like function defaults from topic 05.
# 4. resnet_cfg and vit_cfg are fully independent objects. Modifying one
#    does not touch the other.
# 5. total_steps reads self.batch_size and self.epochs — it has access to all
#    instance variables, not just the ones passed to that specific method call.
