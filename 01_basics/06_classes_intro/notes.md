# Notes — 06 Classes and Objects

---

## What clicked immediately

_(fill in after working through the examples)_

---

## What took time

_(fill in after working through the exercises)_

---

## My questions — answered

**What is self and why is it always the first parameter?**

self is the object the method was called on. Python passes it automatically —
you never type it as an argument, only as a parameter in the definition.

    run = TrainingRun("resnet50")
    run.step(0.92)
    # Python translates this to: TrainingRun.step(run, 0.92)
    # run is self inside the method

Without self, a method has no way to know which specific object it's working on.
There's nothing special about the name "self" — by convention everyone uses it,
but Python would accept any name.

**What is the difference between __str__ and __repr__?**

Both control how an object becomes a string. The context determines which runs:

    print(obj)          → __str__
    f"{obj}"            → __str__
    str(obj)            → __str__
    repr(obj)           → __repr__
    [obj]               → __repr__ (inside a collection)
    obj in the REPL     → __repr__

Rule of thumb:
- __str__: clean, human-readable. Think log lines.
- __repr__: unambiguous, developer-readable. Should look like the constructor call.

If you define only __repr__, Python uses it for both. If you define only __str__,
repr() falls back to the default memory-address form.

**What is an instance variable vs a class variable?**

    class Counter:
        count = 0          # class variable — one copy, shared by all instances

        def __init__(self, name):
            self.name = name   # instance variable — one per object

    a = Counter("A")
    b = Counter("B")
    Counter.count = 5   # changes it for everyone
    print(a.count)      # 5
    print(b.count)      # 5

    a.name = "Z"        # only changes a's name
    print(b.name)       # "B" — unchanged

Class variables are like global variables within a class. They cause the same
kinds of bugs — use them sparingly, and only for genuinely shared constants.

**What does __init__ actually do?**

__init__ is called by Python immediately after the object is created. Its job
is to set up the object's initial state by assigning values to self.x.

It does NOT create the object — that happens in __new__ (which you'll rarely
touch). __init__ just initialises the already-created object.

    # What Python does when you write ModelConfig("resnet50", 0.001, 30):
    obj = object.__new__(ModelConfig)   # creates empty object
    ModelConfig.__init__(obj, "resnet50", 0.001, 30)  # initialises it
    # obj is now cfg

**Why is the class variable mutable default a bug?**

    class Detector:
        results = []    # created ONCE when the class is defined

    a = Detector()
    b = Detector()
    a.results.append(1)
    print(b.results)    # [1] — b sees it too!

The list is created once when the class is first loaded, not each time __init__
runs. Both a and b point to the same list. Appending to a.results mutates the
shared object, so b.results reflects the change too.

Fix: always create mutable defaults inside __init__:

    def __init__(self):
        self.results = []   # fresh list for every instance

---

## Connections to other topics

- **05 — Functions**: __init__, __str__, and methods are just functions with self.
  Default values, *args, and return work identically.
- **07 — Memory and Mutability**: when you pass an object to a function, you pass a
  reference. The function can mutate the object's instance variables.
- **08 — Lists**: self.checkpoints = [] and list operations inside classes.
- **02_oop/01_classes_deep**: name mangling, @property, @staticmethod, @classmethod.
- **02_oop/03_namespaces_mro**: how Python looks up attributes — instance dict first,
  then class dict, then base classes.

---

## Things to revisit later

- [ ] @property — control attribute access without breaking the interface (02_oop/02)
- [ ] @staticmethod and @classmethod — methods that don't need self (02_oop/02)
- [ ] __new__ — how objects are actually created before __init__ runs (02_oop/01)
- [ ] __eq__, __lt__, __hash__ — making objects comparable and hashable (02_oop/05)
- [ ] Dataclasses — @dataclass generates __init__, __str__, __repr__ automatically (02_oop/01)
- [ ] Type hints on self — not required but part of modern Python style (05_typing_quality/01)

---

## One-line summary

_(fill in after completing all three exercises)_
