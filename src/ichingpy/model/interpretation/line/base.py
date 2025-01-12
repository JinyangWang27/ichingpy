from typing import ClassVar

from ichingpy.enum.language import Language
from ichingpy.enum.line_status import LineStatus
from ichingpy.model.interpretation.base import InterpretationBase


class LineInterpretationBase(InterpretationBase):
    display_language: ClassVar[Language] = Language.CHINESE
    status: LineStatus

    @property
    def is_yang(self) -> bool:
        """bool: Whether the Yao is a solid line (阳爻)"""
        return True if self.status in [LineStatus.STATIC_YANG, LineStatus.CHANGING_YANG] else False

    @property
    def is_yin(self) -> bool:
        """bool: Whether the Yao is a broken line (阴爻)"""
        return True if self.status in [LineStatus.STATIC_YIN, LineStatus.CHANGING_YIN] else False

    @property
    def is_transform(self) -> bool:
        """bool: Whether the Yao needs to be transformed (变爻)"""
        return True if self.status in [LineStatus.CHANGING_YIN, LineStatus.CHANGING_YANG] else False

    @classmethod
    def set_language(cls, language: str):
        """Set the display language for the Line class."""
        cls.display_language = Language(language)
