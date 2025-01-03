from yi.enum import EarthlyBranch, HeavenlyStem
from yi.model.sexagenary_cycle import SexagenaryCycle


def test_stem():
    jia = HeavenlyStem.Jia
    assert int(jia) == 1
    assert jia + 1 == HeavenlyStem.Yi
    assert 1 + jia == HeavenlyStem.Yi
    assert jia + jia == HeavenlyStem.Yi
    assert jia + 2 == HeavenlyStem.Bing
    assert jia + 10 == HeavenlyStem.Jia


def test_branch():
    zi = EarthlyBranch.Zi
    assert int(zi) == 1
    assert zi + 1 == EarthlyBranch.Chou
    assert 1 + zi == EarthlyBranch.Chou
    assert zi + zi == EarthlyBranch.Chou
    assert zi + 2 == EarthlyBranch.Yin
    assert zi + 12 == EarthlyBranch.Zi


def test_sexagenary_cycle():
    jia_zi = SexagenaryCycle(HeavenlyStem.Jia, EarthlyBranch.Zi)
    assert jia_zi.stem == HeavenlyStem.Jia
    assert jia_zi.branch == EarthlyBranch.Zi
    assert repr(jia_zi) == "甲子"
    assert jia_zi + 1 == SexagenaryCycle(HeavenlyStem.Yi, EarthlyBranch.Chou)
    assert jia_zi + 60 == jia_zi
    assert 60 + jia_zi == jia_zi


def test_sexagenary_cycle_from_int():
    assert SexagenaryCycle.from_int(1) == SexagenaryCycle(HeavenlyStem.Jia, EarthlyBranch.Zi)
    assert SexagenaryCycle.from_int(61) == SexagenaryCycle(HeavenlyStem.Jia, EarthlyBranch.Zi)
