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
        # (
        #     [1, 2, 1, 1, 1, 2],  # 泽火革
        #     HeavenlyStem.Ji,
        #     HeavenlyStem.Ding,
        #     [EarthlyBranch.Chen, EarthlyBranch.Xu, EarthlyBranch.Chou],
        #     [EarthlyBranch.Yin, EarthlyBranch.Mao, EarthlyBranch.Chen],
        # ),
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

    # ge = Hexagram.from_binary([1, 2, 1, 1, 1, 2])  #   泽火革
    # six_line_engine._assign_stems(ge)
    # assert all([stem == HeavenlyStem.Ji for stem in ge.inner.stem])
    # assert all([stem == HeavenlyStem.Ding for stem in ge.outer.stem])

    # zhun = Hexagram.from_binary([1, 2, 2, 2, 1, 2])  # 水雷屯
    # six_line_engine._assign_stems(zhun)
    # assert all([stem == HeavenlyStem.Geng for stem in zhun.inner.stem])
    # assert all([stem == HeavenlyStem.Wu for stem in zhun.outer.stem])

    # jian = Hexagram.from_binary([2, 2, 1, 2, 1, 1])  #
    # six_line_engine._assign_stems(jian)
    # assert all([stem == HeavenlyStem.Bing for stem in jian.inner.stem])
    # assert all([stem == HeavenlyStem.Xin for stem in jian.outer.stem])


# def test_hexagram_assign_branch(six_line_engine: SixLinesDivinationEngine):


#     shi = Hexagram.from_binary([2, 1, 2, 2, 2, 2])
#     six_line_engine._assign_branches(shi)
#     assert shi.inner.branch == [EarthlyBranch.Yin, EarthlyBranch.Chen, EarthlyBranch.Wu]
#     assert shi.outer.branch == [EarthlyBranch.Chou, EarthlyBranch.Hai, EarthlyBranch.You]
