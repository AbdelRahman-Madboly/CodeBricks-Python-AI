# Phase 1 — Python Fundamentals

> Build the mental model: how Python thinks, manages memory, and structures programs.

This phase covers the full foundation — not just syntax, but the reasoning behind
how Python works. Every topic includes a concept explanation, real-world examples
grounded in AI/ML contexts, and exercises that push past surface-level understanding.

---

## Boot.dev Alignment

These topics map directly to the Boot.dev Python course chapters:

| Boot.dev Chapter | Repo Topic |
|-----------------|------------|
| Ch 1: Introduction | 01_printing |
| Ch 2: Variables | 02_variables_data_types |
| Ch 3: Functions + Ch 4: Scope | 05_functions |
| Ch 6: Computing + Ch 7: Comparisons | 03_operators |
| Ch 8: Loops | 04_control_flow |
| Ch 9: Lists | 08_lists |
| Ch 10: Dictionaries + Ch 11: Sets | 12_dicts_sets |
| Ch 12: Errors | 15_exceptions |

---

## Topics

| # | Topic | Boot.dev | Key Concept | Interview Relevance |
|---|-------|----------|-------------|---------------------|
| 01 | [Printing](./01_printing/) | Ch 1 | `print()`, f-strings, sep, end, formatting | Low — but fluency is noticed |
| 02 | [Variables and Data Types](./02_variables_data_types/) | Ch 2 | Dynamic typing, `type()`, `is` vs `==`, casting | Medium |
| 03 | [Operators](./03_operators/) | Ch 6–7 | Arithmetic, comparison, logical, short-circuit | Medium |
| 04 | [Control Flow](./04_control_flow/) | Ch 8 | `if/elif/else`, `while`, `for`, `for/else` | High — FizzBuzz, loop logic |
| 05 | [Functions](./05_functions/) | Ch 3–4 | Scope, `*args`, `**kwargs`, mutable defaults | High — mutable default trap |
| 06 | [Classes and Objects](./06_classes_intro/) | — | `__init__`, `self`, `__str__`, `__repr__` | High — OOP fundamentals |
| 07 | [Memory and Mutability](./07_memory_mutability/) | — | References, shallow vs deep copy | High — aliasing bugs |
| 08 | [Lists](./08_lists/) | Ch 9 | Slicing, comprehensions, `sort` vs `sorted` | High |
| 09 | [Tuples](./09_tuples/) | — | Immutability, unpacking, dict keys | Medium |
| 10 | [Strings](./10_strings/) | — | Methods, `join`, f-strings, immutability | High |
| 11 | [Nested Lists](./11_nested_lists/) | — | 2D indexing, `*` copy trap, transpose | High — matrix ops |
| 12 | [Dictionaries and Sets](./12_dicts_sets/) | Ch 10–11 | Hash tables, `.get()`, set operations | High — frequency counting |
| 13 | [Modules and Packages](./13_modules_packages/) | — | Import system, `__name__`, `pathlib` | Medium |
| 14 | [File I/O](./14_file_io/) | — | `with open()`, JSON, CSV, line iteration | Medium |
| 15 | [Exceptions](./15_exceptions/) | Ch 12 | `try/except/else/finally`, custom exceptions | High |
| 16 | [Advanced Functions](./16_advanced_functions/) | — | Closures, `partial`, `map`, `filter` | High — closures |
| 17 | [Recursion](./17_recursion/) | — | Base case, memoisation, `lru_cache` | High — tree traversal |

---

## Folder Structure (per topic)

```
<topic>/
├── README.md          — concept, mental model, AI connection, common mistakes
├── notes.md           — personal learning journal (fill in after exercises)
├── test.py            — run with 'python test.py', no external dependencies
│
├── examples/
│   ├── 01_<name>.py   — Easy example with AI/ML context, detailed comments
│   ├── 02_<name>.py   — Medium example, builds on example 1
│   └── 03_<name>.py   — Advanced example, forward-references noted
│
├── exercises/
│   ├── 01_<name>.py   — Easy: single concept, exact expected output shown
│   ├── 02_<name>.py   — Medium: combining 2–3 concepts
│   └── 03_<name>.py   — Hard: requires design thinking or scope reasoning
│
└── solutions/
    ├── 01_<name>.py   — Solution with "Why this works" explanation
    ├── 02_<name>.py
    └── 03_<name>.py
```

---

## How to Work Through Each Topic

1. Read `README.md` — understand the concept and the mental model before touching code
2. Open each `examples/` file — **predict the output** before running
3. Attempt each `exercises/` file — write your solution before looking at anything
4. Check `solutions/` — compare approaches, read the "why" explanations
5. Fill in `notes.md` — in your own words, not copied from the README
6. Run `test.py` — all tests should pass before you mark a topic complete

The notes step is the easiest to skip and the most valuable not to skip.

---

## Phase 1 Completion Checklist

You are ready to move to Phase 2 when you can do all of these from memory:

- [ ] Explain dynamic typing and give an example where it causes a bug
- [ ] Write a function with type hints, a docstring, and a mutable default fix
- [ ] Build a class with `__init__`, `__str__`, and two methods from memory
- [ ] Explain the difference between `is` and `==` with a concrete example
- [ ] Explain shallow vs deep copy and when each is needed
- [ ] Write a list comprehension with a filter condition
- [ ] Write a recursive function with a clear base case and memoisation
- [ ] Group a list of dicts by a key field using only a dict and a loop
- [ ] Parse a JSON file and handle `FileNotFoundError` gracefully
- [ ] Explain what a closure is and write one from scratch

---

## Key Patterns to Carry Forward

These appear in every phase and every real project:

```python
# Mutable default fix
def func(items=None):
    if items is None:
        items = []

# Safe dict access
value = d.get("key", default)

# Frequency counting
counts = {}
for item in data:
    counts[item] = counts.get(item, 0) + 1

# Safe file loading with exception handling
try:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    data = {}

# main() entry point pattern
def main():
    ...   # all logic here

if __name__ == "__main__":
    main()
```

---

→ [Phase 2 — Object-Oriented Programming](../02_oop/)