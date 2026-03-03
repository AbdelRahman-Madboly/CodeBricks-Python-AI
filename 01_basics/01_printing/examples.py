"""
Printing — Examples

Demonstrates Python's print() function from basic usage to practical
formatting patterns used in real scripts and tools.
"""


# ---------------------------------------------------------------------------
# Example 1 — Basic print and f-strings
# Scenario: a script reports the result of a model evaluation run
# ---------------------------------------------------------------------------

model_name = "ResNet-50"
accuracy = 94.7
epoch = 12

# Old style — hard to read when values mix with text
print("Model:", model_name, "| Accuracy:", accuracy, "| Epoch:", epoch)

# f-string style — readable and precise
print(f"Model: {model_name} | Accuracy: {accuracy:.1f}% | Epoch: {epoch}")

# :.1f means: format as float with 1 decimal place
print(f"Accuracy rounded: {accuracy:.0f}%")


# ---------------------------------------------------------------------------
# Example 2 — sep and end for custom formatting
# Scenario: printing a progress bar and structured log lines
# ---------------------------------------------------------------------------

# sep joins multiple values with a custom separator instead of a space
print("2024", "01", "15", sep="-")          # 2024-01-15
print("user", "login", "success", sep=" | ")  # user | login | success

# end="" suppresses the newline — useful for inline progress display
print("Training", end=" ")
print("epoch 1...", end=" ")
print("done.")
# Output: Training epoch 1... done.

# Building a simple visual separator
print("-" * 40)


# ---------------------------------------------------------------------------
# Example 3 — Printing collections and multi-line output
# Scenario: displaying a summary report after processing a dataset
# ---------------------------------------------------------------------------

class_labels = ["real", "fake", "uncertain"]
class_counts = [820, 150, 30]

print("=== Dataset Summary ===")

# zip lets us iterate two lists together
for label, count in zip(class_labels, class_counts):
    # :>10 right-aligns the count in a 10-character wide column
    print(f"  {label:<12} {count:>6} samples")

print(f"\n  Total: {sum(class_counts):>10} samples")
print("=" * 23)
