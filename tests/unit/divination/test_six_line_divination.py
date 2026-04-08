import pytest

from ichingpy.divination.six_lines import SixLinesDivinationEngine
from ichingpy.enum import HeavenlyStem
from ichingpy.enum.six_spirit import SixSpirit
from ichingpy.model.hexagram import Hexagram
from ichingpy.model.interpretation.hexagram.six_line_hexagram import SixLineHexagramInterp


def test_six_line_divination_interp_has_transformed():
    hexagram = Hexagram.random()
    engine = SixLinesDivinationEngine()
    engine.execute(hexagram)
    assert isinstance(hexagram.interpretation, SixLineHexagramInterp)
    assert isinstance(hexagram.interpretation.transformed, SixLineHexagramInterp)


@pytest.mark.parametrize(
    "stem, expected_spirit",
    [
        (HeavenlyStem.Jia, SixSpirit.AZURE_DRAGON),
        (HeavenlyStem.Yi, SixSpirit.AZURE_DRAGON),
        (HeavenlyStem.Bing, SixSpirit.VERMILION_BIRD),
        (HeavenlyStem.Ding, SixSpirit.VERMILION_BIRD),
        (HeavenlyStem.Wu, SixSpirit.HOOK_KIRIN),
        (HeavenlyStem.Ji, SixSpirit.FLYING_SNAKE),
        (HeavenlyStem.Geng, SixSpirit.WHITE_TIGER),
        (HeavenlyStem.Xin, SixSpirit.WHITE_TIGER),
        (HeavenlyStem.Ren, SixSpirit.BLACK_TORTOISE),
        (HeavenlyStem.Gui, SixSpirit.BLACK_TORTOISE),
    ],
)
def test_assign_spirits_starting_spirit(six_line_engine: SixLinesDivinationEngine, stem: HeavenlyStem, expected_spirit: SixSpirit):
    hexagram = Hexagram.from_binary([1, 1, 1, 1, 1, 1])
    six_line_engine.execute(hexagram)
    six_line_engine.assign_spirits(hexagram.interpretation, stem)
    assert hexagram.interpretation.get_lines()[0].spirit == expected_spirit


def test_assign_spirits_cyclic_order(six_line_engine: SixLinesDivinationEngine):
    hexagram = Hexagram.from_binary([1, 1, 1, 1, 1, 1])
    six_line_engine.execute(hexagram)

    # 甲 starts with 青龙, cycles through all six
    six_line_engine.assign_spirits(hexagram.interpretation, HeavenlyStem.Jia)
    expected_jia = [
        SixSpirit.AZURE_DRAGON,
        SixSpirit.VERMILION_BIRD,
        SixSpirit.HOOK_KIRIN,
        SixSpirit.FLYING_SNAKE,
        SixSpirit.WHITE_TIGER,
        SixSpirit.BLACK_TORTOISE,
    ]
    for i, (line, expected) in enumerate(zip(hexagram.interpretation.get_lines(), expected_jia)):
        assert line.spirit == expected, f"Line {i + 1}: expected {expected}, got {line.spirit}"

    # 壬 starts with 玄武, wraps around
    six_line_engine.assign_spirits(hexagram.interpretation, HeavenlyStem.Ren)
    expected_ren = [
        SixSpirit.BLACK_TORTOISE,
        SixSpirit.AZURE_DRAGON,
        SixSpirit.VERMILION_BIRD,
        SixSpirit.HOOK_KIRIN,
        SixSpirit.FLYING_SNAKE,
        SixSpirit.WHITE_TIGER,
    ]
    for i, (line, expected) in enumerate(zip(hexagram.interpretation.get_lines(), expected_ren)):
        assert line.spirit == expected, f"Line {i + 1}: expected {expected}, got {line.spirit}"
