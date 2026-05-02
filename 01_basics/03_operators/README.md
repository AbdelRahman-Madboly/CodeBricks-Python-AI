# 03 — Operators

> **The vocabulary of computation.**

---

## Why This Matters

Operators are how you express every calculation, every comparison,
and every condition in Python. Every training loop, every threshold
check, every batch size calculation — they all run on operators.

Before you write your first `if` statement or your first loop,
you need to know what Python can compute and how it evaluates it.

---

## Operator Groups

| Group | Operators | What they do |
|-------|-----------|--------------|
| Arithmetic | `+ - * / // % **` | Math |
| In-place assignment | `+= -= *= /= //= %=` | Update a variable |
| Comparison | `== != > < >= <=` | Compare — always returns `bool` |
| Logical | `and or not` | Combine boolean expressions |
| Membership | `in not in` | Check if value is in a collection |
| Identity | `is is not` | Check if two names point to the same object |
| Bitwise | `& \| ^ ~ << >>` | Operate on binary representations |

---

## Arithmetic — The Details That Catch People

```python
# / always returns float — even when the result is whole
10 / 2       # 5.0  not 5

# // floor division — rounds DOWN toward negative infinity
7 // 2       # 3
-7 // 2      # -4  (not -3 — it floors, not truncates)

# % modulo — remainder after floor division
7 % 3        # 1
10 % 32      # 10  (when dividend < divisor)

# ** exponentiation
2 ** 10      # 1024
1e-3         # 0.001  scientific notation — same as 0.001
2e-5         # 0.00002  common for learning rates in ML
```

**AI/ML use of floor division and modulo:**
```python
total_samples = 10_000
batch_size    = 32

full_batches = total_samples // batch_size   # 312  — how many complete batches
remainder    = total_samples % batch_size    # 16   — samples in the last batch
```

---

## In-Place Assignment Operators

```python
loss = 1.0
loss -= 0.1    # same as: loss = loss - 0.1
loss *= 0.9    # same as: loss = loss * 0.9

epoch = 0
epoch += 1     # same as: epoch = epoch + 1
```

Note: Python has no `++` or `--` operators. Always use `+= 1`.

---

## Logical Operators — Short-Circuit Evaluation

`and` and `or` don't just return `True`/`False`. They return one of their
operands — whichever one determined the result.

```python
# 'and' returns the first FALSY value, or the last value if all are truthy
0 and "hello"      # 0       — first falsy value
"hi" and "hello"   # "hello" — both truthy, returns last

# 'or' returns the first TRUTHY value, or the last value if all are falsy
0 or "default"     # "default" — first truthy value
"" or 0 or None    # None     — all falsy, returns last

# This powers a common Python idiom for safe defaults:
raw_lr = 0          # falsy — came from a bad config
lr = raw_lr or 1e-3 # lr = 1e-3 — falls back to default
```

**Short-circuit** means Python stops evaluating as soon as the result
is determined:
```python
# If the first condition is False, 'and' never evaluates the second
is_valid and expensive_operation()   # expensive_operation skipped if is_valid is False

# If the first condition is True, 'or' never evaluates the second
has_cache or load_from_disk()        # load_from_disk skipped if has_cache is True
```

---

## Comparison Operators

All comparison operators return a `bool`:

```python
confidence = 0.87

confidence > 0.90    # False
confidence >= 0.85   # True
confidence == 0.87   # True
confidence != 1.0    # True

# Chaining — Python supports this, most languages don't
0.0 <= confidence <= 1.0   # True — is it a valid probability?
```

---

## Membership and Identity

```python
# 'in' — checks if a value exists in a collection
"bert" in ["bert", "gpt2", "t5"]   # True
"yolo" not in ["bert", "gpt2"]     # True

# Works on strings too
"train" in "train_loss"            # True

# 'is' — checks if two names point to the SAME OBJECT in memory
# Only use 'is' for None, True, False — not for values
result = None
result is None       # True  — correct
result == None       # True  — works but wrong style

# Never use 'is' to compare numbers or strings
a = 1000
b = 1000
a is b    # False — separate objects (outside CPython's small int cache)
a == b    # True  — same value, correct comparison
```

---

## Binary and Bitwise Operators

Python can represent integers in binary using the `0b` prefix:

```python
print(0b0101)   # 5
print(0b1000)   # 8
```

Bitwise operators work column by column on the binary representation:

```python
# & (AND) — 1 only where BOTH bits are 1
0b0101 & 0b0011   # 0b0001 = 1

# | (OR) — 1 where EITHER bit is 1
0b0101 | 0b0011   # 0b0111 = 7
```

**Real use case — permission flags:**
```python
CAN_READ    = 0b0001
CAN_WRITE   = 0b0010
CAN_EXECUTE = 0b0100

user_perms = 0b0011   # read + write

has_read  = user_perms & CAN_READ    # 0b0001 — truthy: has permission
has_exec  = user_perms & CAN_EXECUTE # 0b0000 — falsy: no permission

# Grant execute permission
user_perms = user_perms | CAN_EXECUTE   # 0b0111
```

---

## Operator Precedence

When multiple operators appear in one expression, Python evaluates
them in this order (higher = evaluated first):

```
1. **          (exponentiation)
2. + - (unary) (negation)
3. * / // %    (multiply, divide)
4. + -         (add, subtract)
5. < > <= >= == !=  (comparison)
6. not         (logical not)
7. and         (logical and)
8. or          (logical or)
```

**When in doubt — use parentheses:**
```python
# Ambiguous without parens
result = 2 + 3 * 4        # 14 — not 20

# Clear with parens
result = (2 + 3) * 4      # 20

# Good habit for complex conditions
passes = (score >= 60) and (attempts <= 3) or override
# vs
passes = score >= 60 and attempts <= 3 or override  # reads poorly
```

---

## Common Mistakes

**Using `is` for value comparison**
```python
a = 256; b = 256
a is b    # True  — CPython caches small ints, but DON'T rely on this

a = 1000; b = 1000
a is b    # False — outside cache range
# Always use == for value comparison
```

**Forgetting that `/` returns float**
```python
# This is wrong for batch index calculation
batch_index = total / batch_size   # 312.5 — float, can't use as index
# This is right
batch_index = total // batch_size  # 312 — int, safe to use
```

**Logical operator trap with 0 and empty containers**
```python
count = 0
result = count or "no data"   # "no data" — 0 is falsy, this may be intended
# But if count=0 is a valid meaningful value, don't use 'or' for defaults
# Use: result = count if count is not None else "no data"
```

---

## Folder Structure

```
03_operators/
├── README.md          ← you are here
├── notes.md           ← fill in after exercises
├── test.py            ← run to verify understanding
│
├── examples/
│   ├── 01_arithmetic.py        — floor div, modulo, exponents, scientific notation
│   ├── 02_logical_and_compare.py — short-circuit, comparison chains, defaults
│   └── 03_bitwise.py           — binary representation, &, |, permission flags
│
├── exercises/
│   ├── 01_batch_calculator.py  — Easy: arithmetic on dataset stats
│   ├── 02_qc_filter.py         — Medium: logical conditions, comparison chains
│   └── 03_permissions.py       — Hard: bitwise flags + short-circuit defaults
│
└── solutions/
    ├── 01_batch_calculator.py
    ├── 02_qc_filter.py
    └── 03_permissions.py
```

---

## Connection to the AI Journey

In every training script you'll write something like:

```python
# Floor division for batch counting
n_batches = len(dataset) // batch_size

# Modulo for logging every N steps
if step % log_every == 0:
    print(f"Step {step} | loss: {loss:.4f}")

# Short-circuit for safe defaults
lr = config.get("lr") or 1e-4

# Comparison chain for valid probability
assert 0.0 <= dropout <= 1.0, "dropout must be in [0, 1]"

# Bitwise for feature flags in production ML systems
if model_flags & FEATURE_ATTENTION:
    output = attention_layer(output)
```

Every operator here is in active use.

---

*Previous → [02 — Variables and Data Types](../02_variables_data_types/)*
*Next → [04 — Control Flow](../04_control_flow/)*