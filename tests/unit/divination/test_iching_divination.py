from itertools import product

import pytest

from ichingpy.divination.iching import IChingDivinationEngine
from ichingpy.model.hexagram import Hexagram
from ichingpy.model.interpretation.hexagram.iching_hexagram import IChingHexagramInterp


@pytest.fixture
def hexagram() -> Hexagram:
    hexagram = Hexagram.from_three_coins()
    engine = IChingDivinationEngine()
    engine.execute(hexagram)
    return hexagram


@pytest.mark.parametrize("hexagram_int", product([0, 1], repeat=6))
def test_iching_divination(hexagram_int: list[int]):
    engine = IChingDivinationEngine()
    hexagram = Hexagram.from_binary(hexagram_int)
    engine = IChingDivinationEngine()
    engine.execute(hexagram)
    assert isinstance(hexagram.interpretation, IChingHexagramInterp)
    for line in hexagram.interpretation.get_lines():
        assert isinstance(repr(line), str)
    assert isinstance(repr(hexagram.interpretation), str)
    assert isinstance(hexagram.interpretation.get_judgement(), str)


def test_transformed_hexagram_has_interp(hexagram: Hexagram):
    assert hexagram.interpretation is not None
    assert isinstance(hexagram.interpretation.transformed, IChingHexagramInterp)


def test_iching_hexagram_interp_has_same_line_status(hexagram: Hexagram):
    assert hexagram.interpretation is not None
    assert all(hexagram.interpretation.get_lines()[i].status == hexagram.lines[i].status for i in range(6))
