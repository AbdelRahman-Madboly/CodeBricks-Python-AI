# Modules and Packages

## Concept

A **module** is any `.py` file. When you import it, Python executes the file
and makes its contents available under the module's name.

A **package** is a directory containing an `__init__.py` file (which can be empty).
It groups related modules under a common namespace.

This is how all Python libraries are structured — including numpy, pandas, and torch.

## Mental Model

```
project/
├── main.py
├── utils.py              ← module: import utils
└── pipeline/             ← package: import pipeline
    ├── __init__.py
    ├── loader.py         ← submodule: from pipeline import loader
    └── preprocessor.py
```

When Python sees `import pipeline.loader`, it:
1. Finds the `pipeline/` directory
2. Runs `pipeline/__init__.py`
3. Runs `pipeline/loader.py`
4. Binds the result to `pipeline.loader`

## Key Points

- `import module` — import the whole module; access with `module.func()`
- `from module import func` — import a specific name directly
- `from module import func as f` — import with an alias
- `if __name__ == "__main__":` — code under this guard runs only when
  the file is executed directly, not when it is imported
- `__init__.py` controls what `from package import *` exposes, and can
  re-export names to create a clean public API
- Python searches for modules in: the current directory, `PYTHONPATH`,
  then the standard library and installed packages

## Common Mistakes

- Circular imports: module A imports module B which imports module A —
  Python partially executes A before B tries to import it, causing `ImportError`
  or missing attributes. Fix by restructuring or importing inside a function
- Naming a file the same as a standard library module: `random.py` in your
  project will shadow Python's built-in `random` module
- Forgetting `__init__.py` in a package directory (in Python 3 this creates
  a "namespace package" which behaves differently)

## Interview Angle

*"What does `if __name__ == '__main__'` do?"*
When Python imports a module, `__name__` is set to the module's name.
When Python runs a file directly, `__name__` is set to `"__main__"`.
This guard lets a file be both importable as a library AND runnable as a script.
