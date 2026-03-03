"""
Lists — Solutions
"""


# ---------------------------------------------------------------------------
# Solution 1
# ---------------------------------------------------------------------------

frames = list(range(1, 11))

print(f"First 3   : {frames[:3]}")
print(f"Last 2    : {frames[-2:]}")
print(f"Every other: {frames[::2]}")
print(f"Reversed  : {frames[::-1]}")


# ---------------------------------------------------------------------------
# Solution 2
# ---------------------------------------------------------------------------

detections = [
    {"image": "img_001", "label": "face",       "confidence": 0.94},
    {"image": "img_002", "label": "background", "confidence": 0.87},
    {"image": "img_003", "label": "face",       "confidence": 0.73},
    {"image": "img_004", "label": "face",       "confidence": 0.91},
    {"image": "img_005", "label": "hand",       "confidence": 0.85},
]

filtered = [
    d for d in detections
    if d["confidence"] > 0.80 and d["label"] == "face"
]

labels = [
    f"{d['image']}: {d['label']} @ {d['confidence']:.0%}"
    for d in filtered
]

print(f"Filtered count: {len(filtered)}")
print(labels)


# ---------------------------------------------------------------------------
# Solution 3
# ---------------------------------------------------------------------------

scores = [0.72, 0.95, 0.61, 0.97, 0.88, 0.92, 0.45]


def find_top_k(values: list[float], k: int) -> list[float]:
    """
    Return the k highest values from the list in descending order.
    Uses selection sort logic to extract the top k without built-in sort.
    """
    remaining = values[:]   # copy so we don't mutate the input
    result = []

    for _ in range(k):
        # Find the index of the current maximum manually
        max_index = 0
        for i in range(1, len(remaining)):
            if remaining[i] > remaining[max_index]:
                max_index = i
        result.append(remaining.pop(max_index))

    return result


print(find_top_k(scores, 3))   # [0.97, 0.95, 0.92]
