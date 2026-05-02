"""
solutions/03_permissions.py
────────────────────────────
Topic    : Operators
Solution : Exercise 3 — Permission flags
"""

CAN_VIEW_MODELS = 0b0001
CAN_TRAIN       = 0b0010
CAN_DEPLOY      = 0b0100
CAN_ADMIN       = 0b1000


def has_permission(user_perms: int, required_perm: int) -> bool:
    return bool(user_perms & required_perm)


def grant_permission(user_perms: int, new_perm: int) -> int:
    return user_perms | new_perm


def describe_permissions(user_perms: int) -> list[str]:
    all_perms = [
        (CAN_VIEW_MODELS, "view_models"),
        (CAN_TRAIN,       "train"),
        (CAN_DEPLOY,      "deploy"),
        (CAN_ADMIN,       "admin"),
    ]
    return [name for flag, name in all_perms if user_perms & flag]


def combine_team_permissions(*member_perms: int) -> int:
    result = 0
    for perm in member_perms:
        result = result | perm
    return result


# ── Test output ───────────────────────────────────────────────────────────────

print(has_permission(0b0011, CAN_VIEW_MODELS))   # True
print(has_permission(0b0011, CAN_DEPLOY))         # False

result = grant_permission(0b0011, CAN_DEPLOY)
print(bin(result), result)   # 0b111 7

print(describe_permissions(0b1011))   # ['view_models', 'train', 'admin']
print(describe_permissions(0b0000))   # []

print(combine_team_permissions(0b0001, 0b0010, 0b0100))   # 7

# ── Why this works ────────────────────────────────────────────────────────────
#
# has_permission: bool(user_perms & required_perm)
#   & isolates the bit we care about. If it's set, result is non-zero (truthy).
#   bool() converts it to True/False explicitly.
#   Example: 0b0011 & 0b0010 = 0b0010 = 2 → bool(2) = True
#
# grant_permission: user_perms | new_perm
#   | sets the new bit without touching any existing bits.
#   0b0011 | 0b0100 = 0b0111 — the first two bits stay, third is added.
#
# describe_permissions — list comprehension over flag pairs
#   We loop through all known flags and collect names where the bit is set.
#   user_perms & flag is non-zero (truthy) if that flag is set.
#   You'll learn list comprehensions formally in Phase 3 (topic: comprehensions).
#   For now, read it as: "name for each (flag, name) pair where the bit is set".
#
# combine_team_permissions — *member_perms and accumulating with |
#   Start with 0 (no permissions). OR each member's permissions into result.
#   0 | 0b0001 = 0b0001, then 0b0001 | 0b0010 = 0b0011, etc.
#   Starting at 0 is safe because 0 | x = x for any x.