# 07 — Memory and Mutability | notes.md

> Fill this in after finishing the exercises.

---

## What clicked immediately



---

## What took time



---

## My questions — answered

---

### Q: Why does a = b not create a copy?

Because `=` in Python does not copy anything. It creates a new label
and points it at the same object that `b` already points to.

```python
config_a = {"lr": 0.001}
config_b = config_a     # config_b is a second label on the SAME dict

config_b["lr"] = 0.01   # mutates the dict — both labels see it
print(config_a["lr"])   # 0.01 — changed, even though we only "changed" config_b
```

Think of it as two sticky notes (`config_a` and `config_b`) stuck on the
same piece of paper (the dict object). Writing on the paper changes what
both sticky notes point to.

To actually copy: use `.copy()` for a flat structure, or `copy.deepcopy()`
for a nested one.

---

### Q: What is the difference between shallow and deep copy?

Both create a **new container**. The difference is what happens to the objects inside.

**Shallow copy** — new container, shared contents.

```python
import copy

base = {"tags": ["v1"], "lr": 0.001}
shallow = base.copy()

# Top-level key — independent (new dict, new key slot)
shallow["lr"] = 0.99
print(base["lr"])         # 0.001 — protected

# Nested list — SHARED (same list object)
shallow["tags"].append("v2")
print(base["tags"])       # ["v1", "v2"] — affected!
```

**Deep copy** — new container AND new copies of everything inside, recursively.

```python
deep = copy.deepcopy(base)
deep["tags"].append("v2")
print(base["tags"])       # ["v1"] — protected
```

Rule:
- Flat structure (dict of ints/strings/floats) → `.copy()` is fine
- Nested mutable structure (dict of lists/dicts) → use `copy.deepcopy()`

---

### Q: Why does += behave differently on lists vs ints?

Because `int` is immutable and `list` is mutable.

```python
# int — immutable — += creates a NEW object
n = 5
id_before = id(n)
n += 1
print(id(n) == id_before)   # False — new int object

# list — mutable — += mutates IN PLACE
lst = [1, 2]
id_before = id(lst)
lst += [3]                   # same as lst.extend([3])
print(id(lst) == id_before)  # True — same list object
```

This matters when you have an alias to a list:

```python
a = [1, 2]
b = a
a += [3]       # mutates in place — b sees the change
print(b)       # [1, 2, 3]

x = 5
y = x
x += 1         # creates new int — y unaffected
print(y)       # 5
```

---

### Q: When should I use is vs ==?

`is` checks **identity** — are both sides the same object in memory?
`==` checks **equality** — do both sides have the same value?

```python
a = [1, 2, 3]
b = [1, 2, 3]

a == b    # True  — same values
a is b    # False — different objects (two separate lists)

c = a
a is c    # True  — same object
```

**Use `is` only for:**
```python
x is None       # checking if something is None
x is not None   # checking if something is not None
x is True       # occasionally, when you specifically mean the bool True
```

**Never use `is` for:**
```python
x is "string"   # wrong — strings may or may not be interned
x is 5          # wrong — only reliable for small ints due to CPython cache
x is [1, 2]     # always False — new literal creates new object
```

The reason: `==` calls the object's `__eq__` method, which checks values.
`is` compares memory addresses — much more restrictive.

---

### Q: How does Python pass arguments to functions — by value or by reference?

Neither, exactly. Python passes **object references** by value.

- The function receives a reference to the same object the caller has.
- Mutating the object through that reference affects the caller's object.
- Reassigning the parameter (pointing it at a new object) does NOT affect the caller.

```python
def mutate(lst):
    lst.append(99)    # mutates the caller's list — visible externally

def reassign(lst):
    lst = [1, 2, 3]   # moves LOCAL label only — caller unchanged

data = [10, 20]
mutate(data)
print(data)    # [10, 20, 99] — mutated

reassign(data)
print(data)    # [10, 20, 99] — unchanged
```

Practical rule: if a function receives a mutable argument and you don't
want to modify the caller's object, copy it at the top:
```python
def safe_process(config):
    config = copy.deepcopy(config)   # work on a local copy
    ...
```

---

### Q: What does id() actually return?

`id(obj)` returns an integer that is unique to this object for its lifetime.
In CPython (the standard Python interpreter), it's the memory address of the object.

```python
a = [1, 2, 3]
print(id(a))       # something like 140234567890

b = a
print(id(a) == id(b))   # True — same address, same object

c = a[:]
print(id(a) == id(c))   # False — different address, different object
```

You rarely need `id()` in production code. Its main use is debugging aliasing
issues — comparing `id()` values proves whether two variables share an object.

---

## Connections to other topics

<!-- How does this connect to what you learned in other topics? -->
<!-- Example: "the mutable default argument bug in 05_functions is the same
     aliasing problem — the default list is created once and reused" -->



---

## Things to revisit later

- [ ] NumPy array views vs copies — `arr[:]` returns a VIEW in NumPy, not a copy — Phase 6
- [ ] `copy.copy()` vs `copy.deepcopy()` for custom class instances — Phase 2 OOP
- [ ] `__copy__` and `__deepcopy__` — customising copy behaviour for your own classes — Phase 2 OOP
- [ ] PyTorch `tensor.clone()` — the deepcopy equivalent for tensors — Phase 7
- [ ] Pydantic models — immutable-by-default config objects — Phase 5 typing

---

## One-line summary

> In one sentence: what is the aliasing bug, and how do you prevent it?

<!-- Your words here -->