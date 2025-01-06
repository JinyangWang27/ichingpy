import random
from datetime import datetime
from typing import Self

from pydantic import BaseModel

from ichingpy.enum.line_status import LineStatus
from ichingpy.model.four_pillars import FourPillars
from ichingpy.model.line import Line
from ichingpy.model.trigram import Trigram


class Hexagram(BaseModel):
    """A Hexagram (64卦之一) consists of an inner Trigram (内卦) and an outer Trigram (外卦)."""

    inner: Trigram
    outer: Trigram

    @property
    def lines(self) -> list[Line]:
        """Get the lines of the Hexagram.
        返回卦之六爻。
        """
        return self.inner.lines + self.outer.lines

    def __repr__(self):
        return "\n".join(repr(line) for line in self.lines[::-1])

    def __str__(self):
        return repr(self)

    def get_transformed(self) -> "Hexagram":
        """Get the transformed Hexagram (变卦)."""
        return Hexagram(inner=self.inner.get_transformed(), outer=self.outer.get_transformed())

    @classmethod
    def from_lines(cls, lines: list[Line]) -> Self:
        """Create a new instance of the Hexagram class from a list of Lines."""
        return cls(inner=Trigram(lines=lines[:3]), outer=Trigram(lines=lines[3:]))

    @classmethod
    def from_binary(cls, lines: list[int]) -> Self:
        """Create a new instance of the Hexagram class from a list of binary integers."""
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
    def from_datetime(cls, dt: datetime) -> Self:
        """Create a new instance of the Hexagram class from a datetime object.
        八字起卦：
        1. 年月日三支之和除以8取余为外卦之数，余数0作8
        2. 年月日时四支之和除以8取余为内卦之数，余数0作8
        3. 年月日时四支之和除以6取余为变爻之数，余数0作6
        """
        four_pillars = FourPillars.from_datetime(dt)
        year = four_pillars.year.branch.value
        month = four_pillars.month.branch.value
        day = four_pillars.day.branch.value
        hour = four_pillars.hour.branch.value

        remainder_ymd = (year + month + day) % 8
        remainder_ymd = 8 if remainder_ymd == 0 else remainder_ymd

        remainder_ymdh = (year + month + day + hour) % 8
        remainder_ymdh = 8 if remainder_ymdh == 0 else remainder_ymdh

        outer_trigram_lines = Trigram.from_pre_trigram_number(remainder_ymd).lines
        inner_trigram_lines = Trigram.from_pre_trigram_number(remainder_ymdh).lines
        lines = inner_trigram_lines + outer_trigram_lines

        line_to_transform_int = (year + month + day + hour) % 6
        if line_to_transform_int == 0:
            line_to_transform_int = 6
        line_to_transform_int -= 1
        lines[line_to_transform_int] = lines[line_to_transform_int].transform()
        return cls.from_lines(lines=lines)

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
