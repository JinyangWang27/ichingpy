from typing import Self

from ichingpy.enum.mixed_enum import MixEnum


class HeavenlyStem(MixEnum):
    """The HeavenlyStem (天干) Enum class."""

    Jia = 1, "甲"
    Yi = 2, "乙"
    Bing = 3, "丙"
    Ding = 4, "丁"
    Wu = 5, "戊"
    Ji = 6, "己"
    Geng = 7, "庚"
    Xin = 8, "辛"
    Ren = 9, "壬"
    Gui = 10, "癸"

    def __add__(self, other: Self | int) -> "HeavenlyStem":
        """Add an integer or a HeavenlyStem to the HeavenlyStem.

        Args:
            other (int): The integer to add to the HeavenlyStem.

        Returns:
            HeavenlyStem: The resulting HeavenlyStem after addition.
        """
        return HeavenlyStem((self.value + int(other) - 1) % 10 + 1)

    def __radd__(self, other: Self | int) -> "HeavenlyStem":
        return self.__add__(other)

    def __sub__(self, other: Self | int) -> "HeavenlyStem":
        """Subtract an integer or a HeavenlyStem from the HeavenlyStem.

        Args:
            other (int): The integer to subtract from the HeavenlyStem.

        Returns:
            HeavenlyStem: The resulting HeavenlyStem after subtraction.
        """
        return HeavenlyStem((self.value - int(other) - 1) % 10 + 1)

    def __rsub__(self, other: Self | int) -> "HeavenlyStem":
        return self.__sub__(other)
