# %%
import random
from typing import Self

from yi.model.yao import Yao


class Trigram:

    NAME_MAP: dict[tuple[int, int, int], str] = {
        (1, 1, 1): "乾",
        (1, 1, 0): "兑",
        (1, 0, 1): "离",
        (1, 0, 0): "震",
        (0, 1, 1): "巽",
        (0, 1, 0): "坎",
        (0, 0, 1): "艮",
        (0, 0, 0): "坤",
    }

    def __init__(self, yao: tuple[int, int, int] | None = None):

        if yao is None:
            self._yao = (Yao.random(), Yao.random(), Yao.random())
        elif len(yao) == 3:
            self._yao = (Yao(yao[0]), Yao(yao[1]), Yao(yao[2]))
        else:
            raise ValueError(f"Invalid input {yao}")

    def __repr__(self):
        return "\n".join(repr(yao) for yao in self.yao[::-1])

    @property
    def yao(self) -> tuple[Yao, Yao, Yao]:
        return self._yao

    @property
    def name(self) -> str:
        yao_int = [int(yao.value) for yao in self.yao]
        return self.NAME_MAP[(yao_int[0], yao_int[1], yao_int[2])]


class Hexagram:

    def __init__(self, yao: tuple[Yao, Yao, Yao, Yao, Yao, Yao] | None = None):
        if yao is None:
            self._yao = self.from_three_coins().yao
        elif len(yao) == 6:
            self._yao = (Yao(yao[0]), Yao(yao[1]), Yao(yao[2]), Yao(yao[3]), Yao(yao[4]), Yao(yao[5]))
        else:
            raise ValueError(f"Invalid input {yao}")

    def __repr__(self):
        return "\n".join(repr(yao) for yao in self.yao[::-1])

    @property
    def yao(self) -> tuple[Yao, Yao, Yao, Yao, Yao, Yao]:
        return self._yao

    @property
    def inner(self) -> Trigram:
        return Trigram(self.yao[:3])

    @property
    def outer(self) -> Trigram:
        return Trigram(self.yao[3:])

    @classmethod
    def from_trigram(cls, trigram_inner: Trigram, trigram_outer: Trigram) -> "Hexagram":
        inner_yaos = trigram_inner.yao
        outer_yaos = trigram_outer.yao
        return cls(inner_yaos + outer_yaos)

    @classmethod
    def from_three_coins(cls) -> Self:
        """Create a new instance of the Hexagram class from tossing three coins six times (增删卜易).
        two heads:   lesser  yang  少阳
        one head:    lesser  yin   少阴
        zero head:   greater yang  太阳 (变爻)
        three heads: greater yin   太阴 (变爻)
        """
        six_yaos: list[Yao] = []
        for _ in range(6):
            flip_result = sum((random.getrandbits(1), random.getrandbits(1), random.getrandbits(1)))
            if flip_result in [0, 2]:
                yao = Yao.Yang
            elif flip_result in [1, 3]:
                yao = Yao.Yin
            else:
                raise ValueError(f"Invalid flip result {flip_result}")  # should not enter here

            if flip_result in [0, 3]:
                yao.is_transform = True
            else:
                yao.is_transform = False
            six_yaos.append(yao)
        assert len(six_yaos) == 6
        return cls((six_yaos[0], six_yaos[1], six_yaos[2], six_yaos[3], six_yaos[4], six_yaos[5]))

    @classmethod
    def from_shi_cao(cls) -> Self:
        """Create a new instance of the Hexagram class from ... (蓍草起卦)."""

        yao_list = [cls.get_yao() for _ in range(6)]
        six_yaos: list[Yao] = []
        for result in yao_list:
            if result in [7, 9]:
                yao = Yao.Yang
            elif result in [6, 8]:
                yao = Yao.Yin
            else:
                raise ValueError(f"Invalid result {result}")

            yao.is_transform = True if result in [6, 9] else False
            six_yaos.append(yao)
        assert len(six_yaos) == 6
        return cls((six_yaos[0], six_yaos[1], six_yaos[2], six_yaos[3], six_yaos[4], six_yaos[5]))

    @staticmethod
    def get_yao() -> int:
        total = 50 - 1  # 大衍之数五十，其用四十有九
        yu_ce_1 = Hexagram.bian(total)
        yu_ce_2 = Hexagram.bian(yu_ce_1)
        yu_ce_3 = Hexagram.bian(yu_ce_2)
        return yu_ce_3 // 4

    @staticmethod
    def bian(num: int) -> int:
        # 分而二以象两
        left = random.randint(1, num - 1)
        right = num - left

        # 挂一以象三
        x = 1
        left -= 1

        # 揲之以四以象四时
        if left < 4:
            y = left
        else:
            y = 4 if left % 4 == 0 else left % 4

        if right < 4:
            z = right
        else:
            if right % 4 == 0:
                z = 4
            else:
                z = right % 4

        ce = x + y + z
        return num - ce
