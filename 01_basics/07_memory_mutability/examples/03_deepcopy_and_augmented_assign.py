"""
examples/03_deepcopy_and_augmented_assign.py
──────────────────────────────────────────────
Topic  : Memory and Mutability
Example: 3 of 3 — Advanced
Concept: copy.deepcopy(), += on mutable vs immutable, practical patterns

Context
-------
A data augmentation pipeline creates modified versions of image batches
for training. Without deepcopy, the "augmented" batch and the original
share inner arrays — and augmenting one silently corrupts the other.
This example also clarifies why += behaves differently on lists vs ints,
a distinction that trips up even experienced developers.

Covers:
  - copy.deepcopy() — fully independent copy of nested structures
  - deepcopy vs shallow copy — when each is appropriate
  - += on immutable types (creates new object)
  - += on mutable types (mutates in place — id stays the same)
  - Practical patterns: when to copy, when to trust immutability

Run this file. Predict each output before you see it.
"""

import copy

# ── deepcopy — fully independent copy ────────────────────────────────────────

print("=== deepcopy ===")

base_config = {
    "model":   "EfficientNet-B4",
    "lr":      0.001,
    "tags":    ["baseline", "v1"],
    "augment": {"flip": True, "crop": 0.8},
}

# deepcopy recursively copies every nested object
exp_config = copy.deepcopy(base_config)

exp_config["lr"] = 0.005
exp_config["tags"].append("exp-lr")
exp_config["augment"]["crop"] = 0.9

print(f"base lr       : {base_config['lr']}")            # 0.001 — protected
print(f"base tags     : {base_config['tags']}")          # ['baseline', 'v1'] — protected
print(f"base crop     : {base_config['augment']['crop']}") # 0.8 — protected

print(f"\nexp lr        : {exp_config['lr']}")            # 0.005
print(f"exp tags      : {exp_config['tags']}")           # ['baseline', 'v1', 'exp-lr']
print(f"exp crop      : {exp_config['augment']['crop']}") # 0.9

# Confirm full independence
print(f"\nSame dict?    {base_config is exp_config}")                              # False
print(f"Same tags?    {base_config['tags'] is exp_config['tags']}")              # False
print(f"Same augment? {base_config['augment'] is exp_config['augment']}")        # False

# ── Batch augmentation use case ───────────────────────────────────────────────

print()
print("=== Image batch augmentation ===")

# Simulated image batch: list of lists (each inner list = one image's pixels)
original_batch = [[0.91, 0.74, 0.58], [0.47, 0.39, 0.85]]

# Wrong — shallow copy, shared inner lists
augmented_shallow = original_batch[:]
augmented_shallow[0][0] = 0.0   # "augmenting" first pixel of first image
print(f"original (shallow): {original_batch}")   # affected — bug!

# Reset
original_batch = [[0.91, 0.74, 0.58], [0.47, 0.39, 0.85]]

# Correct — deepcopy, fully independent
augmented_deep = copy.deepcopy(original_batch)
augmented_deep[0][0] = 0.0
print(f"original (deep)   : {original_batch}")   # unchanged — correct
print(f"augmented (deep)  : {augmented_deep}")

# ── += on immutable vs mutable ────────────────────────────────────────────────

print()
print("=== += on immutable (int) ===")

epoch = 5
print(f"id before : {id(epoch)}")
epoch += 1          # creates a NEW int object — same as: epoch = epoch + 1
print(f"id after  : {id(epoch)}")   # different — new object
print(f"epoch     : {epoch}")       # 6

print()
print("=== += on mutable (list) ===")

losses = [0.91, 0.74]
print(f"id before : {id(losses)}")
losses += [0.58]    # extends the list IN PLACE — same as: losses.extend([0.58])
print(f"id after  : {id(losses)}")   # SAME — same object mutated
print(f"losses    : {losses}")       # [0.91, 0.74, 0.58]

# Why this matters — shared reference + +=
shared = [0.91]
alias  = shared
shared += [0.74]    # mutates in place — alias sees the change
print(f"\nshared : {shared}")   # [0.91, 0.74]
print(f"alias  : {alias}")    # [0.91, 0.74] — same object

# ── When to copy and when not to ─────────────────────────────────────────────

print()
print("=== Decision guide ===")

# Rule: immutable inputs to a function never need copying — they can't be mutated
def scale_lr(lr: float, factor: float) -> float:
    lr *= factor   # moves local label to new float — caller's lr unchanged
    return lr

base_lr = 0.001
scaled  = scale_lr(base_lr, 10)
print(f"base_lr after scale_lr: {base_lr}")   # 0.001 — unchanged, as expected

# Rule: mutable inputs that you'll modify inside a function need a copy
def normalise_labels(labels: list[str]) -> list[str]:
    labels = labels[:]              # shallow copy — safe for flat list of strings
    labels = [l.lower() for l in labels]
    return labels

raw = ["Real", "Fake", "Uncertain"]
clean = normalise_labels(raw)
print(f"raw after normalise : {raw}")    # unchanged
print(f"clean               : {clean}")

# ── What to notice ────────────────────────────────────────────────────────────
#
# 1. copy.deepcopy() is the only guaranteed way to get a fully independent copy
#    of a nested structure. It recursively copies every object inside.
#    Cost: it's slower than shallow copy — use it only when you need independence
#    on nested mutable objects.
#
# 2. += on an immutable (int, float, str) always creates a new object.
#    += on a mutable (list, set) mutates the object in place.
#    This asymmetry causes bugs when you have aliases to mutable objects.
#
# 3. Functions receiving immutable arguments are automatically safe —
#    the caller's value can never be mutated through an immutable reference.
#    Functions receiving mutable arguments must decide: copy or mutate?
#    Document this choice. Unexpected mutation is a bug.
#
# 4. Flat structures (list of strings, dict of scalars) → shallow copy is fine.
#    Nested structures (list of lists, dict of lists/dicts) → use deepcopy.
#
# 5. In NumPy (Phase 6), array slicing returns a VIEW not a copy — the same
#    memory, a different label. Modifying the slice modifies the original.
#    np.array.copy() gives you a real copy. You'll need this mental model then.