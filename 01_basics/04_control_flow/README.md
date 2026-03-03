# Control Flow

## Concept

Control flow determines the order in which statements execute.
Without it, a program runs top to bottom, once, unconditionally.
Control flow adds branching (if/elif/else) and repetition (while, for).

## Mental Model

Think of control flow as a flowchart drawn in code:

```
         ┌──────────────┐
         │  condition?  │
         └──────┬───────┘
          True  │  False
        ┌───────┘  └───────┐
        ▼                  ▼
   [do this]          [do that]
```

For loops follow a different model — iteration:

```
for item in collection:
    →  Python asks the collection for its next item
    →  binds it to 'item'
    →  runs the block
    →  repeats until the collection is exhausted
```

## Key Points

- `if / elif / else` — only one branch executes; Python checks top to bottom
  and stops at the first true condition
- `while` — runs as long as the condition is truthy; always ensure the condition
  eventually becomes false or use `break`
- `for` — iterates over any **iterable** (list, string, range, file, generator...)
- `range(start, stop, step)` — generates integers; `stop` is exclusive
- `break` — exits the loop immediately
- `continue` — skips to the next iteration
- `for/else` and `while/else` — the `else` block runs if the loop completed
  without hitting a `break` (useful for search loops)

## Common Mistakes

- Off-by-one in `range`: `range(5)` gives `0,1,2,3,4` — never 5
- Modifying a list while iterating over it — causes skipped items or infinite loops.
  Iterate over a copy (`for item in items[:]`) or build a new list instead
- Infinite while loop: forgetting to update the condition variable inside the loop

## Interview Angle

*"When would you use `for/else`?"*
When searching a sequence and you need to know if the search completed without
finding anything — it avoids a flag variable and reads more clearly than setting
`found = False` and checking after the loop.
