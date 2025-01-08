import pytest

from ichingpy.enum import EarthlyBranch, HeavenlyStem
from ichingpy.enum.line_status import LineStatus
from ichingpy.model.line import Line, LineTransformationError


def test_line_setters():
    line = Line.random()
    line.stem = HeavenlyStem.Jia
    assert line.stem == HeavenlyStem.Jia
    line.branch = EarthlyBranch.Zi
    assert line.branch == EarthlyBranch.Zi


def test_line_transform_static_line_error():
    line = Line(status=LineStatus.STATIC_YANG)
    with pytest.raises(LineTransformationError):
        _ = line.get_transformed()


def test_line_repr_with_stem():
    line = Line(status=LineStatus.STATIC_YANG)
    line.stem = HeavenlyStem.Jia
    assert repr(line) == "甲 -----"
    line.set_language("en")
    assert repr(line) == "Jia  (1) -----"
    line.set_language("zh")


def test_line_repr_with_branch():
    line = Line(status=LineStatus.STATIC_YANG)
    line.branch = EarthlyBranch.Zi
    assert repr(line) == "子水 -----"
    line.set_language("en")
    assert repr(line) == "Zi   (1 ) WATER -----"
    line.set_language("zh")


def test_line_repr_with_both_stem_and_branch():
    line = Line(status=LineStatus.STATIC_YANG)
    line.stem = HeavenlyStem.Jia
    line.branch = EarthlyBranch.Zi
    assert repr(line) == "甲 子水 -----"
    line.set_language("en")
    assert repr(line) == "Jia  (1) Zi   (1 ) WATER -----"
    line.set_language("zh")


def test_changing_line_cannot_transform():
    line = Line(status=LineStatus.CHANGING_YANG)
    with pytest.raises(LineTransformationError):
        _ = line.transform()


def test_static_line_transform():
    line = Line(status=LineStatus.STATIC_YANG)
    assert line.transform().status == LineStatus.CHANGING_YANG

    line = Line(status=LineStatus.STATIC_YIN)
    assert line.transform().status == LineStatus.CHANGING_YIN
