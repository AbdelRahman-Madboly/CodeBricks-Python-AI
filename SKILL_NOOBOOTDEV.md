# CodeBricks — No-Boot.dev Topic Skill

> Use this file when generating topics that have NO Boot.dev chapter.
> These topics are pure Python concepts needed for AI/ML work.
> Upload this file to a new chat and specify which topic to generate.

---

## Context

**CodeBricks Python → AI/ML** — built by Abdelrahman Madboly.
GitHub: `https://github.com/AbdelRahman-Madboly/CodeBricks-Python-AI`
Local: `D:\CodeBricks\Python-AI`  |  Python: 3.11+

These topics have no Boot.dev chapter. All content must be generated
from the concept itself, grounded in AI/ML contexts.

---

## Topics to Generate (choose one per chat)

| Priority | Folder | Key concepts to cover |
|----------|--------|----------------------|
| 🔴 1 | `06_classes_intro` | `class`, `__init__`, `self`, instance vs class vars, `__str__`, `__repr__`, methods, `type()` |
| 🔴 2 | `07_memory_mutability` | `id()`, references vs values, aliasing bug, mutable vs immutable, `copy` vs `deepcopy`, `is` vs `==` |
| 🟡 3 | `09_tuples` | immutability, packing/unpacking, `*rest`, named tuple, when tuple beats list |
| 🟡 4 | `10_strings` | methods (`split`, `join`, `strip`, `replace`, `find`), immutability, f-strings advanced, slicing |
| 🟡 5 | `11_nested_lists` | 2D indexing, `*` copy trap, matrix ops, row/column iteration |
| 🟢 6 | `13_modules_packages` | `import`, `from x import y`, `__name__ == "__main__"`, `pathlib.Path`, `sys.path` |
| 🟢 7 | `14_file_io` | `with open()`, read/write/append modes, JSON load/dump, CSV, `FileNotFoundError` |
| 🟢 8 | `16_advanced_functions` | closures, `functools.partial`, `map`, `filter`, `lambda`, `*args`/`**kwargs` unpacking |
| 🟢 9 | `17_recursion` | base case, recursive case, call stack, memoisation, `functools.lru_cache`, tree traversal |

---

## What to Send to the New Chat

```
I'm building the CodeBricks Python → AI/ML repo.
Generate the full topic folder for `<folder_name>` (Phase 1, no Boot.dev source).

This topic has no Boot.dev chapter — generate the content from the concept itself.

Key concepts to cover:
<paste the "Key concepts" row from the table above>

Use the CodeBricks style:
- AI/ML context in every example and exercise
- examples/exercises/solutions as subfolders (one file each)
- README.md with concept, mental model, common mistakes, AI connection
- notes.md with questions answered and blank reflection sections
- test.py with 20+ tests, stdlib only
- Human comments that explain WHY, not what

Reference topic for style: 08_lists — examples used pipeline slicing,
enumerate/zip loops, comprehensions + shallow copy trap. Exercises had
increasing difficulty. Solutions had "Why this works" sections.
test.py had 38 tests covering all key behaviours.
```

---

## Full Folder Structure (every topic)

```
<number>_<topic_name>/
├── README.md
├── notes.md
├── test.py
├── examples/
│   ├── 01_<name>.py   — Easy, "What to notice" section
│   ├── 02_<name>.py   — Medium
│   └── 03_<name>.py   — Advanced, forward-references noted
├── exercises/
│   ├── 01_<name>.py   — Easy, exact expected output shown
│   ├── 02_<name>.py   — Medium
│   └── 03_<name>.py   — Hard
└── solutions/
    ├── 01_<name>.py   — Solution + "Why this works"
    ├── 02_<name>.py
    └── 03_<name>.py
```

---

## Style Rules (summary)

- **AI/ML context mandatory** — model configs, training logs, batch ops, pipeline stages
- **Comments explain why** — not what
- **Each example** ends with `# ── What to notice ──`
- **Each solution** ends with `# ── Why this works ──`
- **test.py** uses only stdlib, has `check(label, actual, expected)` helper
- **notes.md** answers questions about the concept, has "Things to revisit" checklist
- **Forward-references** noted with `# you'll learn this in topic XX`

---

## Per-Topic Concept Guide

### 06_classes_intro

```
What to cover:
  - class keyword, __init__, self
  - Instance variables vs class variables
  - Instance methods
  - __str__ (human-readable) vs __repr__ (developer-readable)
  - type() on instances
  - Calling methods: obj.method()
  - Why classes: grouping data + behaviour together

AI/ML examples:
  - ModelConfig class (stores lr, epochs, batch_size as instance vars)
  - DetectionResult class (__str__ formats the output for logging)
  - TrainingRun class (tracks epoch, loss, best_loss as state)

Notes questions to answer:
  - What is self and why is it always the first parameter?
  - What is the difference between __str__ and __repr__?
  - What is an instance variable vs a class variable?
  - What does __init__ actually do?
```

### 07_memory_mutability

```
What to cover:
  - id() — memory address, proves two names point to same object
  - Variables are labels, not boxes (reference model)
  - Mutable types: list, dict, set — can be changed in place
  - Immutable types: int, float, str, tuple — cannot be changed
  - Aliasing: a = b means both point to the same object
  - The aliasing bug: modifying a shared mutable object
  - Shallow copy: list[:], list.copy(), dict.copy() — new container, shared contents
  - Deep copy: copy.deepcopy() — fully independent copy
  - When is vs == matters: 'is' checks identity, '==' checks value

AI/ML examples:
  - Config aliasing bug (modifying a shared config dict affects both runs)
  - Image batch copy trap (modifying augmented batch affects original)
  - Accumulating results correctly with deepcopy

Notes questions to answer:
  - Why does a = b not create a copy?
  - What is the difference between shallow and deep copy?
  - Why does += on a list work differently than += on an int?
  - When should I use is vs ==?
```

### 09_tuples

```
What to cover:
  - Tuple literals: (a, b, c) and single-item: (a,)
  - Immutability — can't modify after creation
  - Packing and unpacking: a, b = (1, 2)
  - *rest unpacking: first, *rest = (1, 2, 3, 4)
  - Tuples as dict keys (lists can't be dict keys)
  - Returning multiple values from functions returns a tuple
  - collections.namedtuple — named access without a class
  - When to use tuple vs list

AI/ML examples:
  - Model evaluation returning (accuracy, f1, loss) as a tuple
  - Using (width, height) as a dict key for image dimension tracking
  - Unpacking batch (inputs, labels) in a training loop
```

### 10_strings

```
What to cover:
  - Immutability — strings can't be changed in place
  - Slicing (same syntax as lists)
  - .split(), .join(), .strip(), .lstrip(), .rstrip()
  - .replace(), .find(), .startswith(), .endswith()
  - .upper(), .lower(), .title()
  - .format() (older style — know it to read old code)
  - f-strings with format specs (:.2f, :>, :<, :,)
  - Multi-line strings with triple quotes
  - String methods return NEW strings — original unchanged
  - Palindrome pattern, reversal, contains check

AI/ML examples:
  - Parsing model names from a checkpoint filename
  - Cleaning and normalising text labels before training
  - Building prompt templates for LLMs
```

### 11_nested_lists

```
What to cover:
  - Creating 2D lists (lists of lists)
  - Row/column access: matrix[row][col]
  - The * copy trap: [[0]*3]*3 creates shared inner lists
  - Safe creation: [[0]*3 for _ in range(3)]
  - Row iteration, column iteration
  - Transpose: [[row[i] for row in matrix] for i in range(cols)]
  - Flattening: [x for row in matrix for x in row]

AI/ML examples:
  - Confusion matrix as a 2D list
  - Pixel grid for a small image
  - Batch of samples as a list of feature vectors
```

### 13_modules_packages

```
What to cover:
  - import module
  - from module import name
  - import module as alias
  - __name__ == "__main__" — why and when to use it
  - pathlib.Path — modern file paths, cross-platform
  - Creating your own module (a .py file)
  - The __init__.py convention for packages
  - sys.path — where Python looks for modules
  - Avoiding circular imports

AI/ML examples:
  - Structuring a project: data_loader.py, model.py, train.py
  - Using pathlib to build config paths portably
  - __name__ == "__main__" in a training script
```

### 14_file_io

```
What to cover:
  - with open(path, mode) as f — the safe way to open files
  - Modes: "r" (read), "w" (write), "a" (append), "rb"/"wb" (binary)
  - f.read(), f.readlines(), iterating line by line
  - f.write(), f.writelines()
  - json.load() / json.dump() — reading and writing JSON
  - csv.reader() / csv.writer() / csv.DictReader()
  - FileNotFoundError, PermissionError — safe handling
  - pathlib.Path for constructing file paths

AI/ML examples:
  - Loading a model config from a JSON file
  - Writing training metrics to a CSV log
  - Reading a dataset manifest file line by line
```

### 16_advanced_functions

```
What to cover:
  - First-class functions: functions as values, stored in variables
  - Closures: a function that captures variables from its enclosing scope
  - functools.partial: pre-filling arguments
  - map(func, iterable): apply a function to every item
  - filter(func, iterable): keep items where func returns True
  - lambda: anonymous single-expression function
  - Combining map/filter/lambda
  - Why closures matter: factories, callbacks, decorators (preview)

AI/ML examples:
  - partial to create metric functions with fixed thresholds
  - map to apply normalisation to a batch
  - Closure as a configurable loss function
```

### 17_recursion

```
What to cover:
  - What recursion is: a function that calls itself
  - Base case — the stopping condition
  - Recursive case — moving toward the base case
  - The call stack: how Python tracks recursive calls
  - Stack overflow (RecursionError) — when recursion goes too deep
  - Memoisation: caching results to avoid recomputation
  - functools.lru_cache — automatic memoisation
  - When to use recursion vs iteration
  - Classic examples: factorial, Fibonacci, tree traversal

AI/ML examples:
  - Recursive JSON config flattening (nested dicts → flat dict)
  - Tree traversal for a decision tree structure
  - Fibonacci with lru_cache showing the speed difference
```

---

## After Generating — Git Commit Format

```bash
git add 01_basics/<topic_folder>/
git commit -m "feat(01_basics): add <topic_folder> topic

- README: <key concepts covered>
- examples: <scenario 1>, <scenario 2>, <scenario 3>
- exercises: <exercise 1>, <exercise 2>, <exercise 3>
- solutions: with full 'why this works' explanations
- test.py: <N> tests covering <concepts>
- notes.md: answered — <questions>"

git push origin main
```
