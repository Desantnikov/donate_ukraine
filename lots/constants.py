from enum import Enum


class LOT_STATUS(str, Enum):
    MODERATION = "MODERATION"  # not shown to user
    ACTIVE = "ACTIVE"  # active lots
    CLOSED = "CLOSED"  # finished lots

    @classmethod
    def values(cls):
        return [(i.name, i.value) for i in cls]


class WINNER_PICKING_TYPE(str, Enum):  # who will have the lot
    TOP_DONATER = "TOP_DONATER"  # the one who donated the biggest amount
    RANDOM_DONATER = "RANDOM_DONATER"  # random who donated

    @classmethod
    def values(cls):
        return [(i.name, i.value) for i in cls]
