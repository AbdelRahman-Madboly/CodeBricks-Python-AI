"""
Memory and Mutability — Solutions
"""

import copy


# ---------------------------------------------------------------------------
# Solution 1
# ---------------------------------------------------------------------------

# Q1: [10, 20, 30, 40] — b and a point to the same list; append mutates it
a = [10, 20, 30]
b = a
b.append(40)
print(a)   # [10, 20, 30, 40]

# Q2: 'hello' — strings are immutable; x = x + " world" creates a new object
x = "hello"
y = x
x = x + " world"
print(y)   # hello

# Q3: [1, 2, 3] — p[:] is a shallow copy; q and p are independent lists
p = [1, 2, 3]
q = p[:]
q.append(4)
print(p)   # [1, 2, 3]


# ---------------------------------------------------------------------------
# Solution 2
# ---------------------------------------------------------------------------

def mark_as_reviewed(record: dict) -> dict:
    """Return a copy of the record with 'reviewed' added to its tags."""
    # Use deepcopy because the dict contains a nested list
    reviewed = copy.deepcopy(record)
    reviewed["tags"].append("reviewed")
    return reviewed


original_record = {"id": "img_042", "tags": ["pending"]}
reviewed_record = mark_as_reviewed(original_record)

print(f"Original tags: {original_record['tags']}")   # ['pending']
print(f"Reviewed tags: {reviewed_record['tags']}")   # ['pending', 'reviewed']


# ---------------------------------------------------------------------------
# Solution 3
# ---------------------------------------------------------------------------

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
    """
    experiments = []
    for lr in lrs:
        experiment = copy.deepcopy(template)
        experiment["optimizer"]["learning_rate"] = lr
        experiments.append(experiment)
    return experiments


experiments = create_experiments(config_template, learning_rates)

print(f"Template lr   : {config_template['optimizer']['learning_rate']}")
print(f"Experiment lrs: {[e['optimizer']['learning_rate'] for e in experiments]}")

experiments[0]["augmentations"].append("rotate")
all_independent = all(
    "rotate" not in e["augmentations"] for e in experiments[1:]
)
print(f"All independent: {all_independent}")   # True
