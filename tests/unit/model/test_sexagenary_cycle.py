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


@pytest.mark.parametrize(
    "cycle, expected_void",
    [
        (
            SexagenaryCycle(HeavenlyStem.Jia, EarthlyBranch.Zi),
            (EarthlyBranch.Xu, EarthlyBranch.Hai),
        ),  # 甲子旬 → 戌亥空
        (
            SexagenaryCycle(HeavenlyStem.Jia, EarthlyBranch.Xu),
            (EarthlyBranch.Shen, EarthlyBranch.You),
        ),  # 甲戌旬 → 申酉空
        (
            SexagenaryCycle(HeavenlyStem.Jia, EarthlyBranch.Shen),
            (EarthlyBranch.Wu, EarthlyBranch.Wei),
        ),  # 甲申旬 → 午未空
        (
            SexagenaryCycle(HeavenlyStem.Jia, EarthlyBranch.Wu),
            (EarthlyBranch.Chen, EarthlyBranch.Si),
        ),  # 甲午旬 → 辰巳空
        (
            SexagenaryCycle(HeavenlyStem.Jia, EarthlyBranch.Chen),
            (EarthlyBranch.Yin, EarthlyBranch.Mao),
        ),  # 甲辰旬 → 寅卯空
        (
            SexagenaryCycle(HeavenlyStem.Jia, EarthlyBranch.Yin),
            (EarthlyBranch.Zi, EarthlyBranch.Chou),
        ),  # 甲寅旬 → 子丑空
    ],
)
def test_kong_wang_all_xun(cycle, expected_void):
    assert cycle.kong_wang() == expected_void


def test_kong_wang_non_xun_shou():
    # 乙亥 is in 甲戌旬 (stem offset=1, branch Hai-1=Xu) → void is 申酉
    yi_hai = SexagenaryCycle(HeavenlyStem.Yi, EarthlyBranch.Hai)
    assert yi_hai.kong_wang() == (EarthlyBranch.Shen, EarthlyBranch.You)
