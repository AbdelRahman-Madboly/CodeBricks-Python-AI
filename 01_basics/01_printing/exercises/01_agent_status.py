"""
exercises/01_agent_status.py
─────────────────────────────
Topic    : Printing
Exercise : 1 of 3 — Easy
Concept  : f-strings, basic formatting

Context
-------
You're building a simple AI agent. When it starts up, it prints
a one-line status message so you know what it's doing and where
it's running.

This is the first thing any real agent, bot, or automation tool
outputs. Get the format right.

─────────────────────────────────────────────────────────────────
Task
─────────────────────────────────────────────────────────────────
Using the variables below, print a status line that looks
EXACTLY like this:

  [AGENT] ResearchBot v2 | status: idle | device: cpu | docs loaded: 1,250

Rules:
  - Use the variables — don't hardcode the values
  - The doc count must use comma formatting (1,250 not 1250)
  - Everything on one line
  - Match spacing and punctuation exactly
─────────────────────────────────────────────────────────────────
"""

agent_name   = "ResearchBot"
agent_version = 2
status       = "idle"
device       = "cpu"
docs_loaded  = 1250

# ── Your solution below ──────────────────────────────────────────────────────