"""
03_class_variable_bug.py
──────────────────────────────
Topic  : Classes and Objects
Exercise: 3 of 3 — Hard
Concept: Class variable vs instance variable bug — predict, explain, and fix

Task
----
This file contains three broken classes. For each one:

  PART A — Predict: what does the code print? Write your prediction as a comment.
  PART B — Explain: in one sentence, why does it behave that way?
  PART C — Fix: rewrite the class so it behaves correctly (expected output shown).

Do not run the code until you have written predictions for all three.
This is a debugging and reasoning exercise — the goal is the prediction, not the run.

Attempt before opening solutions.
"""

# ── Bug 1 ─────────────────────────────────────────────────────────────────────
# Two Experiment instances share a results list they should not share.

class Experiment:
    results = []  # ← the bug

    def __init__(self, name):
        self.name = name

    def log(self, value):
        self.results.append(value)

exp_a = Experiment("run-A")
exp_b = Experiment("run-B")
exp_a.log(0.91)
exp_b.log(0.83)

# PART A — Prediction:
# print(exp_a.results) →
# print(exp_b.results) →

print(exp_a.results)
print(exp_b.results)

# PART B — Explanation (one sentence):
# PART C — Fix the Experiment class above so each instance has its own results list.
# Expected output:
#   [0.91]
#   [0.83]


print("---")


# ── Bug 2 ─────────────────────────────────────────────────────────────────────
# A Pipeline class variable is changed externally and affects all instances.

class Pipeline:
    stage = "preprocess"

    def __init__(self, name):
        self.name = name

    def status(self):
        return f"{self.name}: {self.stage}"

pipe1 = Pipeline("pipe-1")
pipe2 = Pipeline("pipe-2")
Pipeline.stage = "inference"

# PART A — Prediction:
# print(pipe1.status()) →
# print(pipe2.status()) →

print(pipe1.status())
print(pipe2.status())

# PART B — Explanation (one sentence):
# PART C — Fix the Pipeline class so each instance tracks its own stage.
#           pipe1 should print "pipe-1: preprocess"
#           pipe2 should print "pipe-2: preprocess"
# Expected output:
#   pipe-1: preprocess
#   pipe-2: preprocess


print("---")


# ── Bug 3 ─────────────────────────────────────────────────────────────────────
# A model config missing __str__ — output is a memory address, not useful info.

class Config:
    def __init__(self, model, lr):
        self.model = model
        self.lr = lr

cfg = Config("yolo", 0.001)

# PART A — Prediction:
# print(cfg) →

print(cfg)

# PART B — Explanation (one sentence):
# PART C — Add __str__ so it prints:
#   Config(model='yolo', lr=0.001)
