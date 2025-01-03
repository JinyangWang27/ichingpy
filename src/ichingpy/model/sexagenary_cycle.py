from typing import Any, Self

from ichingpy.enum import EarthlyBranch, HeavenlyStem


class SexagenaryCycle:
    """The SexagenaryCycle (干支) class."""

    def __init__(self, stem: HeavenlyStem, branch: EarthlyBranch):
        """Initialize a new instance of the SexagenaryCycle class.

        Args:
            stem (HeavenlyStem): The HeavenlyStem to use in the SexagenaryCycle.
            branch (EarthlyBranch): The EarthlyBranch to use in the SexagenaryCycle.
        """
        if stem.value % 2 != branch.value % 2:
            raise ValueError("Invalid combination of HeavenlyStem and EarthlyBranch.")

        self.stem = stem
        self.branch = branch

    @property
    def value(self) -> int:
        """int: Represents the integer value of the SexagenaryCycle."""
        return (self.stem.value - 1) * 12 + self.branch.value

    @classmethod
    def from_int(cls, value: int) -> Self:
        """Create a new instance of the SexagenaryCycle from an integer.

        Args:
            value (int): The integer value
        """
        stem = HeavenlyStem((value - 1) % 12 + 1)
        branch = EarthlyBranch((value - 1) % 12 + 1)
        return cls(stem, branch)

    def __repr__(self) -> str:
        """Return a string representation of the SexagenaryCycle.

        Returns:
            str: A string representation of the SexagenaryCycle.
        """
        return f"{self.stem.label}{self.branch.label}"

    def __int__(self) -> int:
        """Convert the SexagenaryCycle to an integer.

        Returns:
            int: The integer value of the SexagenaryCycle.
        """
        return self.value

    def __add__(self, other: Self | int) -> "SexagenaryCycle":
        """Add an integer or a SexagenaryCycle to the SexagenaryCycle.

        Args:
            other (int): The integer to add to the SexagenaryCycle.

        Returns:
            SexagenaryCycle: The resulting SexagenaryCycle after addition.
        """
        if isinstance(other, int):
            return SexagenaryCycle(self.stem + other, self.branch + other)
        return SexagenaryCycle(self.stem + int(other.stem), self.branch + int(other.branch))

    def __radd__(self, other: Self | int) -> "SexagenaryCycle":
        return self.__add__(other)

    def __eq__(self, other: Any) -> bool:
        """Return True if the SexagenaryCycle is equal to the other SexagenaryCycle.

        Args:
            other (SexagenaryCycle): The other SexagenaryCycle to compare.

        Returns:
            bool: True if the SexagenaryCycle is equal to the other SexagenaryCycle.
        """
        return self.value == other.value
