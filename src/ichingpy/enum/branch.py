from typing import Self

from ichingpy.enum.five_phase import FivePhase
from ichingpy.enum.mixed_enum import MixEnum

PHASE_MAPPING: dict[str, FivePhase] = {
    "Zi": FivePhase.WATER,
    "Chou": FivePhase.EARTH,
    "Yin": FivePhase.WOOD,
    "Mao": FivePhase.WOOD,
    "Chen": FivePhase.EARTH,
    "Si": FivePhase.FIRE,
    "Wu": FivePhase.FIRE,
    "Wei": FivePhase.EARTH,
    "Shen": FivePhase.METAL,
    "You": FivePhase.METAL,
    "Xu": FivePhase.EARTH,
    "Hai": FivePhase.WATER,
}


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

    @property
    def phase(self) -> FivePhase:
        """Return the FivePhases associated with the EarthlyBranch."""
        return PHASE_MAPPING[self.name]

    @property
    def label(self) -> str:
        """Return the label of the EarthlyBranch."""
        return f"{self._label}"

    @label.setter
    def label(self, value: str) -> None:
        """Sets the label of the EarthlyBranch."""
        self._label = value

    @property
    def label_with_phase(self) -> str:
        """Return the label of the EarthlyBranch."""
        return f"{self._label}{self.phase.label}"

    @property
    def name_en(self) -> str:
        return f"{self.name.ljust(4)} ({str(self.value).ljust(2)}) {self.phase.name.ljust(5)}"

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

    def __sub__(self, other: Self | int) -> "EarthlyBranch":
        """Subtract an integer or an EarthlyBranch from the EarthlyBranch.

        Args:
            other (int): The integer to subtract from the EarthlyBranch.

        Returns:
            EarthlyBranch: The resulting EarthlyBranch after subtraction.
        """
        return EarthlyBranch((self.value - int(other) - 1) % 12 + 1)

    def __rsub__(self, other: Self | int) -> "EarthlyBranch":
        return self.__sub__(other)
