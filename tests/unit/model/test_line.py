import pytest

from ichingpy.enum.line_status import LineStatus
from ichingpy.model.line import Line, LineTransformationError


def test_line_transform_static_line_error():
    line = Line(status=LineStatus.STATIC_YANG)
    with pytest.raises(LineTransformationError):
        _ = line.get_transformed()


def test_changing_line_cannot_transform():
    line = Line(status=LineStatus.CHANGING_YANG)
    with pytest.raises(LineTransformationError):
        _ = line.transform()


def test_static_line_transform():
    line = Line(status=LineStatus.STATIC_YANG)
    assert line.transform().status == LineStatus.CHANGING_YANG

    line = Line(status=LineStatus.STATIC_YIN)
    assert line.transform().status == LineStatus.CHANGING_YIN
