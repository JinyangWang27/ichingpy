import pytest

from ichingpy.enum.branch import EarthlyBranch
from ichingpy.enum.stem import HeavenlyStem
from ichingpy.model.interpretation.line.six_line_line import SixLineLineInterp
from ichingpy.model.interpretation.trigram.six_line_trigram import SixLineTrigramInterp
from ichingpy.model.trigram import Trigram


@pytest.fixture
def trigram() -> Trigram:
    trigram = Trigram.random()
    return trigram


@pytest.fixture
def trigram_interp(trigram: Trigram) -> SixLineTrigramInterp:
    return SixLineTrigramInterp(lines=[SixLineLineInterp(status=line.status) for line in trigram.lines])


def test_trigram_stem_setter(trigram_interp: SixLineTrigramInterp):
    trigram_interp.stem = HeavenlyStem.Jia
    assert all(line_interp.stem == HeavenlyStem.Jia for line_interp in trigram_interp.lines)


def test_trigram_branch_setter(trigram_interp: SixLineTrigramInterp):
    branches = [EarthlyBranch.Zi, EarthlyBranch.Yin, EarthlyBranch.Chen]
    trigram_interp.branch = branches
    assert trigram_interp.branch == branches


def test_trigram_raise_value_error_accessing_not_assigned_stem(trigram_interp: SixLineTrigramInterp):
    with pytest.raises(ValueError, match="Stems have not been assigned for all lines in the Trigram"):
        _ = trigram_interp.stem


def test_trigram_raise_value_error_accessing_not_assigned_branch(trigram_interp: SixLineTrigramInterp):
    with pytest.raises(ValueError, match="Branches have not been assigned for all lines in the Trigram"):
        _ = trigram_interp.branch


def test_trigram_raise_value_error_stem_not_same(trigram_interp: SixLineTrigramInterp):
    trigram_interp.stem = HeavenlyStem.Jia
    trigram_interp.lines[1].stem = HeavenlyStem.Bing
    with pytest.raises(ValueError, match="Stems of all lines in a Trigram should be the same"):
        _ = trigram_interp.stem
