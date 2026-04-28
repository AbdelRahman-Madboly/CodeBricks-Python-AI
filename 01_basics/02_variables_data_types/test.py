"""
02 — Variables and Data Types | test.py
────────────────────────────────────────
Verifies your understanding of Python's type system.

Run with: python test.py

Each test checks a specific behaviour — not just "does the code run"
but "does Python actually behave the way you think it does".

When you get to Phase 5, pytest replaces this manual runner.
For now, this shows you what pytest does under the hood.
"""

import math

passed = 0
failed = 0


def check(label, actual, expected):
    global passed, failed
    if actual == expected:
        print(f"  ✓  {label}")
        passed += 1
    else:
        print(f"  ✗  {label}")
        print(f"       expected : {repr(expected)}")
        print(f"       got      : {repr(actual)}")
        failed += 1


print("02 — Variables and Data Types | test.py\n")
print("Running tests...\n")

# ── Types ─────────────────────────────────────────────────────────────────────

check("int type name",     type(42).__name__,       "int")
check("float type name",   type(3.14).__name__,     "float")
check("str type name",     type("hi").__name__,     "str")
check("bool type name",    type(True).__name__,     "bool")
check("NoneType name",     type(None).__name__,     "NoneType")

# ── isinstance and inheritance ────────────────────────────────────────────────

check("isinstance int",        isinstance(10, int),       True)
check("bool is subclass int",  isinstance(True, int),     True)   # bool inherits int
check("True equals 1",         True == 1,                 True)
check("False equals 0",        False == 0,                True)

# ── None identity ─────────────────────────────────────────────────────────────

check("None is None",          None is None,              True)
check("None not equal False",  None == False,             False)

# ── Type conversion ───────────────────────────────────────────────────────────

check("int from string",       int("42"),                 42)
check("float from string",     float("3.14"),             3.14)
check("str from int",          str(100),                  "100")
check("bool from non-empty str", bool("False"),           True)   # the trap
check("correct bool from str", "False" == "True",         False)  # correct way
check("None from string",      None if "None" == "None" else "x", None)

# ── Arithmetic operators ──────────────────────────────────────────────────────

check("floor division",        10 // 3,                   3)
check("modulo",                10 % 3,                    1)
check("true division is float",isinstance(10 / 2, float), True)
check("exponentiation",        2 ** 10,                   1024)

# ── Float precision ───────────────────────────────────────────────────────────

check("float equality trap",   0.1 + 0.2 == 0.3,         False)  # the trap
check("float with round()",    round(0.1 + 0.2, 1) == 0.3, True)
check("float with isclose()",  math.isclose(0.1 + 0.2, 0.3), True)

# ── Underscore in numbers ─────────────────────────────────────────────────────

check("underscore in int",     10_000,                    10000)
check("underscore in float",   1_000.5,                   1000.5)

# ── Summary ───────────────────────────────────────────────────────────────────

print(f"\n{'─' * 40}")
print(f"  {passed} passed   {failed} failed")
print(f"{'─' * 40}\n")

if failed == 0:
    print("  All tests passed.")
    print("  You understand Python's type system for this topic.")
    print("  Move on to 03_operators/ when ready.")
else:
    print(f"  {failed} test(s) failed.")
    print("  Review the failing cases in examples/ before moving on.")