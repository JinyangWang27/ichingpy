import pytest

from ichingpy.enum.palace import Palace
from ichingpy.model.interpretation.hexagram.six_line_hexagram import SixLineHexagramInterp
from ichingpy.model.interpretation.line.six_line_line import SixLineLineInterp
from ichingpy.model.interpretation.trigram.six_line_trigram import SixLineTrigramInterp
from ichingpy.model.trigram import Trigram


@pytest.mark.parametrize(
    "values, palace",
    [
        ([1, 1, 1, 1, 1, 1], Palace.HEAVEN),
        ([1, 1, 0, 1, 1, 0], Palace.LAKE),
        ([1, 0, 1, 1, 0, 1], Palace.FIRE),
        ([1, 0, 0, 1, 0, 0], Palace.THUNDER),
        ([0, 1, 1, 0, 1, 1], Palace.WIND),
        ([0, 1, 0, 0, 1, 0], Palace.WATER),
        ([0, 0, 1, 0, 0, 1], Palace.MOUNTAIN),
        ([0, 0, 0, 0, 0, 0], Palace.EARTH),
        # 归魂卦
        ([1, 1, 1, 1, 0, 1], Palace.HEAVEN),
        ([1, 0, 0, 1, 1, 0], Palace.THUNDER),
        ([0, 1, 0, 0, 0, 0], Palace.WATER),
        ([0, 0, 1, 0, 1, 1], Palace.MOUNTAIN),
    ],
)
def test_get_palace(values: list[int], palace: Palace):
    inner_trigram = Trigram.from_binary(values[:3])
    outer_trigram = Trigram.from_binary(values[3:])
    inner_interp = SixLineTrigramInterp(lines=[SixLineLineInterp(status=line.status) for line in inner_trigram.lines])
    outer_interp = SixLineTrigramInterp(lines=[SixLineLineInterp(status=line.status) for line in outer_trigram.lines])
    hexagram_interp = SixLineHexagramInterp(inner=inner_interp, outer=outer_interp)
    assert hexagram_interp.palace == palace
