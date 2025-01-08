from datetime import datetime
from typing import Self

from ichingpy.enum.branch import EarthlyBranch
from ichingpy.enum.stem import HeavenlyStem
from ichingpy.model.sexagenary_cycle import SexagenaryCycle


class FourPillars:
    """Four Pillars of Destiny (BaZi) model."""

    def __init__(self, year: SexagenaryCycle, month: SexagenaryCycle, day: SexagenaryCycle, hour: SexagenaryCycle):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour

    def get_pillars(self):
        """Get the Four Pillars of Destiny."""
        return f"{self.year}年 {self.month}月 {self.day}日 {self.hour}时"

    def __repr__(self) -> str:
        return f"{repr(self.year)} {repr(self.month)} {repr(self.day)} {repr(self.hour)}"

    @classmethod
    def from_datetime(cls, dt: datetime, month_adjust: int | None = None) -> Self:
        """Create a new instance of the FourPillars class from a datetime object.

        Args:
            dt (datetime): The datetime object.
        """
        year_pillar = cls.get_year_pillar(dt)
        month_pillar = cls.get_month_pillar(dt, year_pillar.stem)
        if month_adjust:
            if dt.month == 2:
                year_pillar += month_adjust
            month_pillar += month_adjust
        day_pillar = cls.get_day_pillar(dt)
        hour_pillar = cls.get_hour_pillar(dt, day_pillar.stem)
        return cls(year_pillar, month_pillar, day_pillar, hour_pillar)

    @staticmethod
    def get_year_pillar(dt: datetime) -> SexagenaryCycle:
        """Get the year pillar from a datetime.

        Args:
            dt (datetime): The datetime object.
        """
        year = dt.year
        year_pillar_int = (year - 3) % 60
        # It should also work for BC dates, but datetime does not support that
        # if year > 0:
        #     year_pillar_int = (year - 3) % 60
        # elif year < 0:
        #     year_pillar_int = 60 - (-year + 2) % 60
        # else:
        #     raise ValueError("Year cannot be 0.")

        if dt < datetime(year, 2, 4):
            year_pillar_int -= 1

        return SexagenaryCycle.from_int(year_pillar_int)

    @staticmethod
    def get_month_pillar(dt: datetime, year_stem: HeavenlyStem) -> SexagenaryCycle:
        """Get the month pillar from a datetime.

        Args:
            dt (datetime): The datetime object.
        """

        month_pillar_int = FourPillars.get_month_pillar_int(dt)
        branch = EarthlyBranch(month_pillar_int)

        match year_stem:
            case HeavenlyStem.Jia | HeavenlyStem.Ji:  # 1, 6 -> 3
                first_stem = HeavenlyStem.Bing  # 甲己之年丙作初
            case HeavenlyStem.Yi | HeavenlyStem.Geng:  # 2, 7 -> 5
                first_stem = HeavenlyStem.Wu  # 乙庚之岁戊为头
            case HeavenlyStem.Bing | HeavenlyStem.Xin:  # 3, 8 -> 7
                first_stem = HeavenlyStem.Geng  # 丙辛岁首从庚起
            case HeavenlyStem.Ding | HeavenlyStem.Ren:  # 4, 9 -> 9
                first_stem = HeavenlyStem.Ren  # 丁壬壬位顺行流
            case HeavenlyStem.Wu | HeavenlyStem.Gui:  # 5, 10 -> 1
                first_stem = HeavenlyStem.Jia  # 若问戊癸何方法，甲寅之上好推求

        stem = first_stem + (month_pillar_int + 9) % 12
        return SexagenaryCycle(stem, branch)

    @staticmethod
    def get_month_pillar_int(dt: datetime) -> int:
        month_starts = [
            (12, 7),
            (1, 6),
            (2, 4),
            (3, 6),
            (4, 5),
            (5, 6),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 8),
            (10, 8),
            (11, 7),
        ]
        for i, (month, day) in enumerate(month_starts):
            if (  # Check if the date is in the current month and on or after the start day
                dt.month == month and dt.day >= day
            ) or (  # Check if the date is in the next month and before the start day of the next month
                dt.month == month_starts[(i + 1) % 12][0] and dt.day < month_starts[(i + 1) % 12][1]
            ):
                return i + 1
        raise NotImplementedError  # Should never reach here

    @staticmethod
    def get_day_pillar(dt: datetime) -> SexagenaryCycle:
        """Get the day pillar from a datetime.

        Args:
            dt (datetime): The datetime object.
        """
        reference_date = datetime(2000, 2, 4, 0, 0, 0)  # this is not precise,
        reference_day = SexagenaryCycle(stem=HeavenlyStem.Ren, branch=EarthlyBranch.Chen)
        return reference_day + (dt - reference_date).days

    @staticmethod
    def get_hour_pillar(dt: datetime, day_stem: HeavenlyStem) -> SexagenaryCycle:
        """Get the hour pillar from a datetime.

        Args:
            dt (datetime): The datetime object.
        """
        # 甲己还生甲，乙庚丙作初

        # 丙辛从戊起，丁壬庚子居，

        # 戊癸何方发，壬子是真途

        match day_stem:
            case HeavenlyStem.Jia | HeavenlyStem.Ji:
                first_stem = HeavenlyStem.Jia
            case HeavenlyStem.Yi | HeavenlyStem.Geng:
                first_stem = HeavenlyStem.Bing
            case HeavenlyStem.Bing | HeavenlyStem.Xin:
                first_stem = HeavenlyStem.Wu
            case HeavenlyStem.Ding | HeavenlyStem.Ren:
                first_stem = HeavenlyStem.Geng
            case HeavenlyStem.Wu | HeavenlyStem.Gui:
                first_stem = HeavenlyStem.Ren

        hour_int = (dt.hour + 1) // 2 % 12 + 1
        stem = HeavenlyStem(first_stem + hour_int - 1)
        branch = EarthlyBranch(hour_int)
        return SexagenaryCycle(stem, branch)
