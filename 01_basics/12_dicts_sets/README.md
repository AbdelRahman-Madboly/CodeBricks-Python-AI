# 12 — Dictionaries and Sets

> **The two data structures that make lookup fast.**

---

## Why This Matters

Lists store sequences. Dicts and sets store relationships and memberships.
In AI/ML work, dicts are everywhere: model configs, training logs, metric
summaries, dataset registries, grouping results by class. Sets answer the
question "have I seen this before?" in O(1) — critical when processing
millions of frames or tokens.

If lists are how you store ordered data, dicts are how you name it,
and sets are how you deduplicate it.

---

## What a Dict Is

```python
config = {
    "model":  "EfficientNet-B4",
    "epochs": 50,
    "lr":     0.001,
}
```

An ordered mapping of unique keys to values. Keys must be immutable
(strings, numbers, tuples). Values can be anything. Lookups, inserts,
and deletes are O(1) on average — backed by a hash table.

```
key          value
───────────  ───────────────
"model"   →  "EfficientNet-B4"
"epochs"  →  50
"lr"      →  0.001
```

Unlike a list (indexed by position 0, 1, 2...), a dict is indexed by name.

---

## What a Set Is

```python
train_labels = {"real", "fake", "uncertain"}
```

An unordered collection of unique values. No keys, no positions.
Adding a duplicate is silently ignored. Membership testing is O(1).

---

## Dict Essentials

```python
d = {"a": 1, "b": 2}

# Access
d["a"]                    # 1 — KeyError if absent
d.get("c")                # None — safe, no error
d.get("c", 0)             # 0 — explicit default

# Membership
"a" in d                  # True — O(1)

# Add / update
d["c"] = 3                # insert or overwrite

# Delete
del d["b"]                # KeyError if absent
d.pop("b", None)          # safe — returns None if absent

# Iterate
for key in d:             # keys only
for key, val in d.items():   # key-value pairs
list(d.keys())            # list of keys
list(d.values())          # list of values

# Frequency counting — the most important pattern
counts = {}
for item in data:
    counts[item] = counts.get(item, 0) + 1

# Grouping — second most important pattern
groups = {}
for item in data:
    groups.setdefault(item["label"], []).append(item["score"])
```

---

## Set Essentials

```python
a = {"real", "fake", "uncertain"}
b = {"real", "fake", "compressed"}

# Operators
a | b   # union — all items in either
a & b   # intersection — items in both
a - b   # difference — in a but not b
a ^ b   # symmetric difference — in exactly one

# Mutation
a.add("blurry")       # no-op if already present
a.discard("blurry")   # no-op if absent (safe)
a.remove("blurry")    # KeyError if absent

# Create
empty = set()          # NOT {} — that's an empty dict
fs = frozenset(a)      # immutable set, usable as a dict key
```

---

## Common Mistakes

**KeyError on missing key**
```python
d = {"a": 1}
d["b"]           # KeyError — key doesn't exist
d.get("b", 0)    # 0 — use .get() for optional keys
```

**`{}` creates a dict, not a set**
```python
empty = {}        # dict — type(empty) is dict
empty = set()     # set  — type(empty) is set
```

**Modifying a dict while iterating**
```python
for key in d:
    del d[key]    # RuntimeError — can't change size during iteration
# Fix: iterate over a copy
for key in list(d.keys()):
    del d[key]
```

**Counting wrong — forgetting the default**
```python
counts[item] += 1              # KeyError on first occurrence
counts[item] = counts.get(item, 0) + 1   # correct
```

**Sets are unordered — don't index them**
```python
s = {"a", "b", "c"}
s[0]    # TypeError — sets have no index
```

---

## Time Complexity

| Operation | Dict | Set | List |
|-----------|------|-----|------|
| Lookup `d[k]` / `x in s` | O(1) | O(1) | O(n) |
| Insert | O(1) | O(1) | O(1) append |
| Delete | O(1) | O(1) | O(n) |
| Iteration | O(n) | O(n) | O(n) |

The O(1) operations are why you reach for a dict or set when you need
fast lookups — not because the syntax is nicer, but because the
performance is fundamentally better.

---

## Interview Angle

*"How would you count the frequency of each item in a list?"*
```python
counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1
# Or: from collections import Counter; counts = Counter(items)
```
Know both. The manual version shows you understand what Counter does.

*"How would you find duplicate IDs in a list?"*
```python
seen = set()
dupes = set()
for x in items:
    if x in seen:
        dupes.add(x)
    seen.add(x)
```

---

## Folder Structure

```
12_dicts_sets/
├── README.md
├── notes.md
├── test.py
│
├── examples/
│   ├── 01_dict_basics.py             — creation, access, .get(), .items(), add/delete
│   ├── 02_frequency_and_grouping.py  — counting, .setdefault(), dict comprehensions
│   └── 03_sets_and_operations.py     — sets, |&-^, dedup, frozenset
│
├── exercises/
│   ├── 01_model_leaderboard.py       — Easy: build, query, filter a dict
│   ├── 02_detection_grouper.py       — Medium: grouping, frequency, duplicate detection
│   └── 03_pipeline_validator.py      — Hard: set-based field validation
│
└── solutions/
    ├── 01_model_leaderboard.py
    ├── 02_detection_grouper.py
    └── 03_pipeline_validator.py
```

---

## Connection to the AI Journey

```python
# Model config — dict is how you pass hyperparameters
config = {"lr": 0.001, "epochs": 50, "batch_size": 32}
lr = config.get("lr", 0.01)   # safe default for optional params

# Class distribution — frequency counting before training
label_counts = {}
for label in dataset_labels:
    label_counts[label] = label_counts.get(label, 0) + 1

# Deduplication — remove seen frame IDs before processing
processed = set()
for frame in stream:
    if frame["id"] not in processed:
        processed.add(frame["id"])
        process(frame)

# Set operations — compare train vs val coverage
missing_from_val = set(train_classes) - set(val_classes)
```

---

*Previous → [08 — Lists](../08_lists/)*
*Next → [15 — Exceptions](../15_exceptions/)*