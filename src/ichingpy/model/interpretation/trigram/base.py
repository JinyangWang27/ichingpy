from typing import Generic, TypeVar

from ichingpy.enum.branch import EarthlyBranch
from ichingpy.enum.stem import HeavenlyStem
from ichingpy.model.interpretation.base import InterpretationBase
from ichingpy.model.interpretation.line.base import LineInterpretationBase

TLineInterp = TypeVar("TLineInterp", bound=LineInterpretationBase, covariant=True)


class TrigramInterpretationBase(InterpretationBase, Generic[TLineInterp]):

    lines: list[TLineInterp]

    def __repr__(self):
        return "\n".join(repr(line) for line in self.lines[::-1])

    @property
    def value(self) -> list[int]:
        return [line.status.value for line in self.lines]

    @property
    def stem(self) -> list[HeavenlyStem]: ...

    @property
    def branch(self) -> list[EarthlyBranch]: ...
