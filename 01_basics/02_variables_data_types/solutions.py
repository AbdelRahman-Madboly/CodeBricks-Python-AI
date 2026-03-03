"""
Variables and Data Types — Solutions
"""


# ---------------------------------------------------------------------------
# Solution 1
# ---------------------------------------------------------------------------

batch_size = 10000
confidence = 0.92
architecture = "ResNet"
is_pretrained = True
checkpoint = None

print(f"{batch_size} -> {type(batch_size)}")
print(f"{confidence} -> {type(confidence)}")
print(f"{architecture} -> {type(architecture)}")
print(f"{is_pretrained} -> {type(is_pretrained)}")
print(f"{checkpoint} -> {type(checkpoint)}")


# ---------------------------------------------------------------------------
# Solution 2
# ---------------------------------------------------------------------------

raw_device_id = "camera-01"
raw_frame_count = "1200"
raw_fps = "29.97"
raw_active = "True"
raw_missing = "None"

device_id = raw_device_id               # already a string
frame_count = int(raw_frame_count)
fps = float(raw_fps)
# bool("True") returns True, but bool("False") also returns True
# because any non-empty string is truthy — so we compare explicitly
active = raw_active == "True"
missing = None if raw_missing == "None" else raw_missing

print(f"Device  : {device_id}")
print(f"Frames  : {frame_count}")
print(f"FPS     : {fps}")
print(f"Active  : {active}")
print(f"Missing : {missing}")


# ---------------------------------------------------------------------------
# Solution 3
# ---------------------------------------------------------------------------

# Q1: False — floating point cannot represent 0.1 and 0.2 exactly
# Q2: True  — bool inherits from int in Python
# Q3: True  — True is stored as 1
# Q4: False — None is not equal to anything except None
# Q5: False — 1000 is outside CPython's cache range (-5 to 256),
#             so two separate objects are created

print("--- Predictions vs Reality ---")
print(f"Q1 float equality   | actual: {0.1 + 0.2 == 0.3}")       # False
print(f"Q2 bool subclass    | actual: {issubclass(bool, int)}")    # True
print(f"Q3 True == 1        | actual: {True == 1}")                # True
print(f"Q4 None == False    | actual: {None == False}")            # False
a = 1000
b = 1000
print(f"Q5 large int is     | actual: {a is b}")                   # False
