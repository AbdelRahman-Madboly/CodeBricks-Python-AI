# Printing

## Concept

`print()` is Python's built-in function for sending output to the terminal.
It accepts any number of values, converts them to strings, and writes them
to standard output followed by a newline by default.

Simple as it sounds, `print()` has options that matter in real work:
controlling separators, line endings, and output destinations.

## Mental Model

Think of `print()` as a messenger that takes whatever you hand it,
converts everything to text, arranges it according to your formatting
rules, and delivers it to the screen (or a file, or a log stream).

```
print(value1, value2, ..., sep=' ', end='\n', file=sys.stdout)
         │                    │         │           │
         │                    │         │           └── where to send output
         │                    │         └── what to put at the end
         │                    └── what to put between values
         └── what to print
```

## Key Points

- `print()` with no arguments prints a blank line
- `sep` controls what goes **between** multiple values (default is a space)
- `end` controls what goes **after** the last value (default is `\n`)
- f-strings (`f"..."`) are the modern, preferred way to embed variables in strings
- `print()` always returns `None` — it is a side effect, not a value

## Common Mistakes

- Using `+` to concatenate mixed types: `print("Score: " + 42)` raises `TypeError`.
  Use an f-string instead: `print(f"Score: {42}")`
- Forgetting that `print()` adds a newline by default — use `end=""` when
  building output incrementally in a loop
- Confusing `print(x)` (shows output) with `return x` (produces a value) —
  a function that only prints cannot be used in further computation

## Interview Angle

Rarely asked directly, but interviewers notice when candidates use
`print(f"...")` fluently and format debug output cleanly during live coding.
It signals familiarity with the language rather than fighting it.
