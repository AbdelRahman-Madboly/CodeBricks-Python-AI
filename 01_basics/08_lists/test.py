"""
08 — Lists | test.py
─────────────────────
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


print("08 — Lists | test.py\n")
print("Running tests...\n")

# ── Indexing ──────────────────────────────────────────────────────────────────

lst = [10, 20, 30, 40, 50]

check("index 0",                  lst[0],           10)
check("index 2",                  lst[2],           30)
check("index -1 (last)",          lst[-1],          50)
check("index -2",                 lst[-2],          40)

# ── Slicing ───────────────────────────────────────────────────────────────────

check("slice [:3]",               lst[:3],          [10, 20, 30])
check("slice [2:]",               lst[2:],          [30, 40, 50])
check("slice [1:4]",              lst[1:4],         [20, 30, 40])
check("slice [::2]",              lst[::2],         [10, 30, 50])
check("slice [::-1]",             lst[::-1],        [50, 40, 30, 20, 10])
check("out of range slice",       lst[2:100],       [30, 40, 50])
check("empty slice",              lst[10:20],       [])

# ── Modifying ────────────────────────────────────────────────────────────────

m = [1, 2, 3]
m.append(4)
check("append",                   m,                [1, 2, 3, 4])
m.insert(1, 99)
check("insert",                   m,                [1, 99, 2, 3, 4])
popped = m.pop(1)
check("pop(1) value",             popped,           99)
check("pop(1) list",              m,                [1, 2, 3, 4])
last = m.pop()
check("pop() last value",         last,             4)
check("pop() list",               m,                [1, 2, 3])
m.remove(2)
check("remove",                   m,                [1, 3])

# ── Built-ins ─────────────────────────────────────────────────────────────────

nums = [3, 1, 4, 1, 5, 9, 2]
check("len",                      len(nums),        7)
check("sum",                      sum(nums),        25)
check("min",                      min(nums),        1)
check("max",                      max(nums),        9)
check("sorted ascending",         sorted(nums),     [1, 1, 2, 3, 4, 5, 9])
check("sorted descending",        sorted(nums, reverse=True), [9, 5, 4, 3, 2, 1, 1])
check("original unchanged",       nums,             [3, 1, 4, 1, 5, 9, 2])
check("in — present",             5 in nums,        True)
check("in — absent",              7 in nums,        False)

# ── Comprehensions ────────────────────────────────────────────────────────────

scores = [0.92, 0.45, 0.88, 0.31, 0.76]

check("filter comprehension",     [s for s in scores if s >= 0.75],
                                  [0.92, 0.88, 0.76])
check("transform comprehension",  [round(s * 100) for s in scores],
                                  [92, 45, 88, 31, 76])
check("squares from range",       [i**2 for i in range(1, 5)],
                                  [1, 4, 9, 16])

# ── Shallow copy trap ─────────────────────────────────────────────────────────

a = [1, 2, 3]
b = a[:]
b.append(4)
check("slice copy — original unchanged",  a, [1, 2, 3])
check("slice copy — copy modified",       b, [1, 2, 3, 4])

nested_bad = [[0]] * 3
nested_bad[0].append(1)
check("* trap — all rows same object",    nested_bad, [[0, 1], [0, 1], [0, 1]])

nested_good = [[0] for _ in range(3)]
nested_good[0].append(1)
check("comprehension — rows independent", nested_good, [[0, 1], [0], [0]])

# ── enumerate and zip ─────────────────────────────────────────────────────────

items = ["a", "b", "c"]
check("enumerate default",  list(enumerate(items)),         [(0,"a"),(1,"b"),(2,"c")])
check("enumerate start=1",  list(enumerate(items,start=1)), [(1,"a"),(2,"b"),(3,"c")])

preds  = [1, 0, 1]
labels = [1, 0, 0]
check("zip pairs",          list(zip(preds, labels)),       [(1,1),(0,0),(1,0)])
check("zip accuracy",       sum(p==l for p,l in zip(preds,labels)), 2)

# ── Summary ───────────────────────────────────────────────────────────────────

print(f"\n{'─' * 44}")
print(f"  {passed} passed   {failed} failed")
print(f"{'─' * 44}\n")

if failed == 0:
    print("  All tests passed.")
    print("  You understand Python lists for this topic.")
    print("  Move on to 09_tuples/ when ready.")
else:
    print(f"  {failed} test(s) failed.")
    print("  Review the failing cases in examples/ before moving on.")