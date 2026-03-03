"""
Exceptions — Exercises
"""


# ---------------------------------------------------------------------------
# Exercise 1 (Easy) — Safe type conversion
#
# Problem:
#   Write a function safe_parse_record() that takes a dict of raw strings
#   (as you'd get from a CSV row) and converts the values to correct types.
#   If any conversion fails, return None and print which field failed and why.
#
#   Expected output for the good record:
#   {'filename': 'img_001.jpg', 'confidence': 0.94, 'width': 1280, 'height': 720}
#
#   Expected output for the bad record:
#   Failed to parse field 'confidence': could not convert string to float: 'N/A'
#   None
#
good_record = {"filename": "img_001.jpg", "confidence": "0.94",
               "width": "1280", "height": "720"}
bad_record  = {"filename": "img_002.jpg", "confidence": "N/A",
               "width": "1920", "height": "1080"}
#
# Your solution below:
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Exercise 2 (Medium) — Custom exception + retry logic
#
# Problem:
#   Define a custom exception class ModelNotReadyError.
#   Then write a function fetch_prediction() that:
#     - Takes an attempt number (int)
#     - Raises ModelNotReadyError if attempt < 3 (simulates model warming up)
#     - Returns {"label": "fake", "confidence": 0.91} on attempt >= 3
#
#   Write a wrapper run_with_retry() that calls fetch_prediction() up to
#   max_attempts times, catching ModelNotReadyError and retrying.
#   If all attempts fail, re-raise the last exception.
#
#   Expected output:
#   Attempt 1 failed: Model not ready (attempt 1/5)
#   Attempt 2 failed: Model not ready (attempt 2/5)
#   Attempt 3 succeeded: {'label': 'fake', 'confidence': 0.91}
#
# Your solution below:
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Exercise 3 (Hard) — Exception hierarchy for a mini pipeline
#
# Problem:
#   Design an exception hierarchy for a video processing pipeline:
#
#   VideoProcessingError (base)
#   ├── VideoReadError      — file can't be opened or is corrupted
#   ├── FrameExtractionError — a specific frame couldn't be extracted
#   │     (stores: frame_index: int)
#   └── EncoderError        — output encoding failed
#         (stores: codec: str, reason: str)
#
#   Then write process_video() that:
#     - Takes filename (str) and frame_count (int)
#     - Raises VideoReadError if filename doesn't end with ".mp4"
#     - Raises FrameExtractionError for frame index 3 (simulate bad frame)
#     - Returns a list of frame indices that were successfully processed
#
#   Write a caller that handles each exception type differently and
#   demonstrates all three error paths.
#
#   Expected output:
#   VideoReadError: Cannot open 'video.avi': unsupported format
#   Partially processed: [0, 1, 2] (stopped at frame 3)
#   FrameExtractionError at frame 3: corrupted keyframe
#
# Your solution below:
# ---------------------------------------------------------------------------
