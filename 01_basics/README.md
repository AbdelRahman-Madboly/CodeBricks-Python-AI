# Phase 1 — Python Fundamentals

> Build the mental model: how Python thinks, manages memory, and structures programs.

This phase covers the full foundation — not just syntax, but the reasoning behind
how Python works. Every topic includes a concept explanation, real-world examples,
and exercises that push past surface-level understanding.

---

## Topics

| # | Topic | Key Concept | Interview Relevance |
|---|-------|-------------|---------------------|
| 01 | [Printing](./01_printing/) | `print()`, f-strings, formatting | Low — but fluency is noticed |
| 02 | [Variables and Data Types](./02_variables_data_types/) | Dynamic typing, `type()`, `is` vs `==` | Medium — `is` vs `==`, float precision |
| 03 | [Operators](./03_operators/) | Short-circuit logic, `//`, `%`, `**` | Medium — `or` as default pattern |
| 04 | [Control Flow](./04_control_flow/) | `if/elif/else`, `while`, `for`, `for/else` | High — FizzBuzz, loop logic |
| 05 | [Functions](./05_functions/) | Scope, `*args`, `**kwargs`, mutable defaults | High — mutable default trap |
| 06 | [Classes and Objects](./06_classes_intro/) | `__init__`, `self`, `__str__`, `__repr__` | High — OOP fundamentals |
| 07 | [Memory and Mutability](./07_memory_mutability/) | References, shallow vs deep copy | High — aliasing bugs |
| 08 | [Lists](./08_lists/) | Slicing, comprehensions, `sort` vs `sorted` | High — O(n) vs O(1) operations |
| 09 | [Tuples](./09_tuples/) | Immutability, unpacking, dict keys | Medium — when to use tuple vs list |
| 10 | [Strings](./10_strings/) | Methods, `join`, f-strings, immutability | High — string reversal, palindrome |
| 11 | [Nested Lists](./11_nested_lists/) | 2D indexing, `*` copy trap, transpose | High — matrix operations |
| 12 | [Dictionaries and Sets](./12_dicts_sets/) | Hash tables, `.get()`, set operations | High — frequency counting |
| 13 | [Modules and Packages](./13_modules_packages/) | Import system, `__name__`, `pathlib` | Medium — `__name__ == "__main__"` |
| 14 | [File I/O](./14_file_io/) | `with open()`, JSON, line iteration | Medium — safe file handling |
| 15 | [Exceptions](./15_exceptions/) | `try/except/else/finally`, custom exceptions | High — exception hierarchy design |
| 16 | [Advanced Functions](./16_advanced_functions/) | Closures, `partial`, `map`, `filter` | High — closures, function composition |
| 17 | [Recursion](./17_recursion/) | Base case, memoisation, `lru_cache` | High — Fibonacci, tree traversal |

---

## How to Work Through Each Topic

1. Read `README.md` — understand the concept and the mental model before touching code
2. Run `examples.py` — read every comment, predict the output before running
3. Attempt `exercises.py` — write your solution before looking at anything else
4. Check `solutions.py` — only after a genuine attempt; compare approaches
5. Fill in `notes.md` — write what clicked, what confused you, and how it connects

The notes step is the one most people skip. It is also the one that makes the
difference between remembering something for a week and understanding it permanently.

---

## Phase 1 Checklist

Work through this before moving to Phase 2. You are ready when you can:

- [ ] Explain dynamic typing and give an example where it causes a bug
- [ ] Write a function with type hints, a docstring, and a mutable default trap fix
- [ ] Build a class with `__init__`, `__str__`, and at least two methods from memory
- [ ] Explain the difference between `is` and `==` with an example
- [ ] Explain shallow vs deep copy and when each is needed
- [ ] Write a list comprehension with a filter condition
- [ ] Write a recursive function with a clear base case and memoisation
- [ ] Group a list of dicts by a key field using only a dict and a loop
- [ ] Parse a JSON file and handle `FileNotFoundError` gracefully
- [ ] Explain what a closure is and write one from scratch

---

## Key Patterns to Carry Forward

These show up in every phase and every real project:

```python
# Safe dict access
value = d.get("key", default)

# Mutable default fix
def func(items=None):
    if items is None:
        items = []

# Frequency counting
counts = {}
for item in data:
    counts[item] = counts.get(item, 0) + 1

# Flatten a nested dict (recursion)
def flatten(d, prefix=""):
    ...

# Safe file loading
try:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    data = {}
```

---

## What Comes Next

Phase 2 builds directly on this foundation — particularly topics 06 (classes)
and 16 (advanced functions). If either of those feels shaky, revisit them before
moving on. OOP is where the real engineering thinking starts.

→ [Phase 2 — Object-Oriented Programming](../02_oop/)
