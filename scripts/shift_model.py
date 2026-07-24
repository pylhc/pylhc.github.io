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

    python -m scripts.shift_model
"""

from __future__ import annotations

from datetime import datetime, timedelta
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
WORK: str = "W"
WORK_NIGHT: str = "WN"
HOLIDAY: str = "H"
HOLIDAY_NIGHT: str = "HN"
ALL_SHIFTS: tuple[str, ...] = (WORK, WORK_NIGHT, HOLIDAY, HOLIDAY_NIGHT)

SHIFT_NAMING: dict[str, str] = {
    WORK: "Mo - Fr (Day)",
    WORK_NIGHT: "Mo - Fr (Night)",
    HOLIDAY: "Holiday/Weekend (Day)",
    HOLIDAY_NIGHT: "Holiday/Weekend (Night)",
}

# Model parameters -------------------------------------------------------------
WORK_START_TIME: dict[str, int] = {"hour": 8, "minute": 30, "second": 0}
WORK_END_TIME: dict[str, int] = {"hour": 17, "minute": 30, "second": 0}
SHIFT_LENGTH: int = 8  # in hours
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

CERN_HOLIDAYS: list[datetime] = [
    _dt(*(int(part) for part in iso.split("-"))) for iso in _HOLIDAYS_ISO
]


# Set of ``(year, month, day)`` tuples for constant-time holiday lookups.
_HOLIDAY_DAYS: frozenset[tuple[int, int, int]] = frozenset(
    (h.year, h.month, h.day) for h in CERN_HOLIDAYS
)


def str_to_dt(date_str: str) -> datetime:
    return datetime.strptime(date_str, DATE_FORMAT).replace(tzinfo=TZ)


def same_day(d1: datetime, d2: datetime) -> bool:
    """True if the dates are on the same day."""
    return (d1.year == d2.year) and (d1.month == d2.month) and (d1.day == d2.day)


def is_holiday(date: datetime) -> bool:
    """True is date is on a known holiday."""
    return (date.year, date.month, date.day) in _HOLIDAY_DAYS


def calculate_shift_parts(start_time: datetime, end_time: datetime) -> dict[str, timedelta]:
    """Split the given shift into work hours, holidays/weekends day or night shifts.

    Args:
        start_time (datetime): Start time of the shift.
        end_time (datetime): End time of the shift.

    Raises:
        ValueError: In case start_time is later than end_time.

    Returns:
        Dict[str, timedelta]: Dictionary of the time deltas.

    """
    if start_time > end_time:
        raise ValueError(f"Start time {start_time} is after end time {end_time}")

    time_split = {shift: timedelta() for shift in ALL_SHIFTS}

    current_time = start_time
    while current_time < end_time:
        if current_time.weekday() < 5 and not is_holiday(current_time):  # Weekday (Monday to Friday)
            day_shift, night_shift = WORK, WORK_NIGHT
        else:
            day_shift, night_shift = HOLIDAY, HOLIDAY_NIGHT

        # hours on this day
        day_end = (current_time + timedelta(days=1)).replace(hour=0, minute=0, second=0)
        work_start = current_time.replace(
            hour=WORK_START_TIME["hour"],
            minute=WORK_START_TIME["minute"],
            second=WORK_START_TIME["second"],
        )
        work_end = current_time.replace(
            hour=WORK_END_TIME["hour"],
            minute=WORK_END_TIME["minute"],
            second=WORK_END_TIME["second"],
        )

        if current_time < work_start:
            # difference to work starting time (or shift)
            time_split[night_shift] += min(work_start, end_time) - current_time
            current_time = work_start

        elif current_time >= work_end:
            # difference to end of the day (or shift)
            time_split[night_shift] += min(day_end, end_time) - current_time
            current_time = day_end

        else:
            # difference to work ending time (or shift ending)
            time_split[day_shift] += min(work_end, end_time) - current_time
            current_time = work_end

    return time_split


def time_delta_to_hours(time_delta: timedelta) -> float:
    return time_delta.total_seconds() / 3600


def time_delta_to_shifts(time_delta: timedelta) -> float:
    return time_delta_to_hours(time_delta) / SHIFT_LENGTH


# Tests ------------------------------------------------------------------------

EPS = 1e-6


def test_timedelta_conversion():
    assert abs(time_delta_to_hours(timedelta(hours=1)) - 1) < EPS
    assert abs(time_delta_to_hours(timedelta(hours=2, minutes=30)) - 2.5) < EPS
    assert abs(time_delta_to_shifts(timedelta(hours=8)) - 1) < EPS
    assert abs(time_delta_to_shifts(timedelta(hours=12)) - 1.5) < EPS


def test_working_hours_friday():
    parts = calculate_shift_parts(
        start_time=_dt(2023, 10, 27, 16, 0), end_time=_dt(2023, 10, 28, 4, 0)
    )
    assert abs(time_delta_to_hours(parts[WORK]) - 1.5) < EPS
    assert abs(time_delta_to_hours(parts[WORK_NIGHT]) - 6.5) < EPS
    assert abs(time_delta_to_hours(parts[HOLIDAY]) - 0.0) < EPS
    assert abs(time_delta_to_hours(parts[HOLIDAY_NIGHT]) - 4.0) < EPS


def test_working_hours_monday_wednesday():
    parts = calculate_shift_parts(
        start_time=_dt(2023, 10, 23, 7, 0), end_time=_dt(2023, 10, 25, 16, 0)
    )
    assert abs(time_delta_to_hours(parts[WORK]) - 25.5) < EPS
    assert abs(time_delta_to_hours(parts[WORK_NIGHT]) - 31.5) < EPS
    assert abs(time_delta_to_hours(parts[HOLIDAY]) - 0) < EPS
    assert abs(time_delta_to_hours(parts[HOLIDAY_NIGHT]) - 0) < EPS


def test_working_hours_single_day():
    parts = calculate_shift_parts(
        start_time=_dt(2023, 10, 23, 9, 0), end_time=_dt(2023, 10, 23, 16, 0)
    )
    assert abs(time_delta_to_hours(parts[WORK]) - 7) < EPS
    assert abs(time_delta_to_hours(parts[WORK_NIGHT]) - 0) < EPS
    assert abs(time_delta_to_hours(parts[HOLIDAY]) - 0) < EPS
    assert abs(time_delta_to_hours(parts[HOLIDAY_NIGHT]) - 0) < EPS


if __name__ == "__main__":
    test_timedelta_conversion()
    test_working_hours_friday()
    test_working_hours_single_day()
    test_working_hours_monday_wednesday()
    print("All shift_model tests passed.")
