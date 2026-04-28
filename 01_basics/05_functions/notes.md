# 05 — Functions | notes.md

> Fill this in after finishing the exercises.
> Write in your own words. If you can explain it here, you own it.

---

## What clicked immediately

<!-- What felt natural as soon as you saw it? -->



---

## What took time

<!-- What confused you? How did you work through it? -->



---

## My questions — answered

---

### Q: What is the difference between a parameter and an argument?

**Parameter** = the name in the function *definition*.
**Argument** = the actual *value* you pass when *calling* the function.

```python
def greet(name: str) -> str:   # 'name' is a parameter
    return f"Hello, {name}"

greet("Abdelrahman")           # "Abdelrahman" is an argument
```

In practice, developers use these words interchangeably.
The distinction matters most in documentation and interview settings.

---

### Q: What is scope and why does it matter?

Scope defines where a name (variable, function) is visible.

Python has four scope levels (LEGB rule):
- **L**ocal — inside the current function
- **E**nclosing — in any surrounding function (closures — topic 16)
- **G**lobal — at the module (file) level
- **B**uilt-in — Python's built-ins (print, len, range, etc.)

When you use a name, Python searches in that order: L → E → G → B.

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)    # "local" — found in L
    inner()
    print(x)        # "enclosing" — found in E (inner's L is gone)

outer()
print(x)            # "global" — found in G
```

**Why it matters for AI work:**
Training scripts often have global config (learning rate, batch size).
Functions should read those if needed but never reassign them.
Instead, pass values in and return values out — keeps functions predictable.

---

### Q: Why does Python create a local scope for each function call?

When Python calls a function, it creates a new **frame** — a private
namespace (dictionary of name → object mappings) for that call.

```python
def add(a, b):
    result = a + b   # 'result' lives in this frame only
    return result

add(2, 3)   # frame created: {a: 2, b: 3, result: 5}
            # frame destroyed: result is gone
add(10, 20) # new frame: {a: 10, b: 20, result: 30}
```

Each call gets its own frame. This is what makes recursion work —
each recursive call has its own copies of all local variables
(you'll explore this in topic 17).

---

### Q: Why does Python mark a variable as local if I assign to it anywhere in the function?

This is a compile-time decision. When Python reads the `def` block,
it scans for any assignment statements. If it finds `x = ...` anywhere
in the function, it marks `x` as local for the **entire** function —
even lines that come before the assignment.

```python
x = 10

def f():
    print(x)   # line A — tries to read x
    x = 99     # line B — assignment makes x local for the whole function
    print(x)   # line C

f()
# UnboundLocalError at line A
# Python marked x as local because of line B
# But at line A, the local x hasn't been assigned yet
```

This surprises most developers. The fix: pass `x` as a parameter.

---

### Q: When should a function print vs return?

**Return** when the value will be used elsewhere — stored, compared,
passed to another function, formatted differently. This is almost always.

**Print** (return None) only when the function's entire purpose is
producing output — a logger, a display function, a progress reporter.

```python
# This can't be composed — loss is None
def compute_loss():
    loss = 0.043
    print(loss)   # side effect only

total = compute_loss() + compute_loss()   # TypeError: NoneType + NoneType

# This can be composed — loss is usable
def compute_loss() -> float:
    return 0.043

total = compute_loss() + compute_loss()   # 0.086
```

Rule of thumb: if you're tempted to print inside a function, ask
"does the caller need this value?" If yes → return it.

---

### Q: What exactly is the mutable default trap and why does Python work this way?

Default parameter values are evaluated **once**, when the `def` statement
is executed — not each time the function is called.

```python
def f(items=[]):   # [] is created once, right here, at def time
    items.append(1)
    return items

print(id(f.__defaults__[0]))   # the default list's memory address
f()
f()
print(id(f.__defaults__[0]))   # same address — same object
```

Python stores default values in `function.__defaults__` — a tuple
attached to the function object. Mutable defaults accumulate changes
because they're the same object every time.

**Why Python works this way:**
It's a consequence of functions being first-class objects. The defaults
are created with the function, not with each call. For immutable defaults
(int, str, None) this doesn't matter — they can't be changed in-place.
For mutable defaults (list, dict, set) it causes shared state.

**The fix pattern:**
```python
def f(items=None):
    if items is None:
        items = []   # fresh object created here, at call time
    items.append(1)
    return items
```

---

### Q: What is `pass` and when do you use it?

`pass` is a no-op statement — it does nothing. It's a placeholder
for code you haven't written yet.

```python
def train():
    pass   # I'll implement this later

class Model:
    pass   # empty class — valid syntax

if condition:
    pass   # handle this case later
```

Python requires at least one statement in a block (function body,
class body, if branch, etc.). `pass` satisfies that requirement
without doing anything.

In real code, `pass` in a function body is a sign it's not implemented.
You'll sometimes see `raise NotImplementedError()` instead —
that's more honest: it crashes loudly if someone calls the stub.

---

## Connections to other topics

<!-- How does this connect to Boot.dev or things you've seen before? -->
<!-- Example: "main() reminds me of int main() in C++" -->



---

## Things to revisit later

- [ ] Closures — functions that capture variables from an enclosing scope — topic 16
- [ ] `functools.partial` — pre-filling function arguments — topic 16
- [ ] `*args` unpacking when calling: `f(*my_list)` — topic 16
- [ ] Type hints for complex types (`list[int]`, `tuple[float, float]`) — Phase 5
- [ ] `global` and `nonlocal` keywords — exist but should almost never be used
- [ ] How frames work in the call stack — connects to recursion (topic 17)

---

## One-line summary

> In one sentence: what is a function and what problem does it solve?

<!-- Your words here -->