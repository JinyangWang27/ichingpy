# %%
import random
from typing import Self

from pydantic import BaseModel

from ichingpy.enum import EarthlyBranch, HeavenlyStem, LineStatus


class LineTransformationError(Exception):
    pass


class Line(BaseModel):
    """A Line (爻) of a trigram or a hexagram in the I Ching"""

    status: LineStatus

    def __repr__(self) -> str:
        representation = f"-----" if self.is_yang else f"-- --"

        if self.is_transform:
            if self.is_yin:
                representation += f" X -> -----"
            else:
                representation += f" O -> -- --"

        stem = f"{self.stem.label} " if hasattr(self, "_stem") else ""
        branch = f"{self.branch.label} " if hasattr(self, "_branch") else ""

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
        """Get the transformed Line, which is always a static line"""
        match self.status:
            case LineStatus.STATIC_YANG | LineStatus.STATIC_YIN:
                raise LineTransformationError("Line is already static")
            case LineStatus.CHANGING_YANG:
                return Line(status=LineStatus.STATIC_YIN)
            case LineStatus.CHANGING_YIN:
                return Line(status=LineStatus.STATIC_YANG)

    @property
    def stem(self) -> HeavenlyStem:
        return self._stem

    @stem.setter
    def stem(self, value: HeavenlyStem) -> None:
        self._stem = value

    @property
    def branch(self) -> EarthlyBranch:
        return self._branch

    @branch.setter
    def branch(self, value: EarthlyBranch) -> None:
        self._branch = value

    @classmethod
    def random(cls) -> Self:
        """Create a random Line instance."""
        return cls(status=LineStatus(random.getrandbits(2)))


# %%
