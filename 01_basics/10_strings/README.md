# Strings

## Concept

A string is an immutable sequence of Unicode characters. In Python, text is a
first-class data type with a rich set of built-in methods for searching,
splitting, formatting, and transforming text — no imports needed.

Strings are everywhere in real code: file paths, labels, config values,
log messages, API responses, and data coming from CSV or JSON files.

## Mental Model

Think of a string as a read-only list of characters:

```
s = "deepfake"
     d  e  e  p  f  a  k  e
     0  1  2  3  4  5  6  7
    -8 -7 -6 -5 -4 -3 -2 -1
```

You can index and slice a string exactly like a list, but you cannot modify
individual characters — every transformation returns a new string.

## Key Points

**Formatting** (use f-strings — they are the modern standard):
- `f"Hello {name}"` — embed any expression directly
- `f"{value:.2f}"` — format spec after the colon
- `f"{value!r}"` — repr conversion, adds quotes around strings

**Common methods** (all return new strings — strings are immutable):
- `.strip()` / `.lstrip()` / `.rstrip()` — remove whitespace
- `.lower()` / `.upper()` / `.title()`
- `.replace(old, new)`
- `.split(sep)` → list; `.join(iterable)` → string
- `.startswith(prefix)` / `.endswith(suffix)` → bool
- `.find(sub)` → index or -1; `.count(sub)` → int
- `.zfill(width)` — zero-pad: `"5".zfill(3)` → `"005"`

## Common Mistakes

- Concatenating in a loop with `+`: `result = ""; for s in lst: result += s`
  is O(n²) — use `"".join(lst)` instead (O(n))
- Forgetting that `.split()` with no argument splits on any whitespace AND
  removes empty strings, while `.split(" ")` splits on exactly one space
  and can produce empty strings
- `str.replace()` replaces **all** occurrences by default — pass a count
  argument if you only want the first: `s.replace("a", "b", 1)`

## Interview Angle

*"Reverse a string in Python."*
`s[::-1]` — slicing with step -1. This is the expected Pythonic answer.

*"Check if a string is a palindrome."*
`s == s[::-1]` for simple cases. For real use, normalize first:
`s.lower().replace(" ", "") == s.lower().replace(" ", "")[::-1]`
