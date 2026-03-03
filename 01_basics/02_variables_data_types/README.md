# Variables and Data Types

## Concept

A variable is a name that points to a value stored in memory.
Python is **dynamically typed** — you never declare a type explicitly.
The interpreter figures out the type at runtime based on the value assigned.

Python's core built-in types:

| Type    | Example            | Use case                        |
|---------|--------------------|---------------------------------|
| `int`   | `42`               | Counts, indices, whole numbers  |
| `float` | `3.14`             | Measurements, probabilities     |
| `bool`  | `True / False`     | Flags, conditions               |
| `str`   | `"hello"`          | Text, labels, identifiers       |
| `None`  | `None`             | Absence of a value              |

## Mental Model

Think of a variable as a label on a sticky note that you attach to a box.
The box holds the actual value. You can move the label to a different box
at any time — that is dynamic typing.

```
x = 10        →   label "x" points to box containing 10
x = "hello"   →   label "x" now points to box containing "hello"
                  (the number 10 box still exists until garbage collected)
```

## Key Points

- `type(value)` returns the type of any value
- Python names are case-sensitive: `Score` and `score` are different variables
- `None` is its own type (`NoneType`) — it is not zero, not False, not an empty string
- Integer division `//` always returns an `int`; `/` always returns a `float`
- `bool` is a subclass of `int` in Python: `True == 1` and `False == 0`

## Common Mistakes

- Naming variables after built-ins: `list = [1, 2, 3]` shadows the built-in `list` type
  and causes confusing errors later in the same script
- Assuming `0.1 + 0.2 == 0.3` is `True` — floating point representation means
  it is actually `0.30000000000000004`. Use `round()` or `math.isclose()` for comparisons
- Treating `None` as `False` in comparisons — always use `is None`, never `== None`

## Interview Angle

Common question: *"What is the difference between `is` and `==`?"*
`==` compares values. `is` compares identity (whether two names point to the
same object in memory). Small integers (-5 to 256) are cached in CPython,
so `a = 5; b = 5; a is b` returns `True` — but this is an implementation
detail you should never rely on.
