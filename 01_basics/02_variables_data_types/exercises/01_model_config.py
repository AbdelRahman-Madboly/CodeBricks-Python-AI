"""
exercises/01_model_config.py
─────────────────────────────
Topic    : Variables and Data Types
Exercise : 1 of 3 — Easy
Concept  : Declaring variables, types, type inspection, f-strings

Context
-------
Every AI project starts with a configuration block — the settings
that control how a model trains. Getting the types right here
prevents crashes later when libraries expect specific types.

─────────────────────────────────────────────────────────────────
Task
─────────────────────────────────────────────────────────────────
Declare all five config variables with the correct types and values,
then print a config summary that looks EXACTLY like this:

  ╔══════════════════════════════════════╗
  ║         Model Configuration          ║
  ╠══════════════════════════════════════╣
  ║  model      : bert-base-uncased      ║
  ║  epochs     : 20                     ║
  ║  lr         : 0.0002                 ║
  ║  pretrained : True                   ║
  ║  checkpoint : None                   ║
  ╠══════════════════════════════════════╣
  ║  Types                               ║
  ║  model      : str                    ║
  ║  epochs     : int                    ║
  ║  lr         : float                  ║
  ║  pretrained : bool                   ║
  ║  checkpoint : NoneType               ║
  ╚══════════════════════════════════════╝

Rules:
  - model      → string: "bert-base-uncased"
  - epochs     → integer: 20
  - lr         → float: 0.0002
  - pretrained → boolean: True
  - checkpoint → no value yet (NoneType)
  - Use type().__name__ for the type names — not hardcoded strings
  - Match spacing exactly — left-align inside the box
─────────────────────────────────────────────────────────────────
"""

# ── Declare your variables here ──────────────────────────────────────────────


# ── Print the config summary here ────────────────────────────────────────────