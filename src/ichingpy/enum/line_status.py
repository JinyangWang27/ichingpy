from enum import Enum


class LineStatus(Enum):
    """An Enum representing the status of a line in a hexagram.

    Attributes:
        CHANGING_YANG (int): A solid line that is changing to a broken line.
        STATIC_YIN (int): A static broken line, representing dark, feminine, etc.
        STATIC_YANG (int): A static solid line, representing light, masculine, etc.
        CHANGING_YIN (int): A broken line that is changing to a solid line.
    """

    CHANGING_YIN = 0
    STATIC_YANG = 1
    STATIC_YIN = 2
    CHANGING_YANG = 3
