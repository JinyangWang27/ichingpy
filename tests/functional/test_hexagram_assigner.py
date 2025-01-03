import pytest

from ichingpy.assigners.assigner import StemBranchAssigner
from ichingpy.enum import HeavenlyStem
from ichingpy.enum.branch import EarthlyBranch
from ichingpy.model.hexagram import Hexagram


@pytest.fixture
def assigner() -> StemBranchAssigner:
    return StemBranchAssigner()


def test_hexagram_assign_stem(assigner: StemBranchAssigner):
    qian = Hexagram.from_binary([1, 3, 3, 3, 3, 3])  # 乾之姤
    assigner.assign_stems(qian)
    assert all([stem == HeavenlyStem.Jia for stem in qian.inner.stem])
    assert all([stem == HeavenlyStem.Ren for stem in qian.outer.stem])

    kun = Hexagram.from_binary([2, 2, 2, 2, 2, 2])
    assigner.assign_stems(kun)
    assert all([stem == HeavenlyStem.Yi for stem in kun.inner.stem])
    assert all([stem == HeavenlyStem.Gui for stem in kun.outer.stem])

    ge = Hexagram.from_binary([1, 2, 1, 1, 1, 2])  #   泽火革
    assigner.assign_stems(ge)
    assert all([stem == HeavenlyStem.Ji for stem in ge.inner.stem])
    assert all([stem == HeavenlyStem.Ding for stem in ge.outer.stem])

    zhun = Hexagram.from_binary([1, 2, 2, 2, 1, 2])  # 水雷屯
    assigner.assign_stems(zhun)
    assert all([stem == HeavenlyStem.Geng for stem in zhun.inner.stem])
    assert all([stem == HeavenlyStem.Wu for stem in zhun.outer.stem])

    jian = Hexagram.from_binary([2, 2, 1, 2, 1, 1])  #
    assigner.assign_stems(jian)
    assert all([stem == HeavenlyStem.Bing for stem in jian.inner.stem])
    assert all([stem == HeavenlyStem.Xin for stem in jian.outer.stem])


def test_hexagram_assign_branch(assigner: StemBranchAssigner):
    qian = Hexagram.from_binary([1, 1, 1, 1, 1, 1])
    assigner.assign_branches(qian)
    assert qian.inner.branch == [EarthlyBranch.Zi, EarthlyBranch.Yin, EarthlyBranch.Chen]
    assert qian.outer.branch == [EarthlyBranch.Wu, EarthlyBranch.Shen, EarthlyBranch.Xu]

    shi = Hexagram.from_binary([2, 1, 2, 2, 2, 2])
    assigner.assign_branches(shi)
    assert shi.inner.branch == [EarthlyBranch.Yin, EarthlyBranch.Chen, EarthlyBranch.Wu]
    assert shi.outer.branch == [EarthlyBranch.Chou, EarthlyBranch.Hai, EarthlyBranch.You]
