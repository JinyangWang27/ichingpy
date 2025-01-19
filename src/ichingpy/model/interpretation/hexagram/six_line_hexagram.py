from ichingpy.enum.palace import Palace
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

    @property
    def transformed(self) -> "SixLineHexagramInterp":
        if hasattr(self, "_transformed"):
            return self._transformed
        raise AttributeError("Transformed Hexagram interpretation not set.")

    @transformed.setter
    def transformed(self, value: "SixLineHexagramInterp"):
        self._transformed = value

    @property
    def palace(self) -> Palace:
        """Get the palace of the Hexagram."""
        inner = self.inner.palace.value
        outer = self.outer.palace.value
        if {inner, outer} in [{1, 3}, {2, 4}, {5, 7}, {6, 8}]:
            # 归魂卦
            return self.inner.palace
        elif inner % 2 == outer % 2:
            # 内外同奇偶 属外卦的卦宫
            return self.outer.palace
        else:
            # 内外异奇偶：属内卦错卦的卦宫
            return self.inner.opposite.palace
