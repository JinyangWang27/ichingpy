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

    @classmethod
    def _missing_(cls, value: object):
        """Return an Enum member matching the provided label, or invoke the superclass's _missing_.

        This method extends Enum's functionality to allow lookup by string label if the direct value
        does not match an Enum member.

        Args:
            value (object): The value or label to look up in the Enum.

        Returns:
            Enum: The Enum member if found by label, otherwise the result from superclass's _missing_ method.
        """
        for member in cls:
            if member.label == value:
                return member
        return super()._missing_(value)

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
