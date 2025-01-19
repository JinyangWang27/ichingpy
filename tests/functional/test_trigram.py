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


@pytest.mark.parametrize(
    "line, name, number",
    [
        ([1, 1, 1], "乾", 1),
        ([1, 1, 0], "兑", 2),
        ([1, 0, 1], "离", 3),
        ([1, 0, 0], "震", 4),
        ([0, 1, 1], "巽", 5),
        ([0, 1, 0], "坎", 6),
        ([0, 0, 1], "艮", 7),
        ([0, 0, 0], "坤", 8),
    ],
)
def test_pre_trigram_number(line: list[int], name: str, number: int):
    trigram = Trigram.from_binary(line)
    assert trigram.pre_trigram_number == number

    # test alternative constructor
    trigram = Trigram.from_pre_trigram_number(number)
    assert trigram.name == name
