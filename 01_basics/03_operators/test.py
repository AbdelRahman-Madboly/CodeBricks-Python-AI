"""
03 — Operators | test.py
─────────────────────────
Run with: python test.py
"""

import math

passed = 0
failed = 0


def check(label: str, actual, expected) -> None:
    global passed, failed
    if actual == expected:
        print(f"  ✓  {label}")
        passed += 1
    else:
        print(f"  ✗  {label}")
        print(f"       expected : {repr(expected)}")
        print(f"       got      : {repr(actual)}")
        failed += 1


print("03 — Operators | test.py\n")
print("Running tests...\n")

# ── Arithmetic ────────────────────────────────────────────────────────────────

check("/ returns float",          type(10 / 2),       float)
check("/ exact result",           10 / 2,             5.0)
check("// returns int",           type(10 // 3),      int)
check("// floors positive",       10 // 3,            3)
check("// floors negative",       -7 // 2,            -4)
check("% positive remainder",     10 % 3,             1)
check("% when no remainder",      12 % 4,             0)
check("% divisor > dividend",     5 % 32,             5)
check("** exponentiation",        2 ** 10,            1024)
check("scientific notation",      2e-5,               0.00002)
check("underscore in number",     10_000,             10000)

# ── In-place operators ────────────────────────────────────────────────────────

x = 10
x += 3;  check("+= adds",         x, 13)
x -= 5;  check("-= subtracts",    x, 8)
x *= 2;  check("*= multiplies",   x, 16)
x //= 3; check("//= floor divs",  x, 5)
x %= 3;  check("%= modulo",       x, 2)

# ── Comparison ────────────────────────────────────────────────────────────────

check("== equal values",          5 == 5,             True)
check("!= not equal",             5 != 6,             True)
check("> greater than",           6 > 5,              True)
check("< less than",              4 < 5,              True)
check(">= equal case",            5 >= 5,             True)
check("<= less case",             4 <= 5,             True)
check("chained comparison true",  0 <= 0.5 <= 1.0,   True)
check("chained comparison false", 0 <= 1.5 <= 1.0,   False)

# ── Logical operators — short-circuit return values ───────────────────────────

check("and — first falsy",        0 and "hi",         0)
check("and — all truthy",         "a" and "b",        "b")
check("or — first truthy",        0 or "default",     "default")
check("or — all falsy",           0 or "" or None,    None)
check("not True",                 not True,           False)
check("not 0",                    not 0,              True)
check("not empty string",         not "",             True)

# ── Short-circuit default pattern ────────────────────────────────────────────

raw = 0
check("or default when falsy",    raw or 10,          10)
raw = 5
check("or keeps when truthy",     raw or 10,          5)

# ── Membership and identity ───────────────────────────────────────────────────

check("in — present",             "bert" in ["bert", "gpt2"],  True)
check("not in — absent",          "yolo" not in ["bert"],       True)
check("in — string substring",    "train" in "train_loss",      True)
check("is None — correct",        None is None,                 True)
_val = "x"
check("is not None — non-null",   _val is not None,            True)

# ── Bitwise ───────────────────────────────────────────────────────────────────

check("& AND",                    0b0101 & 0b0011,    0b0001)
check("& mask — bit set",         bool(0b1010 & 0b0010), True)
check("& mask — bit not set",     bool(0b1010 & 0b0001), False)
check("| OR combine",             0b0101 | 0b0011,    0b0111)
check("| grant permission",       0b0011 | 0b0100,    0b0111)
check("binary literal",           0b1101,             13)
check("int from binary string",   int("1101", 2),     13)
check("bin() representation",     bin(13),            "0b1101")

# ── Summary ───────────────────────────────────────────────────────────────────

print(f"\n{'─' * 42}")
print(f"  {passed} passed   {failed} failed")
print(f"{'─' * 42}\n")

if failed == 0:
    print("  All tests passed.")
    print("  You understand Python operators for this topic.")
    print("  Move on to 04_control_flow/ when ready.")
else:
    print(f"  {failed} test(s) failed.")
    print("  Review the failing cases in examples/ before moving on.")