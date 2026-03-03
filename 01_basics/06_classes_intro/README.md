# Classes and Objects

## Concept

A class is a blueprint for creating objects. An object is an instance of a class —
it bundles together **data** (attributes) and **behaviour** (methods) into one unit.

This is the foundation of Object-Oriented Programming. Instead of passing data
around as loose variables and calling functions on them, you model the world as
objects that know their own state and can act on it.

## Mental Model

Think of a class as a cookie cutter and objects as the cookies:

```
Class (blueprint)          Objects (instances)
─────────────────          ───────────────────
  class Dog:               fido = Dog("Fido", "Labrador")
      name                 rex  = Dog("Rex",  "German Shepherd")
      breed
      bark()               fido.bark()  →  "Woof! I'm Fido"
                           rex.bark()   →  "Woof! I'm Rex"
```

Each object has its own copy of the data, but shares the method definitions
from the class.

## Key Points

- `__init__` is the constructor — called automatically when you create an instance
- `self` refers to the specific object being created or used — it is always the
  first parameter of instance methods
- `__str__` controls what `print(obj)` displays — always define it
- `__repr__` controls the developer-facing representation (shown in the REPL)
- Attributes set on `self` inside `__init__` are **instance attributes** —
  each object gets its own copy
- Methods are just functions defined inside a class that receive `self`

## Common Mistakes

- Forgetting `self.` when setting attributes: writing `name = value` inside
  `__init__` creates a local variable that disappears — use `self.name = value`
- Forgetting `self` as the first method parameter — Python passes the instance
  automatically, but you still have to declare the slot
- Not defining `__str__` — you get something unreadable like `<__main__.Dog object at 0x...>`

## Interview Angle

*"What is the difference between `__str__` and `__repr__`?"*
`__str__` is for end users — readable, formatted output.
`__repr__` is for developers — should ideally be a string that could recreate the object.
If only one is defined, Python falls back to `__repr__` for both.
