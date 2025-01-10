from ichingpy.enum import EarthlyBranch, HeavenlyStem
from ichingpy.enum.line_status import LineStatus
from ichingpy.model.interpretation.line.six_line_line import SixLineLineInterp


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
