# 08 — Lists | notes.md

> Fill this in after finishing the exercises.

---

## What clicked immediately



---

## What took time



---

## My questions — answered

---

### Q: What is the difference between a list and a range?

`range()` is a **lazy sequence** — it doesn't store all the numbers in memory.
It generates them one at a time as requested. It's an object that knows its
start, stop, and step, and produces values on demand.

```python
r = range(0, 1_000_000)   # instant — no memory used
r[500_000]                 # 500000 — O(1) calculation, not stored

lst = list(range(1_000_000))  # stores one million ints in memory
```

**When to use each:**
- Use `range()` in for loops when you just need the numbers: `for i in range(n)`
- Use `list(range(n))` only when you actually need a list object (to slice, append, etc.)

---

### Q: What is a list comprehension and when should I use a loop instead?

A comprehension is a compact syntax for building a list from another iterable:

```python
# These are equivalent:

# Loop version
result = []
for item in source:
    if condition(item):
        result.append(transform(item))

# Comprehension version
result = [transform(item) for item in source if condition(item)]
```

**Use a comprehension when:**
- The transformation is a single expression
- The filter is a single condition
- The result fits on one readable line (PEP 8 says under ~79 chars)

**Use a loop when:**
- The body has multiple statements
- You need to `break` or `continue`
- You need to accumulate side effects (logging, printing, updating counters)
- The logic is complex enough that the comprehension would require mental parsing

---

### Q: What is the difference between sort() and sorted()?

```python
lst = [3, 1, 4, 1, 5]

# sorted() — non-destructive, returns a NEW list
new = sorted(lst)
print(lst)   # [3, 1, 4, 1, 5] — unchanged
print(new)   # [1, 1, 3, 4, 5]

# .sort() — destructive, modifies IN PLACE, returns None
lst.sort()
print(lst)   # [1, 1, 3, 4, 5] — sorted
result = lst.sort()
print(result)  # None — common mistake: thinking it returns the sorted list
```

**Rule:** use `sorted()` when you need both the original and the sorted version.
Use `.sort()` when you only need the sorted version and don't need the original.

---

### Q: What does "shallow copy" mean and why does it matter?

A **shallow copy** creates a new list object, but the elements inside
are still references to the same objects as the original.

```python
original = [1, 2, 3]
copy = original[:]    # shallow copy — new list, same element values

copy.append(4)
print(original)   # [1, 2, 3] — unaffected, because integers are immutable
```

For flat lists of immutable items (ints, floats, strings), shallow copy is safe.

The problem is with **nested mutable objects:**

```python
original = [[1, 2], [3, 4]]
copy = original[:]   # new outer list, but SAME inner lists

copy[0].append(99)
print(original)   # [[1, 2, 99], [3, 4]] — original was modified!
```

The outer list is new, but the inner lists are shared.
To get truly independent copies of nested structures, use `copy.deepcopy()`.

In AI work this matters for image arrays, batch data, and weight matrices —
always be explicit about whether you're copying or aliasing.

---

### Q: What is the time complexity of common list operations?

| Operation | Complexity | Note |
|-----------|-----------|------|
| `lst[i]` | O(1) | Direct memory address |
| `len(lst)` | O(1) | Stored as a counter |
| `lst.append(x)` | O(1) amortized | Occasional resize is O(n) |
| `lst.pop()` | O(1) | Remove last |
| `lst.pop(0)` | O(n) | Shifts all elements |
| `lst.insert(0, x)` | O(n) | Shifts all elements |
| `x in lst` | O(n) | Linear scan |
| `lst.sort()` | O(n log n) | Timsort |
| `sorted(lst)` | O(n log n) | Returns new list |

**Practical impact:**
- Building a list with `append` is fast — use it freely
- `x in lst` in a hot loop is slow — convert to a set first if needed
- `pop(0)` in a queue is slow — use `collections.deque` for O(1) popleft

---

### Q: How does looping over a list work internally?

When Python runs `for item in lst`, it calls `iter(lst)` to get an iterator,
then repeatedly calls `next()` on it until `StopIteration` is raised.

```python
lst = [10, 20, 30]
it = iter(lst)
print(next(it))   # 10
print(next(it))   # 20
print(next(it))   # 30
# next(it)        # StopIteration
```

You don't normally write this — `for item in lst` handles it automatically.
But understanding it explains why you can iterate over any iterable (files,
generators, ranges) the same way. They all implement `__iter__` and `__next__`.

---

## Connections to other topics

<!-- How does this connect to what you learned in other topics? -->
<!-- Example: "list slicing is the same syntax I'll use with NumPy arrays" -->



---

## Things to revisit later

- [ ] `copy.deepcopy()` — deep copy for nested structures — Phase 4 stdlib
- [ ] `collections.deque` — O(1) append and popleft — Phase 4 stdlib
- [ ] `heapq.nlargest(k, lst)` — efficient top-k — Phase 4 stdlib
- [ ] NumPy array slicing — same syntax as list slicing but on n-dimensional arrays — Phase 6
- [ ] List comprehensions vs generator expressions — Phase 3 (Pythonic)
- [ ] `itertools.chain`, `zip_longest` — advanced iteration — Phase 4

---

## One-line summary

> In one sentence: what is a list in Python, and what makes it different
> from a tuple or a NumPy array?

<!-- Your words here -->