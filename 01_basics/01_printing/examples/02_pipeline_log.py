"""
examples/02_pipeline_log.py
───────────────────────────
Topic  : Printing
Example: 2 of 3 — Pipeline step logging

Context
-------
An AI pipeline is a sequence of steps: load data → clean it →
tokenize → embed → run through model → save results.

When you run a pipeline, you need to see what step is running
and whether each one succeeded or failed. This example shows
how to format that output cleanly using sep= and end=.

This example covers:
  - end=""  to stay on the same line
  - sep=    to join values with a custom separator
  - \n      inside strings to add newlines manually
  - Simple status logging pattern

Run this file and predict the output before you see it.
"""

# ── Pipeline definition ──────────────────────────────────────────────────────

pipeline_steps = [
    "load_data",
    "clean_text",
    "tokenize",
    "embed",
    "classify",
    "save_results",
]

step_status = {
    "load_data":    "ok",
    "clean_text":   "ok",
    "tokenize":     "ok",
    "embed":        "ok",
    "classify":     "ok",
    "save_results": "ok",
}

# ── Part 1: Show the pipeline as one line ────────────────────────────────────

print("Pipeline:")
print(*pipeline_steps, sep=" → ")
# Output: load_data → clean_text → tokenize → embed → classify → save_results

# *pipeline_steps unpacks the list — passes each item as a separate argument
# sep=" → " puts that string between each pair of items instead of a space

print()

# ── Part 2: Show each step running with a status ─────────────────────────────

print("Running pipeline...\n")

for step in pipeline_steps:
    # end="" keeps the cursor on the same line — no newline yet
    print(f"  [{step}]", end="")

    # ... simulating work happening ...
    # In a real pipeline, you'd actually run the step here.
    # For now we just look up the pre-set status.

    status = step_status[step]
    if status == "ok":
        print("  ✓")    # now we print the checkmark and move to next line
    else:
        print(f"  ✗  ERROR: {status}")

print()
print("All steps complete.")

# ── What to notice ───────────────────────────────────────────────────────────
#
# 1. end=""
#    Suppresses the newline that print() normally adds.
#    This lets you print the step name first, then add the status
#    on the same line after "work" finishes.
#    Pattern: print(step, end="") → do work → print(result)
#
# 2. *pipeline_steps
#    The * unpacks the list into individual arguments.
#    print(*["a", "b", "c"], sep=" → ")
#    is the same as:
#    print("a", "b", "c", sep=" → ")
#    You'll learn this properly in Functions (topic 05).
#
# 3. \n inside a string
#    \n is the newline character — it moves to the next line.
#    "Running pipeline...\n" prints the text then adds an extra blank line.
#    Same as calling print() twice.
#
# 4. Why end="" for pipeline logging?
#    In real AI pipelines you often want: "Embedding documents...  done (2.3s)"
#    all on one line. You print the "doing..." part, run the work,
#    measure the time, then print the result on the same line.