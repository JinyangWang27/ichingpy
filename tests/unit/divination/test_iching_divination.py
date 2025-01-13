from ichingpy.divination.iching import IChingDivinationEngine
from ichingpy.model.hexagram import Hexagram


def test_iching_divination():
    engine = IChingDivinationEngine()
    hexagram = Hexagram.from_binary([1, 1, 3, 1, 1, 3])
    engine = IChingDivinationEngine()
    engine.execute(hexagram)
    assert hexagram.interpretation is not None
    for line in hexagram.interpretation.get_lines():
        assert isinstance(repr(line), str)
    assert isinstance(repr(hexagram.interpretation), str)
