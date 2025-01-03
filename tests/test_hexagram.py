from yi.enum import HeavenlyStem
from yi.model.hexagram import Hexagram, Trigram


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


def test_hexagram_correct_range_of_line_number():
    results: list[int] = []
    for _ in range(100):
        yu_ce_1 = Hexagram.bian(49)
        yu_ce_2 = Hexagram.bian(yu_ce_1)
        yu_ce_3 = Hexagram.bian(yu_ce_2)
        results.append(yu_ce_3 // 4)
    assert max(results) == 9
    assert min(results) == 6


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
