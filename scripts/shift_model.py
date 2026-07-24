# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""
Core shift model shared by the logbook tooling (pure standard library).

This module is the single source of truth for *how* a shift interval is split
into work/night and weekday/holiday buckets. It has no third-party
dependencies so it can be imported by both the plotting layer
(``shift_calculations.py``) and the table updater (``update_shift_column.py``).

Run it directly to execute the unit tests::

    uv run scripts/shift_model.py
"""

from __future__ import annotations

from datetime import date, datetime, time, timedelta
from enum import StrEnum
from zoneinfo import ZoneInfo

# All times are interpreted in CERN's local timezone.
TZ: ZoneInfo = ZoneInfo("Europe/Zurich")


def _dt(year: int, month: int, day: int, hour: int = 0, minute: int = 0) -> datetime:
    """A timezone-aware ``datetime`` in CERN local time (Europe/Zurich)."""
    return datetime(year, month, day, hour, minute, tzinfo=TZ)

# Markdown table columns -------------------------------------------------------
COLUMN_START: str = "Start Date"
COLUMN_END: str = "End Date"
COLUMN_SHIFTS: str = "Shifts"
COLUMN_TYPE: str = "Type"

# Shift categories -------------------------------------------------------------
class Shift(StrEnum):
    WORK = "W"
    WORK_NIGHT = "WN"
    HOLIDAY = "H"
    HOLIDAY_NIGHT = "HN"


SHIFT_NAMING: dict[Shift, str] = {
    Shift.WORK: "Mo - Fr (Day)",
    Shift.WORK_NIGHT: "Mo - Fr (Night)",
    Shift.HOLIDAY: "Holiday/Weekend (Day)",
    Shift.HOLIDAY_NIGHT: "Holiday/Weekend (Night)",
}

# Model parameters -------------------------------------------------------------
WORK_START_TIME: time = time(8, 30)
WORK_END_TIME: time = time(17, 30)
SHIFT_LENGTH: timedelta = timedelta(hours=8)
DATE_FORMAT: str = r"%Y-%m-%d %H:%M"

# Official CERN holidays as ISO ``YYYY-MM-DD`` dates. The source page is noted
# per year; the flat, tz-aware ``CERN_HOLIDAYS`` list below is derived from this.
_HOLIDAYS_ISO: list[str] = [
    # https://web.archive.org/web/20260520135841/https://home.cern/official-holidays/
    "2026-01-01", "2026-04-03", "2026-04-06", "2026-05-01", "2026-05-14",
    "2026-05-25", "2026-09-10", "2026-12-24", "2026-12-25", "2026-12-31",
    # https://web.archive.org/web/20251119045710/https://home.cern/news/official-news/cern/official-holidays-2025-and-end-year-closure-20252026
    "2025-01-01", "2025-04-18", "2025-04-21", "2025-05-01", "2025-05-29",
    "2025-06-09", "2025-09-11", "2025-12-24", "2025-12-25", "2025-12-31",
    # https://web.archive.org/web/20251225020504/https://home.cern/news/official-news/cern/official-holidays-2024-and-end-year-closure-20242025
    "2024-01-01", "2024-03-29", "2024-04-01", "2024-05-01", "2024-05-09",
    "2024-05-20", "2024-09-05", "2024-12-24", "2024-12-25", "2024-12-31",
    # https://web.archive.org/web/20250123005611/https://home.cern/official-holidays/2023
    "2023-01-02", "2023-04-07", "2023-04-10", "2023-05-01", "2023-05-18",
    "2023-05-29", "2023-09-07",
    # https://web.archive.org/web/20250123143215/https://home.cern/official-holidays/2022
    "2022-01-03", "2022-04-15", "2022-04-18", "2022-05-26", "2022-05-27",
    "2022-06-06", "2022-09-08",
    # https://web.archive.org/web/20250124010437/https://home.cern/official-holidays/2021
    "2021-01-01", "2021-04-02", "2021-04-05", "2021-05-13", "2021-05-14",
    "2021-05-24", "2021-09-09",
]

CERN_HOLIDAYS: frozenset[date] = frozenset(map(date.fromisoformat, _HOLIDAYS_ISO))


def str_to_dt(date_str: str) -> datetime:
    return datetime.strptime(date_str, DATE_FORMAT).replace(tzinfo=TZ)


def calculate_shift_parts(
    start_time: datetime, end_time: datetime
) -> dict[Shift, timedelta]:
    """Split the given shift into work hours, holidays/weekends day or night shifts.

    Args:
        start_time (datetime): Start time of the shift.
        end_time (datetime): End time of the shift.

    Raises:
        ValueError: In case start_time is later than end_time.

    Returns:
        dict[Shift, timedelta]: Dictionary of the time deltas.

    """
    if start_time > end_time:
        raise ValueError(f"Start time {start_time} is after end time {end_time}")

    time_split = {shift: timedelta() for shift in Shift}

    current_time = start_time
    while current_time < end_time:
        day = current_time.date()
        day_shift, night_shift = (
            (Shift.WORK, Shift.WORK_NIGHT)
            if day.weekday() < 5 and day not in CERN_HOLIDAYS
            else (Shift.HOLIDAY, Shift.HOLIDAY_NIGHT)
        )

        work_start = datetime.combine(day, WORK_START_TIME, tzinfo=TZ)
        work_end = datetime.combine(day, WORK_END_TIME, tzinfo=TZ)
        next_midnight = datetime.combine(day + timedelta(days=1), time.min, tzinfo=TZ)

        if current_time < work_start:
            shift, boundary = night_shift, work_start
        elif current_time < work_end:
            shift, boundary = day_shift, work_end
        else:
            shift, boundary = night_shift, next_midnight

        time_split[shift] += min(boundary, end_time) - current_time
        current_time = boundary

    return time_split


# Tests ------------------------------------------------------------------------


def test_working_hours_friday():
    parts = calculate_shift_parts(
        start_time=_dt(2023, 10, 27, 16, 0), end_time=_dt(2023, 10, 28, 4, 0)
    )
    assert parts[Shift.WORK] == timedelta(hours=1.5)
    assert parts[Shift.WORK_NIGHT] == timedelta(hours=6.5)
    assert parts[Shift.HOLIDAY] == timedelta()
    assert parts[Shift.HOLIDAY_NIGHT] == timedelta(hours=4)


def test_working_hours_monday_wednesday():
    parts = calculate_shift_parts(
        start_time=_dt(2023, 10, 23, 7, 0), end_time=_dt(2023, 10, 25, 16, 0)
    )
    assert parts[Shift.WORK] == timedelta(hours=25.5)
    assert parts[Shift.WORK_NIGHT] == timedelta(hours=31.5)
    assert parts[Shift.HOLIDAY] == timedelta()
    assert parts[Shift.HOLIDAY_NIGHT] == timedelta()


def test_working_hours_single_day():
    parts = calculate_shift_parts(
        start_time=_dt(2023, 10, 23, 9, 0), end_time=_dt(2023, 10, 23, 16, 0)
    )
    assert parts[Shift.WORK] == timedelta(hours=7)
    assert parts[Shift.WORK_NIGHT] == timedelta()
    assert parts[Shift.HOLIDAY] == timedelta()
    assert parts[Shift.HOLIDAY_NIGHT] == timedelta()


if __name__ == "__main__":
    test_working_hours_friday()
    test_working_hours_single_day()
    test_working_hours_monday_wednesday()
    print("All shift_model tests passed.")
