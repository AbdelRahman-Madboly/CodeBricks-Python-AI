"""
solutions/03_training_bar.py
─────────────────────────────
Topic    : Printing
Solution : Exercise 3 — One-line training progress

Open this only after a genuine attempt at the exercise.
"""

training_log = [
    (1, 0.8821, 0.6123),
    (2, 0.6134, 0.7452),
    (3, 0.4502, 0.8134),
    (4, 0.3211, 0.8671),
    (5, 0.2498, 0.9012),
]

# ── Solution ─────────────────────────────────────────────────────────────────

print("Training: ", end="")

for i, (epoch, loss, acc) in enumerate(training_log):
    block = f"E{epoch}(loss={loss:.4f},acc={acc * 100:.1f}%)"

    if i < len(training_log) - 1:
        print(block, end=" → ")   # not the last — add arrow, no newline
    else:
        print(block, end=" ✓ done\n")   # last — add done marker, then newline

# ── Why this works ───────────────────────────────────────────────────────────
#
# enumerate(training_log)
#   Gives you (index, value) so you can check whether you're on
#   the last item. Without the index, you'd have to track it manually.
#
# i < len(training_log) - 1
#   True for every item except the last.
#   Lets you add " → " after each epoch except the final one.
#   This is the standard pattern for "separator between items" problems.
#
# end=" → " and end=" ✓ done\n"
#   end= controls what goes after the print call.
#   By default it's "\n". Here we replace it to stay on the same line.
#   The \n in the last call moves to the next line when we're done.
#
# acc * 100
#   acc is stored as 0.6123 (a fraction).
#   Multiplying by 100 converts it to 61.23 for display.
#   :.1f then rounds to 1 decimal: 61.2%.
#
# Why build block as a variable first?
#   It keeps the print() call readable. You could put the whole f-string
#   inside print() but it becomes hard to read.
#   Separating the formatting from the output logic is good practice.
#
# Alternative approach — valid and clean:
#   separator = " → "
#   parts = [f"E{e}(loss={l:.4f},acc={a*100:.1f}%)" for e, l, a in training_log]
#   print("Training:", separator.join(parts), "✓ done")
#
#   This builds a list of formatted strings then joins them.
#   You'll learn list comprehensions in Phase 3. Both approaches are correct.