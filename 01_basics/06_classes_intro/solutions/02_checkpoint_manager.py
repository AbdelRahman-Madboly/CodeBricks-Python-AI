"""
02_checkpoint_manager.py — Solution
──────────────────────────────
Topic  : Classes and Objects
Solution: 2 of 3 — Medium
"""


class CheckpointManager:
    def __init__(self, run_name: str):
        self.run_name    = run_name
        self.checkpoints: list[dict] = []

    def save(self, epoch: int, loss: float, path: str) -> None:
        checkpoint = {"epoch": epoch, "loss": loss, "path": path}
        self.checkpoints.append(checkpoint)

    def best(self):
        if not self.checkpoints:
            return None
        # min() with a key function finds the checkpoint with the lowest loss.
        return min(self.checkpoints, key=lambda c: c["loss"])

    def latest(self):
        if not self.checkpoints:
            return None
        # The last element in the list is the most recently saved.
        return self.checkpoints[-1]

    def __str__(self) -> str:
        n = len(self.checkpoints)
        if n == 0:
            best_str = "none"
        else:
            best_str = f"{self.best()['loss']:.4f}"
        return f"{self.run_name} | {n} checkpoints | best_loss={best_str}"


mgr = CheckpointManager("resnet50-run1")
print(mgr)

for epoch, loss, path in [(1, 0.92, "ckpt_01.pt"), (2, 0.78, "ckpt_02.pt"), (3, 0.81, "ckpt_03.pt")]:
    mgr.save(epoch, loss, path)
    print(f"Saved: {mgr.latest()}")

print(mgr)
print(f"Best checkpoint: {mgr.best()}")
print(f"Latest checkpoint: {mgr.latest()}")


# ── Why this works ─────────────────────────────────────────────────────────────
# self.checkpoints = [] creates a fresh list for every instance.
# save() builds a dict and appends it — the object grows over time.
# best() uses min() with a lambda key — you'll learn lambdas in topic 16.
# latest() uses [-1] indexing — the last item is always the most recent append.
# __str__ guards against the empty case to avoid calling min() on an empty list.
