"""
examples/01_indexing_and_slicing.py
────────────────────────────────────
Topic  : Lists
Example: 1 of 3 — Indexing, slicing, negative indices, list creation

Context
-------
A training pipeline is a sequence of named stages. You need to inspect
individual stages, extract subsets, reverse the order for debugging, and
verify the pipeline structure before starting a long training run.

Covers:
  - list literals and list()
  - Positive indexing: lst[0], lst[2]
  - Negative indexing: lst[-1], lst[-2]
  - Slicing: lst[start:stop:step]
  - Slicing never raises IndexError — out-of-bounds clips silently
  - Indexing DOES raise IndexError
  - len(), in operator
  - Modifying: append, insert, pop, remove

Run this file. Predict each output before you see it.
"""

# ── Creating lists ────────────────────────────────────────────────────────────

# Literal
pipeline = ["load", "validate", "preprocess", "train", "evaluate", "save"]

# From a range — common for generating test data
batch_ids = list(range(0, 10))    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
epoch_range = list(range(1, 6))   # [1, 2, 3, 4, 5]
print(f"Batch IDs   : {batch_ids}")
print(f"Epoch range : {epoch_range}")

# ── Indexing ──────────────────────────────────────────────────────────────────

print()
print("=== Indexing ===")
print(f"First stage      : {pipeline[0]}")    # load
print(f"Third stage      : {pipeline[2]}")    # preprocess
print(f"Last stage       : {pipeline[-1]}")   # save
print(f"Second to last   : {pipeline[-2]}")   # evaluate

# IndexError — uncomment to see it crash
# print(pipeline[10])    # IndexError: list index out of range

# ── Slicing ───────────────────────────────────────────────────────────────────

print()
print("=== Slicing ===")
print(f"First 3          : {pipeline[:3]}")          # ['load', 'validate', 'preprocess']
print(f"From index 3     : {pipeline[3:]}")          # ['train', 'evaluate', 'save']
print(f"Middle [1:4]     : {pipeline[1:4]}")         # ['validate', 'preprocess', 'train']
print(f"Every 2nd        : {pipeline[::2]}")         # ['load', 'preprocess', 'evaluate']
print(f"Reversed         : {pipeline[::-1]}")        # ['save', 'evaluate', ...]

# Slicing never crashes on out-of-range indices — it clips
print(f"Out of range     : {pipeline[2:100]}")       # ['preprocess', 'train', 'evaluate', 'save']
print(f"Empty slice      : {pipeline[10:20]}")       # []

# ── Useful checks ─────────────────────────────────────────────────────────────

print()
print("=== Checks ===")
print(f"Length           : {len(pipeline)}")         # 6
print(f"'train' in list  : {'train' in pipeline}")   # True
print(f"'deploy' in list : {'deploy' in pipeline}")  # False
print(f"Index of 'train' : {pipeline.index('train')}")  # 3

# ── Modifying ────────────────────────────────────────────────────────────────

print()
print("=== Modifying ===")

pipeline.append("log")            # add to end
print(f"After append     : {pipeline}")

pipeline.insert(1, "checksum")    # insert at index 1 — shifts everything right
print(f"After insert     : {pipeline}")

removed = pipeline.pop(1)         # remove and return item at index 1
print(f"Popped           : {removed}")
print(f"After pop(1)     : {pipeline}")

pipeline.remove("log")            # remove first occurrence of "log"
print(f"After remove     : {pipeline}")

# pop() with no argument removes the LAST item
last = pipeline.pop()
print(f"Popped last      : {last}")
print(f"Final pipeline   : {pipeline}")

# ── What to notice ────────────────────────────────────────────────────────────
#
# 1. pipeline[-1] is ALWAYS the last item, regardless of list length.
#    Much cleaner than pipeline[len(pipeline) - 1].
#
# 2. Slicing returns a NEW list — the original is not modified.
#    pipeline[:3] gives you a copy of the first 3 items.
#
# 3. Slices never raise IndexError. pipeline[2:100] just gives you
#    everything from index 2 to the end. Useful for safe "take up to N" patterns.
#
# 4. append() is O(1) — fast. insert(0, x) is O(n) — slow for large lists
#    because every element after the insertion point must shift right.
#    For queues (add to one end, remove from the other), use collections.deque.
#
# 5. pipeline[::-1] is the idiomatic Python way to reverse a list.
#    reversed(pipeline) also works but returns an iterator, not a list.