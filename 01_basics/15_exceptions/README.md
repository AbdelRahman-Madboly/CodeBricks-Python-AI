# 15 — Exceptions

> **How Python signals that something went wrong — and how you respond.**

---

## Why This Matters

Every real program runs in an unpredictable environment. Files go missing.
Users supply bad input. Networks drop. Models get fed corrupt data. None of
these are bugs — they're expected failure modes, and your job is to handle
them gracefully instead of letting the program crash.

In AI/ML work, exception handling is everywhere: loading checkpoints that may
not exist, parsing records that may be malformed, calling APIs that may time
out. A pipeline that crashes on the first bad record is useless in production.

---

## Two Kinds of Errors

**Syntax errors** — caught before the program runs. The interpreter refuses
to execute malformed code. Nothing to handle at runtime.

**Exceptions** — raised during execution. The program is syntactically valid
but something goes wrong at runtime. These can be caught and handled.

```python
# Syntax error — interpreter rejects this before running
if True
    print("missing colon")

# Exception — valid syntax, fails at runtime
int("not a number")   # ValueError: invalid literal for int()
```

---

## The try/except Pattern

```python
try:
    result = risky_operation()
except SomeError as e:
    handle_the_error(e)
```

The `try` block runs until an exception is raised or it completes.
The `except` block runs **only** if an exception was raised in `try`.
If no exception is raised, `except` is skipped entirely.

---

## raise — Signalling Errors

```python
def load_checkpoint(path: str) -> dict:
    if not path.endswith(".pt"):
        raise ValueError(f"expected .pt file, got: {path!r}")
    return {"weights": "..."}
```

`raise` stops execution immediately. The caller wraps the call in
`try/except` and decides what to do. The function does **not** catch
its own raises — that's the caller's responsibility.

**Errors are not bugs.** A bug is when code behaves unexpectedly.
An exception you raise deliberately is a contract: "here are the inputs
I accept — anything else and I'll tell you clearly."

---

## Specific Exception Types

```python
try:
    x = record["confidence"]    # KeyError if missing
    y = float(x)                # ValueError if not numeric
    z = y / record["scale"]     # ZeroDivisionError if scale=0
except KeyError as e:
    print(f"missing field: {e}")
except ValueError as e:
    print(f"bad value: {e}")
except ZeroDivisionError:
    print("scale is zero")
except Exception as e:
    print(f"unexpected: {e}")   # catch-all — always last
```

**Always put specific types before the general `Exception`.**
Python stops at the first matching clause — `Exception` matches everything,
so anything below it never runs.

---

## Common Built-in Exception Types

| Exception | When it's raised |
|-----------|-----------------|
| `ValueError` | Right type, wrong value — `int("abc")` |
| `TypeError` | Wrong type entirely — `"a" + 1` |
| `KeyError` | Dict key not found — `d["missing"]` |
| `IndexError` | List index out of range — `lst[100]` |
| `ZeroDivisionError` | Division by zero — `1 / 0` |
| `FileNotFoundError` | File doesn't exist — `open("missing.txt")` |
| `AttributeError` | Attribute doesn't exist — `None.split()` |
| `RuntimeError` | General runtime failure |

---

## else and finally

```python
try:
    result = load_data(source)
except DataError as e:
    print(f"failed: {e}")
    return None
else:
    # Only runs if NO exception was raised
    print(f"loaded {len(result)} records")
    return result
finally:
    # ALWAYS runs — exception or not
    print("cleanup done")
```

`else` — post-success logic, kept outside `try` so its own errors
aren't accidentally caught by the `except` block.

`finally` — guaranteed cleanup: close files, release GPU memory,
flush logs. Runs even if an exception propagated past all `except` clauses.

---

## Custom Exceptions

```python
class PipelineError(Exception):
    """Base class for all pipeline errors."""

class DataError(PipelineError):
    """Raised for bad or missing input data."""

class EpochError(PipelineError):
    """Raised for training failures."""
```

Custom exceptions let callers respond at the right level:

```python
except DataError    # only data problems
except EpochError   # only training problems
except PipelineError  # any pipeline problem
except Exception    # absolutely anything
```

Inherit from `Exception` (or a project base class). Add a docstring.
That's usually all you need — no extra methods required.

---

## Common Mistakes

**Catching too broadly too early**
```python
try:
    result = complex_operation()
except Exception:
    pass   # silently swallows ALL errors — including bugs you haven't found yet
```

**Catching your own raises**
```python
# Don't do this — the function hides its own errors
def load(path):
    try:
        if not path:
            raise ValueError("empty path")
    except ValueError:
        print("handled")   # caller never knows it failed
```

**Wrong catch order**
```python
except Exception:   # catches everything — IndexError below never runs
    ...
except IndexError:
    ...
```

**Using bare `except:` without a type**
```python
except:   # catches even SystemExit and KeyboardInterrupt — almost never correct
    ...
# Use: except Exception:
```

---

## Interview Angle

*"What is the difference between an error and a bug?"*
An error (exception) is an expected failure mode your code handles.
A bug is when code behaves in a way users don't expect.
Raising a `ValueError` for bad input is not a bug — it's a contract.

*"When would you use a custom exception?"*
When you want callers to distinguish between failure modes.
`except DataError` and `except EpochError` respond differently;
`except Exception` treats both the same.

---

## Folder Structure

```
15_exceptions/
├── README.md
├── notes.md
├── test.py
│
├── examples/
│   ├── 01_try_except_basics.py       — try/except, raise, exceptions are not bugs
│   ├── 02_exception_types.py         — specific types, multiple excepts, catch order
│   └── 03_advanced_error_handling.py — else, finally, custom exceptions, re-raise
│
├── exercises/
│   ├── 01_input_guards.py            — Easy: guard clauses with raise
│   ├── 02_batch_processor.py         — Medium: multiple except, specific types
│   └── 03_pipeline_runner.py         — Hard: custom exceptions, else/finally
│
└── solutions/
    ├── 01_input_guards.py
    ├── 02_batch_processor.py
    └── 03_pipeline_runner.py
```

---

## Connection to the AI Journey

```python
# Loading a checkpoint that may not exist
try:
    checkpoint = torch.load(path)
except FileNotFoundError:
    checkpoint = None   # start from scratch

# Parsing a record that may be malformed
try:
    score = float(record["confidence"])
except (KeyError, ValueError):
    continue   # skip bad record, process the rest

# Custom exceptions in a training pipeline
class OutOfMemoryError(PipelineError):
    """Raised when GPU memory is exhausted."""

# Guaranteed cleanup with finally
try:
    run_epoch(model, dataloader)
finally:
    torch.cuda.empty_cache()   # always release GPU memory
```

---

*Previous → [12 — Dictionaries and Sets](../12_dicts_sets/)*
*Next → [06 — Classes and Objects](../06_classes_intro/)*