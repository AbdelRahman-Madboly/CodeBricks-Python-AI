"""
exercises/03_permissions.py
────────────────────────────
Topic    : Operators
Exercise : 3 of 3 — Hard
Concept  : Bitwise &, |, binary representation, permission flag systems

Context
-------
A multi-user AI platform controls what each user can do via permission flags.
Each permission is a single bit in a 4-bit integer. You need to write
functions that check permissions, grant them, and combine them.

─────────────────────────────────────────────────────────────────
Permission flags (do not change):
─────────────────────────────────────────────────────────────────
"""

CAN_VIEW_MODELS   = 0b0001   # 1
CAN_TRAIN         = 0b0010   # 2
CAN_DEPLOY        = 0b0100   # 4
CAN_ADMIN         = 0b1000   # 8

"""
─────────────────────────────────────────────────────────────────
Task A — has_permission()
─────────────────────────────────────────────────────────────────
Write a function that returns True if the user has a specific permission.

Signature:
  def has_permission(user_perms: int, required_perm: int) -> bool

Expected:
  has_permission(0b0011, CAN_VIEW_MODELS)  → True
  has_permission(0b0011, CAN_TRAIN)        → True
  has_permission(0b0011, CAN_DEPLOY)       → False

─────────────────────────────────────────────────────────────────
Task B — grant_permission()
─────────────────────────────────────────────────────────────────
Write a function that adds a permission to a user's existing permissions.

Signature:
  def grant_permission(user_perms: int, new_perm: int) -> int

Expected:
  grant_permission(0b0011, CAN_DEPLOY) → 0b0111 = 7

─────────────────────────────────────────────────────────────────
Task C — describe_permissions()
─────────────────────────────────────────────────────────────────
Write a function that returns a list of permission names the user has.

Signature:
  def describe_permissions(user_perms: int) -> list[str]

Expected:
  describe_permissions(0b1011) → ["view_models", "train", "admin"]
  describe_permissions(0b0000) → []

─────────────────────────────────────────────────────────────────
Task D — combine_team_permissions()
─────────────────────────────────────────────────────────────────
Write a function that takes any number of permission integers
and returns the union of all of them (all bits that appear in any).

Signature:
  def combine_team_permissions(*member_perms: int) -> int

Expected:
  combine_team_permissions(0b0001, 0b0010, 0b0100) → 0b0111 = 7
─────────────────────────────────────────────────────────────────
"""

# ── Your functions ────────────────────────────────────────────────────────────


# ── Test calls (uncomment after writing your functions) ───────────────────────

# Task A
# print(has_permission(0b0011, CAN_VIEW_MODELS))  # True
# print(has_permission(0b0011, CAN_TRAIN))        # True
# print(has_permission(0b0011, CAN_DEPLOY))       # False
# print(has_permission(0b0000, CAN_ADMIN))        # False

# Task B
# result = grant_permission(0b0011, CAN_DEPLOY)
# print(bin(result))  # 0b111
# print(result)       # 7

# Task C
# print(describe_permissions(0b1011))  # ['view_models', 'train', 'admin']
# print(describe_permissions(0b0000))  # []
# print(describe_permissions(0b1111))  # ['view_models', 'train', 'deploy', 'admin']

# Task D
# print(combine_team_permissions(0b0001, 0b0010, 0b0100))  # 7
# print(combine_team_permissions(0b1000, 0b0011))          # 11