"""
Memory and Mutability — Examples

Demonstrates Python's reference model, mutable vs immutable objects,
aliasing pitfalls, and safe copying strategies.
"""

import copy


# ---------------------------------------------------------------------------
# Example 1 — References vs values
# Scenario: two variables pointing to the same list
# ---------------------------------------------------------------------------

pipeline_stages = ["load", "preprocess", "infer"]
active_stages = pipeline_stages     # NOT a copy — both names point to the same list

active_stages.append("postprocess")

# Modifying through one name affects the other — they share the object
print(pipeline_stages)   # ['load', 'preprocess', 'infer', 'postprocess']
print(active_stages)     # ['load', 'preprocess', 'infer', 'postprocess']
print(pipeline_stages is active_stages)  # True — same object in memory

# To make an independent copy:
pipeline_stages = ["load", "preprocess", "infer"]
active_stages = pipeline_stages[:]   # shallow copy

active_stages.append("postprocess")
print(pipeline_stages)   # ['load', 'preprocess', 'infer']  — unchanged
print(active_stages)     # ['load', 'preprocess', 'infer', 'postprocess']


# ---------------------------------------------------------------------------
# Example 2 — Immutable objects: reassignment creates new objects
# Scenario: tracking a learning rate across training steps
# ---------------------------------------------------------------------------

learning_rate = 0.01
original_lr = learning_rate

# Reassigning creates a new float object — original_lr still points to 0.01
learning_rate = learning_rate * 0.9
print(f"current : {learning_rate}")   # 0.009
print(f"original: {original_lr}")     # 0.01 — unchanged

# id() confirms they are different objects
print(id(learning_rate) == id(original_lr))  # False

# Strings work the same way — every "change" is a new object
tag = "deepfake"
original_tag = tag
tag = tag.upper()          # creates a new string "DEEPFAKE"
print(original_tag)        # deepfake — original untouched


# ---------------------------------------------------------------------------
# Example 3 — Shallow vs deep copy with nested structures
# Scenario: augmenting a batch without corrupting the original
# ---------------------------------------------------------------------------

original_batch = [
    {"id": "img_001", "labels": ["real"]},
    {"id": "img_002", "labels": ["fake"]},
]

# Shallow copy — outer list is new, but inner dicts are shared
shallow = original_batch[:]
shallow[0]["labels"].append("augmented")   # modifies the shared dict!

print("After shallow copy mutation:")
print(original_batch[0]["labels"])  # ['real', 'augmented'] — corrupted

# Deep copy — everything is duplicated recursively
original_batch = [
    {"id": "img_001", "labels": ["real"]},
    {"id": "img_002", "labels": ["fake"]},
]

deep = copy.deepcopy(original_batch)
deep[0]["labels"].append("augmented")      # only affects the deep copy

print("\nAfter deep copy mutation:")
print(original_batch[0]["labels"])  # ['real'] — safe
print(deep[0]["labels"])            # ['real', 'augmented']
