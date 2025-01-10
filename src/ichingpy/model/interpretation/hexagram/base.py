from typing import Generic, TypeVar

from ichingpy.model.interpretation.base import InterpretationBase
from ichingpy.model.interpretation.line.base import LineInterpretationBase
from ichingpy.model.interpretation.trigram.base import TrigramInterpretationBase

TTrigramInterp = TypeVar("TTrigramInterp", bound=TrigramInterpretationBase[LineInterpretationBase], covariant=True)


class HexagramInterpretationBase(InterpretationBase, Generic[TTrigramInterp]):

    inner: TTrigramInterp
    outer: TTrigramInterp

    def __repr__(self):
        return ""
