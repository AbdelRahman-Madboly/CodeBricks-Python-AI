# 07 — Memory and Mutability

> **Variables are labels. Objects live in memory. Two labels can point to the same object.**

---

## Why This Matters

The aliasing bug is one of the most common and hardest-to-trace bugs in Python.
You create what looks like a separate copy of a config, modify it for an experiment,
and silently corrupt the original. Your training run uses wrong hyperparameters.
Your data augmentation pipeline corrupts the original batch. A function you call
modifies data you didn't expect it to touch.

Understanding how Python stores objects in memory is the difference between
writing code that works and writing code that mostly works.

---

## The Mental Model — Labels, Not Boxes

Most languages teach you to think of variables as boxes that contain values.
Python is different. In Python:

- **Objects** live in memory. They have a type, a value, and an address.
- **Variables** are labels (references) attached to objects.
- Multiple labels can point to the same object.
- Reassigning a label moves it to a different object — it does NOT change the object.

```
           memory
           ┌─────────────┐
           │  {"lr":0.001}│  ← one dict object
           └─────────────┘
                 ▲  ▲
          config    alias     ← two labels, one object
```

---

## id() — Proving Identity

`id(obj)` returns the memory address of the object. If two variables have the
same `id()`, they are the same object — one thing with two labels.

```python
a = [1, 2, 3]
b = a
print(id(a) == id(b))   # True — same object

c = a[:]
print(id(a) == id(c))   # False — different objects, same content
```

---

## Mutable vs Immutable

**Immutable** — cannot be changed in place. "Changing" moves the label to a new object.

| Type | Example |
|------|---------|
| `int` | `x = 5` |
| `float` | `lr = 0.001` |
| `str` | `name = "ResNet"` |
| `tuple` | `shape = (224, 224)` |

**Mutable** — can be changed in place. All labels pointing to the object see the change.

| Type | Example |
|------|---------|
| `list` | `stages = ["load", "train"]` |
| `dict` | `config = {"lr": 0.001}` |
| `set` | `labels = {"real", "fake"}` |

---

## is vs ==

```python
a = [1, 2, 3]
b = [1, 2, 3]

a == b    # True  — same VALUE
a is b    # False — different OBJECTS

c = a
a is c    # True  — same OBJECT

# Correct use of is:
x is None       # checking for None
x is not None   # checking for not None

# Never use is for value comparison:
x is "string"   # wrong — use ==
x is 5          # wrong — use ==
```

---

## The Aliasing Bug

```python
base = {"lr": 0.001, "tags": ["v1"]}
experiment = base         # NOT a copy — same object

experiment["lr"] = 0.01   # mutates the shared object
print(base["lr"])         # 0.01 — bug! base was changed
```

---

## Shallow Copy

Creates a **new container** but the nested objects inside are still shared.

```python
base = {"lr": 0.001, "tags": ["v1"]}
copy = base.copy()         # new dict

copy["lr"] = 0.01          # only affects copy — protected
print(base["lr"])          # 0.001

copy["tags"].append("v2")  # mutates the SHARED inner list
print(base["tags"])        # ["v1", "v2"] — bug! still shared
```

**When shallow copy is safe:** flat structures with immutable values (strings, numbers, tuples).

**When shallow copy is NOT safe:** nested mutable objects (list of lists, dict of lists).

---

## Deep Copy

Creates a **fully independent copy** — recursively copies every nested object.

```python
import copy

base = {"lr": 0.001, "tags": ["v1"], "aug": {"flip": True}}
deep = copy.deepcopy(base)

deep["tags"].append("v2")
deep["aug"]["flip"] = False

print(base["tags"])          # ["v1"]  — protected
print(base["aug"]["flip"])   # True    — protected
```

**Rule of thumb:**
- Flat structure → `.copy()` or `[:]`
- Nested mutable structure → `copy.deepcopy()`

---

## += on Mutable vs Immutable

```python
# Immutable — creates a new object
n = 5
n += 1      # same as: n = n + 1 — new int object
# n is now a label on 6, not 5

# Mutable — mutates in place
lst = [1, 2]
alias = lst
lst += [3]  # same as: lst.extend([3]) — same list object
print(alias)   # [1, 2, 3] — alias sees the change
```

---

## Function Arguments

Python passes object **references** to functions — not copies.

```python
def add_tag(config, tag):
    config["tags"].append(tag)   # mutates the caller's dict

cfg = {"tags": ["v1"]}
add_tag(cfg, "v2")
print(cfg["tags"])   # ["v1", "v2"] — caller's dict was mutated
```

Reassigning the parameter inside the function does NOT affect the caller:

```python
def try_replace(config):
    config = {"lr": 99}   # moves local label — caller unchanged

cfg = {"lr": 0.001}
try_replace(cfg)
print(cfg)   # {"lr": 0.001} — unchanged
```

---

## Common Mistakes

**Aliasing instead of copying**
```python
exp = base_config          # alias — same object
exp = base_config.copy()   # shallow copy — new top-level dict
exp = copy.deepcopy(base_config)  # deep copy — fully independent
```

**Shallow copy on nested structures**
```python
copy = config.copy()
copy["nested_list"].append(x)  # still mutates the original's nested list
```

**Mutable default argument**
```python
def log(entry, history=[]):   # history shared across all calls — bug
def log(entry, history=None):  # correct
    if history is None:
        history = []
```

---

## Connection to the AI Journey

```python
# Safe config branching for hyperparameter search
import copy
base_config = {"lr": 0.001, "augment": {"flip": True}}
exp_configs = [copy.deepcopy(base_config) for _ in range(5)]

# NumPy arrays (Phase 6) — slicing returns a VIEW, not a copy
import numpy as np
arr = np.array([1, 2, 3])
view = arr[:]          # shares memory — modifying view modifies arr
arr_copy = arr.copy()  # independent — same mental model as Python lists

# PyTorch (Phase 7) — tensor.clone() is the deepcopy equivalent
tensor = torch.tensor([1.0, 2.0])
clone = tensor.clone()   # independent copy
```

---

## Folder Structure

```
07_memory_mutability/
├── README.md
├── notes.md
├── test.py
│
├── examples/
│   ├── 01_references_and_identity.py    — id(), labels, mutable vs immutable, is vs ==
│   ├── 02_aliasing_and_shallow_copy.py  — aliasing bug, .copy(), nested trap, functions
│   └── 03_deepcopy_and_augmented_assign.py — deepcopy, +=, practical patterns
│
├── exercises/
│   ├── 01_predict_the_output.py         — Easy: predict 6 aliasing/copy snippets
│   ├── 02_fix_the_aliasing_bugs.py      — Medium: fix 3 broken pipeline functions
│   └── 03_safe_experiment_manager.py    — Hard: design a class with copy discipline
│
└── solutions/
    ├── 01_predict_the_output.py
    ├── 02_fix_the_aliasing_bugs.py
    └── 03_safe_experiment_manager.py
```

---

*Previous → [06 — Classes and Objects](../06_classes_intro/)*
*Next → [13 — Modules and Packages](../13_modules_packages/)*