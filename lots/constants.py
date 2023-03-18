from enum import Enum


class LOT_STATUS(str, Enum):
    MODERATION = "MODERATION"  # not shown to user
    ACTIVE = "ACTIVE"  # active lots
    CLOSED = "CLOSED"  # finished lots

    @classmethod
    def values(cls):
        return [(i.name, i.value) for i in cls]
