# Exceptions

## Concept

An exception is Python's way of signalling that something went wrong at runtime.
When an error occurs, Python creates an exception object and "raises" it.
If nothing handles it, the program crashes with a traceback.

**Exception handling** lets you anticipate failures, recover gracefully,
and give users (or callers) meaningful error messages instead of raw tracebacks.

## Mental Model

```
try:
    risky_operation()        ← attempt the work
except SpecificError as e:   ← catch only what you can handle
    handle_it()
except AnotherError:
    handle_differently()
else:
    success_path()           ← runs only if NO exception was raised
finally:
    always_runs()            ← cleanup — always executes, exception or not
```

Think of `try/except` as a safety net under a tightrope walker.
The walker always tries the walk (`try`). If they fall, the net catches them (`except`).
The `finally` block is the crew that packs up regardless of what happened.

## Key Points

- Catch the **most specific** exception you can — catching bare `Exception`
  hides bugs and swallows errors you didn't intend to catch
- `raise` re-raises the current exception; `raise NewError("msg")` raises a new one
- `raise NewError("msg") from original_error` — chains exceptions, preserving context
- Custom exceptions: subclass `Exception` to create domain-specific error types
- `else` runs only when no exception occurred — useful to separate the happy path
- `finally` always runs — use it to release resources (though `with` is usually better)

## Common Mistakes

- Bare `except:` — catches everything including `KeyboardInterrupt` and `SystemExit`,
  making programs impossible to stop. Always specify the exception type
- Silencing exceptions without logging: `except Exception: pass` — bugs disappear silently
- Over-catching: catching `Exception` when you only expect `ValueError` —
  hides unrelated errors that should crash loudly

## Interview Angle

*"When would you create a custom exception class?"*
When your library or module has error conditions that callers need to handle
specifically — e.g. `InsufficientDataError`, `ModelNotTrainedError`.
Custom exceptions let callers write `except InsufficientDataError` instead
of parsing error message strings.
