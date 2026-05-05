# 08 — Lists

> **The workhorse data structure of Python.**

---

## Why This Matters

In AI/ML work, a list is the first thing you reach for:
a batch of images, a sequence of loss values, a pipeline of steps,
a collection of model predictions. Before NumPy arrays, before
DataFrames — everything starts as a list.

Understanding how lists are indexed, sliced, modified, and iterated
is not optional. It's the foundation every other data structure builds on.

---

## What a List Is

```python
losses = [0.92, 0.74, 0.58, 0.47, 0.39]
```

An ordered, mutable sequence. Order is preserved. Items can be changed.
Any mix of types is allowed (though in practice you keep them consistent).

```
index:   0      1      2      3      4
       ┌──────┬──────┬──────┬──────┬──────┐
       │ 0.92 │ 0.74 │ 0.58 │ 0.47 │ 0.39 │
       └──────┴──────┴──────┴──────┴──────┘
neg:    -5     -4     -3     -2     -1
```

- Positive indices count from the front, starting at 0
- Negative indices count from the back: `-1` is always the last item

---

## Indexing and Slicing

```python
stages = ["load", "preprocess", "train", "evaluate", "save"]

stages[0]      # "load"      — first item
stages[-1]     # "save"      — last item
stages[1:4]    # ["preprocess", "train", "evaluate"]  — stop is exclusive
stages[:3]     # ["load", "preprocess", "train"]      — from start
stages[2:]     # ["train", "evaluate", "save"]        — to end
stages[::2]    # ["load", "train", "save"]             — every 2nd item
stages[::-1]   # ["save", "evaluate", "train", "preprocess", "load"]  — reversed
```

**Slicing never raises an IndexError** — out-of-range slices are clipped silently.
**Indexing does raise IndexError** — `stages[10]` crashes if the list has fewer items.

---

## Modifying a List

```python
pipeline = ["load", "train", "save"]

pipeline.append("log")          # add to end         — O(1)
pipeline.insert(1, "validate")  # insert at index 1  — O(n)
pipeline.pop()                  # remove + return last item  — O(1)
pipeline.pop(0)                 # remove + return item at index 0  — O(n)
pipeline.remove("train")        # remove first occurrence by value  — O(n)
pipeline.extend(["deploy"])     # add all items from another iterable
pipeline.clear()                # remove all items
```

---

## Iterating

```python
losses = [0.9, 0.7, 0.5, 0.4]

# Basic iteration
for loss in losses:
    print(loss)

# With index — use enumerate, never a manual counter
for i, loss in enumerate(losses):
    print(f"Epoch {i+1}: {loss}")

# Two lists in parallel
predictions = [1, 0, 1, 1]
labels      = [1, 0, 0, 1]
for pred, label in zip(predictions, labels):
    print(pred == label)

# Accumulate a running total
total = 0
for loss in losses:
    total += loss
avg = total / len(losses)
```

---

## Useful Built-in Functions

```python
scores = [0.72, 0.91, 0.55, 0.88]

len(scores)          # 4      — number of items
sum(scores)          # 3.06   — total
min(scores)          # 0.55   — smallest
max(scores)          # 0.91   — largest
sorted(scores)       # [0.55, 0.72, 0.88, 0.91]  — new sorted list
sorted(scores, reverse=True)   # [0.91, 0.88, 0.72, 0.55]
scores.sort()        # sorts IN PLACE — modifies the original list
0.72 in scores       # True   — membership check: O(n)
scores.index(0.91)   # 1      — index of first occurrence
scores.count(0.72)   # 1      — how many times it appears
```

**`sorted()` vs `.sort()`**
- `sorted(lst)` — returns a new sorted list, original unchanged
- `lst.sort()` — sorts in place, returns `None`

Use `sorted()` when you need both the original and a sorted version.
Use `.sort()` when you only need the sorted version.

---

## List Comprehensions

A compact way to build a list from another iterable:

```python
# [expression for item in iterable if condition]

scores = [0.92, 0.45, 0.88, 0.31, 0.76]

# Filter
high = [s for s in scores if s >= 0.75]           # [0.92, 0.88, 0.76]

# Transform
pct = [f"{s:.0%}" for s in scores]                 # ['92%', '45%', ...]

# Filter + transform
high_pct = [f"{s:.0%}" for s in scores if s >= 0.75]

# From a range
squares = [i ** 2 for i in range(1, 6)]            # [1, 4, 9, 16, 25]

# From another list with index
indexed = [(i, s) for i, s in enumerate(scores)]
```

Comprehensions are faster than a manual `append` loop and more readable
once you're used to them. Use them for simple transformations and filters.
If the logic is complex, use a regular loop — readability wins.

---

## sort() with a key

```python
checkpoints = [
    ("epoch_05.pt", 0.82),
    ("epoch_15.pt", 0.91),
    ("epoch_10.pt", 0.88),
]

# Sort by accuracy — key= extracts the comparison value
best_first = sorted(checkpoints, key=lambda x: x[1], reverse=True)
# [("epoch_15.pt", 0.91), ("epoch_10.pt", 0.88), ("epoch_05.pt", 0.82)]
```

---

## Time Complexity — Matters for AI Work

| Operation | Time | Why it matters |
|-----------|------|---------------|
| `lst[i]` index | O(1) | Fast random access |
| `append` | O(1) amortized | Good for accumulating results |
| `insert(0, x)` | O(n) | Slow — shifts all elements |
| `pop()` (end) | O(1) | Fast removal |
| `pop(0)` (start) | O(n) | Use `collections.deque` for queues |
| `x in lst` | O(n) | Use a `set` if you do this often |
| `len(lst)` | O(1) | Stored, not counted |

When building large batches: `append` is fine. When checking membership
repeatedly: convert to a set. When you need fast insertion at the front:
use `collections.deque`.

---

## Common Mistakes

**Index out of range**
```python
lst = [1, 2, 3]
lst[3]    # IndexError — valid range is 0 to len-1 (0, 1, 2)
lst[-4]   # IndexError — valid negative range is -1 to -len (-1, -2, -3)
```

**`*` copies are shallow**
```python
rows = [[0]] * 3         # looks like 3 separate lists
rows[0].append(1)        # but they're all the SAME list
print(rows)              # [[0, 1], [0, 1], [0, 1]] — bug!

# Fix: use a comprehension
rows = [[0] for _ in range(3)]   # 3 genuinely separate lists
```

**Sorting mixed types crashes**
```python
[3, "two", 1].sort()   # TypeError — can't compare int and str
```

**Mutating while iterating**
```python
items = [1, 2, 3, 4]
for item in items:
    if item % 2 == 0:
        items.remove(item)   # skips items — bug!
# Use: items = [x for x in items if x % 2 != 0]
```

---

## Folder Structure

```
08_lists/
├── README.md
├── notes.md
├── test.py
│
├── examples/
│   ├── 01_indexing_and_slicing.py  — indices, slicing, negative indexing
│   ├── 02_methods_and_loops.py     — append, pop, sort, enumerate, zip
│   └── 03_comprehensions.py        — filter, transform, nested, key sorting
│
├── exercises/
│   ├── 01_pipeline_slicer.py       — Easy: slice and index a pipeline
│   ├── 02_detection_filter.py      — Medium: comprehensions on detections
│   └── 03_top_k.py                 — Hard: implement top-k without sort/max
│
└── solutions/
    ├── 01_pipeline_slicer.py
    ├── 02_detection_filter.py
    └── 03_top_k.py
```

---

## Connection to the AI Journey

```python
# Accumulate losses over an epoch
epoch_losses = []
for batch in dataloader:
    loss = model(batch)
    epoch_losses.append(loss.item())

avg_loss = sum(epoch_losses) / len(epoch_losses)

# Keep only the top predictions above a threshold
confident_preds = [p for p in predictions if p["score"] >= threshold]

# Sort checkpoints and load the best one
best = sorted(checkpoints, key=lambda c: c["val_loss"])[0]
```

---

*Previous → [04 — Control Flow](../04_control_flow/)*
*Next → [09 — Tuples](../09_tuples/)*