import pytest

from ichingpy.divination.six_lines import SixLinesDivinationEngine
from ichingpy.enum import HeavenlyStem
from ichingpy.enum.branch import EarthlyBranch
from ichingpy.model.hexagram import Hexagram


@pytest.mark.parametrize(
    "binary, inner_stem, outer_stem, inner_branch, outer_branch",
    [
        (
            [1, 1, 1, 1, 1, 1],  # 乾
            HeavenlyStem.Jia,
            HeavenlyStem.Ren,
            [EarthlyBranch.Zi, EarthlyBranch.Yin, EarthlyBranch.Chen],
            [EarthlyBranch.Wu, EarthlyBranch.Shen, EarthlyBranch.Xu],
        ),
        (
            [2, 2, 2, 2, 2, 2],  # 坤
            HeavenlyStem.Yi,
            HeavenlyStem.Gui,
            [EarthlyBranch.Wei, EarthlyBranch.Si, EarthlyBranch.Mao],
            [EarthlyBranch.Chou, EarthlyBranch.Hai, EarthlyBranch.You],
        ),
        (
            [1, 2, 1, 1, 1, 2],  # 泽火革
            HeavenlyStem.Ji,
            HeavenlyStem.Ding,
            [EarthlyBranch.Mao, EarthlyBranch.Chou, EarthlyBranch.Hai],
            [EarthlyBranch.Hai, EarthlyBranch.You, EarthlyBranch.Wei],
        ),
        (
            [2, 1, 2, 1, 2, 2],  # 雷水解
            HeavenlyStem.Wu,
            HeavenlyStem.Geng,
            [EarthlyBranch.Yin, EarthlyBranch.Chen, EarthlyBranch.Wu],
            [EarthlyBranch.Wu, EarthlyBranch.Shen, EarthlyBranch.Xu],
        ),
        (
            [2, 2, 1, 2, 1, 1],  # 风山渐
            HeavenlyStem.Bing,
            HeavenlyStem.Xin,
            [EarthlyBranch.Chen, EarthlyBranch.Wu, EarthlyBranch.Shen],
            [EarthlyBranch.Wei, EarthlyBranch.Si, EarthlyBranch.Mao],
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
):

    hexagram = Hexagram.from_binary(binary)
    six_line_engine.execute(hexagram)
    assert hexagram.inner.interpretation is not None
    assert hexagram.outer.interpretation is not None
    assert all([stem == inner_stem for stem in hexagram.inner.interpretation.stem])
    assert all([stem == outer_stem for stem in hexagram.outer.interpretation.stem])
    assert hexagram.inner.interpretation.branch == inner_branch
    assert hexagram.outer.interpretation.branch == outer_branch
