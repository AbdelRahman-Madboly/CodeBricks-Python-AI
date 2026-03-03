# Operators

## Concept

Operators are symbols that tell Python to perform a computation or comparison
between values. Every operator maps to an underlying method on the object —
which is why you can later override them in custom classes.

Python operator groups:

| Group        | Operators                              |
|--------------|----------------------------------------|
| Arithmetic   | `+ - * / // % **`                     |
| Assignment   | `= += -= *= /= //= %= **=`            |
| Relational   | `== != > < >= <=`                     |
| Logical      | `and or not`                           |
| Membership   | `in not in`                            |
| Identity     | `is is not`                            |
| Bitwise      | `& \| ^ ~ << >>`                      |

## Mental Model

Operators are just shorthand for function calls. When you write `a + b`,
Python internally calls `a.__add__(b)`. This is why operator overloading
in OOP works — you define `__add__` on your class and suddenly `+` works
on your objects.

```
a + b       →   a.__add__(b)
a == b      →   a.__eq__(b)
a in seq    →   seq.__contains__(a)
```

## Key Points

- `/` always returns `float`: `10 / 2` → `5.0`
- `//` returns the floor (rounded down): `7 // 2` → `3`, `-7 // 2` → `-4`
- `%` returns the remainder: `7 % 3` → `1`
- `**` is exponentiation: `2 ** 8` → `256`
- `and` / `or` are **short-circuit** operators — they stop evaluating as soon
  as the result is determined and return the actual value, not just True/False
- `and` returns the first falsy value, or the last value if all are truthy
- `or` returns the first truthy value, or the last value if all are falsy

## Common Mistakes

- Integer division surprise: `5 / 2` returns `2.5` not `2` — use `//` when
  you need integer division
- Short-circuit misunderstanding: `0 or "default"` returns `"default"`, not `False`.
  This is used frequently as a default-value pattern in Python
- Operator precedence: `2 + 3 * 4` is `14`, not `20`. When in doubt, use parentheses

## Interview Angle

*"What does `x = x or default_value` do?"*
It assigns `default_value` to `x` if `x` is falsy (0, None, "", [], etc.).
This is a common Python idiom for setting defaults without an if-statement.
