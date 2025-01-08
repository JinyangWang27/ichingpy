from enum import Enum


class MixEnum(Enum):
    def __new__(cls, value: int, label: str):
        """Create a new Enum member.

        Args:
            value (int): The integer value of the Enum member.
            label (str): The string label for the Enum member.

        Returns:
            obj: A new instance of the SimpleEnum.
        """
        obj = object.__new__(cls)
        obj._value_ = value
        obj.label = label
        return obj

    @property
    def label(self) -> str:
        """str: Represents the string label of the Enum member."""
        return self._label

    @label.setter
    def label(self, value: str) -> None:
        """Sets the label of the Enum member.

        Args:
            value (str): The string to set as the label of the Enum member.
        """
        self._label = value

    def __int__(self) -> int:
        """Convert the Enum to an integer.

        Returns:
            int: The integer value of the Enum.
        """
        return self.value
