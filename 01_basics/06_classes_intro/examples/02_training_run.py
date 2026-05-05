"""
02_training_run.py
──────────────────────────────
Topic  : Classes and Objects
Example: 2 of 3 — Medium
Concept: Stateful objects — methods that mutate instance variables over time

Context
-------
A training loop needs to track its own state: current epoch, running loss history,
best loss seen so far, whether to stop early. Storing this in loose variables leads
to tangled code. A TrainingRun class owns its state and exposes a clean interface:
call .step(loss) each epoch, call .should_stop() to check the stopping condition,
call .summary() to get a log-ready string.

Covers:
  - methods that mutate (change) instance variables
  - methods that compute and return values
  - conditional logic inside methods
  - float("inf") as a sentinel for "no best yet"

Run this file. Predict each output before you see it.
"""


class TrainingRun:
    def __init__(self, model_name: str, patience: int = 5):
        self.model_name = model_name
        self.patience   = patience      # stop if no improvement for this many epochs

        # State that evolves as training progresses
        self.epoch      = 0
        self.losses     = []
        self.best_loss  = float("inf")  # infinity means "nothing is better yet"
        self._no_improve = 0            # epochs since last improvement

    def step(self, loss: float) -> None:
        # Called once per epoch. Updates all state.
        self.epoch += 1
        self.losses.append(loss)

        if loss < self.best_loss:
            # New best — reset the patience counter
            self.best_loss  = loss
            self._no_improve = 0
        else:
            self._no_improve += 1

    def should_stop(self) -> bool:
        # Returns True if we've gone patience epochs without improvement.
        # The training loop calls this to decide whether to break.
        return self._no_improve >= self.patience

    def summary(self) -> str:
        if not self.losses:
            return f"{self.model_name}: no epochs run yet"

        avg = sum(self.losses) / len(self.losses)
        return (
            f"{self.model_name} | epoch {self.epoch} | "
            f"best={self.best_loss:.4f} | avg={avg:.4f} | "
            f"no_improve={self._no_improve}"
        )

    def __str__(self) -> str:
        return self.summary()


# ── Simulating a training loop ────────────────────────────────────────────────

run = TrainingRun("resnet50", patience=3)

# Simulated per-epoch losses — drops then plateaus
epoch_losses = [1.42, 1.21, 0.98, 0.87, 0.86, 0.87, 0.88, 0.89]

for loss in epoch_losses:
    run.step(loss)
    print(f"  Epoch {run.epoch:2d} | loss={loss:.2f} | {run.summary()}")
    if run.should_stop():
        print("  Early stopping triggered.")
        break

print()
print(f"Final state: {run}")


# ── What to notice ────────────────────────────────────────────────────────────
# 1. The object remembers everything between method calls. self.epoch, self.losses,
#    self.best_loss all persist — that's the point of instance variables.
# 2. step() mutates state. should_stop() and summary() only read state.
#    Separating mutation from reads makes the class easier to reason about.
# 3. _no_improve uses a leading underscore — convention for "internal use only".
#    You'll learn proper encapsulation with @property in topic 02_oop/02_properties_static.
# 4. float("inf") is a useful sentinel: any real loss will be smaller,
#    so the first epoch always sets a new best.
# 5. The training loop itself has no loss-tracking logic — that lives in the object.
#    The loop just drives the object forward: step, check, break.
