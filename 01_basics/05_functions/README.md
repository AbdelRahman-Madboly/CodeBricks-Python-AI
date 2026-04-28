# 05 — Functions

> **The unit of reusable thinking.**

---

## Why This Matters

Before functions, your code runs top to bottom once.
With functions, you define a piece of logic once and call it
anywhere — with different inputs — as many times as you need.

Every AI pipeline you'll ever write is a chain of functions:
`load_data()` → `preprocess()` → `train()` → `evaluate()` → `save()`.
Each one does one job. Each one can be tested in isolation.
Each one can be reused in a different project.

Functions are also where Python starts feeling like a real language
instead of a calculator.

---

## What a Function Is

```python
def normalize(value: float, min_val: float = 0.0, max_val: float = 1.0) -> float:
    """Scale a value to the range [0.0, 1.0]."""
    return (value - min_val) / (max_val - min_val)
```

Breaking that down:

```
def normalize ( value: float,  min_val: float = 0.0 ) -> float :
 │      │           │                   │                  │
 │      │           │                   │                  └── return type hint
 │      │           │                   └── parameter with default value
 │      │           └── parameter with type hint
 │      └── function name (snake_case)
 └── keyword — "define a function"
```

- **Parameters** are the names in the definition (`value`, `min_val`)
- **Arguments** are the values you pass when calling (`normalize(128, 0, 255)`)
- **`return`** sends a value back and exits immediately
- **No `return`** → the function returns `None`

---

## The Execution Model

Understanding the order things happen is crucial:

```python
def greet(name):          # 1. Python reads this but does NOT run it
    return f"Hello, {name}"

message = greet("Abdelrahman")   # 2. NOW the function runs
print(message)                   # 3. Prints the result
```

Detailed sequence when `greet("Abdelrahman")` is called:
1. Python jumps to the `def greet` definition
2. A new **local scope** is created — a temporary workspace
3. `name` is set to `"Abdelrahman"` inside that scope
4. The function body runs: builds the f-string
5. `return` sends the value back and destroys the local scope
6. The returned value is assigned to `message`

---

## Scope — Where Variables Live

```python
model_name = "bert"          # global scope — lives for the whole script

def load_model():
    weights = "loading..."   # local scope — only exists inside load_model()
    return weights

result = load_model()
print(result)       # "loading..."
print(weights)      # NameError — 'weights' doesn't exist here
```

**Rule:** A function can *read* global variables but cannot *reassign* them
without the `global` keyword (which you should almost never use).

```python
count = 0

def increment():
    count = count + 1   # UnboundLocalError — Python sees assignment → treats as local
                        # but 'count' doesn't exist locally yet

def increment_correctly():
    global count        # declares intent to modify the global
    count = count + 1   # now works — but avoid this pattern in real code
```

**Better pattern:** pass values in and return new values out.
Never rely on global state.

---

## Default Parameters

```python
def train(epochs: int = 10, lr: float = 0.001, verbose: bool = True) -> None:
    ...

train()                        # uses all defaults
train(epochs=20)               # override one
train(epochs=20, lr=0.0003)    # override two
train(5, 0.01, False)          # positional — order matters
```

Required parameters must come before optional (defaulted) ones:

```python
def func(required, optional=10):   # valid
def func(optional=10, required):   # SyntaxError
```

---

## The Mutable Default Trap

This is one of the most common Python bugs and a frequent interview question.

```python
# WRONG — the list [] is created ONCE when the function is defined
# and reused across every call that doesn't pass a batch
def collect(sample, batch=[]):
    batch.append(sample)
    return batch

print(collect("img_001"))   # ['img_001']   — looks fine
print(collect("img_002"))   # ['img_001', 'img_002']  — BUG: shared state!

# CORRECT — use None as the default, create fresh inside
def collect(sample, batch=None):
    if batch is None:
        batch = []
    batch.append(sample)
    return batch

print(collect("img_001"))   # ['img_001']
print(collect("img_002"))   # ['img_002']   — correct
```

**Why it happens:** default values are evaluated once at function *definition*
time, not at call time. Mutable objects (list, dict) keep accumulating.

**Fix:** always use `None` as the default for mutable parameters.

---

## Multiple Return Values

Python functions can return multiple values as a tuple:

```python
def evaluate(predictions, labels):
    accuracy = sum(p == l for p, l in zip(predictions, labels)) / len(labels)
    loss = 1.0 - accuracy   # simplified
    return accuracy, loss   # returns a tuple

acc, loss = evaluate([1, 0, 1], [1, 1, 1])   # unpacking
print(f"Accuracy: {acc:.1%}  Loss: {loss:.4f}")
```

---

## Type Hints and Docstrings

Type hints don't enforce types at runtime — they're documentation
for humans and tools (mypy, your IDE).

```python
def load_checkpoint(
    path: str,
    device: str = "cpu",
    strict: bool = True,
) -> dict:
    """
    Load model weights from a checkpoint file.

    Args:
        path: Path to the .pt or .pth checkpoint file.
        device: Target device ('cpu' or 'cuda').
        strict: Whether to require exact key matching.

    Returns:
        State dict loaded from the checkpoint.
    """
    ...
```

This is the format you'll use in every real project. Learn it now.

---

## *args and **kwargs

When you don't know how many arguments will be passed:

```python
def log(*messages: str, **context) -> None:
    """Accept any number of messages and optional key-value context."""
    text = " ".join(messages)
    extras = ", ".join(f"{k}={v}" for k, v in context.items())
    print(f"[LOG] {text}" + (f" | {extras}" if extras else ""))

log("Training started")
log("Epoch done", epoch=5, loss=0.042)
log("Warning", "low memory", device="cuda", free_mb=200)
```

- `*args` collects extra positional arguments into a **tuple**
- `**kwargs` collects extra keyword arguments into a **dict**
- The names `args` and `kwargs` are convention — the `*` and `**` are what matter

---

## Common Mistakes

**Forgetting `return`**
```python
def add(a, b):
    result = a + b
    # forgot return — function returns None

total = add(2, 3)
print(total * 2)   # TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
```

**Calling before defining**
```python
result = compute()   # NameError — compute doesn't exist yet

def compute():
    return 42
```
Fix: define all functions first, call at the end. Use a `main()` entry point.

**Modifying a mutable argument**
```python
def normalize_labels(labels: list) -> list:
    labels.append("unknown")   # modifies the CALLER's list — bug
    return labels
```
Fix: work on a copy: `labels = labels.copy()` or `labels = list(labels)` at the start.

---

## Folder Structure

```
05_functions/
├── README.md          ← you are here
├── notes.md           ← fill in after exercises
├── test.py            ← run to verify understanding
│
├── examples/
│   ├── 01_normalize_and_hints.py    — def, return, type hints, docstring
│   ├── 02_flexible_logger.py        — *args, **kwargs, multiple returns
│   └── 03_scope_and_defaults.py     — scope, mutable default trap, main()
│
├── exercises/
│   ├── 01_metric_calculator.py      — Easy: write functions with type hints
│   ├── 02_pipeline_builder.py       — Medium: *args/**kwargs + multiple returns
│   └── 03_scope_and_state.py        — Hard: scope reasoning + mutable trap fix
│
└── solutions/
    ├── 01_metric_calculator.py
    ├── 02_pipeline_builder.py
    └── 03_scope_and_state.py
```

---

## Connection to the AI Journey

In Phase 7 you'll write code like this:

```python
def train_epoch(
    model,
    dataloader,
    optimizer,
    device: str = "cuda",
    log_every: int = 10,
) -> tuple[float, float]:
    """Run one training epoch. Returns (avg_loss, avg_accuracy)."""
    total_loss, total_correct, total_samples = 0.0, 0, 0

    for batch_idx, (inputs, labels) in enumerate(dataloader):
        inputs, labels = inputs.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()
        total_correct += (outputs.argmax(1) == labels).sum().item()
        total_samples += len(labels)

        if batch_idx % log_every == 0:
            print(f"  Batch {batch_idx} | loss: {loss.item():.4f}")

    return total_loss / len(dataloader), total_correct / total_samples
```

Every concept from this topic is in that function:
type hints, default parameters, multiple return values, docstring,
local scope, and no global state. Learn them right once.

---

*Next → [06 — Classes and Objects](../06_classes_intro/)*