"""
Control Flow — Solutions
"""


# ---------------------------------------------------------------------------
# Solution 1
# ---------------------------------------------------------------------------

score = 83

if not (0 <= score <= 100):
    print("Invalid score")
elif score >= 90:
    print(f"Score: {score} → Grade: A")
elif score >= 80:
    print(f"Score: {score} → Grade: B")
elif score >= 70:
    print(f"Score: {score} → Grade: C")
elif score >= 60:
    print(f"Score: {score} → Grade: D")
else:
    print(f"Score: {score} → Grade: F")


# ---------------------------------------------------------------------------
# Solution 2
# ---------------------------------------------------------------------------

for number in range(1, 31):
    if number % 15 == 0:      # check 15 first — it's the most specific case
        label = "FizzBuzz"
    elif number % 3 == 0:
        label = "Fizz"
    elif number % 5 == 0:
        label = "Buzz"
    else:
        label = str(number)
    print(label)


# ---------------------------------------------------------------------------
# Solution 3
# ---------------------------------------------------------------------------

checkpoints = [
    ("epoch_01.pt", True),
    ("epoch_05.pt", False),
    ("epoch_10.pt", True),
    ("epoch_15.pt", True),
    ("epoch_20.pt", False),
]

best_checkpoint = None

for filename, is_valid in checkpoints:
    if is_valid:
        # Keep overwriting — last valid one wins
        best_checkpoint = filename

if best_checkpoint is not None:
    print(f"Best checkpoint: {best_checkpoint}")
else:
    print("No valid checkpoint found.")
