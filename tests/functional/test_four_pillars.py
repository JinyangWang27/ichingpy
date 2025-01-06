from datetime import datetime

import pytest

from ichingpy.model.four_pillars import FourPillars


@pytest.mark.parametrize(
    "datetime, year_str",
    [
        (datetime(2025, 1, 1), "甲辰"),
        (datetime(2025, 7, 1), "乙巳"),
    ],
)
def test_four_pillars_get_year_pillar(datetime: datetime, year_str: str):
    assert repr(FourPillars.get_year_pillar(datetime)) == year_str


@pytest.mark.parametrize(
    "datetime, day_str",
    [
        (datetime(2025, 1, 1), "庚午"),
        (datetime(2025, 7, 1), "辛未"),
    ],
)
def test_four_pillars_get_day_pillar(datetime: datetime, day_str: str):
    assert repr(FourPillars.get_day_pillar(datetime)) == day_str


def test_four_pillars():
    assert FourPillars.from_datetime(datetime(2025, 1, 1, 0, 0, 0)).get_pillar() == "甲辰年 丙子月 庚午日 丙子时"
    assert FourPillars.from_datetime(datetime(2025, 3, 1, 0, 0, 0)).get_pillar() == "乙巳年 戊寅月 己巳日 甲子时"
