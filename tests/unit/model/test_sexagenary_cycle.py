import pytest

from ichingpy import EarthlyBranch, HeavenlyStem
from ichingpy.model.sexagenary_cycle import SexagenaryCycle


def test_sexagenary_cycle_raise_value_error_for_invalid_pair():
    with pytest.raises(ValueError):
        _ = SexagenaryCycle(HeavenlyStem.Jia, EarthlyBranch.Chou)


def test_sexagenary_cycle_english_repr():
    SexagenaryCycle.set_language("en")
    sexagenary_cycle = SexagenaryCycle(HeavenlyStem.Jia, EarthlyBranch.Zi)
    assert repr(sexagenary_cycle) == "Jia(1) Zi(1)"
    SexagenaryCycle.set_language("zh")


def test_sexagenary_cycle_can_to_int():
    sexagenary_cycle = SexagenaryCycle(HeavenlyStem.Jia, EarthlyBranch.Zi)
    assert int(sexagenary_cycle) == 1


def test_sexagenary_cycle_can_add():
    jia_zi = SexagenaryCycle(HeavenlyStem.Jia, EarthlyBranch.Zi)
    yi_chou = SexagenaryCycle(HeavenlyStem.Yi, EarthlyBranch.Chou)
    assert jia_zi + yi_chou == SexagenaryCycle(HeavenlyStem.Bing, EarthlyBranch.Yin)
