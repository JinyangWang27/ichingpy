# %%
from ichingpy.divination.base import DivinationEngineBase
from ichingpy.enum import HeavenlyStem
from ichingpy.enum.branch import EarthlyBranch
from ichingpy.model.hexagram import Hexagram
from ichingpy.model.interpretation.hexagram.six_line_hexagram import SixLineHexagramInterp
from ichingpy.model.interpretation.line.six_line_line import SixLineLineInterp
from ichingpy.model.interpretation.trigram.six_line_trigram import SixLineTrigramInterp


class SixLinesDivinationEngine(DivinationEngineBase):
    """Class to assign stems and branches to a hexagram.
    京房六爻 装卦器
    """

    FIRST_BRANCH_MAPPING = {
        (1, 1, 1): EarthlyBranch.Zi,  # 乾 1 (remainder of sum modulo 2)
        (0, 1, 0): EarthlyBranch.Yin,  # 坎 1
        (0, 0, 1): EarthlyBranch.Chen,  # 艮 1
        (1, 0, 0): EarthlyBranch.Zi,  # 震 1
        (0, 1, 1): EarthlyBranch.Chou,  # 巽 0
        (1, 0, 1): EarthlyBranch.Mao,  # 離 0
        (0, 0, 0): EarthlyBranch.Wei,  # 坤 0
        (1, 1, 0): EarthlyBranch.Si,  # 兌 0
    }

    def assign_interpretations(self, hexagram: Hexagram) -> tuple[SixLineTrigramInterp, SixLineTrigramInterp]:
        lines = [SixLineLineInterp(status=line.status) for line in hexagram.lines]
        return SixLineTrigramInterp(lines=lines[:3]), SixLineTrigramInterp(lines=lines[3:])

    def execute(self, hexagram: Hexagram):

        inner_interp, outer_interp = self.assign_interpretations(hexagram)
        self._assign_stems(inner_interp, outer_interp)
        self._assign_branches(inner_interp, outer_interp)
        hexagram.inner.interpretation = inner_interp
        hexagram.outer.interpretation = outer_interp
        hexagram.interpretation = SixLineHexagramInterp(inner=inner_interp, outer=outer_interp)

    def _assign_stems(self, inner_interp: SixLineTrigramInterp, outer_interp: SixLineTrigramInterp):
        """Assign stems to the both inner and outer trigrams of the hexagram."""
        self._assign_stems_for_trigram(inner_interp, inner=True)
        self._assign_stems_for_trigram(outer_interp, inner=False)

    def _assign_branches(self, inner_interp: SixLineTrigramInterp, outer_interp: SixLineTrigramInterp):
        """Assign branches to the both inner and outer trigrams of the hexagram."""
        self._assign_branches_for_trigram(inner_interp, inner=True)
        self._assign_branches_for_trigram(outer_interp, inner=False)

    def _assign_stems_for_trigram(self, trigram: SixLineTrigramInterp, inner: bool):
        """Assign stems to the trigram based on the trigram's value."""
        # 乾内甲外壬，艮丙坎戊震庚；
        # 坤内乙外癸，兑丁离己巽辛
        match tuple(v % 2 for v in trigram.value):
            case (1, 1, 1):  # 乾内甲外壬
                trigram.stem = HeavenlyStem.Jia if inner else HeavenlyStem.Ren
            case (1, 1, 0):  # 兑丁
                trigram.stem = HeavenlyStem.Ding
            case (1, 0, 1):  # 离己
                trigram.stem = HeavenlyStem.Ji
            case (1, 0, 0):  # 震庚
                trigram.stem = HeavenlyStem.Geng
            case (0, 1, 0):  # 坎戊
                trigram.stem = HeavenlyStem.Wu
            case (0, 1, 1):  # 巽辛
                trigram.stem = HeavenlyStem.Xin
            case (0, 0, 1):  # 艮丙
                trigram.stem = HeavenlyStem.Bing
            case (0, 0, 0):  # 坤内乙外癸
                trigram.stem = HeavenlyStem.Yi if inner else HeavenlyStem.Gui
            case _:  # pragma: no cover
                raise ValueError(f"Invalid trigram {trigram.value}")

    def _assign_branches_for_trigram(self, trigram: SixLineTrigramInterp, inner: bool):
        """Assign branches to the trigram based on the trigram's value."""
        # trigram_values = tuple(v % 2 for v in trigram.value) # linter is not smart enough...
        v1, v2, v3 = trigram.value
        trigram_values = (v1 % 2, v2 % 2, v3 % 2)

        first_branch = (
            self.FIRST_BRANCH_MAPPING[trigram_values] if inner else self.FIRST_BRANCH_MAPPING[trigram_values] + 6
        )

        if sum(trigram_values) % 2 == 1:  # remainder is 1
            # 阳顺
            trigram.branch = [first_branch, first_branch + 2, first_branch + 4]
        else:  # remainder is 0
            # 阴逆
            trigram.branch = [first_branch, first_branch - 2, first_branch - 4]


# %%
