"""
examples/03_bitwise.py
───────────────────────
Topic  : Operators
Example: 3 of 3 — Binary numbers and bitwise operators

Context
-------
Binary and bitwise operators show up in AI/ML systems in two main places:
permission flags (what features or roles does this user/model have?) and
low-level data processing (image masks, audio bit depths, network protocol
parsing). Understanding binary is also the foundation for understanding
how floats are stored, which explains the float precision trap from topic 02.

Covers:
  - Binary number representation (0b prefix)
  - Converting between binary and decimal
  - int(string, 2) for parsing binary strings
  - & (bitwise AND) — check if a bit is set
  - | (bitwise OR)  — combine/grant bits
  - Practical use: permission flag systems

Run this file. Predict each output before you see it.
"""

# ── Binary numbers ────────────────────────────────────────────────────────────

print("=== Binary representation ===")

# 0b prefix tells Python this is a binary literal
print(0b0001)   # 1
print(0b0010)   # 2
print(0b0100)   # 4
print(0b1000)   # 8
print(0b1111)   # 15 — all four bits set

# Each position is a power of 2: 8  4  2  1
#                        0b1101 = 8 + 4 + 0 + 1 = 13
print(0b1101)   # 13

# Converting: Python prints binary ints as decimal by default
# Use bin() to see the binary representation
print(bin(13))  # 0b1101
print(bin(255)) # 0b11111111  — 8 bits all set

# Convert binary string → int
print(int("1101", 2))    # 13  — second arg is the base
print(int("11111111", 2)) # 255

# ── Bitwise AND: & ────────────────────────────────────────────────────────────

print()
print("=== Bitwise AND (&) ===")

# & compares bit by bit — result is 1 only where BOTH bits are 1
#   0101  (5)
# & 0011  (3)
# = 0001  (1)
print(f"5 & 3 = {5 & 3}")   # 1

#   0101  (5)
# & 0111  (7)
# = 0101  (5)
print(f"5 & 7 = {5 & 7}")   # 5

# Use & to CHECK if a specific bit is set:
# If (permissions & required_bit) is non-zero → bit is set → has permission
CAN_READ    = 0b0001   # 1
CAN_WRITE   = 0b0010   # 2
CAN_DELETE  = 0b0100   # 4
CAN_ADMIN   = 0b1000   # 8

user_perms = 0b0011   # read + write (binary for 3)

has_read   = user_perms & CAN_READ    # 0b0001 = 1, truthy
has_write  = user_perms & CAN_WRITE   # 0b0010 = 2, truthy
has_delete = user_perms & CAN_DELETE  # 0b0000 = 0, falsy
has_admin  = user_perms & CAN_ADMIN   # 0b0000 = 0, falsy

print(f"\nUser permissions: {bin(user_perms)}")
print(f"  can read   : {bool(has_read)}")    # True
print(f"  can write  : {bool(has_write)}")   # True
print(f"  can delete : {bool(has_delete)}")  # False
print(f"  is admin   : {bool(has_admin)}")   # False

# ── Bitwise OR: | ─────────────────────────────────────────────────────────────

print()
print("=== Bitwise OR (|) ===")

# | compares bit by bit — result is 1 where EITHER bit is 1
#   0101  (5)
# | 0011  (3)
# = 0111  (7)
print(f"5 | 3 = {5 | 3}")   # 7

# Use | to GRANT (combine) permissions
reader_perms = 0b0001   # can read
writer_perms = 0b0010   # can write

combined = reader_perms | writer_perms
print(f"\nCombined perms: {bin(combined)}")  # 0b11

# Grant delete permission to existing user
user_perms = 0b0011   # read + write
user_perms = user_perms | CAN_DELETE
print(f"After grant   : {bin(user_perms)}")  # 0b111 = read + write + delete

# Combine multiple model feature flags with |
FEATURE_ATTENTION  = 0b0001
FEATURE_DROPOUT    = 0b0010
FEATURE_LAYERNORM  = 0b0100

model_features = FEATURE_ATTENTION | FEATURE_DROPOUT | FEATURE_LAYERNORM
print(f"\nModel features: {bin(model_features)}")  # 0b111

# Check a specific feature with &
has_dropout = bool(model_features & FEATURE_DROPOUT)
print(f"Has dropout   : {has_dropout}")  # True

# ── What to notice ────────────────────────────────────────────────────────────
#
# 1. Each power of 2 sets exactly one bit — this is why permission flags
#    use powers of 2 (1, 2, 4, 8, 16...). Each flag occupies one bit position.
#
# 2. & for CHECK, | for COMBINE — this is the standard pattern.
#    "Does this user have this permission?" → user_perms & required_perm
#    "Give this user this permission?"     → user_perms | new_perm
#
# 3. int("1101", 2) converts a binary STRING to an integer.
#    The second argument is the base — base 2 = binary.
#    This is how you'd parse binary data from a file or network packet.
#
# 4. bool(0b0000) is False, bool(anything_nonzero) is True.
#    So you can use the & result directly in an if statement:
#    if user_perms & CAN_ADMIN: ...
#    No need to compare to a specific value.
#
# 5. In ML systems, bitwise flags are used for model feature toggles,
#    dataset split indicators, and GPU memory layout masks in CUDA code.
#    At the Python level it's rare, but at the C/CUDA level it's constant.