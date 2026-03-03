"""
Classes and Objects — Exercises
"""


# ---------------------------------------------------------------------------
# Exercise 1 (Easy) — Define a class from scratch
#
# Problem:
#   Define a class called Sensor that represents a hardware sensor.
#
#   Attributes (set in __init__):
#     - sensor_id: str
#     - sensor_type: str  (e.g. "temperature", "humidity")
#     - unit: str         (e.g. "celsius", "percent")
#
#   Methods:
#     - describe() → str: returns a one-line description
#
#   __str__ should return the same as describe().
#
#   Expected output:
#   Sensor[temp-01] type=temperature unit=celsius
#   Sensor[temp-01] type=temperature unit=celsius
#
# Your solution below:
# ---------------------------------------------------------------------------

# Uncomment to test:
# s = Sensor("temp-01", "temperature", "celsius")
# print(s.describe())
# print(s)


# ---------------------------------------------------------------------------
# Exercise 2 (Medium) — Class with validation and state
#
# Problem:
#   Define a class called BoundingBox that represents a detected object
#   region in an image.
#
#   Attributes:
#     - x, y: int  — top-left corner coordinates
#     - width, height: int — box dimensions
#     - label: str — object class (e.g. "face")
#     - confidence: float — detection confidence [0.0, 1.0]
#
#   Methods:
#     - area() → int: returns width * height
#     - is_valid() → bool: True if width > 0, height > 0, and confidence in [0,1]
#     - scale(factor: float) → None: multiplies x, y, width, height by factor
#       (useful when resizing an image)
#
#   __str__ should show: BoundingBox(label='face', x=10, y=20, 100x80, conf=0.92)
#
# Expected output:
#   Area: 8000
#   Valid: True
#   BoundingBox(label='face', x=20, y=40, 200x160, conf=0.92)
#
# Your solution below:
# ---------------------------------------------------------------------------

# Uncomment to test:
# box = BoundingBox(x=10, y=20, width=100, height=80, label="face", confidence=0.92)
# print(f"Area: {box.area()}")
# print(f"Valid: {box.is_valid()}")
# box.scale(2.0)
# print(box)


# ---------------------------------------------------------------------------
# Exercise 3 (Hard) — Class interaction
#
# Problem:
#   Define two classes: ImageRecord and DetectionResult.
#
#   ImageRecord:
#     - Attributes: filename (str), width (int), height (int)
#     - Method: aspect_ratio() → float: width / height
#     - __str__: "ImageRecord('filename', 1280x720)"
#
#   DetectionResult:
#     - Attributes: image (ImageRecord), detections (list of dicts)
#       Each dict has keys: label (str), confidence (float)
#     - Method: best_detection() → dict | None:
#       returns the detection with highest confidence, or None if list is empty
#     - Method: summary() → str: returns a multi-line string report
#     - __str__: calls summary()
#
#   Expected output:
#   ImageRecord('scene_042.jpg', 1920x1080)
#   Best: {'label': 'face', 'confidence': 0.97}
#   === Detection Report ===
#   Image : scene_042.jpg (1920x1080, ratio=1.78)
#   Count : 3 detections
#   Best  : face @ 0.97
#
# Your solution below:
# ---------------------------------------------------------------------------

# Uncomment to test:
# img = ImageRecord("scene_042.jpg", 1920, 1080)
# result = DetectionResult(
#     image=img,
#     detections=[
#         {"label": "face", "confidence": 0.97},
#         {"label": "hand", "confidence": 0.83},
#         {"label": "background", "confidence": 0.61},
#     ]
# )
# print(img)
# print(f"Best: {result.best_detection()}")
# print(result)
