# Recursion

## Concept

Recursion is when a function calls itself to solve a smaller version of the
same problem. Every recursive solution has two parts:
1. **Base case** — the condition where the function stops calling itself
2. **Recursive case** — where the function calls itself with a simpler input

Recursion is not magic — it is just the call stack doing what it always does.
Each recursive call adds a new frame to the stack. When the base case is hit,
the frames unwind and return values back up the chain.

## Mental Model

```
factorial(4)
  └── 4 * factorial(3)
            └── 3 * factorial(2)
                      └── 2 * factorial(1)
                                └── 1  ← base case, start unwinding
                      └── 2 * 1 = 2
            └── 3 * 2 = 6
  └── 4 * 6 = 24
```

Each call waits for the one below it to return. The base case is the bottom
of the stack. Without it, the stack grows until Python raises `RecursionError`.

## Key Points

- Python's default recursion limit is 1000 frames — use iteration for deep problems
- **Tail recursion** is not optimised in Python — a loop is often faster
- Recursion shines for **naturally recursive structures**: trees, nested dicts,
  file system traversal, graph DFS — problems where the structure mirrors the recursion
- **Memoisation** (`functools.lru_cache`) caches results to avoid redundant calls —
  critical for problems like Fibonacci where the same subproblems repeat

## Common Mistakes

- Missing or wrong base case — causes infinite recursion and `RecursionError`
- Forgetting to return the recursive call: `return func(n - 1)` not just `func(n - 1)`
- Using recursion where a simple loop is clearer — recursion has overhead
  (each frame takes memory and time) and a depth limit

## Interview Angle

*"Implement Fibonacci with and without memoisation and explain the difference."*
Without memoisation: O(2ⁿ) — exponential, recomputes the same values constantly.
With `lru_cache`: O(n) — each value computed once and cached.
This is a classic demonstration of dynamic programming thinking.
