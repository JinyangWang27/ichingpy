from ichingpy.divination.six_lines import SixLinesDivinationEngine
from ichingpy.enum import HeavenlyStem
from ichingpy.enum.branch import EarthlyBranch
from ichingpy.model.hexagram import Hexagram


def test_hexagram_assign_stem(six_line_engine: SixLinesDivinationEngine):
    qian = Hexagram.from_binary([1, 3, 3, 3, 3, 3])  # 乾之姤
    six_line_engine.assign_stems(qian)
    assert all([stem == HeavenlyStem.Jia for stem in qian.inner.stem])
    assert all([stem == HeavenlyStem.Ren for stem in qian.outer.stem])

    kun = Hexagram.from_binary([2, 2, 2, 2, 2, 2])
    six_line_engine.assign_stems(kun)
    assert all([stem == HeavenlyStem.Yi for stem in kun.inner.stem])
    assert all([stem == HeavenlyStem.Gui for stem in kun.outer.stem])

    ge = Hexagram.from_binary([1, 2, 1, 1, 1, 2])  #   泽火革
    six_line_engine.assign_stems(ge)
    assert all([stem == HeavenlyStem.Ji for stem in ge.inner.stem])
    assert all([stem == HeavenlyStem.Ding for stem in ge.outer.stem])

    zhun = Hexagram.from_binary([1, 2, 2, 2, 1, 2])  # 水雷屯
    six_line_engine.assign_stems(zhun)
    assert all([stem == HeavenlyStem.Geng for stem in zhun.inner.stem])
    assert all([stem == HeavenlyStem.Wu for stem in zhun.outer.stem])

    jian = Hexagram.from_binary([2, 2, 1, 2, 1, 1])  #
    six_line_engine.assign_stems(jian)
    assert all([stem == HeavenlyStem.Bing for stem in jian.inner.stem])
    assert all([stem == HeavenlyStem.Xin for stem in jian.outer.stem])


def test_hexagram_assign_branch(six_line_engine: SixLinesDivinationEngine):
    qian = Hexagram.from_binary([1, 1, 1, 1, 1, 1])
    six_line_engine.assign_branches(qian)
    assert qian.inner.branch == [EarthlyBranch.Zi, EarthlyBranch.Yin, EarthlyBranch.Chen]
    assert qian.outer.branch == [EarthlyBranch.Wu, EarthlyBranch.Shen, EarthlyBranch.Xu]

    shi = Hexagram.from_binary([2, 1, 2, 2, 2, 2])
    six_line_engine.assign_branches(shi)
    assert shi.inner.branch == [EarthlyBranch.Yin, EarthlyBranch.Chen, EarthlyBranch.Wu]
    assert shi.outer.branch == [EarthlyBranch.Chou, EarthlyBranch.Hai, EarthlyBranch.You]
