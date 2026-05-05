# 15 — Exceptions | notes.md

> Fill this in after finishing the exercises.

---

## What clicked immediately



---

## What took time



---

## My questions — answered

---

### Q: What is the difference between a syntax error and an exception?

A **syntax error** is caught before the program runs. The Python interpreter
refuses to execute malformed code — nothing has run yet.

An **exception** is raised during execution. The code is syntactically valid
but something goes wrong at runtime.

```python
# Syntax error — interpreter rejects this before anything runs
if True
    print("missing colon")    # SyntaxError: expected ':'

# Exception — valid syntax, fails at runtime
int("abc")     # ValueError: invalid literal for int() with base 10: 'abc'
[1,2,3][10]    # IndexError: list index out of range
```

You handle exceptions with `try/except`. You fix syntax errors by editing the code.

---

### Q: What happens if no exception is raised in the try block?

The `except` block is **completely skipped**. Execution continues after the
entire `try/except` structure as if it wasn't there.

```python
try:
    result = 10 / 2    # no exception
    print(result)      # 5.0 — this runs
except ZeroDivisionError:
    print("never")     # this is skipped
print("after")         # this runs
```

The `except` block is not a guaranteed "always runs" block — that's `finally`.

---

### Q: What is the rule about where to raise vs where to catch?

**Raise in the function. Catch at the call site.**

The function that detects the problem raises the exception.
The caller that calls the function wraps it in `try/except`.

```python
# Function raises — doesn't handle its own error
def load_weights(path: str) -> dict:
    if not path.endswith(".pt"):
        raise ValueError(f"expected .pt file, got: {path!r}")
    return {}

# Caller catches — decides what to do on failure
try:
    weights = load_weights("model.pkl")
except ValueError as e:
    print(f"Bad path: {e}")
    weights = {}
```

Breaking this rule — catching inside the same function that raised — hides
errors from callers and makes the function harder to test.

---

### Q: Why must specific exception types come before Exception?

Python checks `except` clauses **top to bottom** and stops at the first match.
`Exception` is the base class — it matches `IndexError`, `ValueError`,
`ZeroDivisionError`, and virtually everything else.

If `except Exception` comes first, all specific handlers below it are dead code.

```python
# Wrong — general catches everything, IndexError handler never runs
try:
    lst = [1, 2, 3]
    print(lst[10])
except Exception:
    print("general")      # this runs
except IndexError:
    print("index error")  # NEVER reached

# Correct — most specific first, general as fallback
try:
    lst = [1, 2, 3]
    print(lst[10])
except IndexError:
    print("index error")  # this runs
except Exception:
    print("general")      # only for other errors
```

Rule: order your `except` clauses from most specific to least specific.

---

### Q: What is the else clause for in try/except?

`else` runs **only if no exception was raised** in the `try` block.

It separates "success path" code from the `try` block so that errors
in the success code don't get caught by the `except` block above.

```python
try:
    data = load_data(source)
except DataError as e:
    print(f"load failed: {e}")
    return None
else:
    # Only reaches here if load_data succeeded
    # If this raises, it WON'T be caught by except DataError above
    process(data)
    return data
```

Without `else`, you'd put `process(data)` inside `try` — and if it raised
a `DataError`, it would be incorrectly caught by the handler meant for `load_data`.

---

### Q: What is finally for and when does it run?

`finally` **always runs** — whether or not an exception was raised,
whether or not it was caught, even if there's a `return` inside `try` or `except`.

Use it for cleanup that must happen regardless of outcome.

```python
def run_epoch(model, data):
    try:
        train(model, data)
    except RuntimeError as e:
        print(f"training failed: {e}")
    finally:
        torch.cuda.empty_cache()   # always release GPU memory
```

In practice, Python's `with` statement (context managers) automates the
`try/finally` pattern for resources like files and database connections.
You'll learn `with` in Phase 3 (Context Managers).

---

### Q: When should I define a custom exception?

When you want callers to **distinguish between failure modes** and respond differently.

```python
class PipelineError(Exception):  pass
class DataError(PipelineError):  pass    # bad input
class EpochError(PipelineError): pass    # training failure

# Caller can be as specific or as general as needed:
except DataError    # only data problems — alert the data team
except EpochError   # only training failures — maybe retry
except PipelineError  # any pipeline problem — log and stop
```

If you'd handle all errors the same way, a plain `Exception` is fine.
Custom exceptions pay off in larger codebases where error taxonomy matters.

---

## Connections to other topics

<!-- How does this connect to what you learned in other topics? -->
<!-- Example: "raise in a function + try/except at the call site is the
     same pattern I saw with .get() vs d[key] — signal the problem,
     let the caller decide how to respond" -->



---

## Things to revisit later

- [ ] `with` statement — automates try/finally for resources — Phase 3 (Context Managers)
- [ ] `raise X from Y` — exception chaining, preserving the original cause — Phase 3
- [ ] `traceback` module — printing full stack traces programmatically — Phase 4 stdlib
- [ ] `logging` module — logging exceptions to file instead of printing — Phase 4 stdlib
- [ ] `Exception` vs `BaseException` — why `KeyboardInterrupt` isn't caught by `except Exception` — CS fundamentals

---

## One-line summary

> In one sentence: what is an exception, and what is the difference between
> raising one and catching one?

<!-- Your words here -->