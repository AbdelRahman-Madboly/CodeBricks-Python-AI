"""
07 — Memory and Mutability | test.py
─────────────────────────────────────
Run with: python test.py
"""

import copy

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


print("07 — Memory and Mutability | test.py\n")
print("Running tests...\n")

# ── id() and identity ─────────────────────────────────────────────────────────

a = [1, 2, 3]
b = a
check("alias shares id",          id(a) == id(b),          True)

c = a[:]
check("shallow copy differs id",  id(a) == id(c),          False)
check("shallow copy same value",  a == c,                  True)

# ── is vs == ─────────────────────────────────────────────────────────────────

x = [1, 2, 3]
y = [1, 2, 3]
check("== same value different obj",  x == y,   True)
check("is different objects",         x is y,   False)

z = x
check("is same object",               x is z,   True)

check("None check with is",           None is None,  True)

# ── Aliasing — mutation propagates ───────────────────────────────────────────

original = {"lr": 0.001, "epochs": 10}
alias    = original
alias["epochs"] = 99
check("alias mutation visible in original",  original["epochs"],  99)

# ── Shallow copy — flat dict ──────────────────────────────────────────────────

base = {"lr": 0.001, "epochs": 10}
copy_d = base.copy()
copy_d["epochs"] = 99
check("shallow copy protects flat key",  base["epochs"],  10)

# ── Shallow copy — nested list still shared ───────────────────────────────────

nested = {"tags": ["v1"]}
shallow = nested.copy()
shallow["tags"].append("v2")
check("shallow copy shares nested list",  nested["tags"],  ["v1", "v2"])

# ── deepcopy — fully independent ──────────────────────────────────────────────

deep_base = {"lr": 0.001, "tags": ["v1"], "aug": {"flip": True}}
deep_copy = copy.deepcopy(deep_base)

deep_copy["lr"] = 0.99
deep_copy["tags"].append("v2")
deep_copy["aug"]["flip"] = False

check("deepcopy protects scalar",   deep_base["lr"],           0.001)
check("deepcopy protects list",     deep_base["tags"],         ["v1"])
check("deepcopy protects nested",   deep_base["aug"]["flip"],  True)

check("deepcopy different id tags", deep_base["tags"] is deep_copy["tags"], False)
check("deepcopy different id aug",  deep_base["aug"]  is deep_copy["aug"],  False)

# ── List shallow copy ─────────────────────────────────────────────────────────

lst = [1, 2, 3]
lst_slice  = lst[:]
lst_copy   = lst.copy()
lst_list   = list(lst)

lst_slice.append(4)
check("slice copy — original unchanged",    lst,  [1, 2, 3])
check("slice copy — copy extended",         lst_slice, [1, 2, 3, 4])
check("list.copy() independent",            lst_copy,  [1, 2, 3])
check("list() independent",                 lst_list,  [1, 2, 3])

# ── += on immutable vs mutable ────────────────────────────────────────────────

n = 5
n_id_before = id(n)
n += 1
check("+= int creates new object",   id(n) == n_id_before,  False)
check("+= int correct value",        n,                     6)

lst2 = [1, 2]
lst2_id_before = id(lst2)
lst2 += [3]
check("+= list mutates in place",    id(lst2) == lst2_id_before,  True)
check("+= list correct value",       lst2,                         [1, 2, 3])

# ── Mutable default in function — standard fix ───────────────────────────────

def build_config(extras=None):
    if extras is None:
        extras = {}
    extras["built"] = True
    return extras

r1 = build_config()
r2 = build_config()
check("None default — independent calls",  r1 is r2,  False)

# ── Function mutation — mutable arg ──────────────────────────────────────────

def bad_append(lst, val):
    lst.append(val)   # mutates caller's list

source = [1, 2, 3]
bad_append(source, 4)
check("function mutates caller's list",  source,  [1, 2, 3, 4])

def safe_append(lst, val):
    lst = lst[:]      # local copy — caller's list unchanged
    lst.append(val)
    return lst

source2 = [1, 2, 3]
result  = safe_append(source2, 4)
check("safe append — original unchanged",  source2,  [1, 2, 3])
check("safe append — new list returned",   result,   [1, 2, 3, 4])

# ── Immutable — reassign inside function doesn't affect caller ────────────────

def try_mutate_int(n):
    n += 100   # local reassign — caller's n unchanged
    return n

val = 10
try_mutate_int(val)
check("int unchanged after function",  val,  10)

# ── Summary ───────────────────────────────────────────────────────────────────

print(f"\n{'─' * 44}")
print(f"  {passed} passed   {failed} failed")
print(f"{'─' * 44}\n")

if failed == 0:
    print("  All tests passed.")
    print("  You understand Python memory and mutability.")
    print("  Move on to 13_modules_packages/ when ready.")
else:
    print(f"  {failed} test(s) failed.")
    print("  Review the failing cases in examples/ before moving on.")