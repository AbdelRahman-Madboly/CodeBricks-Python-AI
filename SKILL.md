# CodeBricks — Topic Generation Skill v3

> Upload this file to any new Claude chat.
> Paste the Boot.dev lesson content for the next topic.
> The chat will generate a complete, production-quality topic folder
> matching the CodeBricks style exactly.

---

## About This Repo

**CodeBricks Python → AI/ML** — built by Abdelrahman Madboly.
Self-documented learning repo covering Python fundamentals through AI/ML engineering.

- **GitHub:** `https://github.com/AbdelRahman-Madboly/CodeBricks-Python-AI`
- **Local:** `D:\CodeBricks\Python-AI`
- **Python:** 3.11+

---

## Current Progress

### ✅ Completed topics (Phase 1)

| Folder | Boot.dev | What was built |
|--------|----------|---------------|
| `00_debugging` | Ch 5 | README + one example — reference only, no exercises |
| `01_printing` | Ch 1 | Full folder — f-strings, sep/end, alignment |
| `02_variables_data_types` | Ch 2 | Full folder — types, dynamic typing, casting, bool trap |
| `03_operators` | Ch 6–7 | Full folder — arithmetic, logical, bitwise, short-circuit |
| `04_control_flow` | Ch 7–8 | Full folder — if/elif/else, for, while, break, continue, for/else |
| `05_functions` | Ch 3–4 | Full folder — def, scope, *args/**kwargs, mutable defaults |
| `08_lists` | Ch 9 | Full folder — indexing, slicing, methods, comprehensions, shallow copy |

### 🔲 Remaining (do in this order)

| Priority | Folder | Boot.dev | Key concepts |
|----------|--------|----------|-------------|
| **Next** | `12_dicts_sets` | Ch 10–11 | dict creation, `.get()`, `.items()`, sets, hash tables |
| 2 | `15_exceptions` | Ch 12 | try/except/else/finally, hierarchy, custom exceptions |
| 3 | `06_classes_intro` | — | `__init__`, `self`, instance vars, `__str__`, `__repr__` |
| 4 | `07_memory_mutability` | — | references, aliasing, id(), shallow vs deep copy |
| 5 | `09_tuples` | — | immutability, packing/unpacking, namedtuple |
| 6 | `10_strings` | — | methods, join/split, immutability, f-strings advanced |
| 7 | `11_nested_lists` | — | 2D indexing, `*` copy trap, matrix ops |
| 8 | `13_modules_packages` | — | import, from, `__name__`, pathlib |
| 9 | `14_file_io` | — | with open(), read/write, JSON, CSV, FileNotFoundError |
| 10 | `16_advanced_functions` | — | closures, partial, map/filter, lambda |
| 11 | `17_recursion` | — | base case, call stack, memoisation, lru_cache |

---

## Folder Structure (every full topic)

```
<number>_<topic_name>/
├── README.md          — narrative, concept, mental model, AI connection
├── notes.md           — pre-answered questions + blank reflection sections
├── test.py            — 20–40 tests, stdlib only, python test.py
│
├── examples/
│   ├── 01_<name>.py   — Easy: one concept, AI context, "What to notice" section
│   ├── 02_<name>.py   — Medium: builds on example 1
│   └── 03_<name>.py   — Advanced: real AI scenario, forward-references noted
│
├── exercises/
│   ├── 01_<name>.py   — Easy: exact expected output shown, rules listed
│   ├── 02_<name>.py   — Medium: 2–3 concepts
│   └── 03_<name>.py   — Hard: design/prediction challenge
│
└── solutions/
    ├── 01_<name>.py   — Solution + "Why this works" explanation
    ├── 02_<name>.py
    └── 03_<name>.py
```

**Special case — reference folders** (like `00_debugging`):
Only `README.md` + `example_<name>.py`. No exercises, solutions, notes, or test.py.

---

## File Header (every .py file)

```python
"""
<filename>
──────────────────────────────
Topic  : <topic name>
Example/Exercise/Solution : <N> of 3 — Easy/Medium/Hard
Concept: <specific Python concept>

Context
-------
<2–4 sentences: real AI/ML situation this comes from>

Covers:
  - <Python feature>
  - <Python feature>

Run this file. Predict each output before you see it.
  OR
Attempt before opening solutions.
"""
```

---

## Style Rules

### Tone
- Professional but human — write like a senior developer documenting their own work
- No filler phrases: "Great!", "It's worth noting", "As an AI..."
- Prose over bullets everywhere except genuine lists

### AI/ML context — mandatory for every example and exercise

| Phase | Use these contexts |
|-------|--------------------|
| Phase 1 basics | model configs, training logs, batch calculations, dataset summaries, pipeline stages, image preprocessing, agent status, checkpoint management |
| Phase 6 | NumPy/Pandas operations, visualisation |
| Phase 7 | training loops, model evaluation, fine-tuning |
| Phase 8 | CLI tools, APIs, detection pipelines |

**Never** use generic contexts ("calculate the area of a circle", "store names").

### Comments
- Comments explain **why**, not what — the code shows what
- Each example ends with `# ── What to notice ──` (3–6 points)
- Each solution ends with `# ── Why this works ──`
- Forward-references: `# you'll learn this properly in <topic> (topic XX)`

### Section separators
```python
# ── Section name ─────────────────────────────────────────────────────────────
```

### notes.md structure (always in this order)
1. "What clicked immediately" — blank
2. "What took time" — blank
3. "My questions — answered" — questions from Boot.dev content or conversation, answered with code examples
4. "Connections to other topics" — blank
5. "Things to revisit later" — checklist of forward-referenced concepts with topic numbers
6. "One-line summary" — blank, for learner to fill in

### test.py requirements
- stdlib only — no pytest, no external packages
- `check(label, actual, expected)` helper at the top
- 20–40 tests covering all key behaviours, traps, and edge cases
- Pass/fail summary with `─` separator
- Final message pointing to the next topic

---

## Completed Topics — Style Reference

### 08_lists (most recent — match this level)
- **examples:** indexing/slicing on pipeline stages; iteration with enumerate/zip/accumulation; comprehensions + shallow copy trap
- **exercises:** pipeline slicer (no loops, slicing only); detection filter (comprehension + trend arrows + zip accuracy); top-k without sort/max
- **test.py:** 38 tests — indexing, slicing, methods, comprehensions, enumerate, zip, shallow copy trap
- **notes.md:** range vs list, comprehension vs loop, sorted vs sort, shallow copy, time complexity, iterator protocol

### 05_functions
- **examples:** normalize_pixel (def/hints/docstring/defaults); flexible logger (*args/**kwargs/multiple return); scope + mutable default + main()
- **exercises:** metric calculator (accuracy/clamp/normalize composition); pipeline logger + F1 (*args/**kwargs); scope predictions + mutable fix + global→return rewrite
- **test.py:** 24 tests — return, defaults, mutable trap, None return, scope

### 03_operators
- **examples:** arithmetic + batch math; logical + short-circuit + config defaults; bitwise + permission flags
- **exercises:** batch calculator; QC filter (guard clauses + or-defaults); permission flag system (4 functions)
- **test.py:** 46 tests

---

## How to Use This Skill

### Step 1 — Open a new Claude chat

### Step 2 — Upload this SKILL.md file

### Step 3 — Send this message

```
I'm building the CodeBricks Python → AI/ML repo.
Generate the full topic folder for `<folder_name>`
(topic <N> in Phase 1, Boot.dev chapter <X> if applicable).

Boot.dev lesson content:
[paste the Boot.dev chapter text here]

[Optional — if you have existing files to upgrade:]
I'm also uploading the existing files from my repo for this topic.
Upgrade them to the CodeBricks standard: new folder structure
(examples/exercises/solutions subfolders, one file each),
AI/ML context throughout, human comments, and notes.md with
my questions answered.
```

### Step 4 — Verify everything runs

```bash
python 01_basics/<topic>/test.py
python 01_basics/<topic>/examples/01_*.py
python 01_basics/<topic>/examples/02_*.py
python 01_basics/<topic>/examples/03_*.py
```

### Step 5 — Commit and push

```bash
git add 01_basics/<topic_folder>/
git commit -m "feat(01_basics): add <topic_folder> topic

- README: <what it covers>
- examples: <scenario 1>, <scenario 2>, <scenario 3>
- exercises: <exercise 1>, <exercise 2>, <exercise 3>
- solutions: with full 'why this works' explanations
- test.py: <N> tests covering <concepts>
- notes.md: answered — <questions>"

git push origin main
```

---

## Boot.dev Chapter → Repo Topic Mapping

| Boot.dev | Repo folder | Notes |
|----------|-------------|-------|
| Ch 1: Introduction | `01_printing` | ✅ done |
| Ch 2: Variables | `02_variables_data_types` | ✅ done |
| Ch 3: Functions | `05_functions` | ✅ done (merged with Ch 4) |
| Ch 4: Scope | `05_functions/scope_reference.md` | absorbed — no separate folder |
| Ch 5: Testing & Debugging | `00_debugging` | ✅ done (reference only) |
| Ch 6: Computing | `03_operators` | ✅ done (merged with Ch 7) |
| Ch 7: Comparisons | `03_operators` + `04_control_flow` | ✅ done |
| Ch 8: Loops | `04_control_flow` | ✅ done (loops already covered) |
| Ch 9: Lists | `08_lists` | ✅ done |
| Ch 10: Dictionaries | `12_dicts_sets` | 🔲 next |
| Ch 11: Sets | `12_dicts_sets` | 🔲 next (merged with Ch 10) |
| Ch 12: Errors | `15_exceptions` | 🔲 |

---

## Quality Checklist

Before presenting output, verify:
- [ ] Every example and exercise has a real AI/ML scenario
- [ ] Every .py file has the standard header
- [ ] Every example ends with `# ── What to notice ──`
- [ ] Every solution ends with `# ── Why this works ──`
- [ ] notes.md answers questions from Boot.dev content
- [ ] test.py uses only stdlib, has check() helper, 20+ tests, pass/fail summary
- [ ] README links to previous and next topic
- [ ] All files run without errors: `python <file>.py`
- [ ] test.py passes 100%: `python test.py` shows 0 failed
