from ichingpy.divination.iching import IChingDivinationEngine
from ichingpy.model.hexagram import Hexagram


def test_iching_divination():
    engine = IChingDivinationEngine()
    hexagram = Hexagram.from_binary([1, 1, 3, 1, 1, 3])
    engine = IChingDivinationEngine()
    engine.execute(hexagram)
    for line in hexagram.interpretation.lines:  # type: ignore
        assert isinstance(repr(line), str)  # type: ignore
