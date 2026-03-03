# Functions

## Concept

A function is a named, reusable block of code that takes inputs (parameters),
performs work, and optionally returns a value. Functions are the primary tool
for avoiding repetition and breaking a program into testable units.

In Python, functions are **first-class objects** — they can be stored in variables,
passed as arguments, and returned from other functions.

## Mental Model

Think of a function as a machine with an input slot and an output slot:

```
         parameters
              │
    ┌─────────▼──────────┐
    │   function body    │
    │   (does the work)  │
    └─────────┬──────────┘
              │
           return value
```

When you call a function, Python creates a new local scope (a temporary workspace).
Everything created inside that workspace disappears when the function returns.

## Key Points

- Parameters are the names in the definition; arguments are the values you pass in
- `return` sends a value back and exits the function immediately
- A function without `return` (or with bare `return`) returns `None`
- **Default parameters** let you make arguments optional: `def func(x, retries=3)`
- **`*args`** collects extra positional arguments into a tuple
- **`**kwargs`** collects extra keyword arguments into a dict
- **Keyword arguments** can be passed in any order: `func(retries=5, url="...")`
- Type hints annotate expected types but are not enforced at runtime: `def f(x: int) -> str`

## Common Mistakes

- Mutable default arguments: `def func(items=[])` — the list is created ONCE
  and shared across all calls. Use `None` and create the list inside the function
- Forgetting `return` — the function silently returns `None` and callers get
  confused when they try to use the result
- Modifying a mutable argument (list, dict) inside a function changes the caller's
  object — Python passes object references, not copies

## Interview Angle

*"What is the mutable default argument trap?"*
```python
def append_item(item, items=[]):  # BAD — list is shared across calls
    items.append(item)
    return items

def append_item(item, items=None):  # GOOD
    if items is None:
        items = []
    items.append(item)
    return items
```
This comes up frequently in Python interviews and catches many candidates.
