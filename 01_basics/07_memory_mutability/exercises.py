"""
Memory and Mutability — Exercises
"""


# ---------------------------------------------------------------------------
# Exercise 1 (Easy) — Predict the output
#
# Problem:
#   Before running this code, write down what each print() will output.
#   Then run it to verify. Explain why in a comment.
#
# ---------------------------------------------------------------------------

a = [10, 20, 30]
b = a
b.append(40)
# Q1: What does print(a) output?
# Your prediction: ???
print(a)

x = "hello"
y = x
x = x + " world"
# Q2: What does print(y) output?
# Your prediction: ???
print(y)

p = [1, 2, 3]
q = p[:]
q.append(4)
# Q3: What does print(p) output?
# Your prediction: ???
print(p)


# ---------------------------------------------------------------------------
# Exercise 2 (Medium) — Fix the aliasing bug
#
# Problem:
#   The function below is supposed to add a "reviewed" tag to a copy of
#   the record and return that copy, leaving the original unchanged.
#   It currently has an aliasing bug.
#   Fix it so the original record is never modified.
#
#   Expected output:
#   Original tags: ['pending']
#   Reviewed tags: ['pending', 'reviewed']
#
# ---------------------------------------------------------------------------

def mark_as_reviewed(record: dict) -> dict:
    """Return a copy of the record with 'reviewed' added to its tags."""
    # BUG: this modifies the original — fix it
    reviewed = record
    reviewed["tags"].append("reviewed")
    return reviewed


original_record = {"id": "img_042", "tags": ["pending"]}
reviewed_record = mark_as_reviewed(original_record)

print(f"Original tags: {original_record['tags']}")
print(f"Reviewed tags: {reviewed_record['tags']}")


# ---------------------------------------------------------------------------
# Exercise 3 (Hard) — Deep copy scenario
#
# Problem:
#   You have a training configuration template. You want to create three
#   experiment configs based on it, each with a different learning rate,
#   without any of them sharing state.
#
#   Complete the function create_experiments() so that:
#     - Each experiment is an independent deep copy of the template
#     - The learning_rate in each experiment's optimizer config is set
#       to the corresponding value from learning_rates
#     - The original template is never modified
#
#   Expected output:
#   Template lr   : 0.001
#   Experiment lrs: [0.01, 0.001, 0.0001]
#   All independent: True
#
# ---------------------------------------------------------------------------

import copy

config_template = {
    "model": "ResNet-50",
    "epochs": 30,
    "optimizer": {
        "name": "Adam",
        "learning_rate": 0.001,
    },
    "augmentations": ["flip", "crop"],
}

learning_rates = [0.01, 0.001, 0.0001]


def create_experiments(template: dict, lrs: list[float]) -> list[dict]:
    """
    Create one experiment config per learning rate.
    Each config is an independent deep copy of the template.

    Args:
        template: Base configuration dictionary.
        lrs: List of learning rates, one per experiment.

    Returns:
        List of independent experiment configs.
    """
    # TODO: implement this
    pass


experiments = create_experiments(config_template, learning_rates)

print(f"Template lr   : {config_template['optimizer']['learning_rate']}")
print(f"Experiment lrs: {[e['optimizer']['learning_rate'] for e in experiments]}")

# Verify independence — mutating one should not affect others
experiments[0]["augmentations"].append("rotate")
all_independent = all(
    "rotate" not in e["augmentations"] for e in experiments[1:]
)
print(f"All independent: {all_independent}")
