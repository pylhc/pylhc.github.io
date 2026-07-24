# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "matplotlib >= 3.0",
#   "pandas >= 2.0",
# ]
# ///
"""
Script to calculate the shifts from the first markdown table in a given file.
This data can then be plotted with `plot_results`, e.g. for the end-of-year report.
"""

from __future__ import annotations

import re
from datetime import datetime, timedelta
from pathlib import Path

import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from parse_md_table import parse_file

# Check dates ------------------------------------------------------------------
COLUMN_START: str = "Start Date"
COLUMN_END: str = "End Date"
COLUMN_SHIFTS: str = "Shifts"
COLUMN_TYPE: str = "Type"

WORK: str = "W"
WORK_NIGHT: str = "WN"
HOLIDAY: str = "H"
HOLIDAY_NIGHT: str = "HN"
ALL_SHIFTS: tuple[str] = (WORK, WORK_NIGHT, HOLIDAY, HOLIDAY_NIGHT)  # type: ignore

SHIFT_NAMING: dict[str, str] = {
    WORK: "Mo - Fr (Day)",
    WORK_NIGHT: "Mo - Fr (Night)",
    HOLIDAY: "Holiday/Weekend (Day)",
    HOLIDAY_NIGHT: "Holiday/Weekend (Night)",
}

WORK_START_TIME: dict[str, int] = {"hour": 8, "minute": 30, "second": 0}
WORK_END_TIME: dict[str, int] = {"hour": 17, "minute": 30, "second": 0}
SHIFT_LENGTH: int = 8  # in hours
DATE_FORMAT: str = r"%Y-%m-%d %H:%M"

CERN_HOLIDAYS: list[datetime] = [
    # For the 2026 year we look at this reference:
    # https://home.cern/news/official-news/cern/official-holidays-2026-and-end-year-closure-20262027
    datetime(2026, 1, 1),
    datetime(2025, 4, 18),
    datetime(2025, 4, 21),
    datetime(2025, 5, 1),
    datetime(2025, 5, 29),
    datetime(2025, 6, 9),
    datetime(2025, 9, 11),
    datetime(2025, 12, 24),
    datetime(2025, 12, 25),
    datetime(2025, 12, 31),
    # For the 2025 year we look at this reference:
    # https://home.cern/news/official-news/cern/official-holidays-2025-and-end-year-closure-20252026
    datetime(2025, 1, 1),
    datetime(2025, 4, 18),
    datetime(2025, 4, 21),
    datetime(2025, 5, 1),
    datetime(2025, 5, 29),
    datetime(2025, 6, 9),
    datetime(2025, 9, 11),
    datetime(2025, 12, 24),
    datetime(2025, 12, 25),
    datetime(2025, 12, 31),
    # At some point they stopped having a page for each year so for 2024 we can refer to:
    # https://home.cern/news/official-news/cern/official-holidays-2024-and-end-year-closure-20242025
    datetime(2024, 1, 1),
    datetime(2024, 3, 29),
    datetime(2024, 4, 1),
    datetime(2024, 5, 1),
    datetime(2024, 5, 9),
    datetime(2024, 5, 20),
    datetime(2024, 9, 5),
    datetime(2024, 12, 24),
    datetime(2024, 12, 25),
    datetime(2024, 12, 31),
    # https://home.cern/official-holidays/2023
    datetime(2023, 1, 2),
    datetime(2023, 4, 7),
    datetime(2023, 4, 10),
    datetime(2023, 5, 1),
    datetime(2023, 5, 18),
    datetime(2023, 5, 29),
    datetime(2023, 9, 7),
    # https://home.cern/official-holidays/2022
    datetime(2022, 1, 3),
    datetime(2022, 4, 15),
    datetime(2022, 4, 18),
    datetime(2022, 5, 26),
    datetime(2022, 5, 27),
    datetime(2022, 6, 6),
    datetime(2022, 9, 8),
    # https://home.cern/official-holidays/2021
    datetime(2021, 1, 1),
    datetime(2021, 4, 2),
    datetime(2021, 4, 5),
    datetime(2021, 5, 13),
    datetime(2021, 5, 14),
    datetime(2021, 5, 24),
    datetime(2021, 9, 9),
]


def str_to_dt(date_str: str) -> datetime:
    return datetime.strptime(date_str, DATE_FORMAT)


def same_day(d1: datetime, d2: datetime) -> bool:
    """True if the dates are on the same day."""
    return (d1.year == d2.year) and (d1.month == d2.month) and (d1.day == d2.day)


def is_holiday(date: datetime) -> bool:
    """True is date is on a known holiday."""
    return any(same_day(date, h) for h in CERN_HOLIDAYS)


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
        start_time=datetime(2023, 10, 27, 16, 0), end_time=datetime(2023, 10, 28, 4, 0)
    )
    assert abs(time_delta_to_hours(parts[WORK]) - 1.5) < EPS
    assert abs(time_delta_to_hours(parts[WORK_NIGHT]) - 6.5) < EPS
    assert abs(time_delta_to_hours(parts[HOLIDAY]) - 0.0) < EPS
    assert abs(time_delta_to_hours(parts[HOLIDAY_NIGHT]) - 4.0) < EPS


def test_working_hours_monday_wednesday():
    parts = calculate_shift_parts(
        start_time=datetime(2023, 10, 23, 7, 0), end_time=datetime(2023, 10, 25, 16, 0)
    )
    assert abs(time_delta_to_hours(parts[WORK]) - 25.5) < EPS
    assert abs(time_delta_to_hours(parts[WORK_NIGHT]) - 31.5) < EPS
    assert abs(time_delta_to_hours(parts[HOLIDAY]) - 0) < EPS
    assert abs(time_delta_to_hours(parts[HOLIDAY_NIGHT]) - 0) < EPS


def test_working_hours_single_day():
    parts = calculate_shift_parts(
        start_time=datetime(2023, 10, 23, 9, 0), end_time=datetime(2023, 10, 23, 16, 0)
    )
    assert abs(time_delta_to_hours(parts[WORK]) - 7) < EPS
    assert abs(time_delta_to_hours(parts[WORK_NIGHT]) - 0) < EPS
    assert abs(time_delta_to_hours(parts[HOLIDAY]) - 0) < EPS
    assert abs(time_delta_to_hours(parts[HOLIDAY_NIGHT]) - 0) < EPS


# Main --------------------------------------------------------------------------


def calculate_shifts(file_path: str | Path, shift_type: str | None = None) -> dict[str, timedelta]:
    """Calculate the shifts from Start/End Date columns of the first markdown table in a given file.

    Args:
        file_path (str | Path): Path to the markdown file.
        shift_type (str, optional): Regex to filter shift type.

    Returns:
        Dict[str, timedelta]: Dictionary of the total time deltas separated by
        the type of hours (working hours, night hours, holidays or weekends).
    """
    file_path = Path(file_path)
    df = parse_file(file_path)

    if shift_type is not None:
        df = df.loc[df[COLUMN_TYPE].str.match(shift_type), :]

    parts = {shift: timedelta() for shift in ALL_SHIFTS}

    if not all(c in df.columns for c in [COLUMN_START, COLUMN_END]):
        raise ValueError(f"No start or end time column found in {file_path.name}")

    for _, entry in df.iterrows():
        if not entry[COLUMN_START] or not entry[COLUMN_END]:
            continue

        shift_split = calculate_shift_parts(
            start_time=str_to_dt(entry[COLUMN_START]),
            end_time=str_to_dt(entry[COLUMN_END]),
        )
        for key, value in shift_split.items():
            parts[key] += value

    print(f"\nShifts from '{COLUMN_START}'/'{COLUMN_END}' columns in File {file_path.name}")
    for shift, name in SHIFT_NAMING.items():
        print(
            f"{name}: {time_delta_to_shifts(parts[shift]):.1f} ({time_delta_to_hours(parts[shift]):.1f}h)"
        )

    return parts


def manual_shifts(file_path: str | Path, shift_type: str | None = None) -> dict[str, float]:
    """Calculate the shifts from Shifts column of the first markdown table in a given file.

    Args:
        file_path (str | Path): Path to the markdown file.
        shift_type (str): Regex to filter shift-type.

    Returns:
        Dict[str, timedelta]: Dictionary of the total time deltas separated by
        the type of hours (working hours, night hours, holidays or weekends).
    """
    file_path = Path(file_path)
    df = parse_file(file_path)

    if shift_type is not None:
        df = df.loc[df[COLUMN_TYPE].str.match(shift_type), :]

    parts = {shift: 0.0 for shift in ALL_SHIFTS}

    if COLUMN_SHIFTS not in df.columns:
        raise ValueError(f"No shift column found in {file_path.name}")

    for _, entry in df.iterrows():
        if not entry[COLUMN_SHIFTS]:
            continue

        shift_split = re.findall(r"([\d.]+)([WH]N?)", entry[COLUMN_SHIFTS])
        for value, key in shift_split:
            parts[key] += float(value)

    print(f"\nShifts from '{COLUMN_SHIFTS}' column in File {file_path.name}")
    for shift, name in SHIFT_NAMING.items():
        print(f"{name}: {parts[shift]}")

    return parts


def plot_results(parts, title: str = "", output_path: str | Path | None = None) -> Figure:
    """Plot the results of a calculation.

    Args:
        parts (Dict[str, timedelta]): Dictionary of the total time deltas separated by
        the type of hours (working hours, outside working hours, holidays or weekends).
        output_path (str | Path): Path to the output file.
    """
    fig, ax = plt.subplots()

    data = [
        time_delta_to_shifts(value) if isinstance(value, timedelta) else value
        for value in parts.values()
    ]
    labels = [f"{SHIFT_NAMING[k]}: {v:.1f}" for k, v in zip(parts.keys(), data)]
    colors = [f"C{i}" for i, k in enumerate(parts.keys())]  # fix colors
    explode = [0.1 * (s == WORK) for s in parts.keys()]  # explode working hours

    # filter shift-entries that were not present
    def filter_by_data(array):
        return [a for a, d in zip(array, data) if d]

    labels = filter_by_data(labels)
    colors = filter_by_data(colors)
    explode = filter_by_data(explode)
    data = filter_by_data(data)  # filter data last!

    # plot
    ax.pie(
        data,
        labels=labels,
        colors=colors,
        autopct="%1.1f%%",
        explode=explode,
        shadow=True,
        # startangle=90,  # rotate if needed
        # counterclock=False,  # go the other way around
    )

    title += f"\nTotal Shifts: {sum(data):.1f}"
    ax.set_title(title)
    ax.axis("equal")
    fig.tight_layout()
    if output_path:
        fig.savefig(output_path)

    return fig


def plot_all_machines_in_year(
    year: int,
    additional: dict[str, float],
    calculate: bool = False,
    output_path: str | Path | None = None,
) -> Figure:
    """Do a pychart for all machines of a specific year.

    Args:
        year (int): The year to plot.
        additional (dict[str, float]): Additional data to plot.
        calculate (bool, optional): If True, calculate the shifts from the logbook file. Defaults to False.
        output_path (str | Path, optional): Path to the output file.

    Returns:
        Figure: Figure of the plot.
    """
    color_map = {
        name: f"C{ii}" for ii, name in enumerate(["lhc", "sps", "ps", "psb", "leir", "ad", "superkekb"])
    }

    data_map: dict[str, float] = {}
    for file_path in logbook_dir.glob(f"**/{year:4d}_*.md"):
        machine = file_path.stem.split("_")[1]
        if calculate:
            shift = calculate_shifts(file_path)
        else:
            shift = manual_shifts(file_path)
        times = [
            time_delta_to_shifts(value) if isinstance(value, timedelta) else value
            for value in shift.values()
        ]
        data_map[machine] = sum(times)

    for name, value in additional.items():
        if name in data_map:
            data_map[name] += value
        else:
            data_map[name] = value

    # data to list
    data = [d for d in data_map.values() if d]
    colors = [color_map[name] for name, d in data_map.items() if d]
    labels = [f"{name.upper()}: {d:.1f}" for name, d in data_map.items() if d]

    # plot
    fig, ax = plt.subplots()
    ax.pie(
        data,
        labels=labels,
        colors=colors,
        autopct="%1.1f%%",
        shadow=True,
        # startangle=90,  # rotate if needed
        # counterclock=False,  # go the other way around
    )

    title = f"Total OMC Shifts in {year:d}: {sum(data):.1f}"
    ax.set_title(title)
    ax.axis("equal")
    fig.tight_layout()
    if output_path:
        fig.savefig(output_path)

    return fig


if __name__ == "__main__":
    # Run Tests ------------------------------------------------
    test_timedelta_conversion()
    test_working_hours_friday()
    test_working_hours_single_day()
    test_working_hours_monday_wednesday()

    # Examples --------------------------------------------------

    mpl.rcParams["figure.figsize"] = 7.68, 4.8

    repo_dir = Path(__file__).parent.parent
    logbook_dir = repo_dir / "docs" / "logbook"

    # 2022 ---------------------------------------------------------------------

    # shift_m = manual_shifts(logbook_dir / "2022_lhc.md")
    # plot_results(shift_m, title="OMC Shifts LHC 2022", output_path="lhc_2022_shifts.pdf")

    # 2023 ---------------------------------------------------------------------

    # shift_c = calculate_shifts(logbook_dir / "LHC" / "2023_lhc.md")
    # plot_results(shift_c, title="OMC Shifts LHC 2023 (from Start/End)")

    # shift_c = calculate_shifts(logbook_dir / "2023_ps.md")
    # plot_results(shift_c, title="OMC Shifts PS 2023 (from Start/End)")

    shift_m = manual_shifts(logbook_dir / "LHC" / "2023_lhc.md")
    plot_results(shift_m, title="OMC Shifts LHC 2023", output_path="lhc_2023_shifts.pdf")

    shift_m = manual_shifts(logbook_dir / "LHC" / "2023_lhc.md", shift_type="Commissioning")
    plot_results(
        shift_m, title="OMC Shifts LHC 2023 (Commissioning)", output_path="lhc_2023_shifts_commish.pdf"
    )

    # shift_m = manual_shifts(logbook_dir / "2023_ps.md")
    # plot_results(shift_m, title="OMC Shifts PS 2023", output_path="ps_2023_shifts.pdf")

    # shift_m = manual_shifts(logbook_dir / "2023_psb.md")
    # plot_results(shift_m, title="OMC Shifts PSBooster 2023", output_path="psb_2023_shifts.pdf")

    # plot_all_machines_in_year(2023, additional={}, output_path="machines_2023.pdf")

    # 2024 ---------------------------------------------------------------------

    # shift_m = manual_shifts(logbook_dir / "LHC" / "2024_lhc.md")
    # plot_results(shift_m, title="OMC Shifts LHC 2024", output_path="lhc_2024_shifts.pdf")

    # shift_m = manual_shifts(logbook_dir / "LHC" /"2024_lhc.md", shift_type="Commissioning")
    # plot_results(shift_m, title="OMC Shifts LHC 2024 (Commissioning)", output_path="lhc_2024_shifts_commish.pdf")

    # shift_m = manual_shifts(logbook_dir / "2024_lhc.md", shift_type="MD")
    # plot_results(shift_m, title="OMC Shifts LHC 2024 (MDs)", output_path="lhc_2024_shifts_md.pdf")

    # shift_m = manual_shifts(logbook_dir / "2024_ps.md")
    # plot_results(shift_m, title="OMC Shifts PS 2024", output_path="ps_2024_shifts.pdf")

    # shift_m = manual_shifts(logbook_dir / "2024_psb.md")
    # plot_results(shift_m, title="OMC Shifts PSBooster 2024", output_path="psb_2024_shifts.pdf")

    # shift_m = manual_shifts(logbook_dir / "2024_sps.md")
    # plot_results(shift_m, title="OMC Shifts SPS 2024", output_path="sps_2024_shifts.pdf")

    # plot_all_machines_in_year(2024, {"leir": 9, "superkekb": 4}, output_path="machines_2024.pdf")

    # 2025 ---------------------------------------------------------------------

    shift_m = manual_shifts(logbook_dir / "LHC" / "2025_lhc.md")
    plot_results(shift_m, title="OMC Shifts LHC 2025", output_path="lhc_2025_shifts.pdf")

    # shift_m = calculate_shifts(logbook_dir / "LHC" /"2025_lhc.md")
    # plot_results(shift_m, title="OMC Shifts LHC 2025", output_path="lhc_2025_shifts_calc.pdf")

    # shift_m = manual_shifts(logbook_dir / "2024_lhc.md", shift_type="Commissioning")
    # plot_results(shift_m, title="OMC Shifts LHC 2024 (Commissioning)", output_path="lhc_2024_shifts_commish.pdf")

    # shift_m = manual_shifts(logbook_dir / "2024_lhc.md", shift_type="MD")
    # plot_results(shift_m, title="OMC Shifts LHC 2024 (MDs)", output_path="lhc_2024_shifts_md.pdf")

    # shift_m = manual_shifts(logbook_dir / "2024_ps.md")
    # plot_results(shift_m, title="OMC Shifts PS 2024", output_path="ps_2024_shifts.pdf")

    # shift_m = manual_shifts(logbook_dir / "2024_psb.md")
    # plot_results(shift_m, title="OMC Shifts PSBooster 2024", output_path="psb_2024_shifts.pdf")

    # shift_m = manual_shifts(logbook_dir / "2024_sps.md")
    # plot_results(shift_m, title="OMC Shifts SPS 2024", output_path="sps_2024_shifts.pdf")

    # plot_all_machines_in_year(2023, additional={}, output_path="machines_2023.pdf")

    # plot_all_machines_in_year(2024, {"leir": 9, "superkekb": 4}, output_path="machines_2024.pdf")

    plt.show()
