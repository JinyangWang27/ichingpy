import pytest

from yi.model.hexagram import Hexagram, Trigram, Yao
from yi.model.stem_branch import EarthlyBranch, HeavenlyStem


def test_yao():
    yao = Yao.random()
    assert yao.value in [0, 1]

    assert repr(Yao.Yin) == "▅▅  ▅▅"
    assert repr(Yao.Yang) == "▅▅▅▅▅▅"


def test_yao_setters():
    yao = Yao.random()
    yao.stem = HeavenlyStem.Jia
    assert yao.stem == HeavenlyStem.Jia
    yao.branch = EarthlyBranch.Zi
    assert yao.branch == EarthlyBranch.Zi


def test_yao_transform():
    yao = Yao.random()
    assert yao.transform().value == 1 - yao.value


@pytest.mark.parametrize(
    "yao, name, symbol",
    [
        ((1, 1, 1), "乾", "▅▅▅▅▅▅\n▅▅▅▅▅▅\n▅▅▅▅▅▅"),
        ((1, 1, 0), "兑", "▅▅  ▅▅\n▅▅▅▅▅▅\n▅▅▅▅▅▅"),
        ((1, 0, 1), "离", "▅▅▅▅▅▅\n▅▅  ▅▅\n▅▅▅▅▅▅"),
        ((1, 0, 0), "震", "▅▅  ▅▅\n▅▅  ▅▅\n▅▅▅▅▅▅"),
        ((0, 1, 1), "巽", "▅▅▅▅▅▅\n▅▅▅▅▅▅\n▅▅  ▅▅"),
        ((0, 1, 0), "坎", "▅▅  ▅▅\n▅▅▅▅▅▅\n▅▅  ▅▅"),
        ((0, 0, 1), "艮", "▅▅▅▅▅▅\n▅▅  ▅▅\n▅▅  ▅▅"),
        ((0, 0, 0), "坤", "▅▅  ▅▅\n▅▅  ▅▅\n▅▅  ▅▅"),
    ],
)
def test_trigram(yao: tuple[int, int, int], name: str, symbol: str):
    trigram = Trigram(yao)
    assert len(trigram.yao) == 3
    assert trigram.name == name
    assert repr(trigram) == symbol


def test_trigram_random():
    assert isinstance(Trigram(), Trigram)


def test_Trigram_raise_value_error_on_invalid_input():
    with pytest.raises(ValueError):
        _ = Trigram([1, 1, 1, 1])  # type: ignore


def test_hexagram():
    hexagram = Hexagram()
    assert len(hexagram.yao) == 6
    assert isinstance(hexagram.inner, Trigram)
    assert isinstance(hexagram.outer, Trigram)