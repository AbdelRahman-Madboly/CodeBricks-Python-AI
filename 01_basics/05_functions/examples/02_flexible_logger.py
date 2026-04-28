"""
examples/02_flexible_logger.py
───────────────────────────────
Topic  : Functions
Example: 2 of 3 — *args, **kwargs, multiple return values

Context
-------
Every serious training script needs a logger — a function that formats
and prints status messages with context (epoch number, loss, device, etc.).

The challenge: you don't always know upfront how many messages or how
much context you'll need to log. That's where *args and **kwargs shine.

This example also shows functions that return multiple values — the
same pattern you'll use when a training epoch needs to report both
loss and accuracy back to the caller.

Covers:
  - *args: variable positional arguments (collected as a tuple)
  - **kwargs: variable keyword arguments (collected as a dict)
  - Returning multiple values (as a tuple)
  - Unpacking multiple return values
  - None return (functions that only produce side effects)

Run this file. Predict each output before you see it.
"""


# ── Part 1: *args and **kwargs ────────────────────────────────────────────────

def log_event(level: str, *messages: str, **context) -> None:
    """
    Log a structured training event to the console.

    Args:
        level: Severity — INFO, WARNING, or ERROR.
        *messages: One or more message strings, joined with a space.
        **context: Optional key=value metadata (epoch, loss, device, etc.).

    Returns:
        None — this function exists for its side effect (printing).
    """
    # *messages is a tuple of all positional args after level
    text = " ".join(messages)

    # **context is a dict of all keyword args
    extras = "  |  " + "  ".join(f"{k}={v}" for k, v in context.items()) \
             if context else ""

    print(f"[{level:<7}]  {text}{extras}")


# Calling with different numbers of arguments — all valid
log_event("INFO", "Pipeline starting")
log_event("INFO", "Epoch complete", epoch=3, loss=0.0421, acc=0.934)
log_event("WARNING", "GPU memory low", device="cuda:0", free_mb=512)
log_event("ERROR", "Checkpoint", "not found", path="/models/run_42.pt")

# ── Part 2: multiple return values ────────────────────────────────────────────

print()

def compute_metrics(predictions: list, labels: list) -> tuple[float, float, int]:
    """
    Compute accuracy and error rate for a set of predictions.

    Args:
        predictions: Model output class indices.
        labels: Ground-truth class indices.

    Returns:
        Tuple of (accuracy, error_rate, correct_count).
    """
    correct = sum(p == l for p, l in zip(predictions, labels))
    total = len(labels)
    accuracy = correct / total
    error_rate = 1.0 - accuracy
    return accuracy, error_rate, correct   # returns a tuple of three values


# Unpack into three variables — order matches the return statement
preds  = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1]
labels = [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]

accuracy, error_rate, n_correct = compute_metrics(preds, labels)

print(f"Accuracy    : {accuracy:.1%}")
print(f"Error rate  : {error_rate:.1%}")
print(f"Correct     : {n_correct} / {len(labels)}")

# You can also ignore values you don't need with _ (convention for "discard")
acc, _, _ = compute_metrics(preds, labels)
print(f"\nAccuracy only: {acc:.1%}")

# ── What to notice ────────────────────────────────────────────────────────────
#
# 1. *messages collects all positional args after 'level' into a TUPLE.
#    log_event("INFO", "a", "b", "c") → messages = ("a", "b", "c")
#    You can then iterate it, join it, slice it — it's just a tuple.
#
# 2. **context collects all keyword args into a DICT.
#    log_event("INFO", "msg", epoch=5, loss=0.04) → context = {"epoch": 5, "loss": 0.04}
#    Order is preserved (Python 3.7+).
#
# 3. *args MUST come before **kwargs in the signature. Always.
#    def f(*args, **kwargs) → valid
#    def f(**kwargs, *args) → SyntaxError
#
# 4. Multiple return values are just a tuple.
#    return accuracy, error_rate, correct
#    is the same as:
#    return (accuracy, error_rate, correct)
#    Python's unpacking (a, b, c = func()) does the rest.
#
# 5. _ as a variable name means "I'm deliberately ignoring this value".
#    It's a convention — the value exists, you just don't use it.
#    Common in loops too: for _, value in enumerate(items) when you don't need index.
#
# 6. None return
#    log_event returns None — it exists only to print.
#    result = log_event("INFO", "done")  → result is None
#    Don't capture the return of functions that are pure side effects.