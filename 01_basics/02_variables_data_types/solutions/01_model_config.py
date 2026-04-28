"""
solutions/01_model_config.py
─────────────────────────────
Topic    : Variables and Data Types
Solution : Exercise 1 — Model configuration block

Open this only after a genuine attempt at the exercise.
"""

# ── Variables ─────────────────────────────────────────────────────────────────

model      = "bert-base-uncased"   # str
epochs     = 20                    # int
lr         = 0.0002                # float — note: scientific notation 2e-4 also works
pretrained = True                  # bool
checkpoint = None                  # NoneType — not yet assigned

# ── Config summary ────────────────────────────────────────────────────────────

print("  ╔══════════════════════════════════════╗")
print("  ║         Model Configuration          ║")
print("  ╠══════════════════════════════════════╣")
print(f"  ║  {'model':<12}: {model:<22}║")
print(f"  ║  {'epochs':<12}: {epochs:<22}║")
print(f"  ║  {'lr':<12}: {lr:<22}║")
print(f"  ║  {'pretrained':<12}: {pretrained:<22}║")
print(f"  ║  {'checkpoint':<12}: {str(checkpoint):<22}║")
print("  ╠══════════════════════════════════════╣")
print("  ║  Types                               ║")
print(f"  ║  {'model':<12}: {type(model).__name__:<22}║")
print(f"  ║  {'epochs':<12}: {type(epochs).__name__:<22}║")
print(f"  ║  {'lr':<12}: {type(lr).__name__:<22}║")
print(f"  ║  {'pretrained':<12}: {type(pretrained).__name__:<22}║")
print(f"  ║  {'checkpoint':<12}: {type(checkpoint).__name__:<22}║")
print("  ╚══════════════════════════════════════╝")

# ── Why this works ────────────────────────────────────────────────────────────
#
# {model:<22}
#   Left-aligns model's value in a 22-character field.
#   This keeps the right border of the box aligned regardless of value length.
#   The field width was chosen to fit the box: 2 indent + 12 label + 2 colon-space
#   + 22 value + 1 border = 39 chars inside.
#
# str(checkpoint)
#   None doesn't format inside f-strings as "None" automatically —
#   well, it does, but being explicit with str() makes the intention clear.
#   When in doubt, convert to str explicitly.
#
# type().__name__
#   type(x) returns the class object, e.g. <class 'int'>
#   .____name__ gives just the name string: "int", "str", "NoneType"
#   Much cleaner for display than printing the full class object.
#
# lr = 0.0002 vs lr = 2e-4
#   Both are identical. Scientific notation (2e-4 = 2 × 10^-4 = 0.0002)
#   is common in ML configs for learning rates. Know both forms.