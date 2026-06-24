from datetime import datetime
from typing import Self

from ichingpy.enum.branch import EarthlyBranch
from ichingpy.enum.stem import HeavenlyStem
from ichingpy.model.sexagenary_cycle import SexagenaryCycle


# ─── Stem-to-first-stem lookup tables ───────────────────────────────────────
# These are used by both month pillar and hour pillar computation.
# Extracted from the duplicated match statements for DRY principle.

# Month pillar: which HeavenlyStem starts the month cycle for a given year stem?
# 甲己之年丙作初, 乙庚之岁戊为头, 丙辛岁首从庚起, 丁壬壬位顺行流, 若问戊癸何方法，甲寅之上好推求
MONTH_FIRST_STEM: dict[int, HeavenlyStem] = {
    1: HeavenlyStem.Bing,   # Jia → Bing
    6: HeavenlyStem.Bing,   # Ji → Bing
    2: HeavenlyStem.Wu,     # Yi → Wu
    7: HeavenlyStem.Wu,     # Geng → Wu
    3: HeavenlyStem.Geng,   # Bing → Geng
    8: HeavenlyStem.Geng,   # Xin → Geng
    4: HeavenlyStem.Ren,    # Ding → Ren
    9: HeavenlyStem.Ren,    # Ren → Ren
    5: HeavenlyStem.Jia,    # Wu → Jia
    10: HeavenlyStem.Jia,   # Gui → Jia
}

# Hour pillar: which HeavenlyStem starts the hour cycle for a given day stem?
# 甲己还生甲, 乙庚丙作初, 丙辛从戊起, 丁壬庚子居, 戊癸何方发, 壬子是真途
HOUR_FIRST_STEM: dict[int, HeavenlyStem] = {
    1: HeavenlyStem.Jia,    # Jia → Jia
    6: HeavenlyStem.Jia,    # Ji → Jia
    2: HeavenlyStem.Bing,   # Yi → Bing
    7: HeavenlyStem.Bing,   # Geng → Bing
    3: HeavenlyStem.Wu,     # Bing → Wu
    8: HeavenlyStem.Wu,     # Xin → Wu
    4: HeavenlyStem.Geng,   # Ding → Geng
    9: HeavenlyStem.Geng,   # Ren → Geng
    5: HeavenlyStem.Ren,    # Wu → Ren
    10: HeavenlyStem.Ren,   # Gui → Ren
}

# ─── Month boundary data ────────────────────────────────────────────────────
# Each tuple is (calendar_month, start_day) marking the start of a solar term period.
# Index 0 = month 12 (大雪/冬至 period), index 1 = month 1, etc.

MONTH_STARTS: list[tuple[int, int]] = [
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


def _resolve_month_pillar_int(dt: datetime) -> int:
    """Determine the lunar month pillar index from a datetime.

    Walks the MONTH_STARTS table to find which solar-term period the date
    falls into. Returns 1-based index (1 = month 12 period, 12 = month 11 period).
    """
    for i, (month, day) in enumerate(MONTH_STARTS):
        next_month, next_day = MONTH_STARTS[(i + 1) % 12]
        in_current_period = dt.month == month and dt.day >= day
        in_next_before_start = dt.month == next_month and dt.day < next_day
        if in_current_period or in_next_before_start:
            return i + 1
    raise NotImplementedError  # Should never reach here


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
            month_adjust (int | None): Optional adjustment to month/year pillars.
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

        The year pillar advances at 立春 (Start of Spring), which falls on
        February 4 in most years. If the date is before Feb 4, the year
        pillar belongs to the previous year.

        Args:
            dt (datetime): The datetime object.
        """
        year = dt.year
        year_pillar_int = (year - 3) % 60

        if dt < datetime(year, 2, 4):
            year_pillar_int -= 1

        return SexagenaryCycle.from_int(year_pillar_int)

    @staticmethod
    def get_month_pillar(dt: datetime, year_stem: HeavenlyStem) -> SexagenaryCycle:
        """Get the month pillar from a datetime and the year's HeavenlyStem.

        The first HeavenlyStem of the month cycle is determined by the year stem
        according to the 五虎遁 (Five Tiger Escape) rule.

        Args:
            dt (datetime): The datetime object.
            year_stem (HeavenlyStem): The year's HeavenlyStem.
        """
        month_pillar_int = _resolve_month_pillar_int(dt)
        branch = EarthlyBranch(month_pillar_int)
        first_stem = MONTH_FIRST_STEM[year_stem.value]
        stem = first_stem + (month_pillar_int + 9) % 12
        return SexagenaryCycle(stem, branch)

    @staticmethod
    def get_month_pillar_int(dt: datetime) -> int:
        """Get the 1-based month pillar index from a datetime.

        Delegates to _resolve_month_pillar_int for the actual computation.
        Kept as a public API for backward compatibility.

        Args:
            dt (datetime): The datetime object.
        """
        return _resolve_month_pillar_int(dt)

    @staticmethod
    def get_day_pillar(dt: datetime) -> SexagenaryCycle:
        """Get the day pillar from a datetime.

        Computed by offsetting from a known reference date (2000-02-04 = 壬辰).

        Args:
            dt (datetime): The datetime object.
        """
        reference_date = datetime(2000, 2, 4, 0, 0, 0)
        reference_day = SexagenaryCycle(stem=HeavenlyStem.Ren, branch=EarthlyBranch.Chen)
        return reference_day + (dt - reference_date).days

    @staticmethod
    def get_hour_pillar(dt: datetime, day_stem: HeavenlyStem) -> SexagenaryCycle:
        """Get the hour pillar from a datetime and the day's HeavenlyStem.

        The first HeavenlyStem of the hour cycle is determined by the day stem
        according to the 五鼠遁 (Five Rat Escape) rule.

        Args:
            dt (datetime): The datetime object.
            day_stem (HeavenlyStem): The day's HeavenlyStem.
        """
        first_stem = HOUR_FIRST_STEM[day_stem.value]
        hour_int = (dt.hour + 1) // 2 % 12 + 1
        stem = HeavenlyStem(first_stem + hour_int - 1)
        branch = EarthlyBranch(hour_int)
        return SexagenaryCycle(stem, branch)
