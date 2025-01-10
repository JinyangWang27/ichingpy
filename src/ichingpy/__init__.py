from ichingpy.divination import *
from ichingpy.enum import *
from ichingpy.model import *
from ichingpy.model.interpretation.line.six_line_line import SixLineLineInterp


def set_language(language: str):
    """Set the display language for the Line and SexagenaryCycle classes."""
    SexagenaryCycle.set_language(language)
    SixLineLineInterp.set_language(language)


__all__ = [
    "Line",
    "LineStatus",
    "HeavenlyStem",
    "EarthlyBranch",
    "Hexagram",
    "Trigram",
    "SexagenaryCycle",
    "SixLinesDivinationEngine",
    "FourPillars",
    "set_language",
]
