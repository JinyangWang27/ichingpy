import pytest

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


def test_trigram_has_repr():
    trigram = Trigram.random()
    assert repr(trigram) == "\n".join(repr(line) for line in trigram.lines[::-1])
