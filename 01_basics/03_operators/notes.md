# 03 — Operators | notes.md

> Fill this in after finishing the exercises.

---

## What clicked immediately



---

## What took time



---

## My questions — answered

---

### Q: What is the difference between / and // ?

`/` (true division) always returns a `float`, even when the result is whole:
```python
10 / 2    # 5.0  — float
10 / 3    # 3.3333...  — float
```

`//` (floor division) returns the floor of the result as an `int`:
```python
10 // 2   # 5   — int
10 // 3   # 3   — int (3.333 floored to 3)
-7 // 2   # -4  — floors toward negative infinity, not toward zero
```

**When to use each:**
- Use `/` when you need the exact decimal result
- Use `//` when you need a whole number — batch sizes, loop ranges, array indices

---

### Q: What does short-circuit evaluation mean?

Python's `and` and `or` stop evaluating as soon as the result is determined.

`and` stops at the first **falsy** value:
```python
False and expensive_call()   # expensive_call() is NEVER called
0 and "hello"                # returns 0, never evaluates "hello"
```

`or` stops at the first **truthy** value:
```python
True or expensive_call()    # expensive_call() is NEVER called
"hi" or "default"           # returns "hi", never evaluates "default"
```

This has two benefits:
1. **Performance** — skips unnecessary computation
2. **Safety** — prevents errors when the second operand depends on the first

```python
# Safe: items[0] is never accessed if items is empty
items and items[0].upper()
```

---

### Q: What do `and` and `or` actually return — is it always True or False?

No. They return one of their **operands**, not necessarily a bool.

`and` returns the **first falsy operand**, or the **last operand** if all are truthy:
```python
0 and "hi"       # 0       — stopped here (falsy)
"hi" and "bye"   # "bye"   — both truthy, returns last
```

`or` returns the **first truthy operand**, or the **last operand** if all are falsy:
```python
0 or "default"   # "default" — 0 is falsy
"hi" or "bye"    # "hi"      — truthy, returns first
0 or "" or None  # None      — all falsy, returns last
```

This powers the default-value pattern:
```python
lr = config.get("lr") or 1e-4   # if lr is 0 or None, use 1e-4
```

---

### Q: When should I use `is` vs `==`?

`==` compares **values** — use this for almost everything.
`is` compares **identity** — whether two names point to the exact same object.

```python
a = [1, 2, 3]
b = [1, 2, 3]
a == b    # True  — same values
a is b    # False — different objects in memory

a = b     # now both point to the same object
a is b    # True
```

**The rule:** use `is` only for `None`, `True`, `False`:
```python
result is None       # correct
result == None       # works but triggers linter warning
```

For everything else, use `==`.

---

### Q: What is binary and why does it matter for Python?

Binary (base 2) is how computers store everything. Each bit is 0 or 1.

```
Decimal:  8   4   2   1   (place values)
Binary:   1   1   0   1   = 8+4+0+1 = 13
```

In Python, write binary literals with `0b`:
```python
0b1101   # 13
0b1111   # 15
0b0001   # 1
```

**Why it matters:**
1. Understanding binary explains why floats have precision issues — they're stored in binary and most decimals can't be represented exactly
2. Permission flag systems use binary for compact storage (one int = many on/off flags)
3. NumPy and PyTorch use fixed-size binary types (int32, float32) for GPU performance

---

### Q: What does operator precedence mean?

When multiple operators appear, Python evaluates in a fixed order:

```
** (highest)  →  * / // %  →  + -  →  < > == !=  →  not  →  and  →  or (lowest)
```

```python
2 + 3 * 4     # 14  — * before +
2 ** 3 + 1    # 9   — ** before +
not True or False   # False — not before or
```

**Practical rule:** use parentheses whenever the order matters or isn't obvious.
Parentheses always take priority and make the intent explicit:

```python
result = (score >= 60) and (attempts <= 3)   # clear
result = score >= 60 and attempts <= 3        # also works, but harder to read fast
```

---

## Connections to other topics

<!-- How does this connect to Boot.dev or things you've seen before? -->



---

## Things to revisit later

- [ ] `__add__`, `__mul__` etc. — operator overloading in classes (Phase 2 OOP)
- [ ] `<<` and `>>` bitwise shift operators — rarely needed, Phase 4+
- [ ] `^` (XOR) bitwise operator — useful for toggle flags
- [ ] Augmented assignment with numpy arrays: `arr += 1` — Phase 6
- [ ] Walrus operator `:=` — assigns and returns a value in one expression — Phase 3

---

## One-line summary

> In one sentence: what do operators do, and which one trips up Python beginners most?

<!-- Your words here -->