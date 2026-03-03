# Dictionaries and Sets

## Concept

**Dictionary** (`dict`): an unordered mapping of unique keys to values.
Lookups, insertions, and deletions are O(1) on average — backed by a hash table.
Use it whenever you need to associate a label with a value or look something up by name.

**Set** (`set`): an unordered collection of unique values.
Also O(1) for membership tests, add, and remove. Use it for deduplication
and set operations (union, intersection, difference).

## Mental Model

```
Dict — a labelled filing cabinet          Set — a bag that rejects duplicates
───────────────────────────────           ──────────────────────────────────
{ "model":  "ResNet",                     { "real", "fake", "uncertain" }
  "epochs": 30,          }
    │         │
   key      value        ← access by key, not by position
```

## Key Points

**Dict essentials:**
- `d[key]` — raises `KeyError` if missing; use `d.get(key, default)` for safety
- `d[key] = value` — insert or overwrite
- `key in d` — O(1) membership test
- `.keys()`, `.values()`, `.items()` — views (not copies)
- `d.setdefault(key, default)` — inserts default only if key is absent
- Dict comprehension: `{k: v for k, v in iterable}`

**Set essentials:**
- `set.add(x)`, `set.discard(x)` (no error if missing), `set.remove(x)` (raises if missing)
- `a | b` — union, `a & b` — intersection, `a - b` — difference, `a ^ b` — symmetric difference
- `frozenset` — immutable set, can be used as a dict key

## Common Mistakes

- Using `d[key]` when the key might be absent — use `.get()` defensively
- Modifying a dict while iterating over it — raises `RuntimeError`; iterate over `list(d.items())` instead
- Assuming sets are ordered — they are not; use a `list` if order matters
- `set([1, 2, 3])` creates a set; `{1, 2, 3}` also creates a set; but `{}` creates an empty **dict**, not a set — use `set()` for empty sets

## Interview Angle

*"How would you count the frequency of each item in a list?"*
```python
counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1
```
Or in one line with `collections.Counter(items)`.
Interviewers expect you to know both — the manual version shows you understand
what Counter is doing under the hood.
