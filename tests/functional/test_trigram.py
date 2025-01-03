import pytest

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
