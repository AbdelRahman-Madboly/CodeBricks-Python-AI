"""
05 — Functions | test.py
─────────────────────────
Verifies the specific behaviours covered in this topic.
Run with: python test.py
"""

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


# ── Functions under test ──────────────────────────────────────────────────────

def normalize(value: float, min_val: float, max_val: float) -> float:
    return (value - min_val) / (max_val - min_val)

def clamp(value: float, min_val: float = 0.0, max_val: float = 1.0) -> float:
    if value < min_val:
        return min_val
    if value > max_val:
        return max_val
    return value

def accuracy(correct: int, total: int) -> float:
    return correct / total

def compute_metrics(predictions: list, labels: list) -> tuple:
    correct = sum(p == l for p, l in zip(predictions, labels))
    total = len(labels)
    acc = correct / total
    return acc, 1.0 - acc

def collect_sample(sample: str, batch: list | None = None) -> list:
    if batch is None:
        batch = []
    batch.append(sample)
    return batch

def no_return_func():
    x = 42   # no return statement

def explicit_none():
    return None

def bare_return():
    return

# ── Tests ─────────────────────────────────────────────────────────────────────

print("05 — Functions | test.py\n")
print("Running tests...\n")

# Basic return
check("normalize black pixel",    round(normalize(0, 0, 255), 4),   0.0)
check("normalize midpoint",       round(normalize(128, 0, 255), 4), 0.502)
check("normalize white pixel",    normalize(255, 0, 255),            1.0)
check("normalize custom range",   normalize(150, 100, 200),          0.5)

# Default parameters
check("clamp below min",          clamp(-0.5),       0.0)
check("clamp within range",       clamp(0.75),       0.75)
check("clamp above max",          clamp(1.8),        1.0)
check("clamp custom range",       clamp(5, 0, 10),   5)
check("clamp custom min hit",     clamp(-1, 0, 10),  0)
check("clamp custom max hit",     clamp(11, 0, 10),  10)

# Accuracy
check("accuracy perfect",         accuracy(10, 10),  1.0)
check("accuracy zero",            accuracy(0, 10),   0.0)
check("accuracy partial",         accuracy(7, 8),    0.875)

# Multiple return values
acc, err = compute_metrics([1, 0, 1], [1, 0, 0])
check("multiple return — accuracy",   round(acc, 4),  0.6667)
check("multiple return — error rate", round(err, 4),  0.3333)
check("multiple return — sum to 1",   round(acc + err, 10), 1.0)

# Mutable default fix
r1 = collect_sample("a")
r2 = collect_sample("b")
check("mutable default — r1 length",    len(r1), 1)
check("mutable default — r2 length",    len(r2), 1)
check("mutable default — r1 not r2",    r1 is r2, False)

# Explicit batch still works
existing = ["x"]
r3 = collect_sample("y", existing)
check("explicit batch extended",        r3, ["x", "y"])

# None return
check("no return → None",              no_return_func() is None, True)
check("explicit return None → None",   explicit_none() is None,  True)
check("bare return → None",            bare_return() is None,    True)

# Scope — local assignment doesn't change outer
outer_x = 10
def modify_local():
    outer_x = 99
    return outer_x
modify_local()
check("local assignment doesn't touch global", outer_x, 10)

# ── Summary ───────────────────────────────────────────────────────────────────

print(f"\n{'─' * 40}")
print(f"  {passed} passed   {failed} failed")
print(f"{'─' * 40}\n")

if failed == 0:
    print("  All tests passed.")
    print("  You understand Python functions for this topic.")
    print("  Move on to 06_classes_intro/ when ready.")
else:
    print(f"  {failed} test(s) failed.")
    print("  Review the failing cases in examples/ before moving on.")