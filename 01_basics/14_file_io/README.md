# File I/O

## Concept

File I/O lets your program read data from disk and write results back.
In Python, the built-in `open()` function handles text and binary files.
The `with` statement (context manager) ensures files are always closed
properly — even if an exception occurs.

## Mental Model

```
with open("file.txt", mode) as file_handle:
    # file is open here
    data = file_handle.read()
# file is automatically closed here — even if an exception was raised
```

Think of `open()` as borrowing a book from a library. The `with` block is the
borrowing period. When you leave the block, the book is returned — no matter what.

## Key Points

**Modes:**
| Mode | Meaning                              |
|------|--------------------------------------|
| `r`  | Read text (default)                  |
| `w`  | Write text — creates or overwrites   |
| `a`  | Append text                          |
| `rb` | Read binary                          |
| `wb` | Write binary                         |

**Reading:**
- `.read()` — entire file as one string
- `.readline()` — one line at a time
- `.readlines()` — list of all lines (includes `\n`)
- `for line in file` — memory-efficient iteration (best for large files)

**Writing:**
- `.write(string)` — write a string (no automatic newline)
- `.writelines(list)` — write a list of strings

**Encoding:** always specify `encoding="utf-8"` for text files to avoid
platform-dependent behaviour on Windows.

## Common Mistakes

- Not using `with` — forgetting to call `.close()` leaks file handles
- Reading a large file with `.read()` — loads everything into memory;
  iterate line by line for large files
- Writing without `\n` — `.write()` does not add newlines automatically
- `w` mode silently overwrites existing files — use `x` mode if you want
  to fail when a file already exists

## Interview Angle

*"How do you safely read a file that might not exist?"*
```python
try:
    with open("config.json", encoding="utf-8") as f:
        data = f.read()
except FileNotFoundError:
    data = None
```
Or use `pathlib.Path("config.json").exists()` to check first.
