# Phase 1 — Python Fundamentals

> Build the mental model: how Python thinks, manages memory, and structures programs.

This phase covers the full foundation — not just syntax, but the reasoning behind
how Python works. Every topic includes a concept explanation, real-world examples
grounded in AI/ML contexts, and exercises that push past surface-level understanding.

---

## Status

**Boot.dev chapters: 12 / 12 complete ✅**
**Repo topics: 11 done · 7 remaining (optional, do alongside Phase 2)**

---

## Boot.dev Alignment

| Boot.dev | Repo Topic | Status |
|---------|------------|--------|
| Ch 1: Introduction | `01_printing` | ✅ |
| Ch 2: Variables | `02_variables_data_types` | ✅ |
| Ch 3 + 4: Functions + Scope | `05_functions` | ✅ |
| Ch 5: Testing & Debugging | `00_debugging` | ✅ |
| Ch 6 + 7: Computing + Comparisons | `03_operators` + `04_control_flow` | ✅ |
| Ch 8: Loops | `04_control_flow` | ✅ (absorbed) |
| Ch 9: Lists | `08_lists` | ✅ |
| Ch 10 + 11: Dicts + Sets | `12_dicts_sets` | ✅ |
| Ch 12: Errors | `15_exceptions` | ✅ |
| Ch 13: Practice | — | ✅ (absorbed into exercises) |
| Ch 14: Quiz | — | ✅ (absorbed into test.py) |

---

## All Topics

| # | Topic | Boot.dev | Priority | Status |
|---|-------|----------|----------|--------|
| 00 | [Debugging](./00_debugging/) | Ch 5 | Reference | ✅ Done |
| 01 | [Printing](./01_printing/) | Ch 1 | — | ✅ Done |
| 02 | [Variables and Data Types](./02_variables_data_types/) | Ch 2 | — | ✅ Done |
| 03 | [Operators](./03_operators/) | Ch 6–7 | — | ✅ Done |
| 04 | [Control Flow](./04_control_flow/) | Ch 7–8 | — | ✅ Done |
| 05 | [Functions](./05_functions/) | Ch 3–4 | — | ✅ Done |
| 06 | [Classes and Objects](./06_classes_intro/) | No Boot.dev | — | ✅ Done |
| 07 | [Memory and Mutability](./07_memory_mutability/) | No Boot.dev | — | ✅ Done |
| 08 | [Lists](./08_lists/) | Ch 9 | — | ✅ Done |
| 09 | [Tuples](./09_tuples/) | No Boot.dev | 🟡 Anytime | 🔲 |
| 10 | [Strings](./10_strings/) | No Boot.dev | 🟡 Anytime | 🔲 |
| 11 | [Nested Lists](./11_nested_lists/) | No Boot.dev | 🟡 Anytime | 🔲 |
| 12 | [Dictionaries and Sets](./12_dicts_sets/) | Ch 10–11 | — | ✅ Done |
| 13 | [Modules and Packages](./13_modules_packages/) | No Boot.dev | 🟢 Parallel | 🔲 |
| 14 | [File I/O](./14_file_io/) | No Boot.dev | 🟢 Parallel | 🔲 |
| 15 | [Exceptions](./15_exceptions/) | Ch 12 | — | ✅ Done |
| 16 | [Advanced Functions](./16_advanced_functions/) | No Boot.dev | 🟢 Parallel | 🔲 |
| 17 | [Recursion](./17_recursion/) | No Boot.dev | 🟢 Parallel | 🔲 |

### Priority Legend
- 🟡 **Anytime** — complete during or after Phase 2, does not block anything
- 🟢 **Parallel** — do alongside Phase 2, or batch after finishing it

---

## Phase 1 is Complete — Start Phase 2

All Boot.dev chapters are done. Classes and memory are done.
You have everything you need to open `02_oop/`.

The 7 remaining topics (09, 10, 11, 13, 14, 16, 17) don't block OOP.
Do one per week alongside Phase 2, or batch them after finishing it.
Use `SKILL_NOOBOOTDEV.md` to generate any of them in a new chat.

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

Exception: `00_debugging` is a reference folder — `README.md` + one example only.

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

All of these should be answerable from memory before opening Phase 2:

- [x] Write a function with type hints, a docstring, and a mutable default fix
- [x] Build a class with `__init__`, `__str__`, and two methods
- [x] Explain the difference between `is` and `==` with a concrete example
- [x] Explain shallow vs deep copy and show when each is needed
- [x] Write a list comprehension with a filter condition
- [x] Count item frequencies in a list using a dict
- [x] Use a set to find items in one list but not another
- [x] Handle a missing key with `.get()` and a missing file with `try/except`
- [x] Explain the aliasing bug and fix it with `.copy()` or `deepcopy()`
- [x] Explain the difference between mutable and immutable types

---

→ [Phase 2 — Object-Oriented Programming](../02_oop/)