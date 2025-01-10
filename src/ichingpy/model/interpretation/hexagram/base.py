from typing import Generic, TypeVar

from ichingpy.model.interpretation.base import InterpretationBase
from ichingpy.model.interpretation.line.base import LineInterpretationBase
from ichingpy.model.interpretation.trigram.base import TrigramInterpretationBase

TTrigramInterp = TypeVar("TTrigramInterp", bound=TrigramInterpretationBase[LineInterpretationBase], covariant=True)


class HexagramInterpretationBase(InterpretationBase, Generic[TTrigramInterp]):

    inner: TTrigramInterp
    outer: TTrigramInterp

    @property
    def lines(self) -> list[LineInterpretationBase]:
        """Get the lines of the Hexagram.
        返回卦之六爻。
        """
        return self.inner.lines + self.outer.lines

    def __repr__(self) -> str:
        return "\n".join(repr(line) for line in self.lines[::-1])
