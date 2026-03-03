"""
Classes and Objects — Examples

Covers class definition, __init__, instance attributes, methods,
__str__, __repr__, and building a small but realistic class from scratch.
"""


# ---------------------------------------------------------------------------
# Example 1 — Basic class with constructor and methods
# Scenario: representing a video frame in a processing pipeline
# ---------------------------------------------------------------------------

class VideoFrame:
    """A single frame extracted from a video file."""

    def __init__(self, frame_id: int, width: int, height: int, is_keyframe: bool = False) -> None:
        self.frame_id = frame_id
        self.width = width
        self.height = height
        self.is_keyframe = is_keyframe
        self.labels: list[str] = []   # starts empty — populated later

    def resolution(self) -> str:
        """Return the resolution as a WxH string."""
        return f"{self.width}x{self.height}"

    def add_label(self, label: str) -> None:
        """Attach a classification label to this frame."""
        if label not in self.labels:
            self.labels.append(label)

    def pixel_count(self) -> int:
        """Total number of pixels in this frame."""
        return self.width * self.height

    def __str__(self) -> str:
        """Human-readable summary — used by print()."""
        key = " [keyframe]" if self.is_keyframe else ""
        return f"Frame {self.frame_id:04d} | {self.resolution()}{key} | labels: {self.labels}"

    def __repr__(self) -> str:
        """Developer representation — shown in REPL and debuggers."""
        return (
            f"VideoFrame(frame_id={self.frame_id}, width={self.width}, "
            f"height={self.height}, is_keyframe={self.is_keyframe})"
        )


frame = VideoFrame(frame_id=42, width=1920, height=1080, is_keyframe=True)
frame.add_label("real")
frame.add_label("high-quality")

print(frame)            # uses __str__
print(repr(frame))      # uses __repr__
print(frame.pixel_count())
print(frame.resolution())


# ---------------------------------------------------------------------------
# Example 2 — Multiple instances share the class, not the data
# Scenario: two frames from different videos — each has independent state
# ---------------------------------------------------------------------------

frame_a = VideoFrame(1, 1280, 720)
frame_b = VideoFrame(2, 640, 480)

frame_a.add_label("fake")
frame_b.add_label("real")

# Each object's labels list is completely independent
print(frame_a.labels)   # ['fake']
print(frame_b.labels)   # ['real']


# ---------------------------------------------------------------------------
# Example 3 — A class that does real work
# Scenario: a simple confidence tracker that accumulates predictions
# ---------------------------------------------------------------------------

class ConfidenceTracker:
    """Accumulates model prediction scores and reports statistics."""

    def __init__(self, model_name: str) -> None:
        self.model_name = model_name
        self.scores: list[float] = []

    def record(self, score: float) -> None:
        """Add a new confidence score to the tracker."""
        if not (0.0 <= score <= 1.0):
            raise ValueError(f"Score must be in [0, 1], got {score}")
        self.scores.append(score)

    def average(self) -> float:
        """Return the mean confidence score, or 0.0 if no scores recorded."""
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)

    def above_threshold(self, threshold: float = 0.80) -> int:
        """Count how many scores exceed the given threshold."""
        return sum(1 for s in self.scores if s > threshold)

    def __str__(self) -> str:
        return (
            f"[{self.model_name}] "
            f"samples={len(self.scores)} | "
            f"avg={self.average():.3f} | "
            f"above_0.8={self.above_threshold()}"
        )


tracker = ConfidenceTracker("EfficientNet-B4")
for score in [0.92, 0.75, 0.88, 0.61, 0.95]:
    tracker.record(score)

print(tracker)
