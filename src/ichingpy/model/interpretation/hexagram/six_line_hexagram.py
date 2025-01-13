from ichingpy.model.interpretation.hexagram.base import HexagramInterpretationBase
from ichingpy.model.interpretation.line.six_line_line import SixLineLineInterp
from ichingpy.model.interpretation.trigram.six_line_trigram import SixLineTrigramInterp


class SixLineHexagramInterp(HexagramInterpretationBase[SixLineTrigramInterp, SixLineLineInterp]):
    inner: SixLineTrigramInterp
    outer: SixLineTrigramInterp

    @property
    def lines(self) -> list[SixLineLineInterp]:
        """Get the lines of the Hexagram.
        返回卦之六爻。
        """
        return self.inner.lines + self.outer.lines

    def get_lines(self) -> list[SixLineLineInterp]:
        return self.lines

    def __repr__(self) -> str:
        return "\n".join(repr(line) for line in self.lines[::-1])
