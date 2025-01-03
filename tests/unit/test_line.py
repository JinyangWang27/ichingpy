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