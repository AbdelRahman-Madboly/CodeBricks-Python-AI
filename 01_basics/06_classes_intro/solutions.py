"""
Classes and Objects — Solutions
"""


# ---------------------------------------------------------------------------
# Solution 1
# ---------------------------------------------------------------------------

class Sensor:
    """Represents a hardware sensor with a type and measurement unit."""

    def __init__(self, sensor_id: str, sensor_type: str, unit: str) -> None:
        self.sensor_id = sensor_id
        self.sensor_type = sensor_type
        self.unit = unit

    def describe(self) -> str:
        """Return a one-line description of the sensor."""
        return f"Sensor[{self.sensor_id}] type={self.sensor_type} unit={self.unit}"

    def __str__(self) -> str:
        return self.describe()


s = Sensor("temp-01", "temperature", "celsius")
print(s.describe())
print(s)


# ---------------------------------------------------------------------------
# Solution 2
# ---------------------------------------------------------------------------

class BoundingBox:
    """A rectangular region in an image with a detection label and confidence."""

    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        label: str,
        confidence: float,
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
        self.confidence = confidence

    def area(self) -> int:
        """Return the area of the bounding box in pixels."""
        return self.width * self.height

    def is_valid(self) -> bool:
        """Return True if dimensions are positive and confidence is in [0, 1]."""
        return self.width > 0 and self.height > 0 and 0.0 <= self.confidence <= 1.0

    def scale(self, factor: float) -> None:
        """Scale the box coordinates and dimensions by a given factor."""
        self.x = int(self.x * factor)
        self.y = int(self.y * factor)
        self.width = int(self.width * factor)
        self.height = int(self.height * factor)

    def __str__(self) -> str:
        return (
            f"BoundingBox(label='{self.label}', x={self.x}, y={self.y}, "
            f"{self.width}x{self.height}, conf={self.confidence})"
        )


box = BoundingBox(x=10, y=20, width=100, height=80, label="face", confidence=0.92)
print(f"Area: {box.area()}")
print(f"Valid: {box.is_valid()}")
box.scale(2.0)
print(box)


# ---------------------------------------------------------------------------
# Solution 3
# ---------------------------------------------------------------------------

class ImageRecord:
    """Metadata for a single image file."""

    def __init__(self, filename: str, width: int, height: int) -> None:
        self.filename = filename
        self.width = width
        self.height = height

    def aspect_ratio(self) -> float:
        """Return the width-to-height ratio."""
        return self.width / self.height

    def __str__(self) -> str:
        return f"ImageRecord('{self.filename}', {self.width}x{self.height})"


class DetectionResult:
    """Holds all detections for a single image."""

    def __init__(self, image: ImageRecord, detections: list[dict]) -> None:
        self.image = image
        self.detections = detections

    def best_detection(self) -> dict | None:
        """Return the detection with the highest confidence, or None if empty."""
        if not self.detections:
            return None
        return max(self.detections, key=lambda d: d["confidence"])

    def summary(self) -> str:
        """Return a formatted multi-line detection report."""
        best = self.best_detection()
        best_str = f"{best['label']} @ {best['confidence']}" if best else "none"
        return (
            f"=== Detection Report ===\n"
            f"Image : {self.image.filename} "
            f"({self.image.width}x{self.image.height}, "
            f"ratio={self.image.aspect_ratio():.2f})\n"
            f"Count : {len(self.detections)} detections\n"
            f"Best  : {best_str}"
        )

    def __str__(self) -> str:
        return self.summary()


img = ImageRecord("scene_042.jpg", 1920, 1080)
result = DetectionResult(
    image=img,
    detections=[
        {"label": "face", "confidence": 0.97},
        {"label": "hand", "confidence": 0.83},
        {"label": "background", "confidence": 0.61},
    ],
)
print(img)
print(f"Best: {result.best_detection()}")
print(result)
