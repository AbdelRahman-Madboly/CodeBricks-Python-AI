"""
solutions/03_safe_experiment_manager.py
─────────────────────────────────────────
Topic    : Memory and Mutability
Solution : Exercise 3 — Safe experiment manager
"""

import copy


class ExperimentManager:
    def __init__(self):
        self._store: dict[str, dict] = {}

    def register(self, name: str, config: dict) -> None:
        # deepcopy on the way IN — external mutations after register() can't
        # reach the stored config
        self._store[name] = copy.deepcopy(config)

    def get(self, name: str) -> dict | None:
        if name not in self._store:
            return None
        # deepcopy on the way OUT — callers can mutate their copy freely
        return copy.deepcopy(self._store[name])

    def branch(self, name: str, overrides: dict) -> dict | None:
        if name not in self._store:
            return None
        # deepcopy the stored config, then apply overrides on top
        branched = copy.deepcopy(self._store[name])
        branched.update(overrides)
        return branched

    def list_names(self) -> list[str]:
        return list(self._store.keys())


# ── Test calls ────────────────────────────────────────────────────────────────

manager = ExperimentManager()

resnet_cfg = {"lr": 0.001, "epochs": 30, "tags": ["v1"]}
manager.register("resnet-base", resnet_cfg)
manager.register("vit-base", {"lr": 0.0001, "epochs": 50, "tags": ["v1"]})

print("--- register and get ---")
retrieved = manager.get("resnet-base")
retrieved["lr"] = 0.99
print(f"stored lr      : {manager.get('resnet-base')['lr']}")
print(f"caller changed : {retrieved['lr']}")
print(f"stored still   : {manager.get('resnet-base')['lr']}")

print()
print("--- branch ---")
branched = manager.branch("resnet-base", {"lr": 0.01, "tags": ["v1", "exp-A"]})
print(f"base tags   : {manager.get('resnet-base')['tags']}")
print(f"branch tags : {branched['tags']}")
print(f"base lr     : {manager.get('resnet-base')['lr']}")
print(f"branch lr   : {branched['lr']}")

print()
print("--- list_names ---")
print(manager.list_names())

# ── Why this works ────────────────────────────────────────────────────────────
#
# register — deepcopy on the way IN
#   If you stored a reference: self._store[name] = config
#   then the caller still holds a label on the same object. Any mutation
#   after register() would corrupt the stored config.
#   Deepcopy severs that link immediately.
#
# get — deepcopy on the way OUT
#   If you returned a reference: return self._store[name]
#   the caller could mutate the stored config directly.
#   Returning a deepcopy means callers can freely modify what they get
#   without touching the internal state.
#
# branch — deepcopy then update
#   dict.update(overrides) applies overrides in place on the copy.
#   The stored config is never touched because we deepcopy before updating.
#   Overrides are a flat dict — update is safe here.
#
# This "deepcopy in, deepcopy out" pattern is the standard for any class
# that must guarantee immutability of its internal state.
# In production Python you'd use dataclasses or Pydantic models
# (which enforce this at the type level) — topic 05_typing_quality/02_pydantic.