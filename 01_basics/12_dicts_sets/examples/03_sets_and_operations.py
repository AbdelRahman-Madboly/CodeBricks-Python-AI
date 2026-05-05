"""
examples/03_sets_and_operations.py
────────────────────────────────────
Topic  : Dictionaries and Sets
Example: 3 of 3 — Advanced
Concept: Sets, set operations (|, &, -, ^), deduplication, frozenset, membership speed

Context
-------
When managing dataset splits, you often need to know which classes
appear in train but not validation, which IDs were already processed,
and whether two annotation sets agree. Set operations answer all of these
in one line — and do it in O(1) per lookup instead of O(n).

Covers:
  - Set literals: {a, b, c}
  - Empty set: set() — NOT {} (that's an empty dict)
  - .add(), .discard(), .remove()
  - Operators: | (union), & (intersection), - (difference), ^ (symmetric diff)
  - Membership: x in set — O(1) vs O(n) for lists
  - Order-preserving deduplication
  - frozenset — immutable set, usable as a dict key
  - Converting between list and set

Run this file. Predict each output before you see it.
"""

# ── Creating sets ─────────────────────────────────────────────────────────────

print("=== Creating sets ===")

train_labels = {"real", "fake", "uncertain", "blurry"}
val_labels   = {"real", "fake", "compressed"}

print(f"train_labels : {train_labels}")   # order not guaranteed
print(f"val_labels   : {val_labels}")

# {} without key:value pairs is an empty DICT — use set() for an empty set
empty_dict = {}
empty_set  = set()
print(f"type({{}})       : {type(empty_dict)}")   # <class 'dict'>
print(f"type(set())  : {type(empty_set)}")        # <class 'set'>

# ── Set operations ────────────────────────────────────────────────────────────

print()
print("=== Set operations ===")

# Union — all labels that appear in either split
all_labels = train_labels | val_labels
print(f"Union (|)         : {all_labels}")

# Intersection — labels that appear in BOTH splits
shared = train_labels & val_labels
print(f"Intersection (&)  : {shared}")

# Difference — labels in train but NOT in val (coverage gap)
train_only = train_labels - val_labels
print(f"Train only (-)    : {train_only}")

val_only = val_labels - train_labels
print(f"Val only          : {val_only}")

# Symmetric difference — labels in exactly ONE of the two sets
exclusive = train_labels ^ val_labels
print(f"Exclusive (^)     : {exclusive}")

# Subset / superset
small = {"real", "fake"}
print(f"\n{small} ⊆ train? : {small.issubset(train_labels)}")       # True
print(f"train ⊇ {small}? : {train_labels.issuperset(small)}")     # True

# ── Membership speed ──────────────────────────────────────────────────────────

print()
print("=== Membership: set vs list ===")

# Imagine 100k processed IDs — checking membership is O(1) for a set
processed_ids = set(range(100_000))        # 100k integers

# O(1) — hash lookup — instant regardless of size
print(f"99999 in set     : {99999 in processed_ids}")   # True
print(f"100001 in set    : {100001 in processed_ids}")  # False

# O(n) — linear scan — slows down as the list grows
processed_list = list(range(100_000))
print(f"99999 in list    : {99999 in processed_list}")  # True — but slower

# ── Deduplication ─────────────────────────────────────────────────────────────

print()
print("=== Deduplication ===")

# Simplest — but loses order
raw = ["fake", "real", "fake", "uncertain", "real", "blurry"]
unique_unordered = list(set(raw))
print(f"set() dedup      : {unique_unordered}")   # order not preserved

# Order-preserving deduplication
seen: set[str] = set()
unique_ordered: list[str] = []
for label in raw:
    if label not in seen:
        seen.add(label)
        unique_ordered.append(label)

print(f"Ordered dedup    : {unique_ordered}")   # original order preserved

# ── .add(), .discard(), .remove() ────────────────────────────────────────────

print()
print("=== Mutating a set ===")

active_classes: set[str] = {"real", "fake"}
active_classes.add("uncertain")       # adds if not present; no-op if present
active_classes.add("real")            # no error, no change
print(f"After adds       : {active_classes}")

active_classes.discard("blurry")      # no error if absent
active_classes.remove("uncertain")    # KeyError if absent — uncomment to see
# active_classes.remove("missing")    # KeyError

print(f"After removes    : {active_classes}")

# ── frozenset — immutable set usable as a dict key ───────────────────────────

print()
print("=== frozenset ===")

# Use case: cache results keyed by a set of class names
# Regular sets are mutable — they can't be dict keys
# frozenset is immutable — safe to use as a key

cache: dict[frozenset, float] = {}

class_combo_a = frozenset({"real", "fake"})
class_combo_b = frozenset({"real", "fake", "uncertain"})

cache[class_combo_a] = 0.941
cache[class_combo_b] = 0.928

lookup = frozenset({"fake", "real"})
print(f"Binary acc       : {cache[lookup]}")   # 0.941
print(f"Ternary acc      : {cache[class_combo_b]}")                  # 0.928

# ── What to notice ────────────────────────────────────────────────────────────
#
# 1. {} creates an empty dict, NOT an empty set. This is one of Python's
#    historical quirks — {} was dict syntax before sets existed.
#    Always use set() for an empty set.
#
# 2. Set operations use operators (|, &, -, ^) for inline use, or method
#    names (.union(), .intersection(), .difference(), .symmetric_difference())
#    for explicit named calls. Both do the same thing.
#
# 3. Membership testing in a set is O(1) — it computes a hash and checks
#    one bucket. In a list it's O(n) — it scans every element.
#    If you check membership in a hot loop, convert to a set first.
#
# 4. Sets are unordered — you can't index into them (set[0] raises TypeError).
#    If you need both uniqueness and order, keep a list + a set as seen above.
#
# 5. frozenset is to set what tuple is to list — immutable, hashable,
#    usable as dict keys or set elements. You'll encounter it when caching
#    results keyed by a variable collection of features or class names.