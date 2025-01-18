from pydantic import field_validator

from ichingpy.model.interpretation.hexagram.base import HexagramInterpretationBase
from ichingpy.model.interpretation.line.iching_line import IChingLineInterp
from ichingpy.model.interpretation.trigram.iching_trigram import IChingTrigramInterp


class IChingHexagramInterp(HexagramInterpretationBase[IChingTrigramInterp, IChingLineInterp]):
    name: str
    text: str
    image: str
    lines: list[IChingLineInterp]
    use: IChingLineInterp | None = None  # 乾用九，坤用六

    @field_validator("lines", mode="before")
    @classmethod
    def create_trigram(cls, value: dict[str, dict[str, str]]) -> list[IChingLineInterp]:
        interp_list = [IChingLineInterp.model_validate(v) for v in value.values()]
        assert len(interp_list) == 6, "Hexagram must have 6 lines."
        return interp_list

    def get_lines(self) -> list[IChingLineInterp]:
        return self.lines

    def __repr__(self) -> str:
        hexagram_names = f"{self.name} -> {self.transformed.name}" if self.name != self.transformed.name else self.name
        graph_repr = "\n".join(repr(line) for line in self.lines[::-1])
        text = ""
        for line in self.lines:
            if line.is_transform:
                text += f"{line.name} {line.text}\n"
        return f"{hexagram_names}\n{self.text}\n{self.image}\n{graph_repr}\n{text}"

    def get_judgement(self) -> str:
        judgement = ""
        number_of_transformed_lines = sum(1 for line in self.lines if line.is_transform)

        # 凡卦的六爻皆不可变，就用筮得之卦的卦辞判断吉凶；
        if number_of_transformed_lines == 0:
            judgement = self.text

        # 若筮得之卦（本卦）中有一爻可变，就用本卦的这一爻的爻辞判断吉凶；
        if number_of_transformed_lines == 1:
            judgement = next(line.text for line in self.lines if line.is_transform)

        # 本卦有二爻可变，用上一爻的爻辞为主来判断吉凶；
        if number_of_transformed_lines == 2:
            text = [line.text for line in self.lines if not line.is_transform]
            judgement = f"{text[0]}\n{text[1]}"

        # 三爻可变，则用本卦及之卦的卦辞相结合判断吉凶；
        if number_of_transformed_lines == 3:
            judgement = f"{self.text}\n{self.transformed.text}"

        # 四爻可变，则用之卦中不变的二爻爻辞，并以下爻的爻辞为主来判断吉凶；
        if number_of_transformed_lines == 4:
            text = [line.text for line in self.transformed.lines if not line.is_transform]
            judgement = f"{text[1]}\n{text[0]}"

        # 五爻可变，用之卦中不变的一爻爻辞判断吉凶；
        if number_of_transformed_lines == 5:
            text = [line.text for line in self.transformed.lines if not line.is_transform]
            judgement = text[0]

        # 六爻皆可变
        if number_of_transformed_lines == 6:

            # 乾坤二卦用“用爻”的爻辞判断吉凶
            if all(line.is_yang for line in self.lines) or all(line.is_yin for line in self.lines):
                assert self.use is not None
                judgement = self.use.text
            else:  # 其他卦则用之卦的卦辞来判断吉凶
                judgement = self.transformed.text
            judgement = self.use.text if self.use is not None else self.text

        return judgement

    @property
    def transformed(self) -> "IChingHexagramInterp":
        if hasattr(self, "_transformed"):
            return self._transformed
        raise AttributeError("Transformed Hexagram interpretation not set.")

    @transformed.setter
    def transformed(self, value: "IChingHexagramInterp"):
        self._transformed = value
