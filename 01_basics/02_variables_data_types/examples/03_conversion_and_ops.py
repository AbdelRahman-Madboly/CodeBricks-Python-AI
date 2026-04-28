"""
examples/03_conversion_and_ops.py
──────────────────────────────────
Topic  : Variables and Data Types
Example: 3 of 3 — Type conversion, operators, and the float trap

Context
-------
In AI pipelines, data rarely arrives in the right type.
Config files give you strings. APIs give you strings.
CSV files give you strings. Everything is a string until
you convert it.

This example shows how to convert between types safely,
covers Python's operators (arithmetic, unary, binary),
and demonstrates the floating-point precision trap that
trips up every developer at least once.

Covers:
  - int(), float(), str(), bool() — type casting
  - The bool("False") trap
  - Arithmetic operators: + - * / // % **
  - Binary vs unary operators
  - Floating point precision and how to handle it
  - Python int vs C++ int — no overflow

Run this file. Predict each line's output before you see it.
"""

import math   # we'll use math.isclose() for float comparison

# ── Type conversion — casting ─────────────────────────────────────────────────

print("=== Type conversion ===")

# In real pipelines, everything from a file or API arrives as a string
raw_epochs    = "50"
raw_lr        = "0.0003"
raw_verbose   = "True"
raw_dropout   = "0.1"

# Cast to the correct types for use
epochs  = int(raw_epochs)
lr      = float(raw_lr)
dropout = float(raw_dropout)

# bool("True") DOES NOT work as you'd expect — DO NOT use it
# bool() on a non-empty string is ALWAYS True, even for "False"
print(f'bool("True")  = {bool("True")}')   # True  — expected
print(f'bool("False") = {bool("False")}')  # True  — NOT what you want!
print(f'bool("")      = {bool("")}')        # False — empty string is falsy

# Correct way to convert string "True"/"False" to bool:
verbose = raw_verbose == "True"   # True if raw is exactly "True"
print(f"verbose (correct) = {verbose}")

print(f"\nEpochs  : {epochs}  ({type(epochs).__name__})")
print(f"LR      : {lr}  ({type(lr).__name__})")
print(f"Dropout : {dropout}  ({type(dropout).__name__})")
print(f"Verbose : {verbose}  ({type(verbose).__name__})")

# ── Operators ─────────────────────────────────────────────────────────────────

print()
print("=== Arithmetic operators ===")

# All binary operators — they sit BETWEEN two operands
a, b = 10, 3

print(f"{a} + {b}  = {a + b}")     # 13   addition
print(f"{a} - {b}  = {a - b}")     # 7    subtraction
print(f"{a} * {b}  = {a * b}")     # 30   multiplication
print(f"{a} / {b}  = {a / b:.4f}") # 3.3333  division — ALWAYS float
print(f"{a} // {b} = {a // b}")    # 3    floor division — ALWAYS int (rounds down)
print(f"{a} % {b}  = {a % b}")     # 1    modulo (remainder after division)
print(f"{a} ** {b} = {a ** b}")    # 1000 exponentiation

# Unary operators — sit BEFORE one operand
x = 5
print(f"\nUnary -x  : {-x}")       # -5   negation
print(f"Unary not : {not True}")   # False logical NOT
print(f"Unary not : {not False}")  # True

# Real AI use — floor division for batch indexing
total_samples = 10_000
batch_size    = 32
num_batches   = total_samples // batch_size   # always a whole number
remainder     = total_samples % batch_size    # samples in last incomplete batch
print(f"\nTotal: {total_samples:,} | Batch: {batch_size}")
print(f"Full batches : {num_batches}")
print(f"Last batch   : {remainder} samples")

# ── The floating point trap ───────────────────────────────────────────────────

print()
print("=== Float precision trap ===")

# Floats are stored in binary — most decimals can't be represented exactly
result = 0.1 + 0.2
print(f"0.1 + 0.2       = {result}")          # 0.30000000000000004
print(f"0.1 + 0.2 == 0.3  → {result == 0.3}")  # False — TRAP

# Solution 1: round() for simple cases
print(f"round(result, 1) == 0.3  → {round(result, 1) == 0.3}")  # True

# Solution 2: math.isclose() for precise comparisons
print(f"math.isclose(result, 0.3)  → {math.isclose(result, 0.3)}")  # True

# In practice: never compare floats with ==
# Use round() or math.isclose() depending on the precision you need

# ── Python int vs C++ int — no size limit ─────────────────────────────────────

print()
print("=== Python int — unlimited size ===")

# C++ int: 32-bit, max ~2 billion. Overflow wraps or causes undefined behaviour.
# Python int: grows as needed — no overflow, ever.

googol = 10 ** 100
print(f"10^100 = {googol}")   # prints perfectly — no overflow

# 2 ** 256 is a common number in cryptography
big = 2 ** 256
print(f"2^256  = {big}")

# Practical note for AI:
# numpy and PyTorch use fixed-size types (int32, int64) inside arrays
# for performance. Python's unlimited int is for regular Python code.
print()
print(f"Max int32 (numpy) : {2**31 - 1:,}")   # 2,147,483,647
print(f"Max int64 (numpy) : {2**63 - 1:,}")   # 9,223,372,036,854,775,807
print("Python int        : no limit")

# ── What to notice ────────────────────────────────────────────────────────────
#
# 1. / always returns float, // always returns int
#    10 / 2 = 5.0 (float), 10 // 2 = 5 (int)
#    Use // for array indexing, loop ranges, and batch counting.
#
# 2. bool("False") is True — because "False" is a non-empty string.
#    Always convert booleans from strings with == "True", never with bool().
#
# 3. Float comparison with == will fail you.
#    Use round() for display, math.isclose() for logic.
#
# 4. Python int has no max size — but numpy/PyTorch use fixed sizes for speed.
#    Know which context you're in.
#
# 5. Unary operators (-, not) vs binary operators (+, -, *, /)
#    Unary: one operand — -x, not x
#    Binary: two operands — a + b, a * b
#    The minus sign is binary in "a - b" and unary in "-a".