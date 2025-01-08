from ichingpy.divination import *
from ichingpy.enum import *
from ichingpy.model import *


def set_language(language: str):
    """Set the display language for the Line and SexagenaryCycle classes."""
    Line.set_language(language)
    SexagenaryCycle.set_language(language)


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
