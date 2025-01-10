from ichingpy.enum.line_status import LineStatus
from ichingpy.model.interpretation.base import InterpretationBase


class LineInterpretationBase(InterpretationBase):

    status: LineStatus
