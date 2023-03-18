from enum import Enum


class LOT_STATUS(str, Enum):
    MODERATION = "Under moderation"  # not shown to user
    ACTIVE = "Active"  # active lots
    CLOSED = "Closed"  # finished lots

    @classmethod
    def values(cls):
        # [("MODERATION", "Under moderation"), ("ACTIVE", "Active"), ...]
        return [(i.value, i.name) for i in cls]
