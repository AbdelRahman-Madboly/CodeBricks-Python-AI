# CodeBricks · Python → AI/ML

A structured, self-paced learning repository for going from Python fundamentals
to production-ready AI/ML engineering. Built around the principle that
understanding *why* code works matters more than memorizing *how* to write it.

---

## Roadmap

```
Phase 1 ──► Phase 2 ──► Phase 3 ──► Phase 4 ──► Phase 5 ──► Phase 6 ──► Phase 7 ──► Phase 8
Basics      OOP         Pythonic    Std Lib     Quality     Data Sci    AI/ML       Projects
3 weeks     2 weeks     1 week      1 week      1 week      2 weeks     4 weeks     2 weeks
  ✅ Done
```

---

### 🧱 Phase 1 — Python Fundamentals `✅ Complete`
> Build the mental model: how Python thinks, manages memory, and structures programs.

| # | Topic | Status |
|---|-------|--------|
| 01 | [Printing](./01_basics/01_printing/) | ✅ |
| 02 | [Variables and Data Types](./01_basics/02_variables_data_types/) | ✅ |
| 03 | [Operators](./01_basics/03_operators/) | ✅ |
| 04 | [Control Flow](./01_basics/04_control_flow/) | ✅ |
| 05 | [Functions](./01_basics/05_functions/) | ✅ |
| 06 | [Classes and Objects](./01_basics/06_classes_intro/) | ✅ |
| 07 | [Memory and Mutability](./01_basics/07_memory_mutability/) | ✅ |
| 08 | [Lists](./01_basics/08_lists/) | ✅ |
| 09 | [Tuples](./01_basics/09_tuples/) | ✅ |
| 10 | [Strings](./01_basics/10_strings/) | ✅ |
| 11 | [Nested Lists](./01_basics/11_nested_lists/) | ✅ |
| 12 | [Dictionaries and Sets](./01_basics/12_dicts_sets/) | ✅ |
| 13 | [Modules and Packages](./01_basics/13_modules_packages/) | ✅ |
| 14 | [File I/O](./01_basics/14_file_io/) | ✅ |
| 15 | [Exceptions](./01_basics/15_exceptions/) | ✅ |
| 16 | [Advanced Functions](./01_basics/16_advanced_functions/) | ✅ |
| 17 | [Recursion](./01_basics/17_recursion/) | ✅ |

---

### 🔷 Phase 2 — Object-Oriented Programming `(~2 weeks)`
> Learn to model real systems, not just write classes for the sake of it.

- Class internals: name mangling, `@property`, static vs class methods
- Namespaces and the MRO (Method Resolution Order)
- Inheritance: single, multilevel, multiple, `super()`
- Polymorphism: duck typing, operator overloading, abstract base classes
- OOP design: SOLID principles, composition vs inheritance
- UML: reading and sketching class diagrams

---

### ⚡ Phase 3 — Pythonic Patterns `(~1 week)`
> Write code that experienced Python engineers actually respect.

- Comprehensions: list, dict, set, generator expressions
- Generators and `yield`: lazy evaluation, memory efficiency
- Decorators: function wrappers, `functools`, parameterized decorators
- Context managers: `with` statement, `__enter__ / __exit__`, `contextlib`

---

### 📦 Phase 4 — Standard Library `(~1 week)`
> Stop reinventing what Python already ships with.

- `datetime` and `time`: parsing, formatting, timezones
- `os` and `pathlib`: filesystem operations
- `re`: regular expressions for real-world text processing
- `json` and `csv`: data serialization and parsing
- `threading` and `concurrent.futures`: parallelism basics

---

### ✅ Phase 5 — Code Quality `(~1 week)`
> Write code you can maintain six months from now.

- Type hints and `mypy`: annotating functions and data structures
- `pydantic`: runtime validation and settings management
- `pytest`: unit tests, fixtures, parametrize, mocking
- `ruff`: linting and formatting at scale

---

### 📊 Phase 6 — Data Science Foundation `(~2 weeks)`
> The bridge between Python engineering and AI/ML work.

- `numpy`: vectorized operations, broadcasting, linear algebra
- `pandas`: DataFrames, groupby, merging, time series
- `matplotlib` / `seaborn`: visualization for exploration and reporting

---

### 🤖 Phase 7 — AI/ML Engineering `(~4 weeks)`
> Go from toy examples to understanding what production ML actually looks like.

- ML concepts: bias/variance, overfitting, cross-validation, metrics
- `scikit-learn`: pipelines, preprocessing, model selection
- Deep learning: neural network fundamentals, backpropagation
- `PyTorch`: tensors, autograd, building and training networks
- Transformers and `HuggingFace`: fine-tuning, inference, embeddings
- Computer vision basics: image processing, CNNs, feature extraction

---

### 🚀 Phase 8 — Projects `(~2 weeks)`
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
│
├── README.md
├── LEARNING_PLAN.md
├── PROGRESS.md
│
├── 01_basics/            ✅ complete — 17 topics
├── 02_oop/               🔲 next
├── 03_pythonic/
├── 04_standard_library/
├── 05_typing_quality/
├── 06_data_science/
├── 07_ai_ml_path/
├── 08_projects/
│
└── notebooks/
```

Each topic folder contains:

```
<topic>/
├── README.md      — concept, mental model, common mistakes, interview angle
├── examples.py    — 3 clean real-world examples, fully commented
├── exercises.py   — 3 exercises at increasing difficulty, no solutions
├── solutions.py   — open only after attempting
└── notes.md       — personal notes template
```

---

## Philosophy

**Think like an engineer, not a syntax memorizer.**

- Understand the *why* before the *how* — a concept understood at the design level transfers to any language
- Code review your own work as if you're the person who inherits it in six months
- Connect every pattern to a real problem — if you can't describe the use case, you don't understand the tool
- Difficult exercises are features, not obstacles — resistance is where the learning happens
- Shipping imperfect code and fixing it beats studying perfect code and shipping nothing

---

## Getting Started

```bash
git clone https://github.com/AbdelRahman-Madboly/CodeBricks-Python-AI.git
cd CodeBricks-Python-AI
python setup_repo.py
```

Python 3.11+ recommended. No external dependencies required for phases 1–5.

---

## Progress

Track your progress in [`PROGRESS.md`](./PROGRESS.md).
Suggested pace: one topic folder per day for phases 1–5, slower and more deliberate for phases 6–8.
