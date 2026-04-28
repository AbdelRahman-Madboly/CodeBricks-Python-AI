# 01 — Printing | notes.md

> Fill this in after finishing the exercises — not before.
> Write in your own words. If you can explain it clearly here,
> you actually understand it. If you're copying from the README,
> you don't yet.

---

## What clicked immediately

<!-- What felt natural or obvious? -->



---

## What took time to understand

<!-- What confused you? How did you get past it? -->



---

## My questions — answered

These came up while working through this topic. Writing the answers
here is better than just reading them.

---

### Q: What's the difference between a parser and an interpreter?

When you run `python script.py`, two things happen in sequence:

**Step 1 — The parser** reads your source code (text) and checks
whether it's valid Python. It turns the code into a tree structure
called an AST (Abstract Syntax Tree). If you have a `SyntaxError`,
the parser catches it here — before anything runs.

**Step 2 — The interpreter** takes that tree and executes it,
instruction by instruction. This is what actually "runs" your program.
Errors here (like `NameError`, `TypeError`) happen at runtime.

Short version: **parser checks shape, interpreter runs logic.**

```
SyntaxError  → caught by parser  (structure is wrong)
NameError    → caught by interpreter  (structure was fine, something blew up)
```

---

### Q: What is an IndentationError?

Python uses indentation (spaces) to define blocks of code.
Most languages use `{}` — Python uses whitespace instead.

```python
# Valid — 4 spaces inside the if block
if True:
    print("this is inside the block")

# IndentationError — Python expected indentation here
if True:
print("this is not indented")
```

The parser catches this before anything runs. It's not a logic error —
it's a structural one. Python doesn't know where your block begins or ends.

**Rule:** Use exactly 4 spaces per indentation level. Never mix tabs and spaces.

---

### Q: How is Python different from C++ in how it actually runs?

**C++ — compiled**
```
your .cpp file
      ↓
   Compiler (g++)         ← translates everything BEFORE running
      ↓
   Machine code (.exe)
      ↓
   CPU runs it directly   ← very fast
```

**Python — interpreted**
```
your .py file
      ↓
   Parser                 ← checks syntax, builds AST
      ↓
   Bytecode (.pyc)        ← intermediate format, done automatically
      ↓
   Python VM (CPython)    ← executes bytecode line by line
      ↓
   Result                 ← slower than C++, but you write it in minutes
```

**Practical difference:**
- C++: write → compile (wait) → fix compile errors → run
- Python: write → run immediately (errors appear at runtime)

For AI work, this is why Python dominates: the feedback loop is instant.
You run a cell in a notebook and see results in seconds.
C++ is faster at execution; Python is faster at development.

When performance matters (model inference at scale), the heavy lifting
is done by libraries like NumPy and PyTorch — which are themselves
written in C/C++. Python is the glue.

---

## Connections to other topics

<!-- How does this connect to what you learned on Boot.dev or elsewhere? -->
<!-- Examples: "end= is like print without \n in C", "f-strings remind me of..." -->



---

## Things to revisit later

- [ ] `*list` unpacking — used in example 2, explained in Functions (topic 05)
- [ ] `lambda` — used in example 3, explained in Advanced Functions (topic 16)
- [ ] Generator expressions `sum(x for x in ...)` — used in solution 2, explained in Phase 3
- [ ] Dict `.items()` and `.values()` — used in solution 2, explained in Dicts (topic 12)
- [ ] List comprehensions as an alternative to the loop in solution 3 — Phase 3

---

## One-line summary

> In one sentence, what does `print()` do and why does it matter for AI work?

<!-- Write it here — in your own words -->