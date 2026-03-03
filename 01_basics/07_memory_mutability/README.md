# Memory and Mutability

## Concept

Every value in Python lives in memory as an **object**. A variable is not a
container — it is a **reference** (a label) that points to an object.

**Mutability** describes whether an object's value can change after creation:
- **Mutable** objects can be modified in place: `list`, `dict`, `set`, custom classes
- **Immutable** objects cannot be changed: `int`, `float`, `str`, `tuple`, `bool`, `None`

## Mental Model

```
Mutable (list)                    Immutable (int)
──────────────                    ───────────────
a = [1, 2, 3]                     x = 10
b = a          ← same object      y = x

a.append(4)                       x = 20          ← new object, old 10 unchanged

print(b)  →  [1, 2, 3, 4]        print(y)  →  10
             b sees the change!              y still points to 10
```

When you assign a mutable object to another variable, both names point to the
**same object**. Modifying through either name affects both.

## Key Points

- `id(obj)` returns the memory address of an object — use it to check identity
- `is` compares identity (same object?); `==` compares value (same content?)
- To copy a list safely: `copy = original[:]` or `copy = list(original)`
- For nested structures, use `import copy; copy.deepcopy(obj)` — shallow copy
  only copies the outer container, inner objects are still shared
- Strings are immutable — every "modification" creates a new string object
- Function arguments receive references — mutating a list inside a function
  affects the caller's list; reassigning the parameter does not

## Common Mistakes

- Aliasing a list and mutating it: `b = a; b.append(x)` changes `a` too
- Thinking `+=` on a list is the same as `+`: `a += [4]` mutates `a` in place;
  `a = a + [4]` creates a new list
- Shallow copy surprise: `copy = original[:]` copies the outer list but inner
  lists are still shared references

## Interview Angle

*"What is the difference between shallow copy and deep copy?"*
Shallow copy creates a new container but the elements inside still point to
the same objects. Deep copy recursively creates new objects for everything.
This matters whenever you have nested mutable structures like a list of lists.
