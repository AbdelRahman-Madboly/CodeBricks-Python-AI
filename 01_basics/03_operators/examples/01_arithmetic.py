"""
examples/01_arithmetic.py
──────────────────────────
Topic  : Operators
Example: 1 of 3 — Arithmetic operators

Context
-------
Before a model trains, you calculate how the dataset splits into batches,
how many steps each epoch takes, and how learning rates decay. All of it
is arithmetic. Getting the operator types right (int vs float) prevents
silent bugs in array indexing and loop ranges.

Covers:
  - + - * / // % ** and their return types
  - When / returns float and // returns int
  - floor division for batch counting and indexing
  - modulo for periodic logging
  - ** for learning rate decay
  - Scientific notation (1e-3) for small floats
  - Underscore separators in large numbers for readability
  - In-place operators: +=, -=, *=

Run this file. Predict each output before you see it.
"""

# ── Dataset and batch configuration ──────────────────────────────────────────

total_samples = 12_800    # underscore = visual separator, same as 12800
batch_size    = 32
num_epochs    = 5

# ── Floor division vs true division ──────────────────────────────────────────

# / always returns float — even when the result is a whole number
exact_ratio = total_samples / batch_size
print(f"/ result    : {exact_ratio}  ({type(exact_ratio).__name__})")  # 400.0, float

# // returns int — floors toward negative infinity
full_batches = total_samples // batch_size
print(f"// result   : {full_batches}  ({type(full_batches).__name__})")  # 400, int

# This distinction matters when you use the result as a loop range or array index
# range(400.0) would crash — range() needs an int, not a float

# ── Modulo — the remainder operator ──────────────────────────────────────────

leftover = total_samples % batch_size
print(f"Leftover    : {leftover} samples in last batch")  # 0

# More interesting case — uneven split
dataset_2 = 10_000
leftover_2 = dataset_2 % batch_size
full_2     = dataset_2 // batch_size
print(f"\n10,000 samples: {full_2} full batches + {leftover_2} leftover")

# Modulo for periodic logging — log every 50 steps
print("\nLogging every 50 steps:")
for step in range(1, 201):
    if step % 50 == 0:    # True when step is exactly divisible by 50
        print(f"  Step {step:>4} — log checkpoint")

# ── Exponentiation and learning rate ─────────────────────────────────────────

print()

# Scientific notation — how ML practitioners write small numbers
lr_initial = 2e-5       # 0.00002 — typical BERT fine-tuning learning rate
warmup_lr  = 1e-6       # 0.000001 — warmup starting point
max_lr     = 3e-4       # 0.0003

print(f"Initial LR  : {lr_initial}")
print(f"Warmup LR   : {warmup_lr}")
print(f"Max LR      : {max_lr}")

# ** for decay calculation — halve the learning rate every 2 epochs
epoch = 4
decay_factor = 0.5 ** (epoch // 2)
current_lr   = lr_initial * decay_factor
print(f"\nEpoch {epoch} LR  : {current_lr:.2e}")  # .2e = scientific notation format

# ── In-place operators ────────────────────────────────────────────────────────

print()

loss      = 2.0
accuracy  = 0.0
step_count = 0

# Simulating one training step update
loss      -= 0.1     # loss = loss - 0.1
accuracy  += 0.05    # accuracy = accuracy + 0.05
step_count += 1      # step_count = step_count + 1

print(f"After step {step_count}: loss={loss:.2f}  acc={accuracy:.2f}")

# *= for scaling
confidence = 0.95
confidence *= 0.9    # apply a confidence penalty
print(f"Penalized confidence: {confidence:.3f}")

# ── What to notice ────────────────────────────────────────────────────────────
#
# 1. / always returns float: 12800 / 32 = 400.0 (not 400)
#    Use // when you need an integer result for indexing or range().
#
# 2. // floors toward -infinity, not toward zero:
#    -7 // 2 = -4 (not -3) — it goes further negative
#    This matters if you ever index from the end of an array.
#
# 3. step % log_every == 0 is the standard pattern for "every N iterations".
#    You'll see this in every training loop: log, checkpoint, validate.
#
# 4. 2e-5 is the same as 0.00002 — scientific notation is standard
#    in ML for learning rates. Know how to read it and write it.
#
# 5. In-place operators (+=, -=, *=, /=) are cleaner than
#    x = x + 1. They also have a subtle performance advantage
#    for mutable objects (lists, numpy arrays) — relevant in Phase 6.