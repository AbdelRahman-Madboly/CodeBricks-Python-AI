# Advanced Functions

## Concept

Python treats functions as **first-class objects** — they can be stored in
variables, passed as arguments, returned from other functions, and stored
in data structures. This unlocks powerful patterns: closures, decorators,
higher-order functions, and functional-style programming.

## Mental Model

```
Functions as values:
    process = some_function        ← store a function in a variable
    result  = apply(process, data) ← pass a function as an argument
    factory = make_function()      ← return a function from a function
```

A **closure** is a function that remembers variables from the enclosing
scope where it was created — even after that scope has finished executing.

```
def make_threshold_checker(threshold):
    def check(score):              ← inner function
        return score >= threshold  ← captures 'threshold' from outer scope
    return check                   ← returns the inner function

is_high_confidence = make_threshold_checker(0.90)
is_high_confidence(0.95)  → True
is_high_confidence(0.70)  → False
```

## Key Points

- **Lambda**: `lambda x: x * 2` — anonymous one-line function;
  use only for simple expressions passed inline (e.g. to `sorted()` or `map()`)
- **`map(func, iterable)`** — apply a function to every element; returns an iterator
- **`filter(func, iterable)`** — keep only elements where func returns True
- **Closures** capture variables by reference, not value — be careful in loops
- **`functools.partial`** — create a new function with some arguments pre-filled
- **Type annotations for functions**: `Callable[[int, str], bool]`

## Common Mistakes

- Lambda in a loop captures the loop variable by reference:
  `funcs = [lambda x: x + i for i in range(3)]` — all three lambdas use the
  final value of `i`. Fix with a default argument: `lambda x, i=i: x + i`
- Overusing lambda — if the logic is more than one expression, write a proper
  named function for readability and testability
- Forgetting that `map()` and `filter()` return iterators, not lists —
  wrap with `list()` if you need to index or iterate more than once

## Interview Angle

*"What is a closure and when would you use one?"*
A closure is a function bundled with the variables from its enclosing scope.
Use cases: factory functions that produce configured callbacks, memoisation,
and decorators (which are closures that wrap other functions).
