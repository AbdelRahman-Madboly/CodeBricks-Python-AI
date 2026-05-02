# 04 — Control Flow | notes.md

> Fill this in after finishing the exercises.

---

## What clicked immediately



---

## What took time



---

## My questions — answered

---

### Q: What is the difference between if / elif / else?

```python
if condition_1:
    # runs if condition_1 is True
elif condition_2:
    # runs if condition_1 is False AND condition_2 is True
elif condition_3:
    # runs if all above are False AND condition_3 is True
else:
    # runs if ALL conditions above are False
```

**Only one branch runs.** Python checks top to bottom and stops the moment
it finds a True condition. The remaining branches are skipped entirely.

`elif` and `else` are both optional. You can have any number of `elif`s.
You can have `else` without any `elif`. You can't have `elif` without `if`.

---

### Q: What does range() actually produce?

`range()` is a lazy sequence — it doesn't create a list, it generates
numbers one at a time as the loop asks for them.

```python
range(5)           # 0, 1, 2, 3, 4     — stop only
range(2, 8)        # 2, 3, 4, 5, 6, 7  — start, stop
range(0, 10, 2)    # 0, 2, 4, 6, 8     — start, stop, step
range(10, 0, -1)   # 10, 9, 8, ... 1   — counting down
```

**Key fact:** `stop` is always exclusive — `range(5)` never produces 5.

To iterate with a 1-based index, use `range(1, n+1)` or `enumerate(items, start=1)`.

---

### Q: What is the difference between break and continue?

```python
for item in items:
    if bad_condition:
        continue    # skip THIS item, move to the NEXT one in the loop
    if stop_condition:
        break       # exit the ENTIRE loop now — no more iterations
    process(item)
```

`continue` — jumps to the top of the loop for the next iteration.
Code AFTER `continue` in the loop body is skipped for this iteration only.

`break` — exits the loop completely.
Code after the loop (outside it) still runs normally.

Both work in `while` and `for` loops with the same rules.

---

### Q: What is for/else and when should I use it?

```python
for item in collection:
    if found_it(item):
        break
else:
    # Runs ONLY if break never fired
    print("not found")
```

The `else` on a `for` loop runs when the loop **exhausted all items** without
hitting `break`. It does NOT run if `break` exited the loop.

**Important edge case:** if the collection is empty, the loop body never runs,
but the `else` still runs (the loop "exhausted" an empty sequence).

**When to use it:** search patterns where you need to report failure.
Without `for/else`, you need a flag variable:

```python
# Without for/else
found = False
for item in collection:
    if condition(item):
        found = True
        break
if not found:
    print("not found")

# With for/else — cleaner
for item in collection:
    if condition(item):
        break
else:
    print("not found")
```

---

### Q: What is a ternary expression?

A one-line if/else that produces a value:

```python
# Full form
if score >= 0.5:
    result = "pass"
else:
    result = "fail"

# Ternary — same thing
result = "pass" if score >= 0.5 else "fail"
```

Syntax: `value_if_true if condition else value_if_false`

Use for simple single-value choices. Avoid nesting ternaries —
use full `if/else` when the logic is complex.

---

### Q: How does a while loop know when to stop?

The `while` loop checks its condition **before each iteration**.
If the condition is False at the start, the loop body never runs.
The loop stops when the condition becomes False.

```python
count = 0
while count < 5:    # checked before every iteration
    print(count)
    count += 1      # must update the condition variable inside!
# If you forget count += 1, the loop runs forever
```

**Always** make sure something inside the loop will eventually make
the condition False — unless you're using `break` to exit explicitly.

```python
while True:          # always True — loop runs forever
    data = get_data()
    if data is None:
        break        # only way out
    process(data)
```

---

### Q: What does enumerate() actually do?

`enumerate()` wraps an iterable and yields `(index, value)` pairs:

```python
items = ["a", "b", "c"]

for i, item in enumerate(items):
    print(i, item)   # 0 a / 1 b / 2 c

for i, item in enumerate(items, start=1):
    print(i, item)   # 1 a / 2 b / 3 c
```

It's always better than maintaining a manual counter because:
- The counter can never get out of sync with the loop
- You can't forget to increment it
- The code reads as "index and value" — the intent is explicit

---

## Connections to other topics

<!-- How does this connect to things you've seen in Boot.dev or elsewhere? -->



---

## Things to revisit later

- [ ] List comprehensions — a compact for loop that builds a list — Phase 3
- [ ] Generator expressions — lazy version of list comprehensions — Phase 3
- [ ] `itertools` — advanced iteration tools (zip_longest, chain, etc.) — Phase 4
- [ ] `match/case` (structural pattern matching) — Python 3.10+ — advanced
- [ ] Walrus operator `:=` — assign and test in one expression — Phase 3
- [ ] `while True` with `break` — common pattern for event loops and servers

---

## One-line summary

> In one sentence: what does control flow do, and which construct do you
> think you'll use most in AI/ML work?

<!-- Your words here -->