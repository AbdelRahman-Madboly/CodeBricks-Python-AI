# Tuples

## Concept

A tuple is an ordered, **immutable** sequence of items. Once created, its
contents cannot be changed. This immutability is not a limitation — it is
a signal to the reader that this data is fixed and should not be modified.

Use a tuple when the structure has a fixed meaning:
a coordinate is always `(x, y)`, a color is always `(r, g, b)`,
a function returning two things is returning a tuple.

## Mental Model

```
List  → a collection you build and change over time  [item, item, item]
Tuple → a fixed record with a defined structure      (x, y, z)
```

If a list is a shopping cart (items come and go), a tuple is a GPS coordinate
(once you fix a location, those numbers mean something specific together).

## Key Points

- Created with parentheses: `point = (10, 20)` — or just commas: `point = 10, 20`
- A single-item tuple **requires** a trailing comma: `single = (42,)` — without
  the comma, `(42)` is just the integer 42 in parentheses
- **Unpacking**: `x, y = point` — assigns each element to a variable
- **Extended unpacking**: `first, *rest = (1, 2, 3, 4)` — `rest` gets `[2, 3, 4]`
- Tuples are hashable (if their contents are) — so they can be used as dict keys
  and added to sets, unlike lists
- Functions commonly return tuples to hand back multiple values

## Common Mistakes

- Forgetting the trailing comma on single-element tuples: `(42)` is an int,
  `(42,)` is a tuple
- Trying to modify a tuple element: `t[0] = 5` raises `TypeError`
- Confusing tuple unpacking count: `a, b = (1, 2, 3)` raises `ValueError` —
  the number of names must match the number of elements (unless using `*`)

## Interview Angle

*"When would you use a tuple instead of a list?"*
Three cases: (1) data that should not change — using a tuple enforces that
contract at the type level; (2) dict keys or set members — tuples are hashable,
lists are not; (3) returning multiple values from a function — the caller unpacks
naturally without needing a class.
