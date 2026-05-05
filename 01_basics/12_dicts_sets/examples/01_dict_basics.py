"""
examples/01_dict_basics.py
───────────────────────────
Topic  : Dictionaries and Sets
Example: 1 of 3 — Easy
Concept: Dict creation, indexing, safe access, .items() iteration, add/update/delete

Context
-------
Every model training run is controlled by a config dict. You need to read
values safely (some keys are optional), update settings mid-run, and iterate
over the full config to log it. This is the most common dict pattern in AI work.

Covers:
  - Dict literals: {key: value}
  - Access: d[key] — raises KeyError if missing
  - Safe access: d.get(key, default) — returns default if missing
  - Membership: key in d
  - Add / update: d[key] = value
  - Delete: del d[key], d.pop(key, default)
  - Iteration: for key in d, for key, value in d.items()
  - len(), d.keys(), d.values()

Run this file. Predict each output before you see it.
"""

# ── Creating a dict ───────────────────────────────────────────────────────────

config = {
    "model":          "EfficientNet-B4",
    "epochs":         50,
    "learning_rate":  0.001,
    "optimizer":      "Adam",
    "batch_size":     32,
}

# ── Accessing values ──────────────────────────────────────────────────────────

print("=== Access ===")
print(f"Model     : {config['model']}")       # EfficientNet-B4
print(f"Epochs    : {config['epochs']}")      # 50
print(f"Last key  : batch_size in config? {'batch_size' in config}")  # True

# d[key] raises KeyError if the key is absent — uncomment to see it crash
# print(config["dropout"])   # KeyError: 'dropout'

# ── Safe access with .get() ───────────────────────────────────────────────────

print()
print("=== Safe access (.get) ===")

# Returns None when key is absent
dropout = config.get("dropout")
print(f"dropout (absent) : {dropout}")         # None

# Returns the supplied default instead of None
dropout = config.get("dropout", 0.5)
print(f"dropout (default): {dropout}")         # 0.5

# Returns the real value when the key exists
lr = config.get("learning_rate", 0.01)
print(f"lr (present)     : {lr}")              # 0.001 — not the default

# ── Adding and updating ───────────────────────────────────────────────────────

print()
print("=== Add / update ===")

config["dropout"] = 0.3          # add a new key
config["epochs"]  = 100          # overwrite existing key

print(f"dropout added    : {config['dropout']}")   # 0.3
print(f"epochs updated   : {config['epochs']}")    # 100

# ── Deleting ─────────────────────────────────────────────────────────────────

print()
print("=== Delete ===")

# pop() removes the key and returns its value — safe with a default
removed_opt = config.pop("optimizer", None)
print(f"Removed optimizer: {removed_opt}")     # Adam
print(f"'optimizer' still in config? {'optimizer' in config}")  # False

# del raises KeyError if the key doesn't exist
del config["dropout"]
# del config["dropout"]   # uncomment — KeyError the second time

# ── Iterating ─────────────────────────────────────────────────────────────────

print()
print("=== Iteration ===")

# Keys only (default iteration)
print("Keys:", list(config.keys()))

# Values only
print("Values:", list(config.values()))

# Key-value pairs — .items() is the standard way to loop
print("\nFull config:")
for key, value in config.items():
    print(f"  {key:<16} : {value}")

# ── Practical pattern — build config from parallel sources ────────────────────

print()
print("=== Build from args ===")

defaults = {"lr": 0.001, "epochs": 10, "batch_size": 32, "dropout": 0.0}
overrides = {"epochs": 50, "dropout": 0.3}

# Merge: start with defaults, then overwrite with overrides
run_config = {}
for k, v in defaults.items():
    run_config[k] = v
for k, v in overrides.items():
    run_config[k] = v

print("Resolved run config:")
for k, v in run_config.items():
    source = "override" if k in overrides else "default"
    print(f"  {k:<12} = {v}  [{source}]")

# ── What to notice ────────────────────────────────────────────────────────────
#
# 1. d[key] is fast (O(1)) but crashes on missing keys.
#    d.get(key, default) is the safe alternative — use it when a key is optional.
#
# 2. Assigning to an existing key overwrites — there's no warning or error.
#    config["epochs"] = 100 silently replaces 50. Always check in d first
#    if you want to avoid accidental overwrites.
#
# 3. for key, value in d.items() is the idiomatic way to iterate over both.
#    for key in d alone gives only keys — you then access d[key] inside the loop.
#
# 4. Dicts preserve insertion order since Python 3.7.
#    The for loop above always visits keys in the order they were added.
#
# 5. pop(key, default) is the safe delete — equivalent to .get() for removal.
#    del d[key] will raise KeyError if the key doesn't exist.