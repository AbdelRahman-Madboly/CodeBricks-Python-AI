# Phase 2 — Object-Oriented Programming

> Learn to model real systems, not just write classes for the sake of it.

---

## What This Phase Is About

Phase 1 gave you `__init__`, `self`, and basic methods.
Phase 2 goes deeper: how to hide complexity, how to share behaviour
across related classes, how to write code that works with objects
it's never seen before, and how to design systems that stay maintainable
as they grow.

Every AI framework you'll use — PyTorch, HuggingFace, scikit-learn —
is built on these patterns. `nn.Module`, `Dataset`, `Estimator`:
all of them are class hierarchies using inheritance, abstraction,
and polymorphism. Learning OOP properly here means Phase 7 won't
feel like magic.

---

## Boot.dev Alignment

| Boot.dev | Repo Topic | Key concept |
|----------|------------|-------------|
| Ch 2: Inheritance | `02_inheritance` | Sharing behaviour, `super()`, MRO |
| Ch 3: Encapsulation | `01_encapsulation` | `__private`, `@property`, name mangling |
| Ch 4: Abstraction | `03_abstraction` | `ABC`, abstract methods, interfaces |
| Ch 5: Polymorphism | `04_polymorphism` | Duck typing, operator overloading, `isinstance` |
| No Boot.dev | `05_solid_design` | SOLID principles, composition vs inheritance |

> **Note:** `06_classes_intro` in Phase 1 covers the Boot.dev Ch 1 (Classes)
> basics — `__init__`, `self`, `__str__`, `__repr__`. Phase 2 builds on that.
> You do not need to redo it here.

---

## Topics

| # | Topic | Boot.dev | Status |
|---|-------|----------|--------|
| 01 | [Encapsulation](./01_encapsulation/) | Ch 3 | 🔲 |
| 02 | [Inheritance](./02_inheritance/) | Ch 2 | 🔲 |
| 03 | [Abstraction](./03_abstraction/) | Ch 4 | 🔲 |
| 04 | [Polymorphism](./04_polymorphism/) | Ch 5 | 🔲 |
| 05 | [SOLID Design](./05_solid_design/) | No Boot.dev | 🔲 |

---

## What Changed from the Old Structure

The original `02_oop` had 8 folders mirroring a textbook breakdown.
This structure has 5 — aligned to Boot.dev chapters with one extra
for design principles. The reasons:

- **Fewer folders = clearer progress.** 8 topics at the same level
  feels like a wall. 5 topics with clean scope is a roadmap.
- **Encapsulation comes first.** It's the foundation the others build on.
  You learn to hide state before you learn to share it (inheritance)
  or replace it (polymorphism).
- **`@property` lives in Encapsulation, not its own folder.**
  Properties are a tool for controlled access — they belong with
  the encapsulation concept, not as a separate topic.
- **MRO and namespaces merge into Inheritance.**
  You need MRO to understand multiple inheritance — they're one topic.
- **Abstract classes merge into Abstraction.**
  The `ABC` module is the Python mechanism for abstraction — same chapter.
- **SOLID gets its own topic** because it has no Boot.dev chapter
  and needs dedicated space. It's the bridge between learning OOP
  syntax and designing OOP systems.

---

## Folder Structure (each topic)

```
<number>_<topic>/
├── README.md          — concept, why it exists, mental model, AI connection
├── notes.md           — personal learning journal
├── test.py            — python test.py, stdlib only
│
├── examples/
│   ├── 01_<name>.py   — Easy: one pattern, AI context, "What to notice"
│   ├── 02_<name>.py   — Medium: builds on example 1
│   └── 03_<name>.py   — Advanced: real AI scenario, forward-references
│
├── exercises/
│   ├── 01_<name>.py   — Easy: exact expected output shown
│   ├── 02_<name>.py   — Medium: 2–3 concepts combined
│   └── 03_<name>.py   — Hard: design/modelling challenge
│
└── solutions/
    ├── 01_<name>.py   — Solution + "Why this works"
    ├── 02_<name>.py
    └── 03_<name>.py
```

---

## How to Work Through Each Topic

1. Read `README.md` — understand the design reasoning, not just the syntax
2. Open each `examples/` file — predict the output before running
3. Attempt each `exercises/` file — write your solution first
4. Check `solutions/` — read the "why" section, not just the code
5. Fill in `notes.md` — in your own words
6. Run `test.py` — all tests pass before marking done

---

## Phase 2 Completion Checklist

You are ready for Phase 3 when you can do all of these:

- [ ] Write a class with private attributes and `@property` getter/setter
- [ ] Explain the difference between `__private` and `_protected`
- [ ] Build a class hierarchy with `super()` and explain when to use it
- [ ] Explain MRO and what `C3 linearisation` means at a high level
- [ ] Write an abstract base class with `@abstractmethod`
- [ ] Explain why `isinstance()` is better than `type()` for polymorphism
- [ ] Override `__add__`, `__str__`, and `__eq__` on a custom class
- [ ] Explain the Single Responsibility Principle with a concrete example
- [ ] Explain composition vs inheritance and when to choose each
- [ ] Write a duck-typed function that works on any object with `.predict()`

---

## Connection to the AI Journey

```python
# PyTorch's nn.Module — inheritance + abstraction
class MyModel(nn.Module):          # inherits from nn.Module
    def __init__(self):
        super().__init__()         # calls nn.Module.__init__
        self.linear = nn.Linear(784, 10)

    def forward(self, x):          # abstract method — MUST be overridden
        return self.linear(x)


# HuggingFace Trainer — polymorphism
# Any object with a forward() method works — duck typing
trainer = Trainer(model=MyModel(), ...)


# scikit-learn — all estimators share the same interface
# fit(), predict(), transform() — polymorphic across 50+ classes
model.fit(X_train, y_train)
preds = model.predict(X_test)
```

Every pattern in Phase 2 appears in Phase 7.

---

*Previous → [Phase 1 — Python Fundamentals](../01_basics/)*
*Next → [Phase 3 — Pythonic Patterns](../03_pythonic/)*