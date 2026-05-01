# Scope — Quick Reference

> This is a supplement to `05_functions/README.md`.
> Boot.dev covers scope as Chapter 4, but it's part of the same mental model
> as functions — variables defined inside a function don't exist outside it.

---

## The Core Rule

A variable only exists in the **scope** where it was created.

```python
def compute(x, y):
    result = x + y    # 'result' exists only inside compute()
    return result

print(result)         # NameError — 'result' doesn't exist here
```

When `compute()` returns, its local scope is destroyed.
`result`, `x`, and `y` are all gone.

---

## Global vs Local

```python
# Global scope — accessible everywhere
learning_rate = 0.001
model_name = "bert"

def train():
    # Local scope — only accessible here
    loss = 0.043
    print(f"Training {model_name} with lr={learning_rate}")  # reads globals — fine
    return loss

result = train()
print(result)   # 0.043 — returned value is now in global scope
print(loss)     # NameError — 'loss' was local to train()
```

---

## The Assignment Rule

Python decides at **parse time** whether a name is local or global.
If it sees any assignment (`=`) to a name inside a function,
that name is **local for the entire function** — including lines
before the assignment.

```python
count = 0

def broken():
    print(count)   # UnboundLocalError — Python marked count as local
    count = 99     # because of this assignment below

# Fix: pass the value in, return the new value out
def fixed(count: int) -> int:
    count = count + 1   # local count shadows the parameter — fine
    return count

count = fixed(count)
```

---

## Reading a Global vs Reassigning It

```python
MAX_EPOCHS = 50   # global constant

# Reading → always fine
def get_remaining(current_epoch: int) -> int:
    return MAX_EPOCHS - current_epoch   # reads global, doesn't assign

# Reassigning → requires 'global' keyword (almost never do this)
def reset_epochs():
    global MAX_EPOCHS   # declares intent to modify the global
    MAX_EPOCHS = 100    # works — but avoid this pattern

# Better: return new values instead of modifying globals
def with_more_epochs(current: int, extra: int) -> int:
    return current + extra
```

---

## Mutating a Global Object (Lists, Dicts)

Mutation (`.append`, `.update`, `[key] = value`) is NOT assignment.
Python finds the global object and modifies it in place.

```python
results = []

def record(accuracy: float) -> None:
    results.append(accuracy)   # mutation — finds global results, appends to it

record(0.82)
record(0.89)
print(results)   # [0.82, 0.89] — the global list was modified
```

This works — but it creates hidden dependencies between functions
and global state. Prefer passing the list in and returning it.

---

## Summary Table

| Action | Works? | Notes |
|--------|--------|-------|
| Read a global inside a function | ✅ | Python walks up to global scope |
| Reassign a global without `global` keyword | ❌ | Creates a local variable instead |
| Reassign a global with `global` keyword | ✅ | Works — but avoid in real code |
| Mutate a global list/dict | ✅ | Not assignment — finds and modifies the object |
| Access a local variable outside its function | ❌ | NameError — local scope is gone |
| Access a parameter outside its function | ❌ | Same — parameters are local |

---

## The Right Pattern

Don't fight scope. Work with it:

```python
# Instead of this (global state)
best_loss = float("inf")

def update_best(loss):
    global best_loss
    if loss < best_loss:
        best_loss = loss

# Do this (pass in, return out)
def update_best(loss: float, current_best: float) -> float:
    return loss if loss < current_best else current_best

best_loss = float("inf")
best_loss = update_best(0.043, best_loss)
best_loss = update_best(0.031, best_loss)
```

This makes `update_best` a **pure function** — its output depends
only on its inputs. Pure functions are easier to test, debug, and reuse.

---

*This concept is fully covered in `05_functions/` — see `README.md`,
`examples/03_scope_and_defaults.py`, and `exercises/03_scope_and_state.py`.*