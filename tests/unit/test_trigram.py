import pytest

from ichingpy import HeavenlyStem
from ichingpy.model.line import Line
from ichingpy.model.trigram import Trigram


def test_trigram_random():
    assert isinstance(Trigram.random(), Trigram)


def test_trigram_raise_value_error_on_invalid_input():
    line = Line.random()
    with pytest.raises(ValueError):
        _ = Trigram(lines=[line, line, line, line])


def test_trigram_transform():
    qian_dynamic = Trigram.from_binary([3, 3, 3])
    transformed = qian_dynamic.get_transformed()
    assert transformed.name == "坤"


def test_trigram_raise_value_error_accessing_not_assigned_stem():
    trigram = Trigram.random()
    with pytest.raises(ValueError, match="Stems have not been assigned for all lines in the Trigram"):
        _ = trigram.stem


def test_trigram_raise_value_error_accessing_not_assigned_branch():
    trigram = Trigram.random()
    with pytest.raises(ValueError, match="Branches have not been assigned for all lines in the Trigram"):
        _ = trigram.branch


def test_trigram_raise_value_error_stem_not_same():
    trigram = Trigram.random()
    trigram.stem = HeavenlyStem.Jia
    trigram.lines[1].stem = HeavenlyStem.Bing
    with pytest.raises(ValueError, match="Stems of all lines in a Trigram should be the same"):
        _ = trigram.stem


def test_trigram_has_repr():
    trigram = Trigram.random()
    assert repr(trigram) == "\n".join(repr(line) for line in trigram.lines[::-1])
