from typing import ClassVar, Self

from pydantic import BaseModel, field_validator

from yi.enum.line_status import LineStatus
from yi.model.line import Line
from yi.model.stem_branch import HeavenlyStem


class Trigram(BaseModel):
    """A Trigram (卦) in the I Ching"""

    # 0: changing yin, 1: static yang, 2: static yin, 3: changing yang
    NAME_MAP: ClassVar[dict[tuple[int, int, int], str]] = {
        (1, 1, 1): "乾",
        (1, 1, 0): "兑",
        (1, 0, 1): "离",
        (1, 0, 0): "震",
        (0, 1, 1): "巽",
        (0, 1, 0): "坎",
        (0, 0, 1): "艮",
        (0, 0, 0): "坤",
    }

    lines: list[Line]

    @field_validator("lines", mode="before")
    @classmethod
    def validate_line_length(cls, lines: list[Line]) -> list[Line]:
        if len(lines) != 3:
            raise ValueError("Trigram should have exactly 3 lines")
        return lines

    @property
    def value(self) -> list[int]:
        return [line.value for line in self.lines]

    @property
    def name(self) -> str:
        # 0: changing yin, 1: static yang, 2: static yin, 3: changing yang
        return self.NAME_MAP[(self.value[0] % 2, self.value[1] % 2, self.value[2] % 2)]

    @property
    def stem(self) -> list[HeavenlyStem]:
        if not all(hasattr(line, "_stem") for line in self.lines):
            raise ValueError("Stems have not been loaded for all lines in the Trigram")
        if not all(self.lines[0].stem == line.stem for line in self.lines):
            raise ValueError("Stems of all lines in a Trigram should be the same")
        return [line.stem for line in self.lines]

    def get_transformed(self) -> "Trigram":
        transformed_lines = [line.get_transformed() if line.is_transform else line for line in self.lines]
        return Trigram(lines=transformed_lines)

    @classmethod
    def from_binary(cls, lines: list[int]) -> Self:
        assert len(lines) == 3
        return cls(lines=[Line(status=LineStatus(i)) for i in lines])

    @classmethod
    def random(cls) -> Self:
        return cls(lines=[Line.random() for _ in range(3)])

    @stem.setter
    def stem(self, value: HeavenlyStem):
        self.lines[0].stem = value
        self.lines[1].stem = value
        self.lines[2].stem = value

    def __repr__(self):
        return "\n".join(repr(line) for line in self.lines[::-1])
