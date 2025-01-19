import pytest

from ichingpy.model.interpretation.line.six_line_line import SixLineLineInterp
from ichingpy.model.interpretation.trigram.six_line_trigram import SixLineTrigramInterp
from ichingpy.model.trigram import Trigram


@pytest.mark.parametrize(
    "line_value",
    [
        ([1, 1, 1]),
        ([1, 1, 0]),
        ([1, 0, 1]),
        ([1, 0, 0]),
        ([0, 1, 1]),
        ([0, 1, 0]),
        ([0, 0, 1]),
        ([0, 0, 0]),
    ],
)
def test_six_line_trigram_opposite(line_value: list[int]):
    trigram = Trigram.from_binary(line_value)

    interp = SixLineTrigramInterp(lines=[SixLineLineInterp(status=line.status) for line in trigram.lines])

    opposite_interp = interp.opposite
    for line, opposite_line in zip(interp.lines, opposite_interp.lines):
        assert line.status.opposite == opposite_line.status
