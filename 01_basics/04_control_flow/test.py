"""
04 — Control Flow | test.py
────────────────────────────
Run with: python test.py
"""

import io, sys

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


def capture(func):
    buf = io.StringIO()
    sys.stdout = buf
    func()
    sys.stdout = sys.__stdout__
    return buf.getvalue().strip()


print("04 — Control Flow | test.py\n")
print("Running tests...\n")

# ── if/elif/else ──────────────────────────────────────────────────────────────

def tier(confidence):
    if confidence >= 0.95:   return "auto_accept"
    elif confidence >= 0.75: return "human_review"
    elif confidence >= 0.50: return "flag"
    else:                    return "reject"

check("if — top tier",          tier(0.97),  "auto_accept")
check("elif — second tier",     tier(0.80),  "human_review")
check("elif — third tier",      tier(0.60),  "flag")
check("else — bottom",          tier(0.30),  "reject")
check("boundary 0.95",          tier(0.95),  "auto_accept")
check("boundary 0.75",          tier(0.75),  "human_review")
check("boundary 0.50",          tier(0.50),  "flag")

# ── ternary expression ────────────────────────────────────────────────────────

check("ternary true branch",    "pass" if 80 >= 60 else "fail",  "pass")
check("ternary false branch",   "pass" if 40 >= 60 else "fail",  "fail")
check("ternary equality",       "yes"  if 5 == 5   else "no",    "yes")

# ── range ─────────────────────────────────────────────────────────────────────

check("range(5) length",        list(range(5)),           [0,1,2,3,4])
check("range(1,6)",             list(range(1,6)),          [1,2,3,4,5])
check("range(0,10,2)",          list(range(0,10,2)),       [0,2,4,6,8])
check("range stop exclusive",   5 in range(5),            False)
check("range down",             list(range(5,0,-1)),       [5,4,3,2,1])

# ── enumerate ────────────────────────────────────────────────────────────────

items = ["a", "b", "c"]
check("enumerate default",      list(enumerate(items)),        [(0,"a"),(1,"b"),(2,"c")])
check("enumerate start=1",      list(enumerate(items,start=1)),[(1,"a"),(2,"b"),(3,"c")])

# ── break and continue ────────────────────────────────────────────────────────

result = []
for i in range(10):
    if i == 3:
        continue
    if i == 6:
        break
    result.append(i)
check("break + continue",       result, [0,1,2,4,5])

# ── for/else ─────────────────────────────────────────────────────────────────

def search(items, target):
    for item in items:
        if item == target:
            return "found"
            break
    else:
        return "not found"

check("for/else — found",       search([1,2,3], 2),   "found")
check("for/else — not found",   search([1,2,3], 9),   "not found")
check("for/else — empty list",  search([], 1),         "not found")

# ── while loop ───────────────────────────────────────────────────────────────

count = 0
total = 0
while count < 5:
    total += count
    count += 1
check("while accumulator",      total, 10)   # 0+1+2+3+4

# ── boolean conditions ────────────────────────────────────────────────────────

check("and all true",           True and True and True,   True)
check("and one false",          True and False and True,  False)
check("or one true",            False or True or False,   True)
check("or all false",           False or False,           False)
check("not reversal",           not False,                True)
check("chained comparison",     1 < 2 < 3,                True)
check("chained fails",          1 < 3 < 2,                False)

# ── filter pattern ────────────────────────────────────────────────────────────

data = [1, 2, 3, 4, 5, 6]
evens = []
for n in data:
    if n % 2 != 0:
        continue
    evens.append(n)
check("continue filter",        evens, [2,4,6])

# ── Summary ───────────────────────────────────────────────────────────────────

print(f"\n{'─' * 42}")
print(f"  {passed} passed   {failed} failed")
print(f"{'─' * 42}\n")

if failed == 0:
    print("  All tests passed.")
    print("  You understand Python control flow for this topic.")
    print("  Move on to 05_functions/ when ready.")
else:
    print(f"  {failed} test(s) failed.")
    print("  Review the failing cases in examples/ before moving on.")