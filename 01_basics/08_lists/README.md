# Lists

## Concept

A list is an ordered, mutable sequence of items. It is Python's most-used
data structure for storing collections where order matters and items may need
to be added, removed, or changed.

Lists can hold any mix of types, including other lists.

## Mental Model

Think of a list as a numbered row of slots:

```
index:    0        1        2        3
        ┌──────┬────────┬────────┬────────┐
items:  │"load"│"infer" │"save"  │"log"   │
        └──────┴────────┴────────┴────────┘
neg idx:  -4       -3       -2       -1
```

Positive indices count from the front (0-based).
Negative indices count from the back (-1 is always the last item).

## Key Points

- `append(x)` — add to the end: O(1)
- `insert(i, x)` — insert at position i: O(n)
- `pop()` — remove and return the last item: O(1)
- `pop(i)` — remove and return item at index i: O(n)
- `remove(x)` — remove the first occurrence of x: O(n)
- `sort()` — sort in place; `sorted(lst)` returns a new sorted list
- `len(lst)` — number of items
- Slicing: `lst[start:stop:step]` — returns a new list; stop is exclusive
- List comprehension: `[expr for item in iterable if condition]`

## Common Mistakes

- Index out of range: accessing `lst[len(lst)]` raises `IndexError` —
  valid indices are `0` to `len(lst) - 1`
- Using `remove()` on a value that doesn't exist raises `ValueError` —
  check with `if x in lst` first
- Sorting a list of mixed types raises `TypeError` in Python 3 —
  all items must be comparable
- `lst * n` repeats the list shallowly — `[[]] * 3` gives three references
  to the **same** inner list

## Interview Angle

*"What is the time complexity of list operations?"*
- `append`, `pop()` (end): O(1) amortized
- `insert`, `pop(i)` (middle): O(n) — all following elements shift
- `in` operator on a list: O(n) — use a set when you need O(1) lookup
