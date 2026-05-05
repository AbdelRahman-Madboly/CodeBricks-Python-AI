# 06 — Classes and Objects

> Previous: [05 — Functions](../05_functions/) | Next: [07 — Memory and Mutability](../07_memory_mutability/)

---

## What Is a Class?

A class is a blueprint. It defines what data a thing holds and what it can do.
An object is a concrete instance of that blueprint — the actual thing in memory.

```python
class ModelConfig:          # the blueprint
    def __init__(self, lr, epochs):
        self.lr = lr
        self.epochs = epochs

cfg = ModelConfig(0.001, 10)  # the object — one concrete instance
```

Every call to ModelConfig(...) creates a brand-new object with its own lr and epochs.
You could create a hundred instances and they would all be independent.

---

## The Mental Model

Think of a class as a form with blank fields:

    ModelConfig form
      lr      : ____
      epochs  : ____

Calling ModelConfig(0.001, 10) fills in that form and hands you the filled copy.
The class itself is never "used up" — it stays as the blank template.

This is different from a dict, which is a generic container. A class says exactly
what fields exist and attaches behaviour to the data.

---

## __init__

__init__ is called automatically the moment an object is created. It's where you
set all the instance variables — the data this specific object carries.

```python
class TrainingRun:
    def __init__(self, model_name, lr):
        self.model_name = model_name   # instance variable
        self.lr = lr                   # instance variable
        self.epoch = 0                 # computed default — not passed in
        self.best_loss = float("inf")  # computed default
```

self is always the first parameter. It's a reference to the object being created.
You use it to attach data: self.x = value.

---

## Instance Variables vs. Class Variables

```python
class Detector:
    framework = "PyTorch"      # class variable — shared by ALL instances

    def __init__(self, name, threshold):
        self.name = name           # instance variable — unique per object
        self.threshold = threshold
```

Instance variables: set via self.x in __init__. Each object has its own copy.
Class variables: defined at the top level. All instances share one copy.

In practice: use instance variables almost always. Class variables are easy to
misuse — one instance changing them affects every other instance.

---

## Methods

A method is a function defined inside a class. It always receives self as its
first argument, which gives it access to the object's data.

```python
class TrainingRun:
    def __init__(self, model_name):
        self.model_name = model_name
        self.epoch = 0
        self.losses = []

    def step(self, loss):           # mutates — changes the object
        self.epoch += 1
        self.losses.append(loss)

    def best_loss(self):            # getter — returns a computed value
        return min(self.losses) if self.losses else None
```

Methods either mutate the object (change its state) or return a computed value.
The key is that self always gives them access to the object's current data.

---

## __str__ and __repr__

```python
class ModelConfig:
    def __str__(self):
        # For humans: print(cfg), f"{cfg}", log files
        return f"{self.name} | lr={self.lr} | epochs={self.epochs}"

    def __repr__(self):
        # For developers: REPL output, inside lists, error messages
        return f"ModelConfig(name={self.name!r}, lr={self.lr}, epochs={self.epochs})"
```

__str__  → clean, readable. What you'd want in a log.
__repr__ → unambiguous. Should look like code you could paste to recreate the object.

Without __str__, print(obj) gives: <__main__.ModelConfig object at 0x...> — useless.

---

## Why Classes Over Dicts?

```python
# Dict — flexible but says nothing about what it contains
cfg = {"name": "resnet", "lr": 0.001}
cfg["typo_key"] = 99  # silent, no warning

# Class — structure is a contract enforced by __init__
cfg = ModelConfig("resnet", 0.001, 10)
# cfg always has .name, .lr, .epochs — and methods
```

Classes also bundle behaviour with data. A TrainingRun doesn't just hold numbers —
it knows how to advance an epoch, compute its best loss, and format itself for a log.

---

## The AI/ML Connection

Every ML library is built from classes:

```python
model = RandomForestClassifier(n_estimators=100, max_depth=5)  # creating an instance
model.fit(X_train, y_train)      # calling a method
predictions = model.predict(X_test)  # another method
print(model.n_estimators)        # reading an instance variable
```

When you understand classes, you understand how scikit-learn, PyTorch, HuggingFace,
and every other library is structured. The API is just a set of classes and methods.

---

## Common Mistakes

Forgetting self in __init__:
```python
def __init__(self, lr):
    lr = lr  # WRONG — local variable, disappears after __init__ returns
    self.lr = lr  # RIGHT — attached to the object
```

Using a class variable when you meant an instance variable:
```python
class Detector:
    results = []  # DANGER — shared between ALL instances

    def add_result(self, r):
        self.results.append(r)  # mutates the shared list!
```

Not defining __str__ — objects print as useless memory addresses.

---

## What to Read Next

- 07 — Memory and Mutability: why passing objects to functions can modify them unexpectedly
- 02_oop/01_classes_deep: @property, name mangling, @staticmethod, @classmethod
