"""
solutions/03_type_predictions.py
─────────────────────────────────
Topic    : Variables and Data Types
Solution : Exercise 3 — Type predictions

Open this only after filling in your own predictions in exercises/03.
"""

a_small = 5
b_small = 5
a_large = 1000
b_large = 1000

# ── Correct answers with explanations ────────────────────────────────────────

q1  = False   # 0.1 + 0.2 = 0.30000000000000004 — float precision error
q2  = True    # bool inherits from int — issubclass(bool, int) is True
q3  = True    # True is stored as 1 — True == 1 is True
q4  = False   # None is not equal to anything except None itself
q5  = True    # 10 / 2 = 5.0 — division ALWAYS returns float in Python 3
q6  = True    # 10 // 3 = 3 — floor division truncates toward negative infinity
q7  = True    # bool("False") = True — any non-empty string is truthy
q8  = True    # CPython caches integers -5 to 256 — same object, same id
q9  = False   # 1000 is outside cache range — two separate objects created
q10 = True    # int("42") returns an int object

actuals = [
    ("0.1 + 0.2 == 0.3",           0.1 + 0.2 == 0.3),
    ("issubclass(bool, int)",       issubclass(bool, int)),
    ("True == 1",                   True == 1),
    ("None == False",               None == False),
    ("10 / 2 is float",             isinstance(10 / 2, float)),
    ("10 // 3 == 3",                10 // 3 == 3),
    ('bool("False")',               bool("False")),
    ("a is b (small int)",          a_small is b_small),
    ("a is b (large int)",          a_large is b_large),
    ("isinstance(int('42'), int)",  isinstance(int("42"), int)),
]

predictions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

print("=== Type Predictions — Solution ===\n")
print(f"  {'Question':<30} {'Predicted':<12} {'Actual':<12} {'Result'}")
print("  " + "─" * 62)

correct = 0
for i, ((label, actual), predicted) in enumerate(zip(actuals, predictions), 1):
    match = predicted == actual
    result = "✓" if match else "✗"
    if match:
        correct += 1
    print(f"  Q{i:<2} {label:<28} {str(predicted):<12} {str(actual):<12} {result}")

print("  " + "─" * 62)
print(f"\n  Score: {correct} / 10\n")

# ── Why each answer is what it is ────────────────────────────────────────────
#
# Q1 — False: Float precision
#   Binary (base-2) cannot represent 0.1 or 0.2 exactly.
#   Their sum is 0.30000000000000004. Use round() or math.isclose().
#
# Q2 — True: bool is a subclass of int
#   In Python's type hierarchy, bool inherits from int.
#   True is literally the integer 1, False is 0.
#   That's why True + True == 2 and False * 100 == 0.
#
# Q3 — True: True == 1
#   Follows directly from Q2. True is stored as 1.
#
# Q4 — False: None == False
#   None is not equal to anything except None.
#   None == False → False. None is None → True.
#   Always use 'is None', never '== None'.
#
# Q5 — True: 10 / 2 returns float
#   In Python 3, / always returns float. 10 / 2 = 5.0, not 5.
#   In Python 2 it returned int — this changed in Python 3.
#   Use // if you need integer division.
#
# Q6 — True: 10 // 3 == 3
#   Floor division truncates toward negative infinity.
#   10 // 3 = 3 (drops the .333), -10 // 3 = -4 (not -3 — floors down).
#
# Q7 — True: bool("False") is True
#   The most common beginner trap in this topic.
#   bool() on any non-empty string returns True — it doesn't parse the content.
#   Fix: use raw == "True" for string-to-bool conversion.
#
# Q8 — True: small integers are cached (a is b)
#   CPython (the standard Python implementation) caches integers from -5 to 256.
#   When you write a = 5 and b = 5, both point to the same cached object.
#   This is an implementation detail — never rely on it for logic.
#
# Q9 — False: large integers are not cached (a is b)
#   1000 is outside the cache range. Python creates two separate int objects.
#   a is b returns False even though a == b is True.
#   This is why == tests value and 'is' tests identity — use == for values.
#
# Q10 — True: int("42") returns int
#   int() is a conversion function that returns an int object.
#   isinstance(int("42"), int) → True.