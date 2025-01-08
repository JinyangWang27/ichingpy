from datetime import datetime

from ichingpy import HeavenlyStem
from ichingpy.model.four_pillars import FourPillars


def test_four_pillars_get_month_pillar():
    assert FourPillars.get_month_pillar(datetime(2025, 1, 1), HeavenlyStem.Bing).stem == HeavenlyStem.Geng
    assert FourPillars.get_month_pillar(datetime(2025, 1, 1), HeavenlyStem.Gui).stem == HeavenlyStem.Jia
    assert FourPillars.get_month_pillar(datetime(2025, 1, 1), HeavenlyStem.Wu).stem == HeavenlyStem.Jia


def test_four_pillars_get_hour_pillar():  # add more test cases
    assert FourPillars.get_hour_pillar(datetime(2025, 3, 28, 11, 0, 0), HeavenlyStem.Bing).stem == HeavenlyStem.Jia
    assert FourPillars.get_hour_pillar(datetime(2025, 3, 29, 11, 0, 0), HeavenlyStem.Ding).stem == HeavenlyStem.Bing
