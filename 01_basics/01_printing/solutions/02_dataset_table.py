"""
solutions/02_dataset_table.py
──────────────────────────────
Topic    : Printing
Solution : Exercise 2 — Dataset summary table

Open this only after a genuine attempt at the exercise.
"""

dataset_name = "Sentiment Analysis"

splits = {
    "Train":      12_000,
    "Validation":  2_571,
    "Test":        2_572,
}

# ── Solution ─────────────────────────────────────────────────────────────────

total = sum(splits.values())   # don't hardcode — let the code count

print(f"  {'═' * 42}")
print(f"    Dataset Summary — {dataset_name}")
print(f"  {'═' * 42}")
print(f"    {'Split':<12} {'Samples':>9} {'% of Total':>12}")
print(f"    {'─' * 34}")

for split_name, count in splits.items():
    percentage = (count / total) * 100
    print(f"    {split_name:<12} {count:>9,} {percentage:>11.1f}%")

print(f"    {'─' * 34}")
print(f"    {'Total':<12} {total:>9,} {'100.0%':>12}")
print(f"  {'═' * 42}")

# ── Why this works ───────────────────────────────────────────────────────────
#
# sum(splits.values())
#   .values() gives you the numbers from the dict.
#   sum() adds them up. Never hardcode a total — if the data changes,
#   the total updates automatically.
#
# splits.items()
#   Gives you (key, value) pairs so you can loop over both at once.
#   You'll use .items() constantly when working with dictionaries.
#
# {count:>9,}
#   :>9   right-align in 9 characters
#   ,     add comma separators
#   Both specs work together — you can combine them.
#
# {'─' * 34}
#   You can put any expression inside f-string braces, including
#   string repetition. Keeps the separator width in one place.
#
# Why does the percentage column say {:>11.1f}% and not {:>12.1f}%?
#   The % sign is printed as a literal character outside the format spec.
#   So the number takes 11 chars, and the % adds 1 more = 12 total.
#   The header "% of Total" is 10 chars — the column still lines up.