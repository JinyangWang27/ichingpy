# %%
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
            self._yao = (
                Yao.random(),
                Yao.random(),
                Yao.random(),
                Yao.random(),
                Yao.random(),
                Yao.random(),
            )
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
