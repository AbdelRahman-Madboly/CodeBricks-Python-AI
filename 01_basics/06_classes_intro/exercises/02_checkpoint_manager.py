"""
02_checkpoint_manager.py
──────────────────────────────
Topic  : Classes and Objects
Exercise: 2 of 3 — Medium
Concept: Stateful object — methods that mutate and compute, __str__

Task
----
Build a CheckpointManager class. It tracks saved model checkpoints during training
and can tell you what to load if you need to resume.

A checkpoint is a dict: {"epoch": int, "loss": float, "path": str}

The class must support:
  - save(epoch, loss, path): add a checkpoint
  - best(): return the checkpoint dict with the lowest loss, or None
  - latest(): return the most recently saved checkpoint dict, or None
  - __str__: see expected output

Rules
-----
- Do not import anything
- best() and latest() must return the full dict, not just one field
- If no checkpoints have been saved, best() and latest() return None
- __str__ should show: name | N checkpoints | best_loss=X.XXXX (or "none" if empty)

Expected output (exact):
    resnet50-run1 | 0 checkpoints | best_loss=none
    Saved: {'epoch': 1, 'loss': 0.92, 'path': 'ckpt_01.pt'}
    Saved: {'epoch': 2, 'loss': 0.78, 'path': 'ckpt_02.pt'}
    Saved: {'epoch': 3, 'loss': 0.81, 'path': 'ckpt_03.pt'}
    resnet50-run1 | 3 checkpoints | best_loss=0.7800
    Best checkpoint: {'epoch': 2, 'loss': 0.78, 'path': 'ckpt_02.pt'}
    Latest checkpoint: {'epoch': 3, 'loss': 0.81, 'path': 'ckpt_03.pt'}

Attempt before opening solutions.
"""


class CheckpointManager:
    def __init__(self, run_name: str):
        pass

    def save(self, epoch: int, loss: float, path: str) -> None:
        pass

    def best(self):
        pass

    def latest(self):
        pass

    def __str__(self) -> str:
        pass


# ── Test it ───────────────────────────────────────────────────────────────────

mgr = CheckpointManager("resnet50-run1")
print(mgr)

for epoch, loss, path in [(1, 0.92, "ckpt_01.pt"), (2, 0.78, "ckpt_02.pt"), (3, 0.81, "ckpt_03.pt")]:
    mgr.save(epoch, loss, path)
    print(f"Saved: {mgr.latest()}")

print(mgr)
print(f"Best checkpoint: {mgr.best()}")
print(f"Latest checkpoint: {mgr.latest()}")
