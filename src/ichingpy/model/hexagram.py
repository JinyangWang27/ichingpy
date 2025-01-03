# %%
import random
from typing import Self

from pydantic import BaseModel

from ichingpy.enum.line_status import LineStatus
from ichingpy.model.line import Line
from ichingpy.model.trigram import Trigram


class Hexagram(BaseModel):

    inner: Trigram
    outer: Trigram

    @property
    def lines(self) -> list[Line]:
        return self.inner.lines + self.outer.lines

    def __repr__(self):
        return "\n".join(repr(line) for line in self.lines[::-1])

    def __str__(self):
        return repr(self)

    def get_transformed(self) -> "Hexagram":
        return Hexagram(inner=self.inner.get_transformed(), outer=self.outer.get_transformed())

    @classmethod
    def from_lines(cls, lines: list[Line]) -> Self:
        return cls(inner=Trigram(lines=lines[:3]), outer=Trigram(lines=lines[3:]))

    @classmethod
    def from_binary(cls, lines: list[int]) -> Self:
        if len(lines) != 6:
            raise ValueError("Hexagram should have exactly 6 lines")
        return cls.from_lines(lines=[Line(status=LineStatus(i)) for i in lines])

    @classmethod
    def from_three_coins(cls) -> Self:
        """Create a new instance of the Hexagram class from tossing three coins six times (增删卜易).
        two heads:   lesser  yang  少阳
        one head:    lesser  yin   少阴
        zero head:   greater yang  太阳 (变爻)
        three heads: greater yin   太阴 (变爻)
        """
        # 0: tail, 1: head
        flip_results = [sum([1 - random.getrandbits(1) for _ in range(3)]) for _ in range(6)]
        lines = [Line(status=LineStatus(res)) for res in flip_results]
        return cls.from_lines(lines=lines)

    @classmethod
    def random(cls) -> Self:
        """Create a random  Hexagram instance. This will"""
        return cls.from_lines(lines=[Line.random() for _ in range(6)])

    @classmethod
    def from_yarrow_stalks(cls) -> Self:
        """Create a new instance of the Hexagram class from ... (蓍草起卦)."""
        # get_lines 6: old yin, 7: young yang, 8: young yin, 9: old yang
        # status    0: old yin, 1: young yang, 2: young yin, 3: old yang
        lines = [Line(status=LineStatus(cls.get_line() - 6)) for _ in range(6)]
        return cls.from_lines(lines=lines)

    @staticmethod
    def get_line() -> int:
        total = 50 - 1  # 大衍之数五十，其用四十有九
        remaining_stalks_1 = Hexagram.bian(total)
        assert remaining_stalks_1 in [40, 44]
        remaining_stalks_2 = Hexagram.bian(remaining_stalks_1)
        assert remaining_stalks_2 in [32, 36, 40]
        remaining_stalks_3 = Hexagram.bian(remaining_stalks_2)
        return remaining_stalks_3 // 4

    @staticmethod
    def bian(num: int) -> int:
        # Divide all stalks into 2 piles
        # 分而二以象两
        left = random.randint(1, num - 1)
        right = num - left

        # Subtract a single stalk from left hand and put between little finger and ring finger
        # 挂一以象三
        x = 1
        left -= 1

        # Get the remainder of the number of stalks in both piles divided by 4
        # 揲之以四以象四时
        y = min(left, 4) if left < 4 else (4 if left % 4 == 0 else left % 4)
        z = min(right, 4) if right < 4 else (4 if right % 4 == 0 else right % 4)
        return num - x - y - z


# %%
