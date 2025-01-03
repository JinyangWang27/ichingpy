import pytest

from ichingpy.model.line import Line
from ichingpy.model.trigram import Trigram


@pytest.mark.parametrize(
    "line, name",
    [
        ([1, 1, 1], "乾"),
        ([1, 1, 0], "兑"),
        ([1, 0, 1], "离"),
        ([1, 0, 0], "震"),
        ([0, 1, 1], "巽"),
        ([0, 1, 0], "坎"),
        ([0, 0, 1], "艮"),
        ([0, 0, 0], "坤"),
    ],
)
def test_trigram(line: list[int], name: str):
    trigram = Trigram.from_binary(line)
    assert len(trigram.lines) == 3
    assert trigram.name == name


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
