# %%

from ichingpy.enum import HeavenlyStem
from ichingpy.model.hexagram import Hexagram, Trigram


class HexagramAssigner:
    """Class to assign stems and branches to a hexagram."""

    def assign(self, hexagram: Hexagram):
        self.assign_stems(hexagram)
        self.assign_branches(hexagram)

    def assign_stems(self, hexagram: Hexagram):

        self._assign_stems_for_trigram(hexagram.outer, inner=False)
        self._assign_stems_for_trigram(hexagram.inner, inner=True)
        # return Hexagram(inner=inner, outer=outer)

    def _assign_stems_for_trigram(self, trigram: Trigram, inner: bool):
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
        # return trigram

    def assign_branches(self, hexagram: Hexagram): ...


# %%
