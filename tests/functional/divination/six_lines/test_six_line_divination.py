import pytest

from ichingpy.divination.six_lines import SixLinesDivinationEngine
from ichingpy.enum import HeavenlyStem
from ichingpy.enum.branch import EarthlyBranch
from ichingpy.enum.palace import Palace
from ichingpy.enum.role import HexagramRole
from ichingpy.model.hexagram import Hexagram
from ichingpy.model.interpretation.hexagram.six_line_hexagram import SixLineHexagramInterp


@pytest.mark.parametrize(
    "binary, inner_stem, outer_stem, inner_branch, outer_branch, palace, role",
    [
        (
            [1, 1, 1, 1, 1, 1],  # 乾
            HeavenlyStem.Jia,
            HeavenlyStem.Ren,
            [EarthlyBranch.Zi, EarthlyBranch.Yin, EarthlyBranch.Chen],
            [EarthlyBranch.Wu, EarthlyBranch.Shen, EarthlyBranch.Xu],
            Palace.HEAVEN,
            {HexagramRole.SUBJECT: 5, HexagramRole.OBJECT: 2},
        ),
        (
            [2, 2, 2, 2, 2, 2],  # 坤
            HeavenlyStem.Yi,
            HeavenlyStem.Gui,
            [EarthlyBranch.Wei, EarthlyBranch.Si, EarthlyBranch.Mao],
            [EarthlyBranch.Chou, EarthlyBranch.Hai, EarthlyBranch.You],
            Palace.EARTH,
            {HexagramRole.SUBJECT: 5, HexagramRole.OBJECT: 2},
        ),
        (
            [1, 2, 1, 1, 1, 2],  # 泽火革
            HeavenlyStem.Ji,
            HeavenlyStem.Ding,
            [EarthlyBranch.Mao, EarthlyBranch.Chou, EarthlyBranch.Hai],
            [EarthlyBranch.Hai, EarthlyBranch.You, EarthlyBranch.Wei],
            Palace.WATER,
            {HexagramRole.SUBJECT: 3, HexagramRole.OBJECT: 0},
        ),
        (
            [2, 1, 2, 1, 2, 2],  # 雷水解
            HeavenlyStem.Wu,
            HeavenlyStem.Geng,
            [EarthlyBranch.Yin, EarthlyBranch.Chen, EarthlyBranch.Wu],
            [EarthlyBranch.Wu, EarthlyBranch.Shen, EarthlyBranch.Xu],
            Palace.THUNDER,
            {HexagramRole.SUBJECT: 1, HexagramRole.OBJECT: 4},
        ),
        (
            [2, 2, 1, 2, 1, 1],  # 风山渐
            HeavenlyStem.Bing,
            HeavenlyStem.Xin,
            [EarthlyBranch.Chen, EarthlyBranch.Wu, EarthlyBranch.Shen],
            [EarthlyBranch.Wei, EarthlyBranch.Si, EarthlyBranch.Mao],
            Palace.MOUNTAIN,
            {HexagramRole.SUBJECT: 2, HexagramRole.OBJECT: 5},
        ),
    ],
)
def test_six_line_engine(
    six_line_engine: SixLinesDivinationEngine,
    binary: list[int],
    inner_stem: HeavenlyStem,
    outer_stem: HeavenlyStem,
    inner_branch: list[EarthlyBranch],
    outer_branch: list[EarthlyBranch],
    palace: Palace,
    role: dict[HexagramRole, int],
):

    hexagram = Hexagram.from_binary(binary)
    six_line_engine.execute(hexagram)
    assert isinstance(hexagram.interpretation, SixLineHexagramInterp)
    assert hexagram.inner.interpretation is not None
    assert hexagram.outer.interpretation is not None

    assert all([stem == inner_stem for stem in hexagram.inner.interpretation.stem])
    assert all([stem == outer_stem for stem in hexagram.outer.interpretation.stem])

    assert hexagram.inner.interpretation.branch == inner_branch
    assert hexagram.outer.interpretation.branch == outer_branch

    assert hexagram.interpretation.palace == palace

    assert hexagram.interpretation.get_lines()[role[HexagramRole.SUBJECT]].role == HexagramRole.SUBJECT  # type: ignore
    assert hexagram.interpretation.get_lines()[role[HexagramRole.OBJECT]].role == HexagramRole.OBJECT  # type: ignore
