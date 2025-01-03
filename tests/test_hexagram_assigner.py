import pytest

from yi.calculator.assigner import HexagramAssigner
from yi.model.hexagram import Hexagram
from yi.model.stem_branch import HeavenlyStem


@pytest.fixture
def assigner() -> HexagramAssigner:
    return HexagramAssigner()


def test_hexagram_assign_stem(assigner: HexagramAssigner):
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
