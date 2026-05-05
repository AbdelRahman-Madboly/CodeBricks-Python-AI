"""
test.py — 06 Classes and Objects
Run: python test.py
stdlib only.
"""


def check(label: str, actual, expected) -> bool:
    if actual == expected:
        print(f"  PASS  {label}")
        return True
    else:
        print(f"  FAIL  {label}")
        print(f"        expected: {expected!r}")
        print(f"        actual  : {actual!r}")
        return False


# ── Classes under test ────────────────────────────────────────────────────────

class ModelConfig:
    def __init__(self, name, lr, epochs, batch_size=32):
        self.name       = name
        self.lr         = lr
        self.epochs     = epochs
        self.batch_size = batch_size

    def __str__(self):
        return f"{self.name} | lr={self.lr} | epochs={self.epochs} | batch={self.batch_size}"

    def __repr__(self):
        return f"ModelConfig(name={self.name!r}, lr={self.lr}, epochs={self.epochs}, batch_size={self.batch_size})"

    def total_steps(self, dataset_size):
        return (dataset_size // self.batch_size) * self.epochs


class TrainingRun:
    def __init__(self, model_name, patience=5):
        self.model_name  = model_name
        self.patience    = patience
        self.epoch       = 0
        self.losses      = []
        self.best_loss   = float("inf")
        self._no_improve = 0

    def step(self, loss):
        self.epoch += 1
        self.losses.append(loss)
        if loss < self.best_loss:
            self.best_loss   = loss
            self._no_improve = 0
        else:
            self._no_improve += 1

    def should_stop(self):
        return self._no_improve >= self.patience


class CheckpointManager:
    def __init__(self, run_name):
        self.run_name    = run_name
        self.checkpoints = []

    def save(self, epoch, loss, path):
        self.checkpoints.append({"epoch": epoch, "loss": loss, "path": path})

    def best(self):
        if not self.checkpoints:
            return None
        return min(self.checkpoints, key=lambda c: c["loss"])

    def latest(self):
        if not self.checkpoints:
            return None
        return self.checkpoints[-1]

    def __str__(self):
        n = len(self.checkpoints)
        best_str = "none" if n == 0 else f"{self.best()['loss']:.4f}"
        return f"{self.run_name} | {n} checkpoints | best_loss={best_str}"


# ── Tests ─────────────────────────────────────────────────────────────────────

passed = 0
failed = 0

def run(label, actual, expected):
    global passed, failed
    if check(label, actual, expected):
        passed += 1
    else:
        failed += 1


print("\n── ModelConfig ──────────────────────────────────────────────────────────")

cfg = ModelConfig("resnet50", 0.001, 30, 64)
run("name",       cfg.name,       "resnet50")
run("lr",         cfg.lr,         0.001)
run("epochs",     cfg.epochs,     30)
run("batch_size", cfg.batch_size, 64)
run("str",        str(cfg),       "resnet50 | lr=0.001 | epochs=30 | batch=64")
run("repr",       repr(cfg),      "ModelConfig(name='resnet50', lr=0.001, epochs=30, batch_size=64)")
run("total_steps 50000", cfg.total_steps(50000), (50000 // 64) * 30)

cfg2 = ModelConfig("vit", 0.0001, 10)
run("default batch_size", cfg2.batch_size, 32)
run("total_steps default batch", cfg2.total_steps(32000), (32000 // 32) * 10)

# Instances are independent
cfg.epochs = 60
run("mutated epochs",   cfg.epochs,  60)
run("other unchanged",  cfg2.epochs, 10)


print("\n── TrainingRun ──────────────────────────────────────────────────────────")

run2 = TrainingRun("yolo", patience=3)
run("initial epoch",      run2.epoch,      0)
run("initial best_loss",  run2.best_loss,  float("inf"))
run("should_stop empty",  run2.should_stop(), False)

run2.step(1.0)
run("epoch after step 1", run2.epoch,     1)
run("best after step 1",  run2.best_loss, 1.0)
run("no_improve after 1", run2._no_improve, 0)

run2.step(0.8)
run("best after step 2",  run2.best_loss, 0.8)
run("no_improve after 2", run2._no_improve, 0)

run2.step(0.9)
run2.step(0.95)
run("no_improve after plateau 2", run2._no_improve, 2)
run("should_stop false",  run2.should_stop(), False)

run2.step(1.0)
run("no_improve 3",       run2._no_improve, 3)
run("should_stop true",   run2.should_stop(), True)

run2.step(0.1)  # new best resets counter
run("reset after new best", run2._no_improve, 0)
run("should_stop after reset", run2.should_stop(), False)


print("\n── CheckpointManager ────────────────────────────────────────────────────")

mgr = CheckpointManager("run-1")
run("str empty",   str(mgr), "run-1 | 0 checkpoints | best_loss=none")
run("best empty",  mgr.best(),   None)
run("latest empty", mgr.latest(), None)

mgr.save(1, 0.92, "ckpt_01.pt")
mgr.save(2, 0.78, "ckpt_02.pt")
mgr.save(3, 0.81, "ckpt_03.pt")

run("checkpoint count", len(mgr.checkpoints), 3)
run("best epoch",       mgr.best()["epoch"],  2)
run("best loss",        mgr.best()["loss"],   0.78)
run("latest epoch",     mgr.latest()["epoch"], 3)
run("str 3 ckpts",      str(mgr), "run-1 | 3 checkpoints | best_loss=0.7800")


print("\n── Class variable isolation ─────────────────────────────────────────────")

# Two CheckpointManagers must not share their checkpoints list
mgr_a = CheckpointManager("A")
mgr_b = CheckpointManager("B")
mgr_a.save(1, 0.5, "a.pt")
run("isolation: A has 1", len(mgr_a.checkpoints), 1)
run("isolation: B has 0", len(mgr_b.checkpoints), 0)

# Two TrainingRuns must not share their losses list
r1 = TrainingRun("r1")
r2 = TrainingRun("r2")
r1.step(1.0)
run("isolation: r1 losses", r1.losses, [1.0])
run("isolation: r2 losses", r2.losses, [])


# ── Summary ───────────────────────────────────────────────────────────────────
total = passed + failed
print(f"\n{'─' * 60}")
print(f"  {passed}/{total} passed  |  {failed} failed")
print(f"{'─' * 60}")
if failed == 0:
    print("  All tests pass. Mark topic 06 done in PROGRESS.md.")
    print("  Next: 07 — Memory and Mutability")
else:
    print("  Fix the failures above before moving on.")
