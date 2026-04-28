"""
solutions/01_agent_status.py
─────────────────────────────
Topic    : Printing
Solution : Exercise 1 — Agent status line

Open this only after a genuine attempt at the exercise.
"""

agent_name    = "ResearchBot"
agent_version = 2
status        = "idle"
device        = "cpu"
docs_loaded   = 1250

# ── Solution ─────────────────────────────────────────────────────────────────

print(f"[AGENT] {agent_name} v{agent_version} | status: {status} | device: {device} | docs loaded: {docs_loaded:,}")

# ── Why this works ───────────────────────────────────────────────────────────
#
# {docs_loaded:,}
#   The comma inside the format spec tells Python to insert commas as
#   thousands separators. 1250 becomes 1,250. 1000000 becomes 1,000,000.
#   This is standard for any number a human has to read quickly.
#
# Everything else is a plain f-string variable insertion — {variable_name}.
# The surrounding text (brackets, pipes, colons) is just literal characters.
#
# One line is correct here.
#   This status message is designed to be scanned quickly in logs.
#   Splitting it across multiple print() calls would make it harder
#   to grep for in a log file.