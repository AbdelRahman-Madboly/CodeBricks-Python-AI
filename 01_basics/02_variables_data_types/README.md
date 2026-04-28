# 02 — Variables and Data Types

> **How Python stores, labels, and thinks about information.**

---

## Why This Matters

Every piece of data your AI program works with lives in a variable.
A model's accuracy, a dataset's size, whether training is complete,
the path to a config file — all of it is stored and moved around
through variables.

Understanding *how* Python handles types — and where it differs
from languages like C++ — saves you from a whole class of bugs
that are subtle and frustrating to debug.

---

## What a Variable Actually Is

In Python, a variable is not a box that holds a value.
It's a **label that points to an object** in memory.

```python
accuracy = 0.94
```

This does three things:
1. Creates a `float` object with value `0.94` somewhere in memory
2. Creates a label called `accuracy`
3. Points that label at the object

```
accuracy ──► [ float: 0.94 ]
```

When you reassign:

```python
accuracy = 0.97
```

The label moves. The old object (`0.94`) still exists in memory
until Python's garbage collector cleans it up.

```
accuracy ──► [ float: 0.97 ]
             [ float: 0.94 ]  ← no label → will be collected
```

This is why Python variables behave differently from C++ variables —
in C++, a variable IS the memory location. In Python, it's just a name.

---

## Python's Core Types

| Type      | Example                  | In AI/ML                              |
|-----------|--------------------------|---------------------------------------|
| `int`     | `epochs = 10`            | counts, indices, batch sizes          |
| `float`   | `lr = 0.001`             | learning rates, loss, accuracy        |
| `bool`    | `is_training = True`     | flags, conditions, masks              |
| `str`     | `model = "bert-base"`    | names, paths, labels, prompts         |
| `None`    | `checkpoint = None`      | unset values, optional returns        |

---

## Dynamic Typing — What It Means

Python figures out the type from the value you assign.
You never write `int x = 5` like in C++ or Java.

```python
x = 5           # Python sees 5 → makes it an int
x = "five"      # Python sees "five" → makes it a str
x = 5.0         # Python sees 5.0 → makes it a float
```

The same name can point to different types at different times.
This is called **dynamic typing**.

**The practical rule:** don't change the type of a variable mid-script.
It's confusing to read and error-prone. If you need a different type,
make a new variable with a descriptive name:

```python
# Bad — same name, different type
threshold = "0.85"
threshold = float(threshold)

# Good — clear intention
raw_threshold = "0.85"
threshold = float(raw_threshold)
```

In Phase 5 you'll add type hints to enforce this at the tool level.

---

## Identifiers — The Rules for Naming

An **identifier** is the technical name for any name you give to a
variable, function, or class in your code.

Valid identifiers:
- Start with a letter or underscore: `model_name`, `_private`, `X`
- Contain only letters, digits, underscores: `layer_1`, `batch_size_v2`

Invalid:
- Start with a digit: `1model` → `SyntaxError`
- Contain spaces: `model name` → `SyntaxError`
- Use reserved keywords: `class`, `for`, `if`, `None`, `True`, `False`

Python convention (**PEP 8**):
- Variables and functions: `snake_case` → `learning_rate`, `load_data`
- Classes: `PascalCase` → `DataLoader`, `TransformerModel`
- Constants: `UPPER_CASE` → `MAX_EPOCHS`, `DEFAULT_LR`

---

## Type Inspection

```python
x = 42
print(type(x))           # <class 'int'>
print(type(x).__name__)  # int  — cleaner for display

# isinstance is better than type() in real code
# because it handles inheritance
print(isinstance(x, int))   # True
print(isinstance(True, int)) # True — bool IS a subclass of int
```

---

## Type Conversion (Casting)

Converting between types is called **casting**. You'll do this constantly
when reading data from files, APIs, or user input — everything comes in
as a string and needs to be converted.

```python
# string → number
int("42")       # 42
float("0.001")  # 0.001

# number → string
str(42)         # "42"

# to bool — careful here
bool(0)         # False
bool(1)         # True
bool("")        # False
bool("False")   # True  ← TRAP: any non-empty string is truthy
bool("0")       # True  ← another trap

# Safe bool conversion from string
"True" == "True"   # True
"False" == "True"  # False — this is the correct way
```

---

## Operators

**Arithmetic operators** (binary — take two operands):

```python
10 + 3    # 13   addition
10 - 3    # 7    subtraction
10 * 3    # 30   multiplication
10 / 3    # 3.333...  division — always returns float
10 // 3   # 3    floor division — always returns int
10 % 3    # 1    modulo (remainder)
10 ** 3   # 1000 exponentiation
```

**Unary operators** (take one operand):

```python
x = 5
-x         # -5   negation
+x         # 5    (rarely used)
not True   # False  logical negation
```

**Binary vs unary** — binary operators sit *between* two values
(`a + b`), unary operators sit *before* one value (`-x`, `not x`).

---

## Python int vs C++ int — The Key Difference

In C++, an `int` is typically 32 bits — it can hold values from
roughly -2 billion to +2 billion. Overflow is your problem.

In Python, `int` has **no fixed size**. It grows as needed:

```python
x = 10 ** 100   # a googol — no problem
print(x)        # Python handles it
```

Python integers use arbitrary precision arithmetic. They're slower
than C++ ints, but they never overflow. For AI work this rarely matters
because numpy and PyTorch use fixed-size types (int32, int64) for
performance inside arrays.

---

## Common Mistakes

**Floating point equality**
```python
0.1 + 0.2 == 0.3    # False — float representation error
round(0.1 + 0.2, 1) == 0.3  # True — use round() or math.isclose()
```

**Shadowing built-in names**
```python
list = [1, 2, 3]   # now 'list' the built-in is gone in this scope
list([4, 5])       # TypeError — you just broke it
```

**`bool("False")` is True**
```python
bool("False")   # True — "False" is a non-empty string
# Use string comparison instead:
"False" == "True"  # False — correct
```

**`None` comparison**
```python
result = None
result == None    # works but wrong style
result is None    # correct — use 'is' for None checks
```

---

## How to Work Through This Topic

1. Read this README — understand the label/object mental model first
2. Open each `examples/` file — predict the output before running
3. Attempt each `exercises/` file — don't open solutions yet
4. Check `solutions/` — read the "why" section, not just the answer
5. Fill in `notes.md` — your own words, not copied text

---

## Folder Structure

```
02_variables_data_types/
├── README.md          ← you are here
├── notes.md           ← fill in after exercises
├── test.py            ← run to verify understanding
│
├── examples/
│   ├── 01_types_and_inspection.py   — core types, type(), isinstance()
│   ├── 02_dynamic_typing.py         — labels, reassignment, the trap
│   └── 03_conversion_and_ops.py     — casting, operators, float precision
│
├── exercises/
│   ├── 01_model_config.py           — Easy: declare and inspect a model config
│   ├── 02_sensor_pipeline.py        — Medium: convert raw string data to correct types
│   └── 03_type_predictions.py       — Hard: predict behaviour before running
│
└── solutions/
    ├── 01_model_config.py
    ├── 02_sensor_pipeline.py
    └── 03_type_predictions.py
```

---

## Connection to the AI Journey

In every AI project you'll write:

```python
# Model config — all types at once
model_name    = "distilbert-base-uncased"   # str
max_length    = 512                          # int
learning_rate = 2e-5                         # float (scientific notation)
use_gpu       = True                         # bool
checkpoint    = None                         # NoneType — not loaded yet
```

Getting types wrong here causes crashes that are hard to trace.
Getting them right is the baseline for everything else.

---

*Next → [03 — Operators](../03_operators/)*