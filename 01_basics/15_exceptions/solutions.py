"""
Exceptions — Solutions
"""


# ---------------------------------------------------------------------------
# Solution 1
# ---------------------------------------------------------------------------

def safe_parse_record(raw: dict) -> dict | None:
    """
    Convert a raw string dict from CSV into typed values.
    Returns None and prints the error if any conversion fails.
    """
    try:
        return {
            "filename":   raw["filename"],
            "confidence": float(raw["confidence"]),
            "width":      int(raw["width"]),
            "height":     int(raw["height"]),
        }
    except (ValueError, KeyError) as e:
        # Find which field caused the error by trying each one
        for field, converter in [("confidence", float), ("width", int), ("height", int)]:
            try:
                converter(raw.get(field, ""))
            except (ValueError, TypeError) as field_error:
                print(f"Failed to parse field {field!r}: {field_error}")
                return None
        print(f"Parse error: {e}")
        return None


good_record = {"filename": "img_001.jpg", "confidence": "0.94",
               "width": "1280", "height": "720"}
bad_record  = {"filename": "img_002.jpg", "confidence": "N/A",
               "width": "1920", "height": "1080"}

print(safe_parse_record(good_record))
print(safe_parse_record(bad_record))


# ---------------------------------------------------------------------------
# Solution 2
# ---------------------------------------------------------------------------

class ModelNotReadyError(Exception):
    """Raised when the model has not finished initialising."""


def fetch_prediction(attempt: int) -> dict:
    """
    Simulate fetching a prediction. Raises ModelNotReadyError for early attempts.

    Args:
        attempt: Current attempt number (1-based).

    Returns:
        Prediction dict on success.

    Raises:
        ModelNotReadyError: If attempt < 3.
    """
    if attempt < 3:
        raise ModelNotReadyError(f"Model not ready (attempt {attempt}/5)")
    return {"label": "fake", "confidence": 0.91}


def run_with_retry(max_attempts: int = 5) -> dict:
    """
    Call fetch_prediction() with retry logic.

    Args:
        max_attempts: Maximum number of attempts before giving up.

    Returns:
        Prediction dict on success.

    Raises:
        ModelNotReadyError: If all attempts fail.
    """
    last_error = None
    for attempt in range(1, max_attempts + 1):
        try:
            result = fetch_prediction(attempt)
            print(f"Attempt {attempt} succeeded: {result}")
            return result
        except ModelNotReadyError as e:
            last_error = e
            print(f"Attempt {attempt} failed: {e}")

    raise last_error  # all attempts exhausted


run_with_retry()


# ---------------------------------------------------------------------------
# Solution 3
# ---------------------------------------------------------------------------

class VideoProcessingError(Exception):
    """Base class for all video processing errors."""


class VideoReadError(VideoProcessingError):
    """Raised when a video file cannot be opened."""
    def __init__(self, filename: str, reason: str) -> None:
        self.filename = filename
        super().__init__(f"Cannot open {filename!r}: {reason}")


class FrameExtractionError(VideoProcessingError):
    """Raised when a specific frame cannot be extracted."""
    def __init__(self, frame_index: int, reason: str) -> None:
        self.frame_index = frame_index
        super().__init__(f"corrupted keyframe")


class EncoderError(VideoProcessingError):
    """Raised when output encoding fails."""
    def __init__(self, codec: str, reason: str) -> None:
        self.codec = codec
        self.reason = reason
        super().__init__(f"Encoder failed [{codec}]: {reason}")


def process_video(filename: str, frame_count: int) -> list[int]:
    """
    Simulate processing a video file frame by frame.

    Raises:
        VideoReadError: If the file format is unsupported.
        FrameExtractionError: If frame index 3 is encountered.
    """
    if not filename.endswith(".mp4"):
        raise VideoReadError(filename, "unsupported format")

    processed = []
    for i in range(frame_count):
        if i == 3:
            raise FrameExtractionError(frame_index=3, reason="corrupted keyframe")
        processed.append(i)

    return processed


# Test VideoReadError
try:
    process_video("video.avi", 5)
except VideoReadError as e:
    print(f"VideoReadError: {e}")

# Test FrameExtractionError
try:
    frames = process_video("video.mp4", 6)
except FrameExtractionError as e:
    partial = list(range(e.frame_index))
    print(f"Partially processed: {partial} (stopped at frame {e.frame_index})")
    print(f"FrameExtractionError at frame {e.frame_index}: {e}")
