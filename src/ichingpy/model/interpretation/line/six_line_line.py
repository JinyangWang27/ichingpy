from ichingpy.enum.branch import EarthlyBranch
from ichingpy.enum.stem import HeavenlyStem
from ichingpy.model.interpretation.line.base import LineInterpretationBase


class SixLineLineInterp(LineInterpretationBase):

    def __repr__(self) -> str:
        return ""

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
