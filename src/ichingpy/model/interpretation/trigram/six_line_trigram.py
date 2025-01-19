from typing import ClassVar

from ichingpy.enum.branch import EarthlyBranch
from ichingpy.enum.palace import Palace
from ichingpy.enum.stem import HeavenlyStem
from ichingpy.model.interpretation.line.six_line_line import SixLineLineInterp
from ichingpy.model.interpretation.trigram.base import TrigramInterpretationBase


class SixLineTrigramInterp(TrigramInterpretationBase[SixLineLineInterp]):
    PALACE_MAPPING: ClassVar[dict[tuple[int, int, int], Palace]] = {
        (1, 1, 1): Palace.HEAVEN,  # "乾"
        (1, 1, 0): Palace.LAKE,  # "兑"
        (1, 0, 1): Palace.FIRE,  # "离"
        (1, 0, 0): Palace.THUNDER,  # "震"
        (0, 1, 1): Palace.WIND,  # "巽"
        (0, 1, 0): Palace.WATER,  # "坎"
        (0, 0, 1): Palace.MOUNTAIN,  # "艮"
        (0, 0, 0): Palace.EARTH,  # "坤"
    }

    @property
    def stem(self) -> list[HeavenlyStem]:
        if not all(hasattr(line, "_stem") for line in self.lines):
            raise ValueError("Stems have not been assigned for all lines in the Trigram")
        if not all(self.lines[0].stem == line.stem for line in self.lines):
            raise ValueError("Stems of all lines in a Trigram should be the same")
        return [line.stem for line in self.lines]

    @property
    def branch(self) -> list[EarthlyBranch]:
        if not all(hasattr(line, "_branch") for line in self.lines):
            raise ValueError("Branches have not been assigned for all lines in the Trigram")
        return [line.branch for line in self.lines]

    @stem.setter
    def stem(self, value: HeavenlyStem):
        self.lines[0].stem = value
        self.lines[1].stem = value
        self.lines[2].stem = value

    @branch.setter
    def branch(self, value: list[EarthlyBranch]):
        self.lines[0].branch = value[0]
        self.lines[1].branch = value[1]
        self.lines[2].branch = value[2]

    @property
    def palace(self) -> Palace:
        """Get the palace of the Trigram."""
        values = (self.value[0] % 2, self.value[1] % 2, self.value[2] % 2)
        return self.PALACE_MAPPING[values]

    @property
    def opposite(self) -> "SixLineTrigramInterp":
        return SixLineTrigramInterp(lines=[SixLineLineInterp(status=line.status.opposite) for line in self.lines])
