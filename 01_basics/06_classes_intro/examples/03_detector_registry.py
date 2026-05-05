"""
03_detector_registry.py
──────────────────────────────
Topic  : Classes and Objects
Example: 3 of 3 — Advanced
Concept: Multiple interacting objects, class variable misuse, objects stored in collections

Context
-------
A detection system runs multiple models in parallel: YOLOv8, EfficientDet, a custom
lightweight model. Each model produces DetectionResult objects. A DetectorRegistry
holds all registered models and can query them in sequence. This example shows how
objects interact — one class creating and consuming instances of another.

Covers:
  - objects that hold references to other objects
  - class variable bug (shared mutable default) and the fix
  - a list of objects iterated with methods called on each
  - __str__ used across multiple classes

Run this file. Predict each output before you see it.
"""

# ── you'll learn this properly in topic 02_oop/02_properties_static ──────────
# @property is used in production code to protect attributes like score.
# For now, we set instance variables directly.


class DetectionResult:
    """One result from one model on one frame."""

    def __init__(self, label: str, score: float, model_name: str):
        self.label      = label
        self.score      = score
        self.model_name = model_name

    def __str__(self) -> str:
        return f"[{self.model_name}] {self.label} ({self.score:.2%})"

    def __repr__(self) -> str:
        return f"DetectionResult(label={self.label!r}, score={self.score}, model={self.model_name!r})"


class Detector:
    """A single detection model with a name and confidence threshold."""

    def __init__(self, name: str, threshold: float = 0.5):
        self.name      = name
        self.threshold = threshold
        # Instance variable — a fresh list for every Detector instance.
        # If this were a class variable (results = [] at class level),
        # all detectors would share one list — a common bug.
        self.results: list[DetectionResult] = []

    def detect(self, label: str, score: float) -> DetectionResult | None:
        # Only accept results above the threshold.
        if score < self.threshold:
            print(f"  {self.name}: '{label}' at {score:.2%} below threshold — skipped")
            return None
        result = DetectionResult(label, score, self.name)
        self.results.append(result)
        return result

    def best_result(self) -> DetectionResult | None:
        return max(self.results, key=lambda r: r.score) if self.results else None

    def __str__(self) -> str:
        return f"Detector({self.name}, threshold={self.threshold}, results={len(self.results)})"


class DetectorRegistry:
    """Holds multiple detectors and runs them against a frame."""

    def __init__(self):
        self.detectors: list[Detector] = []

    def register(self, detector: Detector) -> None:
        self.detectors.append(detector)

    def run_all(self, detections: list[tuple[str, float]]) -> list[DetectionResult]:
        # Distribute detections across detectors in round-robin order.
        # In a real system each detector would process the raw frame independently.
        all_results = []
        for i, (label, score) in enumerate(detections):
            detector = self.detectors[i % len(self.detectors)]
            result   = detector.detect(label, score)
            if result:
                all_results.append(result)
        return all_results

    def best_per_detector(self) -> list[DetectionResult]:
        return [d.best_result() for d in self.detectors if d.best_result()]


# ── Building the registry ─────────────────────────────────────────────────────

yolo    = Detector("YOLOv8",      threshold=0.6)
effdet  = Detector("EfficientDet", threshold=0.5)
lite    = Detector("LiteModel",   threshold=0.4)

registry = DetectorRegistry()
for d in [yolo, effdet, lite]:
    registry.register(d)

# Simulated frame detections: (label, confidence_score)
frame_detections = [
    ("person", 0.92),
    ("car",    0.45),   # below EfficientDet threshold
    ("bicycle", 0.78),
    ("person", 0.33),   # below LiteModel threshold
    ("truck",  0.65),
    ("dog",    0.51),
]

print("Running detections:")
all_results = registry.run_all(frame_detections)

print()
print("Accepted results:")
for result in all_results:
    print(f"  {result}")

print()
print("Best per detector:")
for result in registry.best_per_detector():
    print(f"  {result}")

print()
print("Detector states:")
for d in registry.detectors:
    print(f"  {d}")


# ── What to notice ────────────────────────────────────────────────────────────
# 1. self.results: list[DetectionResult] = [] — instance variable, not class variable.
#    Each Detector gets its own list. If results = [] were at class level,
#    all three detectors would share the same list and corrupt each other's data.
# 2. DetectorRegistry holds a list of Detector objects — objects stored inside objects.
#    This is composition, the alternative to inheritance. (topic 02_oop/07_solid)
# 3. max(self.results, key=lambda r: r.score) — a lambda used as a sort key.
#    You'll learn lambdas properly in topic 16 (Advanced Functions).
# 4. DetectionResult | None is a type hint for "returns this type or None".
#    You'll learn type hints properly in topic 05_typing_quality/01_type_hints.
# 5. Each class has one responsibility: Detector detects, Registry orchestrates,
#    DetectionResult holds one result. This is the Single Responsibility Principle.
#    (topic 02_oop/07_solid)
