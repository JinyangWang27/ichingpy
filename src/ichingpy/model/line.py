import random
from typing import ClassVar, Self

from pydantic import BaseModel

from ichingpy.enum import EarthlyBranch, HeavenlyStem, LineStatus
from ichingpy.enum.language import Language


class LineTransformationError(Exception):
    pass


class Line(BaseModel):
    """A Line (爻) of a trigram or a hexagram in the I Ching"""

    display_language: ClassVar[Language] = Language.CHINESE

    status: LineStatus

    def __repr__(self) -> str:
        representation = f"-----" if self.is_yang else f"-- --"

        if self.is_transform:
            if self.is_yin:
                representation += f" X -> -----"
            else:
                representation += f" O -> -- --"

        has_stem = hasattr(self, "_stem")
        has_branch = hasattr(self, "_branch")
        match self.display_language:
            case Language.ENGLISH:
                stem = f"{self.stem.name.ljust(4)} ({self.stem.value}) " if has_stem else ""
                branch = f"{self.branch.name_en.ljust(4)} " if has_branch else ""
            case Language.CHINESE:
                stem = f"{self.stem.label} " if has_stem else ""
                branch = f"{self.branch.label_with_phase} " if has_branch else ""

        representation = f"{stem}{branch}{representation}"
        return representation

    @property
    def value(self) -> int:
        """int: The integer value of the Line."""
        return self.status.value

    @property
    def is_yang(self) -> bool:
        """bool: Whether the Yao is a solid line (阳爻)"""
        return True if self.status in [LineStatus.STATIC_YANG, LineStatus.CHANGING_YANG] else False

    @property
    def is_yin(self) -> bool:
        """bool: Whether the Yao is a broken line (阴爻)"""
        return True if self.status in [LineStatus.STATIC_YIN, LineStatus.CHANGING_YIN] else False

    @property
    def is_transform(self) -> bool:
        """bool: Whether the Yao needs to be transformed (变爻)"""
        return True if self.status in [LineStatus.CHANGING_YIN, LineStatus.CHANGING_YANG] else False

    def get_transformed(self) -> "Line":
        """Get the transformed Line, which is always a static line
        只作用于动爻，返回变爻
        """
        match self.status:
            case LineStatus.STATIC_YANG | LineStatus.STATIC_YIN:
                raise LineTransformationError("Line is already static")
            case LineStatus.CHANGING_YANG:
                return Line(status=LineStatus.STATIC_YIN)
            case LineStatus.CHANGING_YIN:
                return Line(status=LineStatus.STATIC_YANG)

    def transform(self) -> "Line":
        """Create a transform line from a static line.
        只作用与静爻，返回阴阳与自身相同之动爻。
        """
        match self.status:
            case LineStatus.CHANGING_YANG | LineStatus.CHANGING_YIN:
                raise LineTransformationError("Line is already static")
            case LineStatus.STATIC_YANG:
                return Line(status=LineStatus.CHANGING_YANG)
            case LineStatus.STATIC_YIN:
                return Line(status=LineStatus.CHANGING_YIN)

    @property
    def stem(self) -> HeavenlyStem:
        """The HeavenlyStem associated with the Line."""
        return self._stem

    @stem.setter
    def stem(self, value: HeavenlyStem) -> None:
        """Set the HeavenlyStem associated with the Line."""
        self._stem = value

    @property
    def branch(self) -> EarthlyBranch:
        """The EarthlyBranch associated with the Line."""
        return self._branch

    @branch.setter
    def branch(self, value: EarthlyBranch) -> None:
        """Set the EarthlyBranch associated with the Line."""
        self._branch = value

    @classmethod
    def random(cls) -> Self:
        """Create a random Line instance."""
        return cls(status=LineStatus(random.getrandbits(2)))

    @classmethod
    def set_language(cls, language: str):
        """Set the display language for the Line class."""
        cls.display_language = Language(language)
