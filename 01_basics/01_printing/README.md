# 01 — Printing

> **The first tool every AI engineer uses every single day.**

---

## Why This Matters

Before you train a model, before you build an agent, before you write
a single line of PyTorch — you need to make your program *talk* to you.

`print()` is how you do that.

It's how you debug a broken training loop at 2am. It's how you display
a model's accuracy after each epoch. It's how your RAG pipeline tells
you it found 5 relevant documents. It sounds basic because it is —
and that's exactly why you need to know it cold.

In AI work especially, readable output is the difference between
catching a bug in 10 minutes and spending 3 hours confused.

---

## What print() Actually Does

```python
print("Loading model weights...")
```

`print()` takes whatever you give it, converts it to text, and sends it
to the terminal. That's the whole job.

But it has parameters that change how it behaves:

```
print(value1, value2, ..., sep=' ', end='\n', file=sys.stdout)
         │                    │         │           │
         │                    │         │           └── where to send (default: terminal)
         │                    │         └── what goes at the end (default: new line)
         │                    └── what goes between values (default: space)
         └── what to print
```

---

## The Three Ways to Print Variables

You'll see all three in the wild. Know them all.

```python
model = "GPT-2"
accuracy = 94.3

# 1 — Concatenation  (avoid — crashes on non-strings)
print("Model: " + model)

# 2 — Comma-separated  (simple, limited control)
print("Model:", model, "| Accuracy:", accuracy)

# 3 — f-string  (modern, clear, use this)
print(f"Model: {model} | Accuracy: {accuracy:.1f}%")
```

**Use f-strings.** Every professional Python codebase does.

---

## Formatting Numbers in f-strings

```python
loss     = 0.003412
accuracy = 0.9743
total    = 1_500_000

print(f"Loss:     {loss:.4f}")       # 0.0034  — 4 decimal places
print(f"Accuracy: {accuracy:.1%}")   # 97.4%   — percent format
print(f"Samples:  {total:,}")        # 1,500,000 — comma separator
print(f"{'Label':<15} {'Value':>8}") # aligned columns
```

You don't need to memorize all of these now. You'll reach for them
naturally once you start displaying model metrics and dataset statistics.

---

## Common Mistakes

**Mixing types with `+`**
```python
epoch = 5
print("Epoch: " + epoch)      # TypeError — can't add str + int
print(f"Epoch: {epoch}")      # works
```

**Thinking print() produces a value**
```python
def get_loss():
    print(0.043)     # shows the number but returns None

loss = get_loss()   # loss is None, not 0.043
print(loss * 2)     # crashes — you can't multiply None
```

This is one of the most common early bugs. `print()` is a side effect,
not a value. We'll revisit this properly in Functions (topic 05).

**Forgetting the newline**
```python
# Each print adds \n by default — use end="" to stay on same line
for epoch in range(3):
    print(f"Epoch {epoch}", end=" | ")
print("Done")
# Output: Epoch 0 | Epoch 1 | Epoch 2 | Done
```

---

## Folder Structure

```
01_printing/
├── README.md          ← you are here
├── notes.md           ← fill this in after finishing the exercises
├── test.py            ← run to verify your understanding
│
├── examples/          ← read these first, predict output before running
│   ├── 01_banner.py           — CLI startup banner (AI tool)
│   ├── 02_pipeline_log.py     — logging a multi-step AI pipeline
│   └── 03_model_report.py     — formatted model evaluation report
│
├── exercises/         ← attempt these before opening solutions
│   ├── 01_agent_status.py     — Easy: format an AI agent status line
│   ├── 02_dataset_table.py    — Medium: print an aligned dataset summary
│   └── 03_training_bar.py     — Hard: build a one-line training progress log
│
└── solutions/         ← open only after a genuine attempt
    ├── 01_agent_status.py
    ├── 02_dataset_table.py
    └── 03_training_bar.py
```

---

## How to Work Through This Topic

1. Read this README — understand the concept before touching code
2. Open each `examples/` file — read every comment, **predict the output** before running
3. Attempt each `exercises/` file on your own — don't open solutions yet
4. Check `solutions/` — compare your approach, read the "why" comments
5. Fill in `notes.md` — in your own words, no copying

The notes step is the easiest to skip and the most valuable not to.
You're building a portfolio here, not just doing homework.

---

## Connection to the AI Journey

Every tool you build in this repo will print something:

- A **training loop** prints loss and accuracy every epoch
- A **RAG pipeline** prints which documents it retrieved and why
- An **AI agent** prints what action it decided to take and what it observed
- A **data pipeline** prints how many rows were cleaned, skipped, or failed

The output you write here is the same pattern you'll use in Phase 7
(PyTorch) and Phase 8 (Projects). Learn it right once.

---

*Next → [02 — Variables and Data Types](../02_variables_data_types/)*