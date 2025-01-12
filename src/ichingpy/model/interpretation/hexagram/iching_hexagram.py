from pydantic import field_validator

from ichingpy.model.interpretation.hexagram.base import HexagramInterpretationBase
from ichingpy.model.interpretation.line.base import LineInterpretationBase
from ichingpy.model.interpretation.line.iching_line import IChingLineInterp
from ichingpy.model.interpretation.trigram.iching_trigram import IChingTrigramInterp


class IChingHexagramInterp(HexagramInterpretationBase[IChingTrigramInterp]):
    name: str
    image: str
    lines: list[IChingLineInterp]
    use: IChingLineInterp | None = None

    @field_validator("lines", mode="before")
    @classmethod
    def create_trigram(cls, value: dict[str, dict[str, str]]) -> list[IChingLineInterp]:
        interp_list = [IChingLineInterp.model_validate(v) for v in value.values()]
        assert len(interp_list) == 6, "Hexagram must have 6 lines."
        return interp_list

    def get_lines(self) -> list[LineInterpretationBase]:
        # fix generic type
        return self.lines  # type: ignore

    def __repr__(self) -> str:
        graph_repr = "\n".join(repr(line) for line in self.lines[::-1])
        text = ""
        for line in self.lines:
            if line.is_transform:
                text += f"{line.name} {line.text}\n"
        return f"{self.name} {self.image}\n{graph_repr}\n{text}"
