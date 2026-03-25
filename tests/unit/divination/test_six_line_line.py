import pytest

from ichingpy.enum import EarthlyBranch, HeavenlyStem
from ichingpy.enum.line_status import LineStatus
from ichingpy.model.interpretation.line.six_line_line import SixLineLineInterp
from ichingpy.model.sexagenary_cycle import SexagenaryCycle


def test_line_interpretation_repr():
    line_interp = SixLineLineInterp(status=LineStatus.CHANGING_YANG)
    assert repr(line_interp) == "----- O -> -- --"
    line_interp = SixLineLineInterp(status=LineStatus.CHANGING_YIN)
    assert repr(line_interp) == "-- -- X -> -----"


def test_line_interpretation_setters():
    line_interp = SixLineLineInterp(status=LineStatus.CHANGING_YANG)
    line_interp.stem = HeavenlyStem.Jia
    assert line_interp.stem == HeavenlyStem.Jia
    line_interp.branch = EarthlyBranch.Zi
    assert line_interp.branch == EarthlyBranch.Zi


def test_line_interpretation_repr_with_stem():
    line_interp = SixLineLineInterp(status=LineStatus.STATIC_YANG)
    line_interp.stem = HeavenlyStem.Jia
    assert repr(line_interp) == "甲 -----"
    line_interp.set_language("en")
    assert repr(line_interp) == "Jia  (1) -----"
    line_interp.set_language("zh")


def test_line_interpretation_repr_with_branch():
    line_interp = SixLineLineInterp(status=LineStatus.STATIC_YANG)
    line_interp.branch = EarthlyBranch.Zi
    assert repr(line_interp) == "子水 -----"
    line_interp.set_language("en")
    assert repr(line_interp) == "Zi   (1 ) WATER -----"
    line_interp.set_language("zh")


def test_line_interpretation_repr_with_both_stem_and_branch():
    line_interp = SixLineLineInterp(status=LineStatus.STATIC_YANG)
    line_interp.stem = HeavenlyStem.Jia
    line_interp.branch = EarthlyBranch.Zi
    assert repr(line_interp) == "甲 子水 -----"
    line_interp.set_language("en")
    assert repr(line_interp) == "Jia  (1) Zi   (1 ) WATER -----"
    line_interp.set_language("zh")


@pytest.mark.parametrize(
    "line_branch, day_pillar, expected",
    [
        # Day in 甲子旬 (甲子 itself) → void = 戌亥
        (EarthlyBranch.Xu,  SexagenaryCycle(HeavenlyStem.Jia, EarthlyBranch.Zi),  True),
        (EarthlyBranch.Hai, SexagenaryCycle(HeavenlyStem.Jia, EarthlyBranch.Zi),  True),
        (EarthlyBranch.Zi,  SexagenaryCycle(HeavenlyStem.Jia, EarthlyBranch.Zi),  False),
        # Day in 甲戌旬 (乙亥, non-旬首) → void = 申酉
        (EarthlyBranch.Shen, SexagenaryCycle(HeavenlyStem.Yi, EarthlyBranch.Hai), True),
        (EarthlyBranch.You,  SexagenaryCycle(HeavenlyStem.Yi, EarthlyBranch.Hai), True),
        (EarthlyBranch.Xu,   SexagenaryCycle(HeavenlyStem.Yi, EarthlyBranch.Hai), False),
    ],
)
def test_is_kong_wang(line_branch, day_pillar, expected):
    line = SixLineLineInterp(status=LineStatus.STATIC_YANG)
    line.branch = line_branch
    assert line.is_kong_wang(day_pillar) == expected
