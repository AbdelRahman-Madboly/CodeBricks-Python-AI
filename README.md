# CodeBricks · Python → AI/ML

A structured, self-documented learning repository for going from Python fundamentals
to production-ready AI/ML engineering. Built around the principle that understanding
*why* code works matters more than memorizing *how* to write it.

**GitHub:** [AbdelRahman-Madboly/CodeBricks-Python-AI](https://github.com/AbdelRahman-Madboly/CodeBricks-Python-AI)

---

## Roadmap

```
Phase 1 ──► Phase 2 ──► Phase 3 ──► Phase 4 ──► Phase 5 ──► Phase 6 ──► Phase 7 ──► Phase 8
Basics      OOP         Pythonic    Std Lib     Quality     Data Sci    AI/ML       Projects
3 weeks     2 weeks     1 week      1 week      1 week      3 weeks     4 weeks     2 weeks
🔲 Active
```

---

## Phase 1 — Python Fundamentals `🔲 In Progress`
 
> Build the mental model: how Python thinks, manages memory, and structures programs.
 
| # | Topic | Boot.dev | Status |
|---|-------|----------|--------|
| 00 | [Debugging](./01_basics/00_debugging/) | Ch 5 | ✅ Done |
| 01 | [Printing](./01_basics/01_printing/) | Ch 1 | ✅ Done |
| 02 | [Variables and Data Types](./01_basics/02_variables_data_types/) | Ch 2 | ✅ Done |
| 03 | [Operators](./01_basics/03_operators/) | Ch 6–7 | ✅ Done |
| 04 | [Control Flow](./01_basics/04_control_flow/) | Ch 7–8 | ✅ Done |
| 05 | [Functions](./01_basics/05_functions/) | Ch 3–4 | ✅ Done |
| 06 | [Classes and Objects](./01_basics/06_classes_intro/) | — | 🔲 |
| 07 | [Memory and Mutability](./01_basics/07_memory_mutability/) | — | 🔲 |
| 08 | [Lists](./01_basics/08_lists/) | Ch 9 | ✅ Done |
| 09 | [Tuples](./01_basics/09_tuples/) | — | 🔲 |
| 10 | [Strings](./01_basics/10_strings/) | — | 🔲 |
| 11 | [Nested Lists](./01_basics/11_nested_lists/) | — | 🔲 |
| 12 | [Dictionaries and Sets](./01_basics/12_dicts_sets/) | Ch 10–11 | 🔲 |
| 13 | [Modules and Packages](./01_basics/13_modules_packages/) | — | 🔲 |
| 14 | [File I/O](./01_basics/14_file_io/) | — | 🔲 |
| 15 | [Exceptions](./01_basics/15_exceptions/) | Ch 12 | 🔲 |
| 16 | [Advanced Functions](./01_basics/16_advanced_functions/) | — | 🔲 |
| 17 | [Recursion](./01_basics/17_recursion/) | — | 🔲 |
 
---

## Phase 2 — Object-Oriented Programming `🔲 Not started`

> Learn to model real systems, not just write classes for the sake of it.

- Class internals: name mangling, `@property`, static vs class methods
- Namespaces and the MRO (Method Resolution Order)
- Inheritance: single, multilevel, multiple, `super()`
- Polymorphism: duck typing, operator overloading, abstract base classes
- OOP design: SOLID principles, composition vs inheritance
- UML: reading and sketching class diagrams

---

## Phase 3 — Pythonic Patterns `🔲 Not started`

> Write code that experienced Python engineers actually respect.

- Comprehensions: list, dict, set, generator expressions
- Generators and `yield`: lazy evaluation, memory efficiency
- Decorators: function wrappers, `functools`, parameterized decorators
- Context managers: `with` statement, `__enter__/__exit__`, `contextlib`

---

## Phase 4 — Standard Library `🔲 Not started`

> Stop reinventing what Python already ships with.

- `datetime` and `time`: parsing, formatting, timezones
- `os` and `pathlib`: filesystem operations
- `re`: regular expressions for real-world text processing
- `json` and `csv`: data serialization and parsing
- `threading` and `concurrent.futures`: parallelism basics

---

## Phase 5 — Code Quality `🔲 Not started`

> Write code you can maintain six months from now.

- Type hints and `mypy`: annotating functions and data structures
- `pydantic`: runtime validation and settings management
- `pytest`: unit tests, fixtures, parametrize, mocking
- `ruff`: linting and formatting at scale

---

## Phase 6 — Data Science Foundation `🔲 Not started`

> The bridge between Python engineering and AI/ML work.

- `numpy`: vectorized operations, broadcasting, linear algebra
- `pandas`: DataFrames, groupby, merging, time series
- `matplotlib` / `seaborn`: visualization for exploration and reporting

---

## Phase 7 — AI/ML Engineering `🔲 Not started`

> Go from toy examples to understanding what production ML actually looks like.

- ML concepts: bias/variance, overfitting, cross-validation, metrics
- `scikit-learn`: pipelines, preprocessing, model selection
- Deep learning: neural network fundamentals, backpropagation
- `PyTorch`: tensors, autograd, building and training networks
- Transformers and `HuggingFace`: fine-tuning, inference, embeddings
- Computer vision: image processing, CNNs, feature extraction, deepfake detection

---

## Phase 8 — Projects `🔲 Not started`

> Ship things. Broken code in production teaches more than perfect code in a notebook.

- CLI data pipeline with type-safe configuration
- REST API with FastAPI and Pydantic models
- ML classification project with full training and evaluation loop
- Transformer fine-tuning for a domain-specific NLP task
- Computer vision project (deepfake detection pipeline)

---

## Repository Structure

```
CodeBricks-Python-AI/
├── README.md
├── LEARNING_PLAN.md
├── PROGRESS.md
├── SKILL.md             ← paste into any new chat to generate the next topic
├── GIT_GUIDE.md
│
├── 01_basics/
│   ├── 00_debugging/    ✅  (reference — README + example only)
│   ├── 01_printing/     ✅
│   ├── 02_variables_data_types/  ✅
│   ├── 03_operators/    ✅
│   ├── 04_control_flow/ ✅
│   ├── 05_functions/    ✅
│   ├── 06_classes_intro/
│   ├── 07_memory_mutability/
│   ├── 08_lists/        ✅
│   └── 09–17 ...
│
│
├── 02_oop/
├── 03_pythonic/
├── 04_standard_library/
├── 05_typing_quality/
├── 06_data_science/
├── 07_ai_ml_path/
└── 08_projects/
```

Each topic folder contains:

```
<topic>/
├── README.md       — concept, mental model, AI connection, common mistakes
├── notes.md        — personal learning journal
├── test.py         — run with python test.py, no external dependencies
├── examples/       — 3 AI-grounded examples, one file each
├── exercises/      — 3 exercises at increasing difficulty, one file each
└── solutions/      — solutions with "why this works" explanations
```

---

## Philosophy

**Think like an engineer, not a syntax memorizer.**

- Understand the *why* before the *how* — a concept understood at design level
  transfers to any language or framework
- Every example is grounded in AI/ML work — no abstract "calculate the area of a circle"
- Code review your own work as if you're the person who inherits it in six months
- Connect every pattern to a real problem — if you can't describe the use case,
  you don't fully understand the tool
- Difficult exercises are features, not obstacles — resistance is where learning happens
- Shipping imperfect code and fixing it beats studying perfect code and shipping nothing

---

## Getting Started

```bash
git clone https://github.com/AbdelRahman-Madboly/CodeBricks-Python-AI.git
cd CodeBricks-Python-AI
```

Python 3.11+ recommended. No external dependencies for Phases 1–5.

Track your progress in [`PROGRESS.md`](./PROGRESS.md).
See the full schedule in [`LEARNING_PLAN.md`](./LEARNING_PLAN.md).
Use [`SKILL.md`](./SKILL.md) to generate new topic folders in a new chat.