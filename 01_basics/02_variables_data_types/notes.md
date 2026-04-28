# 02 — Variables and Data Types | notes.md

> Fill this in after finishing the exercises.
> Write in your own words — if you can explain it clearly here,
> you understand it. If you're copying, you don't yet.

---

## What clicked immediately

<!-- What felt obvious or natural right away? -->



---

## What took time

<!-- What confused you? How did you get past it? -->



---

## My questions — answered

These came up while working through this topic.

---

### Q: How does Python assign a variable without declaring a type?

In C++ you write: `int x = 5;` — you tell the compiler the type upfront,
and it allocates the right amount of memory before running.

Python works differently. When you write `x = 5`, Python:
1. Evaluates the right side: sees `5`, creates an `int` object in memory
2. Creates a name `x` in the current **namespace** (a dictionary of names)
3. Points `x` at that object

The type lives with the **object**, not the name. The name is just a label.
This is why the same name can point to different types — the label moves,
but each object always knows its own type.

```python
x = 5        # name 'x' → int object (5)
x = "hello"  # name 'x' → str object ("hello")
             # the int object (5) still exists until garbage collected
```

Under the hood, every Python object stores three things:
- Its type (what kind of thing it is)
- Its reference count (how many names point to it)
- Its value

---

### Q: What is the max size of an int in Python vs C++?

**C++ int:**
- Usually 32 bits (depends on the platform)
- Range: -2,147,483,648 to 2,147,483,647
- If you go over: overflow → undefined behaviour or wrapping

```cpp
int x = 2147483647;
x = x + 1;   // undefined behaviour — might wrap to -2147483648
```

**Python int:**
- No fixed size — grows as needed
- Uses arbitrary precision arithmetic (GMP library internally)
- No overflow, ever — just uses more memory

```python
x = 10 ** 1000   # a 1 followed by 1000 zeros — Python handles it
```

**In practice for AI:**
NumPy and PyTorch use fixed-size integers inside arrays (int32, int64)
for performance — the GPU needs to know the exact memory layout.
Python's unlimited int is only for regular Python code outside of arrays.

```python
# Python int — unlimited
samples = 10 ** 12    # fine

# NumPy — fixed size, but fast
import numpy as np
arr = np.array([1, 2, 3], dtype=np.int32)   # 32-bit, max ~2 billion
```

---

### Q: What is an identifier?

An identifier is the technical term for any name you create in Python:
a variable name, a function name, a class name, a module name.

Rules Python enforces (break these → `SyntaxError`):
- Must start with a letter (a–z, A–Z) or underscore `_`
- Can contain letters, digits (0–9), and underscores
- Cannot be a reserved keyword (`if`, `for`, `class`, `None`, `True`, `False`…)
- Case-sensitive: `Model` and `model` are different identifiers

```python
model_name = "bert"     # valid
_private   = True       # valid — underscore prefix = convention for "internal"
Layer1     = "conv"     # valid — but PascalCase is for classes, not variables

2model = "bad"          # SyntaxError — starts with digit
model name = "bad"      # SyntaxError — spaces not allowed
class = "bad"           # SyntaxError — reserved keyword
```

Python convention (PEP 8 — the style guide everyone follows):
- Variables and functions: `snake_case` → `learning_rate`, `load_dataset`
- Classes: `PascalCase` → `TransformerModel`, `DataLoader`
- Constants: `UPPER_SNAKE_CASE` → `MAX_EPOCHS`, `DEFAULT_BATCH_SIZE`

---

### Q: What are the steps to code review your own code?

Code review is the process of reading code — yours or someone else's —
to find bugs, improve clarity, and catch bad patterns before they cause problems.

When reviewing your own code, go through these steps in order:

**1. Does it run?**
Run it. Fix any crashes before anything else.

**2. Does it produce the correct output?**
Check every case — not just the happy path. What happens with edge cases?

**3. Are the names clear?**
Read each variable name out loud. Does it tell you what the value is
without looking at where it was assigned?
- Bad: `x`, `temp`, `data`, `val`
- Good: `learning_rate`, `validation_accuracy`, `raw_input_str`

**4. Is there unnecessary repetition?**
If you see the same code block twice, it should probably be a function.
(You'll apply this properly in topic 05 — Functions.)

**5. Are the types correct?**
For this topic: check that every variable holds the type you intended.
Add a quick `print(type(x))` if unsure, then remove it.

**6. Are comments explaining *why*, not *what*?**
```python
# Bad comment — the code already shows what happens
x = x + 1   # add 1 to x

# Good comment — explains why
epoch += 1   # increment before logging so output shows 1-indexed epochs
```

**7. Would someone else understand this in 6 months?**
Including yourself. If the answer is no, rename or add a comment.

---

### Q: What is code readability and why does it matter?

Readability is how easily a human can read and understand code.
Computers don't care — they'll run badly named, weirdly formatted code
just fine. Readability is entirely for humans.

It matters because:
- You will read your own code far more than you write it
- Bugs are harder to spot in unreadable code
- Other people (teammates, future you) have to maintain it

Practical rules for this topic:

```python
# 1. Use descriptive names
lr = 0.001              # what is lr?
learning_rate = 0.001   # clear

# 2. Use underscores in large numbers
samples = 10000000      # how many zeros is that?
samples = 10_000_000    # 10 million — obvious

# 3. One idea per line
x = 5; y = 10          # works but hard to read
x = 5                   # better
y = 10

# 4. Constants in UPPER_CASE to signal they shouldn't change
max_epochs = 100         # looks like a variable
MAX_EPOCHS = 100         # clearly a constant

# 5. Group related variables together
# Model hyperparameters
learning_rate = 0.001
batch_size    = 32
max_epochs    = 50

# Dataset settings
train_split   = 0.8
val_split     = 0.1
test_split    = 0.1
```

The official Python style guide is **PEP 8**. Tools like `ruff` (Phase 5)
enforce it automatically.

---

### Q: What are the common built-in functions for this topic?

Built-in functions are functions Python provides without any import:

```python
# Type inspection
type(x)           # returns the type object: <class 'int'>
isinstance(x, t)  # True/False — is x an instance of type t?

# Type conversion (casting)
int("42")         # → 42
float("3.14")     # → 3.14
str(42)           # → "42"
bool(1)           # → True

# Numeric utilities
abs(-5)           # → 5    absolute value
round(3.7)        # → 4    round to nearest int
round(3.141, 2)   # → 3.14 round to 2 decimal places
pow(2, 8)         # → 256  same as 2 ** 8

# Identity and id
id(x)             # integer memory address of the object x points to

# Others you'll use soon
print()           # output (topic 01)
len()             # length of a sequence (topic 08 — lists)
range()           # sequence of numbers (topic 04 — control flow)
input()           # read string from user (topic 05 — functions)
```

---

### Q: How do type conversions (casting) work?

Casting = telling Python to convert a value from one type to another.

```python
# Numeric casts
int(3.9)        # → 3      truncates (does NOT round)
int("42")       # → 42     parses string as integer
int("3.14")     # → ValueError — can't convert float-string directly
int(float("3.14"))  # → 3  convert to float first, then truncate

float(5)        # → 5.0    int to float
float("3.14")   # → 3.14   string to float

# To string
str(42)         # → "42"
str(3.14)       # → "3.14"
str(True)       # → "True"
str(None)       # → "None"   (the string, not None)

# To bool — the rules
bool(0)         # False
bool(0.0)       # False
bool("")        # False
bool([])        # False  (empty list)
bool(None)      # False
# Everything else is True:
bool(1)         # True
bool(-1)        # True
bool("False")   # True  ← non-empty string = truthy
bool([0])       # True  ← non-empty list = truthy
```

The general rule for bool: **zero, empty, and None are False.
Everything else is True.**

---

### Q: What are binary and unary operators?

**Arity** = how many operands an operator takes.

**Unary operators** — take ONE operand:
```python
-x        # arithmetic negation
+x        # positive (rarely used)
not x     # logical NOT — flips True/False
~x        # bitwise NOT (advanced — Phase 4+)
```

**Binary operators** — take TWO operands (one on each side):
```python
# Arithmetic
a + b     # addition
a - b     # subtraction
a * b     # multiplication
a / b     # true division (always float)
a // b    # floor division (always int)
a % b     # modulo (remainder)
a ** b    # exponentiation

# Comparison (return bool)
a == b    # equal value
a != b    # not equal
a < b     # less than
a > b     # greater than
a <= b    # less than or equal
a >= b    # greater than or equal

# Identity / membership
a is b    # same object in memory
a is not b
a in b    # b contains a (strings, lists — topic 08+)
```

Note: `-` is binary in `a - b` (subtraction) and unary in `-a` (negation).
Same symbol, different arity — context determines which one Python uses.

---

## Connections to other topics

<!-- How does this connect to Boot.dev or things you already know? -->
<!-- Example: "dynamic typing reminded me of JavaScript's var" -->



---

## Things to revisit later

- [ ] Type hints (`lr: float = 0.001`) — formally covered in Phase 5
- [ ] `math.isclose()` for float comparison — mentioned in example 3
- [ ] CPython integer caching — implementation detail, don't rely on it
- [ ] `__name__` attribute on type objects — shows up again in classes (topic 06)
- [ ] Ternary expression (`x if condition else y`) — covered in topic 04
- [ ] Namespaces — how Python stores variable names — covered in Phase 2 OOP

---

## One-line summary

> In one sentence: what is a variable in Python and how is it different from C++?

<!-- Write it here — your own words -->