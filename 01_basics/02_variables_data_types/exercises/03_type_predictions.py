"""
exercises/03_type_predictions.py
─────────────────────────────────
Topic    : Variables and Data Types
Exercise : 3 of 3 — Hard
Concept  : Type behaviour, identity vs equality, float precision, operator results

Context
-------
Before you write code that handles data, you need to be able to
predict how Python behaves — not just run it and see.

This exercise tests whether you've built the right mental model.
Reason through each question before running the file.

─────────────────────────────────────────────────────────────────
Task
─────────────────────────────────────────────────────────────────
Fill in each prediction with True or False.
Then run the file to see how many you got right.

No looking anything up. Work through each one with your mental model.
─────────────────────────────────────────────────────────────────
"""

# ── Your predictions — replace each None with True or False ──────────────────

# Q1: Does 0.1 + 0.2 equal 0.3 in Python?
q1 = None

# Q2: Is bool a subclass of int?
q2 = None

# Q3: Does True == 1 evaluate to True?
q3 = None

# Q4: Is None == False?
q4 = None

# Q5: What does 10 / 2 return — int or float?
#     Assign True if you think it returns float, False if int
q5 = None

# Q6: What does 10 // 3 return?
#     Assign True if you think the result is 3 (floor), False if 3.333
q6 = None

# Q7: bool("False") — is this True or False?
q7 = None

# Q8: After: a = 5; b = 5 — does a is b return True?
#     (CPython caches small integers from -5 to 256)
q8 = None

# Q9: After: a = 1000; b = 1000 — does a is b return True?
#     (Same question, but 1000 is outside the cache range)
q9 = None

# Q10: What type does int("42") return?
#      Assign True if you think it's int, False if str
q10 = None

# ── Verification — run this after filling in your predictions ─────────────────

a_small = 5
b_small = 5
a_large = 1000
b_large = 1000

actuals = [
    ("0.1 + 0.2 == 0.3",     0.1 + 0.2 == 0.3),
    ("issubclass(bool, int)", issubclass(bool, int)),
    ("True == 1",             True == 1),
    ("None == False",         None == False),
    ("10 / 2 is float",       isinstance(10 / 2, float)),
    ("10 // 3 == 3",          10 // 3 == 3),
    ('bool("False")',         bool("False")),
    ("a is b (small int)",    a_small is b_small),
    ("a is b (large int)",    a_large is b_large),
    ("isinstance(int('42'), int)", isinstance(int("42"), int)),
]

predictions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

print("=== Type Predictions — Results ===\n")
print(f"  {'Question':<30} {'Predicted':<12} {'Actual':<12} {'Result'}")
print("  " + "─" * 62)

correct = 0
for i, ((label, actual), predicted) in enumerate(zip(actuals, predictions), 1):
    if predicted is None:
        result = "⚪ skipped"
    elif predicted == actual:
        result = "✓ correct"
        correct += 1
    else:
        result = "✗ wrong"
    print(f"  Q{i:<2} {label:<28} {str(predicted):<12} {str(actual):<12} {result}")

print("  " + "─" * 62)
answered = sum(1 for p in predictions if p is not None)
print(f"\n  Score: {correct} / {answered} answered correctly")
print()

if correct == answered == 10:
    print("  All correct. You understand how Python handles types.")
elif correct >= 7:
    print("  Good. Review the ones you missed in examples/03_conversion_and_ops.py")
else:
    print("  Revisit examples/ — especially 02_dynamic_typing.py and 03_conversion_and_ops.py")