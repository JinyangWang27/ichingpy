import pytest

from ichingpy.enum.language import Language
from ichingpy.enum.line_status import LineStatus
from ichingpy.model.line import Line


@pytest.mark.parametrize(
    "status, representation",
    [
        (LineStatus.STATIC_YANG, "-----"),
        (LineStatus.STATIC_YIN, "-- --"),
        (LineStatus.CHANGING_YANG, "----- O -> -- --"),
        (LineStatus.CHANGING_YIN, "-- -- X -> -----"),
    ],
)
def test_line_representation(status: LineStatus, representation: str):
    assert repr(Line(status=status)) == representation


@pytest.mark.parametrize(
    "status, transformed_status",
    [(LineStatus.CHANGING_YANG, LineStatus.STATIC_YIN), (LineStatus.CHANGING_YIN, LineStatus.STATIC_YANG)],
)
def test_line_transform(status: LineStatus, transformed_status: LineStatus):
    line = Line(status=status)
    assert line.is_transform == True
    assert line.get_transformed().status is transformed_status


def test_line_display_language_setter():
    assert Line.display_language == Language.CHINESE
    import ichingpy as icp

    icp.set_language("en")
    assert icp.Line.display_language == Language.ENGLISH
    icp.set_language("zh")
