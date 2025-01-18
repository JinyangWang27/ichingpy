from ichingpy.divination.six_lines import SixLinesDivinationEngine
from ichingpy.model.hexagram import Hexagram
from ichingpy.model.interpretation.hexagram.six_line_hexagram import SixLineHexagramInterp


def test_six_line_divination_interp_has_transformed():
    hexagram = Hexagram.random()
    engine = SixLinesDivinationEngine()
    engine.execute(hexagram)
    assert isinstance(hexagram.interpretation, SixLineHexagramInterp)
    assert isinstance(hexagram.interpretation.transformed, SixLineHexagramInterp)
