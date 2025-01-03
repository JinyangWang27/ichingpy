from ichingpy.enum import HeavenlyStem
from ichingpy.model.hexagram import Hexagram, Trigram


def test_hexagram():
    hexagram = Hexagram.random()
    assert len(hexagram.lines) == 6


def test_hexagram_from_yarrow_stalks():
    hexagram = Hexagram.from_yarrow_stalks()
    assert len(hexagram.lines) == 6


def test_hexagram_from_three_coins():
    hexagram = Hexagram.from_three_coins()
    assert len(hexagram.lines) == 6


def test_hexagram_from_trigrams():
    inner = Trigram.random()
    outer = Trigram.random()
    hexagram = Hexagram(inner=inner, outer=outer)
    assert isinstance(hexagram, Hexagram)


def test_hexagram_inner_setter():
    gua = Hexagram.random()
    gua.inner.stem = HeavenlyStem.Jia
    gua.outer.stem = HeavenlyStem.Bing
    assert gua.inner.stem == [HeavenlyStem.Jia] * 3
    assert gua.outer.stem == [HeavenlyStem.Bing] * 3


def test_hexagram_transform():
    qian_zhi_gou = Hexagram.from_binary([3, 1, 1, 1, 1, 1])
    transformed = qian_zhi_gou.get_transformed()
    assert transformed.inner.name == "巽"
    assert transformed.outer.name == "乾"
