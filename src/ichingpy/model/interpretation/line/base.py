from typing import ClassVar

from ichingpy.enum.language import Language
from ichingpy.enum.line_status import LineStatus
from ichingpy.model.interpretation.base import InterpretationBase


class LineInterpretationBase(InterpretationBase):
    display_language: ClassVar[Language] = Language.CHINESE
    status: LineStatus

    @classmethod
    def set_language(cls, language: str):
        """Set the display language for the Line class."""
        cls.display_language = Language(language)
