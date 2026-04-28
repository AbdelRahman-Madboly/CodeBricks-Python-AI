"""
examples/01_banner.py
─────────────────────
Topic  : Printing
Example: 1 of 3 — CLI startup banner

Context
-------
Every real AI tool prints a startup banner when it launches.
This tells the user what they're running, what version it is,
and what it's about to do. It's the first thing your models,
agents, and pipelines will say.

This example covers:
  - f-strings with variables
  - String repetition with *
  - print() with no arguments (blank line)
  - Multi-line structured output

Run this file and predict the output before you see it.
"""

# ── Configuration ────────────────────────────────────────────────────────────

tool_name   = "CodeBricks AI Trainer"
version     = "0.1.0"
author      = "Abdelrahman"
description = "Fine-tuning pipeline for text classification"
device      = "cuda"   # where the model will run (GPU vs CPU)

# ── Output ───────────────────────────────────────────────────────────────────

print("=" * 50)
print(f"  {tool_name}  v{version}")
print(f"  {description}")
print("=" * 50)
print(f"  Author : {author}")
print(f"  Device : {device}")
print("=" * 50)
print()   # blank line — print() alone just adds breathing room

print("Initializing...")
print()

# ── What to notice ───────────────────────────────────────────────────────────
#
# 1. "=" * 50
#    Multiplying a string by a number repeats it.
#    Change 50 to 30 and rerun — the whole banner adjusts.
#    This is better than typing 50 equals signs by hand.
#
# 2. f"  {tool_name}  v{version}"
#    Variables drop directly into the string.
#    The spaces before them are just for visual indentation inside the banner.
#
# 3. print()
#    No arguments = no content = just a newline.
#    Use it whenever your output needs breathing room.
#
# 4. Why does this matter for AI work?
#    When you run a training script that takes 2 hours, the banner is the
#    first thing you see. It confirms you're running the right script with
#    the right settings before you walk away.