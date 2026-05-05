"""
12 — Dictionaries and Sets | test.py
─────────────────────────────────────
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


print("12 — Dictionaries and Sets | test.py\n")
print("Running tests...\n")

# ── Dict creation and access ──────────────────────────────────────────────────

config = {"model": "ResNet-50", "epochs": 30, "lr": 0.001}

check("access by key",           config["model"],              "ResNet-50")
check("access int value",        config["epochs"],             30)
check("key in dict — present",   "lr" in config,               True)
check("key in dict — absent",    "dropout" in config,          False)
check("len",                     len(config),                  3)

# ── Safe access ───────────────────────────────────────────────────────────────

check(".get — present",          config.get("epochs"),         30)
check(".get — absent → None",    config.get("dropout"),        None)
check(".get — absent + default", config.get("dropout", 0.5),  0.5)
check(".get — present ignores default", config.get("lr", 99), 0.001)

# ── Add, update, delete ───────────────────────────────────────────────────────

d = {"a": 1, "b": 2}
d["c"] = 3
check("add new key",             d,                            {"a": 1, "b": 2, "c": 3})
d["a"] = 99
check("overwrite existing key",  d["a"],                       99)
popped = d.pop("b")
check("pop returns value",       popped,                       2)
check("pop removes key",         "b" in d,                     False)
d.pop("missing_key", None)      # should not raise
check("pop missing with default no error", "missing_key" in d, False)

# ── Iteration ─────────────────────────────────────────────────────────────────

scores = {"accuracy": 0.90, "precision": 0.88, "recall": 0.93}

check(".keys()",     sorted(scores.keys()),   ["accuracy", "precision", "recall"])
check(".values()",   sorted(scores.values()), [0.88, 0.90, 0.93])
check(".items() len", len(list(scores.items())), 3)

# ── Frequency counting ────────────────────────────────────────────────────────

labels = ["real", "fake", "fake", "real", "uncertain", "fake"]
counts: dict[str, int] = {}
for label in labels:
    counts[label] = counts.get(label, 0) + 1

check("frequency count — real",      counts["real"],       2)
check("frequency count — fake",      counts["fake"],       3)
check("frequency count — uncertain", counts["uncertain"],  1)

# ── Nested dict ───────────────────────────────────────────────────────────────

run = {"run_001": {"val_acc": 0.92, "status": "done"}}
check("nested access",      run["run_001"]["val_acc"],   0.92)
check("nested key present", "status" in run["run_001"],  True)

# ── Sets ──────────────────────────────────────────────────────────────────────

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

check("union",                  a | b,          {1, 2, 3, 4, 5, 6})
check("intersection",           a & b,          {3, 4})
check("difference a-b",         a - b,          {1, 2})
check("difference b-a",         b - a,          {5, 6})
check("symmetric difference",   a ^ b,          {1, 2, 5, 6})
check("membership — present",   3 in a,         True)
check("membership — absent",    9 in a,         False)

# ── Set mutation ──────────────────────────────────────────────────────────────

s = {"x", "y"}
s.add("z")
check("add new element",         "z" in s,        True)
s.add("z")
check("add duplicate — no error", len(s),          3)
s.discard("w")                  # no error if absent
check("discard missing — no error", len(s),        3)
s.discard("x")
check("discard existing",        "x" in s,         False)

# ── Deduplication ─────────────────────────────────────────────────────────────

raw = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
check("set dedup length",     len(set(raw)),    7)
check("set dedup contents",   set(raw),         {1, 2, 3, 4, 5, 6, 9})

# ── Empty set vs empty dict ───────────────────────────────────────────────────

check("type of {}",     type({}),      dict)
check("type of set()",  type(set()),   set)

# ── Summary ───────────────────────────────────────────────────────────────────

print(f"\n{'─' * 44}")
print(f"  {passed} passed   {failed} failed")
print(f"{'─' * 44}\n")

if failed == 0:
    print("  All tests passed.")
    print("  You understand Python dicts and sets for this topic.")
    print("  Move on to 15_exceptions/ when ready.")
else:
    print(f"  {failed} test(s) failed.")
    print("  Review the failing cases in examples/ before moving on.")