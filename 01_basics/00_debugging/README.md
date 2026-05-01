# 00 — Debugging

> **Read this once. Use it every day.**

---

## What Debugging Actually Is

Debugging is the process of figuring out why your code doesn't do
what you think it does. Every developer does this constantly —
beginners and seniors alike. The difference is how fast you do it.

The core loop is always the same:

```
write a small piece of code
    ↓
add a print() to see what it's doing
    ↓
run it
    ↓
does it match what you expected?
    ↓
yes → remove the print, move forward
no  → fix it, run again
```

Never write 50 lines and then run. Write 5, check, write 5 more.

---

## Reading a Stack Trace

When Python crashes, it prints a **traceback** (stack trace).
Most beginners panic and ignore it. Don't — it tells you exactly
what went wrong and where.

```
Traceback (most recent call last):
  File "train.py", line 12, in <module>
    result = compute_loss(predictions, labels)
  File "train.py", line 7, in compute_loss
    return sum(errors) / count
ZeroDivisionError: division by zero
```

Read it **bottom to top**:

| Part | What it tells you |
|------|-------------------|
| `ZeroDivisionError: division by zero` | The error type and message — start here |
| `File "train.py", line 7, in compute_loss` | Which function and which line crashed |
| `return sum(errors) / count` | The exact line of code |
| `File "train.py", line 12, in <module>` | What called that function |

The bottom line is always the direct cause.
The lines above it are the call chain that led there.

### Common error types

| Error | What it means | Typical cause |
|-------|---------------|---------------|
| `SyntaxError` | Code is malformed — Python can't even parse it | Missing `:`, mismatched quotes, bad indentation |
| `IndentationError` | Wrong indentation level | Mixed tabs/spaces, off-by-one spaces |
| `NameError` | Used a name that doesn't exist | Typo, wrong scope, called before assignment |
| `TypeError` | Wrong type for the operation | `str + int`, calling a non-function, wrong arg count |
| `ZeroDivisionError` | Divided by zero | Missing guard: `if count > 0` |
| `AttributeError` | Object doesn't have that attribute | Typo in method name, wrong type |
| `IndexError` | List index out of range | Off-by-one, empty list |
| `KeyError` | Dict key doesn't exist | Use `.get()` instead of `[]` |
| `ValueError` | Right type, invalid value | `int("hello")`, `float("None")` |
| `UnboundLocalError` | Local var used before assignment | See scope note below |

---

## The UnboundLocalError — Scope Trap

This one trips up beginners often. It looks like the global variable
should be readable, but it crashes:

```python
count = 0

def increment():
    count = count + 1   # UnboundLocalError
```

**Why:** Python sees `count =` inside the function → marks `count` as
local for the *entire* function → tries to read it on the right side →
local `count` doesn't exist yet → crash.

**Fix:** never reassign globals inside functions. Pass the value in,
return the new value out:

```python
def increment(count: int) -> int:
    return count + 1

count = 0
count = increment(count)
```

If you truly need to read a global (not reassign), Python finds it
automatically — no issue. The problem only appears when you assign.

---

## Debugging Workflow in Practice

Here's how to debug a broken function step by step.

### Scenario
You're writing a function to compute weighted accuracy for a model,
and something's wrong with the output.

**Step 1 — Run it in its broken state. Read the error.**

```python
def weighted_accuracy(correct, total, weight):
    weighted = correct * weight
    return weighted / total

print(weighted_accuracy(8, 10, 1.2))
```

Runs fine. But the output looks wrong. No error — just wrong math.
This is a logic bug, not a crash.

**Step 2 — Add prints at each step to inspect intermediate values.**

```python
def weighted_accuracy(correct, total, weight):
    weighted = correct * weight
    print(f"DEBUG weighted: {weighted}")   # what did we compute?
    result = weighted / total
    print(f"DEBUG result: {result}")       # is this sensible?
    return result
```

Run it. Look at each print. Does `weighted` look right?
Does `result` look right? If not — that's where the bug is.

**Step 3 — Fix the logic. Remove the debug prints. Run clean.**

```python
def weighted_accuracy(correct, total, weight):
    weighted = correct * weight
    return weighted / total
```

**Step 4 — Test edge cases.**

What if `total` is 0? What if `weight` is negative?
Add guards or document the assumptions.

---

## print() for Debugging — Patterns

```python
# Inspect a variable
print(f"DEBUG x: {x}")

# Inspect a variable with its type
print(f"DEBUG x: {x!r}  ({type(x).__name__})")

# Mark a point in execution (did we reach here?)
print("DEBUG: reached checkpoint 1")

# Inspect in a loop
for i, item in enumerate(data):
    print(f"DEBUG [{i}]: {item!r}")
    if i > 5:
        print("DEBUG: truncated output")
        break
```

**Remove all DEBUG prints before committing to git.**
Use `git diff` to check — any remaining `DEBUG` lines will show up.

---

## Scope — Quick Reference

```
Global scope  ─────────────────────────────────────────
  MODEL_NAME = "bert"                 # global constant
  
  def load():                         # function in global scope
    Local scope ────────────────────
      weights = {}                    # local — gone after return
      return weights
    ────────────────────────────────
  
  result = load()                     # global — weights is now gone
─────────────────────────────────────────────────────────
```

**LEGB rule** — Python searches for a name in this order:
1. **L**ocal — current function
2. **E**nclosing — any surrounding function (closures — topic 16)
3. **G**lobal — the module (file) level
4. **B**uilt-in — Python's built-ins (`print`, `len`, `range`...)

First match wins. If none found → `NameError`.

---

## Unit Tests — What They Are and Why They Matter

A **unit test** is a small piece of code that calls your function
with known inputs and checks that it returns the expected output.

```python
# Your function
def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val)

# A unit test for it
def test_normalize_midpoint():
    result = normalize(128, 0, 255)
    assert round(result, 4) == 0.502, f"Expected 0.502, got {result}"

test_normalize_midpoint()
print("test passed")
```

`assert` crashes with an `AssertionError` if the condition is False.
That's the test failing.

**Why write tests?**
- You can change the function later and immediately know if you broke it
- Tests document what the function is *supposed* to do
- Tests catch edge cases you forgot about (`total=0`, empty list, etc.)

Every `test.py` file in this repo is a set of unit tests.
In Phase 5 you'll use `pytest` — which automates running and reporting.
For now, the manual approach in each `test.py` teaches the same concept.

---

## The Debugging Mindset

When something breaks, go through these questions in order:

1. **What does the error message say?** Read the bottom line first.
2. **Which line caused it?** Stack trace tells you.
3. **What did I expect at that line?** State your assumption explicitly.
4. **What was the actual value?** Add a print to find out.
5. **Where did the wrong value come from?** Trace backwards.
6. **What was my assumption that was wrong?** Fix that, not just the symptom.

Most bugs aren't in the line Python points to — they're in the line
that produced the bad value that eventually caused the crash.

---

## This Folder's Role in the Repo

This is a **reference document**, not a topic to complete.
There are no exercises or tests here.

Come back to it whenever:
- You hit a new error type you haven't seen before
- You're stuck and don't know where to start debugging
- You want to remind yourself of the scope rules

The concepts here are absorbed into every other topic's `test.py`
and `notes.md`. When you get to Phase 5, you'll formalize this
with `pytest`, `ruff`, and proper test structure.

---

## Folder Structure (this folder)

```
00_debugging/
├── README.md              ← you are here — read and reference
└── example_debug_session.py  ← walk through a full debug session live
```

---

*Next → [01 — Printing](../01_printing/)*