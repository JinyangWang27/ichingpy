from itertools import product

import pytest

from ichingpy.divination.iching import IChingDivinationEngine
from ichingpy.model.hexagram import Hexagram


@pytest.mark.parametrize("hexagram_int", product([0, 1], repeat=6))
def test_iching_divination(hexagram_int: list[int]):
    engine = IChingDivinationEngine()
    hexagram = Hexagram.from_binary(hexagram_int)
    engine = IChingDivinationEngine()
    engine.execute(hexagram)
    assert hexagram.interpretation is not None
    for line in hexagram.interpretation.get_lines():
        assert isinstance(repr(line), str)
    assert isinstance(repr(hexagram.interpretation), str)
