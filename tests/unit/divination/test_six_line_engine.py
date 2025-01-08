from ichingpy import HeavenlyStem, Hexagram
from ichingpy.divination.six_lines import SixLinesDivinationEngine
from ichingpy.enum.branch import EarthlyBranch


def test_six_lines_engine_can_execute(six_line_engine: SixLinesDivinationEngine):
    qian = Hexagram.from_binary([1, 1, 1, 1, 1, 1])
    six_line_engine.execute(qian)
    assert all([stem == HeavenlyStem.Jia for stem in qian.inner.stem])
    assert all([stem == HeavenlyStem.Ren for stem in qian.outer.stem])
    assert qian.inner.branch == [EarthlyBranch.Zi, EarthlyBranch.Yin, EarthlyBranch.Chen]
    assert qian.outer.branch == [EarthlyBranch.Wu, EarthlyBranch.Shen, EarthlyBranch.Xu]
