"""
03_class_variable_bug.py — Solution
──────────────────────────────
Topic  : Classes and Objects
Solution: 3 of 3 — Hard
"""

# ── Bug 1 — Fix ───────────────────────────────────────────────────────────────
# Prediction:
#   print(exp_a.results) → [0.91, 0.83]   ← both values, not just exp_a's
#   print(exp_b.results) → [0.91, 0.83]   ← same list, both point to it
#
# Explanation: results = [] at class level creates ONE list shared by every instance.
# self.results.append() mutates that shared list — it doesn't create a new one.

class Experiment:
    def __init__(self, name):
        self.name = name
        self.results = []   # ← instance variable: fresh list per object

    def log(self, value):
        self.results.append(value)

exp_a = Experiment("run-A")
exp_b = Experiment("run-B")
exp_a.log(0.91)
exp_b.log(0.83)
print(exp_a.results)  # [0.91]
print(exp_b.results)  # [0.83]


print("---")


# ── Bug 2 — Fix ───────────────────────────────────────────────────────────────
# Prediction:
#   print(pipe1.status()) → "pipe-1: inference"
#   print(pipe2.status()) → "pipe-2: inference"
#
# Explanation: Pipeline.stage = "inference" overwrites the class variable,
# and since no instance has its own .stage, all instances see the updated value.

class Pipeline:
    def __init__(self, name):
        self.name  = name
        self.stage = "preprocess"   # ← instance variable: independent per object

    def status(self):
        return f"{self.name}: {self.stage}"

pipe1 = Pipeline("pipe-1")
pipe2 = Pipeline("pipe-2")
Pipeline.stage = "inference"   # now only affects the class, not the instances
print(pipe1.status())  # pipe-1: preprocess
print(pipe2.status())  # pipe-2: preprocess


print("---")


# ── Bug 3 — Fix ───────────────────────────────────────────────────────────────
# Prediction:
#   print(cfg) → <__main__.Config object at 0x...>
#
# Explanation: Without __str__, Python falls back to object.__str__ which returns
# the class name and memory address — unhelpful for any real debugging.

class Config:
    def __init__(self, model, lr):
        self.model = model
        self.lr    = lr

    def __str__(self) -> str:
        return f"Config(model={self.model!r}, lr={self.lr})"

cfg = Config("yolo", 0.001)
print(cfg)  # Config(model='yolo', lr=0.001)


# ── Why this works ─────────────────────────────────────────────────────────────
# Bug 1: The fix is purely structural — move the list into __init__ so it's
#   created fresh for each instance. self.results = [] runs once per object.
# Bug 2: Instance variables shadow class variables. Once self.stage = "preprocess"
#   is set in __init__, Python finds it on the instance and never looks at the class.
# Bug 3: __str__ is just a method. The !r in {self.model!r} adds quotes around
#   string values — it calls repr() on the value, which includes the quote marks.
