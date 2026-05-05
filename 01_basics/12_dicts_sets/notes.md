# 12 — Dictionaries and Sets | notes.md

> Fill this in after finishing the exercises.

---

## What clicked immediately



---

## What took time



---

## My questions — answered

---

### Q: What is the difference between d[key] and d.get(key)?

`d[key]` raises a `KeyError` if the key is absent — the program crashes.
`d.get(key)` returns `None` if the key is absent — the program continues.
`d.get(key, default)` returns `default` instead of `None`.

```python
config = {"model": "ResNet", "epochs": 30}

# Crashes if "dropout" isn't in config
# lr = config["dropout"]   # KeyError

# Safe — returns None if absent
dropout = config.get("dropout")       # None

# Safe — returns your chosen default
dropout = config.get("dropout", 0.5)  # 0.5
```

**When to use each:**
- Use `d[key]` when you're certain the key exists — it's explicit about the contract.
- Use `.get()` for optional keys — config overrides, user-supplied params,
  any field that may or may not be present.

---

### Q: What is the canonical way to count item frequencies in a list?

```python
labels = ["real", "fake", "fake", "real", "uncertain", "fake"]

counts = {}
for label in labels:
    counts[label] = counts.get(label, 0) + 1

# {'real': 2, 'fake': 3, 'uncertain': 1}
```

Why `.get(label, 0) + 1`?
- First time "fake" appears: `.get("fake", 0)` returns 0 → sets it to 1.
- Second time: `.get("fake", 0)` returns 1 → sets it to 2.
- The default of 0 handles the "first encounter" without an if/in check.

The stdlib version is `collections.Counter(labels)` — same result, one import.
Knowing the manual version shows you understand what Counter does under the hood.

---

### Q: What does .setdefault() do and when should I use it?

`d.setdefault(key, default)` returns the value for `key` if it exists,
or inserts `default` and returns it if it doesn't.

The most common use: grouping items into lists.

```python
# Without setdefault — verbose
grouped = {}
for det in detections:
    label = det["label"]
    if label not in grouped:
        grouped[label] = []
    grouped[label].append(det["confidence"])

# With setdefault — same thing, one line per iteration
grouped = {}
for det in detections:
    grouped.setdefault(det["label"], []).append(det["confidence"])
```

Both are correct. `.setdefault()` is preferred in production because
it's shorter, has no repeated key lookup, and reads as one intent.

---

### Q: Why does {} create a dict and not a set?

Historical reason: dict literal syntax (`{}`) predates set literal syntax.
When sets were added in Python 2.4, `{}` was already reserved for dicts.
So Python uses `{1, 2, 3}` for non-empty set literals, but `{}` had to stay
as empty dict to avoid breaking existing code.

```python
type({})           # <class 'dict'>   — empty dict
type({1, 2, 3})    # <class 'set'>    — non-empty set literal
type(set())        # <class 'set'>    — empty set — always use this
```

This is one of Python's genuine historical warts. Just remember:
**empty set = `set()`**, never `{}`.

---

### Q: When should I use a set instead of a list?

Use a **set** when:
- You need fast membership testing (`x in s` — O(1) vs O(n) for list)
- You need uniqueness guaranteed automatically
- You want set operations: union, intersection, difference

Use a **list** when:
- Order matters
- You need to index by position (`lst[i]`)
- You need duplicates (e.g., keeping all predictions, not just unique ones)

```python
# Checking 100k processed IDs — set is instant, list is slow
processed = set(range(100_000))
99999 in processed      # O(1) — one hash lookup
99999 in list(processed)  # O(n) — scans up to 100k items
```

In AI work: use sets for seen-ID tracking, class name registries,
required-field validation. Use lists for ordered sequences of data.

---

### Q: What is the difference between set.discard() and set.remove()?

Both remove an element. The difference is what happens when it's absent:

```python
s = {"real", "fake"}

s.discard("blurry")   # element absent — no error, no change
s.remove("blurry")    # element absent — KeyError

s.discard("real")     # element present — removes it
s.remove("real")      # element present — removes it (same)
```

**Rule:** use `.discard()` when the element might not be there.
Use `.remove()` when you're certain it's there and want an error if it isn't
(i.e., when absence would indicate a bug in your code).

---

### Q: What is Python's ordering guarantee for dicts?

Since Python 3.7, dicts preserve **insertion order**. When you iterate
over a dict, items come out in the order they were first added.

```python
config = {}
config["lr"]     = 0.001
config["epochs"] = 50
config["model"]  = "ResNet"

for k in config:
    print(k)
# lr
# epochs
# model   ← always in this order
```

Before 3.7, dict order was undefined. If you're reading older Python code
or tutorials, you may see `collections.OrderedDict` — that was the
pre-3.7 way to guarantee order. In modern Python (3.7+) it's unnecessary.

---

## Connections to other topics

<!-- How does this connect to what you learned in other topics? -->
<!-- Example: "frequency counting with dicts is the same pattern I'll use
     with pandas groupby — just lower level" -->



---

## Things to revisit later

- [ ] `collections.Counter` — optimised frequency counter — Phase 4 stdlib
- [ ] `collections.defaultdict` — auto-initialises missing keys — Phase 4 stdlib
- [ ] `collections.OrderedDict` — for pre-3.7 compatibility or explicit order control — Phase 4 stdlib
- [ ] Dict comprehensions with conditional values (`{k: f(v) if cond else g(v) for ...}`) — Phase 3 Pythonic
- [ ] `TypedDict` — type-safe dicts with known keys — Phase 5 typing
- [ ] Hash tables — why dict/set operations are O(1) — CS fundamentals

---

## One-line summary

> In one sentence: when would you use a dict vs a set vs a list?

<!-- Your words here -->