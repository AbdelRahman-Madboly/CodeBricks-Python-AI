"""
Variables and Data Types — Examples

Covers variable assignment, Python's core types, type inspection,
and the dynamic typing behaviour that surprises most newcomers.
"""


# ---------------------------------------------------------------------------
# Example 1 — Core types and type inspection
# Scenario: storing metadata about a machine learning dataset
# ---------------------------------------------------------------------------

dataset_name = "deepfake-detection-v2"   # str
sample_count = 10_000                    # int  (underscores improve readability)
positive_ratio = 0.35                    # float
is_balanced = False                      # bool
validation_split = None                  # NoneType — not yet assigned

print(type(dataset_name))     # <class 'str'>
print(type(sample_count))     # <class 'int'>
print(type(positive_ratio))   # <class 'float'>
print(type(is_balanced))      # <class 'bool'>
print(type(validation_split)) # <class 'NoneType'>

# isinstance() is more useful than type() in real code because it respects inheritance
print(isinstance(sample_count, int))    # True
print(isinstance(is_balanced, int))     # True — bool is a subclass of int


# ---------------------------------------------------------------------------
# Example 2 — Dynamic typing and variable reassignment
# Scenario: a configuration value that changes type during setup
# ---------------------------------------------------------------------------

# Same name, different types at different points in the program
learning_rate = "auto"          # placeholder string during config parsing
print(f"Config stage: {learning_rate!r}")  # !r adds quotes around strings

learning_rate = 0.001           # resolved to float after parsing
print(f"Training stage: {learning_rate}")

# This is valid Python but a bad habit in large codebases —
# type hints (covered in Phase 5) prevent this kind of confusion


# ---------------------------------------------------------------------------
# Example 3 — Type conversion and floating point caution
# Scenario: computing a confidence threshold from user input
# ---------------------------------------------------------------------------

raw_input = "0.85"              # everything from input() comes in as str

# Convert to float for computation
confidence_threshold = float(raw_input)
flagged_samples = int(confidence_threshold * 1000)

print(f"Threshold : {confidence_threshold}")
print(f"Flagged   : {flagged_samples} of 1000 samples")

# Floating point trap — never compare floats with ==
a = 0.1 + 0.2
print(a == 0.3)           # False
print(round(a, 1) == 0.3) # True — use round() for equality checks

# None check — always use 'is', never '=='
result = None
print(result is None)     # True  (correct way)
print(result == None)     # True  (works but wrong style — triggers linter warning)
