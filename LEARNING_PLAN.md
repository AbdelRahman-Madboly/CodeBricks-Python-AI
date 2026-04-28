# Learning Plan — 16 Weeks

Aligned with Boot.dev chapter order. Each repo topic maps to one or more
Boot.dev chapters. Complete the Boot.dev lessons first, then build the
topic folder using the SKILL.md prompt in a new chat.

---

## Week 1 — Python Foundations I

| Day | Repo Topic | Boot.dev Chapter(s) | Key Concepts |
|-----|-----------|---------------------|--------------|
| 1   | 01_printing | Ch 1: Introduction | print(), f-strings, sep, end |
| 2   | 02_variables_data_types | Ch 2: Variables | types, dynamic typing, None, casting |
| 3   | 05_functions | Ch 3: Functions + Ch 4: Scope | def, return, defaults, *args, **kwargs, scope |
| 4   | 03_operators | Ch 6: Computing + Ch 7: Comparisons | arithmetic, comparison, logical, short-circuit |
| 5   | 04_control_flow | Ch 8: Loops | if/elif/else, while, for, for/else, break/continue |

---

## Week 2 — Python Foundations II

| Day | Repo Topic | Boot.dev Chapter(s) | Key Concepts |
|-----|-----------|---------------------|--------------|
| 6   | 08_lists | Ch 9: Lists | indexing, slicing, methods, comprehensions |
| 7   | 12_dicts_sets | Ch 10: Dictionaries + Ch 11: Sets | hash tables, .get(), set ops |
| 8   | 15_exceptions | Ch 12: Errors | try/except/else/finally, custom exceptions |
| 9   | 06_classes_intro | OOP fundamentals | __init__, self, __str__, __repr__ |
| 10  | 07_memory_mutability | Memory model | references, aliasing, shallow/deep copy |

---

## Week 3 — Python Foundations III

| Day | Repo Topic | Boot.dev Chapter(s) | Key Concepts |
|-----|-----------|---------------------|--------------|
| 11  | 09_tuples | Tuples | immutability, unpacking, namedtuple |
| 12  | 10_strings | Strings | methods, join, split, immutability |
| 13  | 11_nested_lists | Nested lists | 2D indexing, matrix ops, copy trap |
| 14  | 13_modules_packages | Modules | import system, __name__, pathlib |
| 15  | 14_file_io | File I/O | with open(), JSON, CSV, line iteration |
| 16  | 16_advanced_functions | Advanced functions | closures, partial, map, filter, lambda |
| 17  | 17_recursion | Recursion | base case, memoisation, lru_cache |

---

## Week 4–6 — Object-Oriented Programming

| Week | Repo Topic | Key Concepts |
|------|-----------|--------------|
| 4    | 02_oop/01_classes_deep | Name mangling, @property, static vs class methods |
| 4    | 02_oop/02_properties_static | Properties, descriptors |
| 5    | 02_oop/03_namespaces_mro | Namespaces, MRO, super() |
| 5    | 02_oop/04_inheritance | Single, multilevel, multiple inheritance |
| 5    | 02_oop/05_polymorphism | Duck typing, operator overloading, ABC |
| 6    | 02_oop/06_abstract | Abstract base classes, protocols |
| 6    | 02_oop/07_solid | SOLID principles, composition vs inheritance |
| 6    | 02_oop/08_uml | Reading and drawing class diagrams |

---

## Week 7 — Pythonic Patterns

| Repo Topic | Key Concepts |
|-----------|--------------|
| 03_pythonic/01_comprehensions | list, dict, set, generator expressions |
| 03_pythonic/02_generators | yield, lazy evaluation, memory efficiency |
| 03_pythonic/03_decorators | wrappers, functools, parameterized decorators |
| 03_pythonic/04_context_managers | with, __enter__/__exit__, contextlib |

---

## Week 8 — Standard Library

| Repo Topic | Key Concepts |
|-----------|--------------|
| 04_standard_library/01_datetime | parsing, formatting, timezones |
| 04_standard_library/02_os_pathlib | filesystem operations |
| 04_standard_library/03_regex | re module, patterns, groups |
| 04_standard_library/04_json_csv | serialization and parsing |
| 04_standard_library/05_threading | threads, concurrent.futures |

---

## Week 9 — Code Quality

| Repo Topic | Key Concepts |
|-----------|--------------|
| 05_typing_quality/01_type_hints | annotations, mypy |
| 05_typing_quality/02_pydantic | runtime validation, settings |
| 05_typing_quality/03_pytest | fixtures, parametrize, mocking |
| 05_typing_quality/04_ruff | linting and formatting |

---

## Week 10–12 — Data Science

| Week | Repo Topic | Key Concepts |
|------|-----------|--------------|
| 10   | 06_data_science/01_numpy | arrays, broadcasting, linear algebra |
| 11   | 06_data_science/02_pandas | DataFrames, groupby, merging |
| 12   | 06_data_science/03_matplotlib | visualization, plotting, seaborn |

---

## Week 13–15 — AI/ML Engineering

| Week | Repo Topic | Key Concepts |
|------|-----------|--------------|
| 13   | 07_ai_ml_path/01_ml_concepts | bias/variance, cross-validation, metrics |
| 13   | 07_ai_ml_path/02_sklearn | pipelines, preprocessing, model selection |
| 14   | 07_ai_ml_path/03_deep_learning | backprop, activations, loss functions |
| 14   | 07_ai_ml_path/04_pytorch | tensors, autograd, training loop |
| 15   | 07_ai_ml_path/05_transformers | HuggingFace, fine-tuning, embeddings |
| 15   | 07_ai_ml_path/06_computer_vision | CNNs, image processing, feature extraction |

---

## Week 16 — Projects

| Repo Topic | Description |
|-----------|-------------|
| 08_projects/01_cli_pipeline | Type-safe CLI data pipeline |
| 08_projects/02_fastapi_rest | REST API with FastAPI + Pydantic |
| 08_projects/03_ml_classification | Full training and evaluation loop |
| 08_projects/04_nlp_finetuning | Transformer fine-tuning, domain NLP |
| 08_projects/05_deepfake_detection | Computer vision end-to-end pipeline |

---

## Notes

- Adjust pace based on how topics feel — this is a guide, not a contract
- If a topic takes 2 days instead of 1, that's fine — depth over speed
- Boot.dev's Ch 5 (Testing and Debugging) and Ch 13 (Practice) / Ch 14 (Quiz)
  are absorbed into the repo's test.py files and exercise progression
- The repo topics 03 (operators) and 04 (control flow) map to Boot.dev
  chapters 6, 7, and 8 — they cover more ground than the Boot.dev split