"""
15 — Exceptions | test.py
──────────────────────────
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


def raises(label: str, exc_type: type, fn) -> None:
    """Check that calling fn() raises the expected exception type."""
    global passed, failed
    try:
        fn()
        print(f"  ✗  {label}")
        print(f"       expected : {exc_type.__name__} to be raised")
        print(f"       got      : no exception")
        failed += 1
    except exc_type:
        print(f"  ✓  {label}")
        passed += 1
    except Exception as e:
        print(f"  ✗  {label}")
        print(f"       expected : {exc_type.__name__}")
        print(f"       got      : {type(e).__name__}: {e}")
        failed += 1


print("15 — Exceptions | test.py\n")
print("Running tests...\n")

# ── try/except basics ─────────────────────────────────────────────────────────

def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

check("no exception → returns result",   safe_div(10, 2),   5.0)
check("ZeroDivisionError → returns None", safe_div(10, 0),  None)

def catch_index():
    try:
        return [1, 2, 3][10]
    except IndexError:
        return "caught"

check("IndexError caught",               catch_index(),     "caught")

def no_exception_skips_except():
    result = []
    try:
        result.append("try")
    except Exception:
        result.append("except")
    return result

check("except skipped when no error",    no_exception_skips_except(), ["try"])

# ── raise ─────────────────────────────────────────────────────────────────────

def guard_positive(n):
    if n <= 0:
        raise ValueError(f"must be positive, got {n}")
    return n

check("raise — happy path",              guard_positive(5),  5)
raises("raise — triggers on bad input",  ValueError, lambda: guard_positive(-1))

def get_exception_message(fn):
    try:
        fn()
    except Exception as e:
        return str(e)

check("raise — message content",
      get_exception_message(lambda: guard_positive(0)),
      "must be positive, got 0")

# ── specific exception types ──────────────────────────────────────────────────

def parse_float(s):
    try:
        return float(s)
    except ValueError:
        return None

check("ValueError caught on bad string",  parse_float("abc"),   None)
check("ValueError not raised on good str", parse_float("0.91"),  0.91)

def safe_key(d, k):
    try:
        return d[k]
    except KeyError:
        return "missing"

check("KeyError caught",                  safe_key({"a": 1}, "b"), "missing")
check("KeyError not raised on valid key", safe_key({"a": 1}, "a"), 1)

# ── catch order — specific before general ────────────────────────────────────

def ordered_catch(error_type):
    """Returns which handler caught the exception."""
    try:
        if error_type == "index":
            raise IndexError("test")
        elif error_type == "value":
            raise ValueError("test")
        elif error_type == "other":
            raise RuntimeError("test")
    except IndexError:
        return "IndexError handler"
    except ValueError:
        return "ValueError handler"
    except Exception:
        return "general handler"
    return "no error"

check("IndexError caught by specific handler",  ordered_catch("index"),  "IndexError handler")
check("ValueError caught by specific handler",  ordered_catch("value"),  "ValueError handler")
check("RuntimeError falls to general handler",  ordered_catch("other"),  "general handler")
check("no exception → returns normally",        ordered_catch("none"),   "no error")

# ── else clause ───────────────────────────────────────────────────────────────

def with_else(value):
    result = []
    try:
        x = int(value)
    except ValueError:
        result.append("except")
    else:
        result.append(f"else:{x}")
    return result

check("else runs on success",         with_else("5"),    ["else:5"])
check("else skipped on exception",    with_else("bad"),  ["except"])

# ── finally clause ────────────────────────────────────────────────────────────

def with_finally(should_raise):
    result = []
    try:
        if should_raise:
            raise RuntimeError("boom")
        result.append("try")
    except RuntimeError:
        result.append("except")
    finally:
        result.append("finally")
    return result

check("finally runs on success",    with_finally(False),  ["try", "finally"])
check("finally runs on exception",  with_finally(True),   ["except", "finally"])

# ── custom exceptions ─────────────────────────────────────────────────────────

class AppError(Exception):
    pass

class NetworkError(AppError):
    pass

def check_hierarchy():
    """NetworkError should be catchable as AppError."""
    try:
        raise NetworkError("timeout")
    except AppError:
        return "caught as AppError"

check("custom exception caught by parent class", check_hierarchy(), "caught as AppError")

raises("custom exception raised correctly", NetworkError,
       lambda: (_ for _ in ()).throw(NetworkError("test")))

# ── catching multiple types ───────────────────────────────────────────────────

def multi_catch(fn):
    try:
        return fn()
    except (ValueError, TypeError):
        return "value or type error"

check("catches ValueError in tuple",  multi_catch(lambda: int("x")),     "value or type error")
check("catches TypeError in tuple",   multi_catch(lambda: "a" + 1),      "value or type error")
check("does not catch other errors",
      multi_catch(lambda: 1),         1)

# ── re-raise ──────────────────────────────────────────────────────────────────

def log_and_reraise():
    log = []
    try:
        try:
            raise ValueError("original")
        except ValueError:
            log.append("logged")
            raise   # bare raise — re-raises original
    except ValueError as e:
        log.append(str(e))
    return log

check("bare raise re-raises original exception", log_and_reraise(), ["logged", "original"])

# ── Summary ───────────────────────────────────────────────────────────────────

print(f"\n{'─' * 44}")
print(f"  {passed} passed   {failed} failed")
print(f"{'─' * 44}\n")

if failed == 0:
    print("  All tests passed.")
    print("  You understand Python exceptions for this topic.")
    print("  Move on to 06_classes_intro/ when ready.")
else:
    print(f"  {failed} test(s) failed.")
    print("  Review the failing cases in examples/ before moving on.")