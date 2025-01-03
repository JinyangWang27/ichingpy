from typing import Self

from ichingpy.enum.mixed_enum import MixEnum


class EarthlyBranch(MixEnum):
    """The EarthlyBranch (地支) Enum class."""

    Zi = 1, "子"
    Chou = 2, "丑"
    Yin = 3, "寅"
    Mao = 4, "卯"
    Chen = 5, "辰"
    Si = 6, "巳"
    Wu = 7, "午"
    Wei = 8, "未"
    Shen = 9, "申"
    You = 10, "酉"
    Xu = 11, "戌"
    Hai = 12, "亥"

    def __add__(self, other: Self | int) -> "EarthlyBranch":
        """Add an integer or an EarthlyBranch to the EarthlyBranch.

        Args:
            other (int): The integer to add to the EarthlyBranch.

        Returns:
            EarthlyBranch: The resulting EarthlyBranch after addition.
        """
        return EarthlyBranch((self.value + int(other) - 1) % 12 + 1)

    def __radd__(self, other: Self | int) -> "EarthlyBranch":
        return self.__add__(other)
