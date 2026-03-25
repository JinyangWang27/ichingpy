import pytest

from ichingpy.enum import EarthlyBranch, HeavenlyStem
from ichingpy.enum.five_phase import FivePhase
from ichingpy.model.sexagenary_cycle import SexagenaryCycle


def test_stem():
    jia = HeavenlyStem.Jia
    assert int(jia) == 1
    assert jia + 1 == HeavenlyStem.Yi
    assert 1 + jia == HeavenlyStem.Yi
    assert jia + jia == HeavenlyStem.Yi
    assert jia + 2 == HeavenlyStem.Bing
    assert jia + 10 == HeavenlyStem.Jia
    assert jia - 1 == HeavenlyStem.Gui
    assert 1 - jia - jia == HeavenlyStem.Ren


def test_branch():
    zi = EarthlyBranch.Zi
    assert int(zi) == 1
    assert zi + 1 == EarthlyBranch.Chou
    assert 1 + zi == EarthlyBranch.Chou
    assert zi + zi == EarthlyBranch.Chou
    assert zi + 2 == EarthlyBranch.Yin
    assert zi + 12 == EarthlyBranch.Zi
    assert zi - 1 == EarthlyBranch.Hai
    assert 1 - zi - zi == EarthlyBranch.Xu


def test_sexagenary_cycle():
    jia_zi = SexagenaryCycle(HeavenlyStem.Jia, EarthlyBranch.Zi)
    assert jia_zi.stem == HeavenlyStem.Jia
    assert jia_zi.branch == EarthlyBranch.Zi
    assert repr(jia_zi) == "甲子"
    assert jia_zi + 1 == SexagenaryCycle(HeavenlyStem.Yi, EarthlyBranch.Chou)
    assert jia_zi + 60 == jia_zi
    assert 60 + jia_zi == jia_zi
    assert jia_zi - 1 == SexagenaryCycle(HeavenlyStem.Gui, EarthlyBranch.Hai)
    assert 1 - jia_zi - jia_zi == SexagenaryCycle(HeavenlyStem.Ren, EarthlyBranch.Xu)


def test_sexagenary_cycle_from_int():
    assert SexagenaryCycle.from_int(1) == SexagenaryCycle(HeavenlyStem.Jia, EarthlyBranch.Zi)
    assert SexagenaryCycle.from_int(61) == SexagenaryCycle(HeavenlyStem.Jia, EarthlyBranch.Zi)


@pytest.mark.parametrize(
    "a, b",
    [
        (EarthlyBranch.Zi, EarthlyBranch.Chou),
        (EarthlyBranch.Yin, EarthlyBranch.Hai),
        (EarthlyBranch.Mao, EarthlyBranch.Xu),
        (EarthlyBranch.Chen, EarthlyBranch.You),
        (EarthlyBranch.Si, EarthlyBranch.Shen),
        (EarthlyBranch.Wu, EarthlyBranch.Wei),
    ],
)
def test_six_combinations(a: EarthlyBranch, b: EarthlyBranch):
    assert a.combines_with == b
    assert b.combines_with == a
    assert a.combines(b)
    assert b.combines(a)
    assert not a.combines(a)


@pytest.mark.parametrize(
    "a, b",
    [
        (EarthlyBranch.Zi, EarthlyBranch.Wu),
        (EarthlyBranch.Chou, EarthlyBranch.Wei),
        (EarthlyBranch.Yin, EarthlyBranch.Shen),
        (EarthlyBranch.Mao, EarthlyBranch.You),
        (EarthlyBranch.Chen, EarthlyBranch.Xu),
        (EarthlyBranch.Si, EarthlyBranch.Hai),
    ],
)
def test_six_clashes(a: EarthlyBranch, b: EarthlyBranch):
    assert a.clashes_with == b
    assert b.clashes_with == a
    assert a.clashes(b)
    assert b.clashes(a)
    assert not a.clashes(a)


@pytest.mark.parametrize(
    "branch, other1, other2, phase",
    [
        (EarthlyBranch.Shen, EarthlyBranch.Zi, EarthlyBranch.Chen, FivePhase.WATER),
        (EarthlyBranch.Zi, EarthlyBranch.Shen, EarthlyBranch.Chen, FivePhase.WATER),
        (EarthlyBranch.Chen, EarthlyBranch.Shen, EarthlyBranch.Zi, FivePhase.WATER),
        (EarthlyBranch.Hai, EarthlyBranch.Mao, EarthlyBranch.Wei, FivePhase.WOOD),
        (EarthlyBranch.Mao, EarthlyBranch.Hai, EarthlyBranch.Wei, FivePhase.WOOD),
        (EarthlyBranch.Wei, EarthlyBranch.Hai, EarthlyBranch.Mao, FivePhase.WOOD),
        (EarthlyBranch.Yin, EarthlyBranch.Wu, EarthlyBranch.Xu, FivePhase.FIRE),
        (EarthlyBranch.Wu, EarthlyBranch.Yin, EarthlyBranch.Xu, FivePhase.FIRE),
        (EarthlyBranch.Xu, EarthlyBranch.Yin, EarthlyBranch.Wu, FivePhase.FIRE),
        (EarthlyBranch.Si, EarthlyBranch.You, EarthlyBranch.Chou, FivePhase.METAL),
        (EarthlyBranch.You, EarthlyBranch.Si, EarthlyBranch.Chou, FivePhase.METAL),
        (EarthlyBranch.Chou, EarthlyBranch.Si, EarthlyBranch.You, FivePhase.METAL),
    ],
)
def test_three_harmony(
    branch: EarthlyBranch, other1: EarthlyBranch, other2: EarthlyBranch, phase: FivePhase
):
    result = branch.three_harmony
    assert result == (other1, other2, phase)
