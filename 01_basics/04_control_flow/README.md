# 04 — Control Flow

> **How your program makes decisions and repeats work.**

---

## Why This Matters

A training loop is a `for` loop. Early stopping is an `if` statement.
Skipping bad samples is `continue`. Finding the best checkpoint is a
`for/else`. Every AI script you write is built from these primitives.

---

## Branching — if / elif / else

```python
confidence = 0.76

if confidence >= 0.90:
    decision = "accept"
elif confidence >= 0.70:
    decision = "review"
elif confidence >= 0.50:
    decision = "flag"
else:
    decision = "reject"
```

**Rules:**
- Only one branch runs — the first one whose condition is `True`
- `elif` and `else` are optional
- `else` has no condition — it's the fallback
- Order matters: put the most specific condition first

---

## Ternary Expression — one-line if/else

```python
# Full form
if score >= 60:
    result = "pass"
else:
    result = "fail"

# Ternary — same thing, one line
result = "pass" if score >= 60 else "fail"

# Common in AI scripts
label = "positive" if prediction >= 0.5 else "negative"
status = "✓" if is_valid else "✗"
```

Use ternary for simple single-value choices. Use full `if/else` when
the body is more than one statement.

---

## while Loops

```python
epoch = 0
patience = 0
best_loss = float("inf")

while epoch < max_epochs and patience < 5:
    loss = train_one_epoch()

    if loss < best_loss:
        best_loss = loss
        patience = 0
    else:
        patience += 1

    epoch += 1
```

**Always ensure the condition eventually becomes `False` — or use `break`.**
An infinite `while True` loop that never breaks will hang your script.

---

## for Loops

Python's `for` iterates over any **iterable** — list, string, range,
file, generator. It asks the collection for its next item each iteration.

```python
# range — most common for numeric loops
for i in range(10):         # 0 to 9
    ...

for i in range(2, 10, 2):  # 2, 4, 6, 8 — start, stop, step
    ...

# Iterating a collection directly
for filename in checkpoints:
    process(filename)

# enumerate — index + value together
for i, item in enumerate(dataset):
    print(f"[{i}] {item}")

# zip — iterate two collections in parallel
for pred, label in zip(predictions, labels):
    ...
```

---

## break and continue

```python
for frame in video_stream:
    if frame.is_corrupted:
        continue        # skip this frame, move to the next

    if frame.is_end_signal:
        break           # stop the loop entirely

    process(frame)
```

- `continue` — skip the rest of this iteration, move to the next
- `break` — exit the loop immediately
- Both work in `while` and `for` loops

---

## for / else (and while / else)

The `else` clause on a loop runs **only if the loop completed without hitting `break`**.

```python
# Search pattern — find the first valid checkpoint
for filename, is_valid in checkpoints:
    if is_valid:
        print(f"Loaded: {filename}")
        break
else:
    # Only runs if no 'break' was hit — no valid checkpoint found
    print("No valid checkpoint found")
```

Without `for/else`, you'd need a flag variable:
```python
found = False
for filename, is_valid in checkpoints:
    if is_valid:
        print(f"Loaded: {filename}")
        found = True
        break
if not found:
    print("No valid checkpoint found")
```

`for/else` is cleaner. Use it for search-and-report patterns.

---

## Common Mistakes

**Off-by-one in range**
```python
range(5)       # 0, 1, 2, 3, 4 — never includes 5
range(1, 6)    # 1, 2, 3, 4, 5 — stop is exclusive
```

**Modifying a list while iterating it**
```python
# Wrong — skips items
items = [1, 2, 3, 4]
for item in items:
    if item % 2 == 0:
        items.remove(item)   # modifies the list mid-iteration

# Right — iterate a copy, or build a new list
items = [item for item in items if item % 2 != 0]
```

**Infinite while loop**
```python
while not converged:
    loss = train()
    # forgot to update 'converged' — runs forever
```

**Missing the `else` on `for/else`**
The `else` is on the `for`, not inside it. Indentation matters:
```python
for item in items:
    if condition:
        break
else:           # ← same indent as 'for', NOT inside the loop
    print("not found")
```

---

## Folder Structure

```
04_control_flow/
├── README.md           ← you are here
├── notes.md
├── test.py
│
├── examples/
│   ├── 01_branching.py         — if/elif/else, ternary, guard clauses
│   ├── 02_loops.py             — for, while, range, enumerate, zip
│   └── 03_break_continue.py    — break, continue, for/else, search pattern
│
├── exercises/
│   ├── 01_confidence_router.py — Easy: classify a model output tier
│   ├── 02_training_loop.py     — Medium: simulate a training loop with early stopping
│   └── 03_checkpoint_search.py — Hard: for/else search + FizzBuzz variant
│
└── solutions/
    ├── 01_confidence_router.py
    ├── 02_training_loop.py
    └── 03_checkpoint_search.py
```

---

## Connection to the AI Journey

```python
# A real training loop uses everything from this topic
for epoch in range(1, max_epochs + 1):
    train_loss = 0.0

    for batch_idx, (inputs, labels) in enumerate(dataloader):
        loss = model(inputs, labels)
        train_loss += loss.item()

        if batch_idx % log_every == 0:
            print(f"  [{epoch}/{max_epochs}] batch {batch_idx} loss: {loss:.4f}")

    avg_loss = train_loss / len(dataloader)

    if avg_loss < best_loss:
        best_loss = avg_loss
        save_checkpoint(model)
    elif patience_count >= max_patience:
        print("Early stopping.")
        break
    else:
        patience_count += 1
else:
    print("Training complete — all epochs finished.")
```

Every construct from this topic is in that loop.

---

*Previous → [03 — Operators](../03_operators/)*
*Next → [05 — Functions](../05_functions/)*