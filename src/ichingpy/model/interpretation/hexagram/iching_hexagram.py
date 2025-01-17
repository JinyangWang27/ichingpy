from pydantic import field_validator

from ichingpy.model.interpretation.hexagram.base import HexagramInterpretationBase
from ichingpy.model.interpretation.line.iching_line import IChingLineInterp
from ichingpy.model.interpretation.trigram.iching_trigram import IChingTrigramInterp


class IChingHexagramInterp(HexagramInterpretationBase[IChingTrigramInterp, IChingLineInterp]):
    name: str
    text: str
    image: str
    lines: list[IChingLineInterp]
    use: IChingLineInterp | None = None

    @field_validator("lines", mode="before")
    @classmethod
    def create_trigram(cls, value: dict[str, dict[str, str]]) -> list[IChingLineInterp]:
        interp_list = [IChingLineInterp.model_validate(v) for v in value.values()]
        assert len(interp_list) == 6, "Hexagram must have 6 lines."
        return interp_list

    def get_lines(self) -> list[IChingLineInterp]:
        return self.lines

    # TODO: implement the following
    # 第一，凡卦的六爻皆不可变，就用筮得之卦的卦辞判断吉凶；
    # 第二，若筮得之卦（本卦）中有一爻可变，就用本卦的这一爻的爻辞判断吉凶；
    # 第三，本卦有二爻可变，用上一爻的爻辞为主来判断吉凶；
    # 第四，有三爻可变，则用本卦及之卦的卦辞相结合判断吉凶；
    # 第五，四爻可变，则用之卦中不变的二爻爻辞，并以下爻的爻辞为主来判断吉凶；
    # 第六，五爻可变，用之卦中不变的一爻爻辞判断吉凶；
    # 第七，六爻皆可变，乾坤二卦用“用爻”的爻辞判断吉凶，其他卦则用之卦的卦辞来判断吉凶。
    def __repr__(self) -> str:
        graph_repr = "\n".join(repr(line) for line in self.lines[::-1])
        text = ""
        for line in self.lines:
            if line.is_transform:
                text += f"{line.name} {line.text}\n"
        return f"{self.name}: {self.text}\n{self.image}\n{graph_repr}\n{text}"
