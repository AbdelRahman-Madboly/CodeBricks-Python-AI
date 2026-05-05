"""
exercises/03_safe_experiment_manager.py
─────────────────────────────────────────
Topic    : Memory and Mutability
Exercise : 3 of 3 — Hard
Concept  : copy discipline in class design, deepcopy, safe return values

Context
-------
An experiment manager creates and stores multiple training configs.
It must guarantee that:
  1. Modifying a returned config never affects the stored original
  2. Branching from a config produces truly independent copies
  3. The internal store cannot be corrupted by external mutation

This is a design exercise — there are right and wrong ways to implement
each method. The test calls at the bottom show exactly what must hold.

─────────────────────────────────────────────────────────────────
Task — Complete the ExperimentManager class
─────────────────────────────────────────────────────────────────

Methods to implement:

  register(name, config)
    Store a deepcopy of config so external mutations can't corrupt the store.

  get(name) -> dict | None
    Return a deepcopy of the stored config so callers can't mutate the store.
    Return None if name is not found.

  branch(name, overrides) -> dict | None
    Return a new config that is a deepcopy of the stored config for 'name',
    with overrides applied on top. Return None if name is not found.
    Must NOT modify the stored config.

  list_names() -> list[str]
    Return a list of all registered experiment names.

─────────────────────────────────────────────────────────────────
Expected output:
  --- register and get ---
  stored lr      : 0.001
  caller changed : 0.99
  stored still   : 0.001

  --- branch ---
  base tags   : ['v1']
  branch tags : ['v1', 'exp-A']
  base lr     : 0.001
  branch lr   : 0.01

  --- list_names ---
  ['resnet-base', 'vit-base']
─────────────────────────────────────────────────────────────────

Attempt before opening solutions.
"""

import copy


class ExperimentManager:
    def __init__(self):
        self._store: dict[str, dict] = {}

    def register(self, name: str, config: dict) -> None:
        # TODO: store a copy so external mutation can't reach the store
        pass

    def get(self, name: str) -> dict | None:
        # TODO: return a copy so callers can't mutate the store
        pass

    def branch(self, name: str, overrides: dict) -> dict | None:
        # TODO: deepcopy stored config, apply overrides, return new config
        pass

    def list_names(self) -> list[str]:
        # TODO: return list of all registered names
        pass


# ── Test calls ────────────────────────────────────────────────────────────────

manager = ExperimentManager()

resnet_cfg = {"lr": 0.001, "epochs": 30, "tags": ["v1"]}
manager.register("resnet-base", resnet_cfg)
manager.register("vit-base", {"lr": 0.0001, "epochs": 50, "tags": ["v1"]})

print("--- register and get ---")
retrieved = manager.get("resnet-base")
retrieved["lr"] = 0.99                    # caller mutates the returned copy
print(f"stored lr      : {manager.get('resnet-base')['lr']}")   # must still be 0.001
print(f"caller changed : {retrieved['lr']}")
print(f"stored still   : {manager.get('resnet-base')['lr']}")

print()
print("--- branch ---")
branched = manager.branch("resnet-base", {"lr": 0.01, "tags": ["v1", "exp-A"]})
print(f"base tags   : {manager.get('resnet-base')['tags']}")    # must be ['v1']
print(f"branch tags : {branched['tags']}")
print(f"base lr     : {manager.get('resnet-base')['lr']}")      # must be 0.001
print(f"branch lr   : {branched['lr']}")

print()
print("--- list_names ---")
print(manager.list_names())    # ['resnet-base', 'vit-base']