import pytest

from yi.enum import EarthlyBranch, HeavenlyStem
from yi.enum.line_status import LineStatus
from yi.model.line import Line, LineTransformationError


@pytest.mark.parametrize(
    "status, representation",
    [
        (LineStatus.STATIC_YANG, "-----"),
        (LineStatus.STATIC_YIN, "-- --"),
        (LineStatus.CHANGING_YANG, "----- O -> -- --"),
        (LineStatus.CHANGING_YIN, "-- -- X -> -----"),
    ],
)
def test_line(status: LineStatus, representation: str):
    assert repr(Line(status=status)) == representation


def test_line_setters():
    line = Line.random()
    line.stem = HeavenlyStem.Jia
    assert line.stem == HeavenlyStem.Jia
    line.branch = EarthlyBranch.Zi
    assert line.branch == EarthlyBranch.Zi


@pytest.mark.parametrize(
    "status, transformed_status",
    [(LineStatus.CHANGING_YANG, LineStatus.STATIC_YIN), (LineStatus.CHANGING_YIN, LineStatus.STATIC_YANG)],
)
def test_line_transform(status: LineStatus, transformed_status: LineStatus):
    line = Line(status=status)
    assert line.is_transform == True
    assert line.get_transformed().status is transformed_status


def test_line_transform_static_line_error():
    line = Line(status=LineStatus.STATIC_YANG)
    with pytest.raises(LineTransformationError):
        _ = line.get_transformed()
