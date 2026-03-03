"""
Operators — Solutions
"""


# ---------------------------------------------------------------------------
# Solution 1
# ---------------------------------------------------------------------------

width = 1280
height = 720
channels = 1
dataset_size = 9000
batch_size = 32
bytes_per_pixel = 1
mb = 1_048_576

total_pixels = width * height * channels
full_batches = dataset_size // batch_size
leftover = dataset_size % batch_size
mb_per_sample = round((width * height * channels * bytes_per_pixel) / mb, 1)

print(f"Total pixels  : {total_pixels}")
print(f"Full batches  : {full_batches}")
print(f"Leftover      : {leftover}")
print(f"MB per sample : {mb_per_sample}")


# ---------------------------------------------------------------------------
# Solution 2
# ---------------------------------------------------------------------------

frame_height = 1080
frame_confidence = 0.80
is_blurry = False
frame_codec = "h264"

high_res = frame_height >= 720
good_confidence = frame_confidence > 0.85
not_blurry = not is_blurry
valid_codec = frame_codec in ("h264", "h265")

passes_qc = high_res and good_confidence and not_blurry and valid_codec
print(f"QC passed: {passes_qc}")

if not passes_qc:
    if not high_res:
        print("Reason: low resolution")
    elif not good_confidence:
        print("Reason: low confidence")
    elif not not_blurry:
        print("Reason: blurry frame")
    elif not valid_codec:
        print("Reason: unsupported codec")


# ---------------------------------------------------------------------------
# Solution 3
# ---------------------------------------------------------------------------

raw_model = ""
raw_epochs = 0
raw_device = None
raw_tag = "untagged"

default_model = "ResNet-50"
default_epochs = 20
default_device = "cpu"
default_tag = "untagged"

# 'or' returns the first truthy value — perfect for fallback defaults
model = raw_model or default_model
epochs = raw_epochs or default_epochs
device = raw_device or default_device
tag = raw_tag or default_tag

print(f"model     : {model}")
print(f"epochs    : {epochs}")
print(f"device    : {device}")
print(f"tag       : {tag}")
