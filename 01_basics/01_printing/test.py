"""
01 — Printing | test.py
────────────────────────
This file does two things:

  1. Tests the specific behaviours of print() so you can verify
     your understanding is correct, not just feel-correct.

  2. Shows you what automated testing looks like before you
     formally learn pytest in Phase 5 (topic: testing & quality).

You don't need to understand every line here yet.
Run it, watch the results, read the comments.

When you get to Phase 5, you'll replace this with pytest —
which does all of this automatically. For now, you're seeing
what pytest does under the hood.
"""

import io
import sys


# ── Test runner helper ────────────────────────────────────────────────────────

def capture(func):
    """Run func() and return everything it printed as a string."""
    buffer = io.StringIO()       # a fake "terminal" stored in memory
    sys.stdout = buffer          # redirect all print() calls to it
    func()
    sys.stdout = sys.__stdout__  # restore the real terminal
    return buffer.getvalue()


passed = 0
failed = 0

def check(test_name, actual, expected):
    global passed, failed
    if actual == expected:
        print(f"  ✓  {test_name}")
        passed += 1
    else:
        print(f"  ✗  {test_name}")
        print(f"       expected : {repr(expected)}")
        print(f"       got      : {repr(actual)}")
        failed += 1


# ── Tests ─────────────────────────────────────────────────────────────────────

print("01 — Printing | test.py\n")
print("Running tests...\n")

# 1. Basic string
output = capture(lambda: print("hello"))
check("basic string", output, "hello\n")

# 2. print() always adds \n at the end by default
output = capture(lambda: print("a"))
check("ends with newline by default", output, "a\n")

# 3. Multiple values are joined with a space by default
output = capture(lambda: print("a", "b", "c"))
check("multiple values, default sep", output, "a b c\n")

# 4. Custom sep
output = capture(lambda: print("a", "b", "c", sep=" → "))
check("custom sep", output, "a → b → c\n")

# 5. end="" suppresses the newline
output = capture(lambda: print("hello", end=""))
check("end='' suppresses newline", output, "hello")

# 6. end="!" replaces the newline with !
output = capture(lambda: print("hello", end="!"))
check("custom end", output, "hello!")

# 7. print() alone produces a blank line (just a newline)
output = capture(lambda: print())
check("empty print gives newline", output, "\n")

# 8. f-string with 2 decimal places
output = capture(lambda: print(f"{3.14159:.2f}"))
check("f-string float precision", output, "3.14\n")

# 9. f-string with comma formatting
output = capture(lambda: print(f"{1500000:,}"))
check("f-string comma separator", output, "1,500,000\n")

# 10. f-string with percentage format
output = capture(lambda: print(f"{0.9441:.1%}"))
check("f-string percent format", output, "94.4%\n")

# 11. Left-aligned column (padded with spaces on right)
output = capture(lambda: print(f"{'Train':<10}|"))
check("left-align :<10", output, "Train     |\n")

# 12. Right-aligned column (padded with spaces on left)
output = capture(lambda: print(f"{'99':>10}|"))
check("right-align :>10", output, "        99|\n")

# ── Summary ───────────────────────────────────────────────────────────────────

print(f"\n{'─' * 35}")
print(f"  {passed} passed   {failed} failed")
print(f"{'─' * 35}\n")

if failed == 0:
    print("  All tests passed. You understand print().")
    print("  Move on to examples/ if you haven't already.")
else:
    print("  Some tests failed. Review the failing cases in the README.")