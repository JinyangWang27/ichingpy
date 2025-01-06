from datetime import datetime

import pytest

from ichingpy.model.four_pillars import FourPillars


@pytest.mark.parametrize(
    "dt, year_str",
    [
        (datetime(2025, 1, 1), "甲辰"),
        (datetime(2025, 7, 1), "乙巳"),
    ],
)
def test_four_pillars_get_year_pillar(dt: datetime, year_str: str):
    assert repr(FourPillars.get_year_pillar(dt)) == year_str


@pytest.mark.parametrize(
    "dt, day_str",
    [
        (datetime(2025, 1, 1), "庚午"),
        (datetime(2025, 7, 1), "辛未"),
    ],
)
def test_four_pillars_get_day_pillar(dt: datetime, day_str: str):
    assert repr(FourPillars.get_day_pillar(dt)) == day_str


@pytest.mark.parametrize(
    "dt, pillar_str",
    [
        (datetime(2025, 1, 1, 0, 0, 0), "甲辰年 丙子月 庚午日 丙子时"),
        (datetime(2025, 3, 1, 0, 0, 0), "乙巳年 戊寅月 己巳日 甲子时"),
        (datetime(2025, 3, 1, 2, 0, 0), "乙巳年 戊寅月 己巳日 乙丑时"),
        (datetime(2000, 7, 15, 11, 0, 0), "庚辰年 癸未月 甲戌日 庚午时"),
    ],
)
def test_four_pillars(dt: datetime, pillar_str: str):
    # add more test cases
    assert FourPillars.from_datetime(dt).get_pillar() == pillar_str
