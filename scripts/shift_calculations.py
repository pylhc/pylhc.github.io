""" Script to calculate the shifts from the first markdown table in a given file. 
This data can then be plotted with `plot_results`, e.g. for the end-of-year report.
"""
from datetime import datetime, timedelta
from pathlib import Path
import re
from typing import Dict, Sequence, Union
import pandas as pd
from matplotlib import pyplot as plt


# Parse Markdown File ----------------------------------------------------------
COLUMN_START = "Start Date"
COLUMN_END = "End Date"
COLUMN_SHIFTS = "Shifts"
DATE_FORMAT = "%Y-%m-%d %H:%M"

def parse_file(file_path: Path) -> pd.DataFrame:
    """ Parses a markdown file, containing a shift-table, into a pandas dataframe.

    Args:
        file_path (Path): Path to the markdown file. 

    Returns:
        pd.DataFrame: DataFrame containing the shift table. 
    """
    header, data = get_table_parts(file_path.read_text().split("\n"))
    df = pd.DataFrame(
        columns=parse_line(header[0]),
        data=[parse_line(line) for line in data], 
    )
    return df


def parse_line(line: str):
    """Convert a single line of a table into a list of parts.

    Args:
        line (str): Line of the table. 

    Returns:
        List[str]: List of the table row entries. 
    """
    return [part.strip() for part in line.split("|")][1:-1]


def get_table_parts(content: Sequence[str]):
    """ Splits a markdown table into header and data. """
    header = []
    data = []
    header_finished = False

    for line in content:
        line = line.strip()

        if not line.startswith("|"):
            if not data:
                continue
            else:
                break
        
        if ":---" in line:
            header_finished = True
            continue

        if not header_finished:
            header.append(line)
        else:
            data.append(line)

    return header, data


def str_to_dt(date_str: str) -> datetime:
    return datetime.strptime(date_str, DATE_FORMAT)


# Check dates ------------------------------------------------------------------
WORK = "W"
NIGHT = "N"  # on a weekday
HOLIDAY = "H"

WORK_START_TIME = {"hour": 8, "minute": 30, "second": 0}
WORK_END_TIME  = {"hour": 17, "minute": 30, "second": 0}
SHIFT_LENGTH = 8  # in hours

CERN_HOLIDAYS = [
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
    #https://home.cern/official-holidays/2021
    datetime(2021, 1, 1),
    datetime(2021, 4, 2),
    datetime(2021, 4, 5),
    datetime(2021, 5, 13),
    datetime(2021, 5, 14),
    datetime(2021, 5, 24),
    datetime(2021, 9, 9),
]


def same_day(d1: datetime, d2: datetime) -> bool:
    """ True if the dates are on the same day. """
    return (d1.year == d2.year) and (d1.month == d2.month) and (d1.day == d2.day)


def is_holiday(date: datetime):
    """ True is date is on a known holiday. """
    return any(same_day(date, h) for h in CERN_HOLIDAYS)


def calculate_shift_parts(start_time: datetime, end_time: datetime) -> Dict[str, timedelta]:
    """Split the given shift into work hours, outside working hours and holidays/weekends.

    Args:
        start_time (datetime): Start time of the shift 
        end_time (datetime): End time of the shift 

    Raises:
        ValueError: In case start_time is later than end_time 

    Returns:
        Dict[str, timedelta]: Dictionary of the time deltas. 

    """
    if start_time > end_time:
        raise ValueError(f"Start time {start_time} is after end time {end_time}")
    
    time_split = {
        WORK: timedelta(),
        NIGHT: timedelta(),
        HOLIDAY: timedelta(),
    }

    current_time = start_time
    while current_time < end_time:
        day_end = current_time.replace(day=current_time.day + 1, hour=0, minute=0, second=0)

        if current_time.weekday() < 5 and not is_holiday(current_time):  # Weekday (Monday to Friday)
            # working hours on this day
            work_start = current_time.replace(**WORK_START_TIME)
            work_end = current_time.replace(**WORK_END_TIME)

            if current_time < work_start:
                # difference to work starting time (or shift)
                time_split[NIGHT] += min(work_start, end_time) - current_time
                current_time = work_start

            elif current_time >= work_end:
                # difference to end of the day (or shift)
                time_split[NIGHT] += min(day_end, end_time) - current_time
                current_time = day_end

            else:
                # difference to work ending time (or shift ending)
                time_split[WORK] += min(work_end, end_time) - current_time
                current_time = work_end

        else:  # Weekend (Saturday or Sunday) or holiday
            # difference to end of the day (or shift)
            time_split[HOLIDAY] += min(day_end, end_time) - current_time
            current_time = day_end

    return time_split 


def time_delta_to_hours(time_delta: timedelta):
    return time_delta.total_seconds() / 3600


def time_delta_to_shifts(time_delta: timedelta):
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
        start_time=datetime(2023, 10, 27, 16, 0), 
        end_time=datetime(2023, 10, 28, 4, 0)
    )
    assert abs(time_delta_to_hours(parts[WORK]) - 1.5) < EPS
    assert abs(time_delta_to_hours(parts[NIGHT]) - 6.5) < EPS
    assert abs(time_delta_to_hours(parts[HOLIDAY]) - 4.0) < EPS


def test_working_hours_monday_wednesday():
    parts = calculate_shift_parts(
        start_time=datetime(2023, 10, 23, 7, 0), 
        end_time=datetime(2023, 10, 25, 16, 0)
    )
    assert abs(time_delta_to_hours(parts[WORK]) - 25.5) < EPS
    assert abs(time_delta_to_hours(parts[NIGHT]) - 31.5) < EPS
    assert abs(time_delta_to_hours(parts[HOLIDAY]) - 0) < EPS


def test_working_hours_single_day():
    parts = calculate_shift_parts(
        start_time=datetime(2023, 10, 23, 9, 0), 
        end_time=datetime(2023, 10, 23, 16, 0)
    )
    assert abs(time_delta_to_hours(parts[WORK]) - 7) < EPS
    assert abs(time_delta_to_hours(parts[NIGHT]) - 0) < EPS
    assert abs(time_delta_to_hours(parts[HOLIDAY]) - 0) < EPS


# Main --------------------------------------------------------------------------

def calculate_shifts(file_path: Union[str, Path]):
    """Calculate the shifts from Start/End Date columns of the first markdown table in a given file.

    Args:
        file_path (Union[str, Path]): Path to the markdown file.

    Returns:
        Dict[str, timedelta]: Dictionary of the total time deltas separated by 
        the type of hours (working hours, night hours, holidays or weekends).
    """
    file_path = Path(file_path)
    df = parse_file(file_path)
    parts = {
        WORK: timedelta(),
        NIGHT: timedelta(),
        HOLIDAY: timedelta(),
    }
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

    print(f"Shifts in File {file_path.name}") 
    # print(f"Time spend during working hours: {time_delta_to_hours(parts[WORK])}h")
    # print(f"Time spend outside of working hours: {time_delta_to_hours(parts[OUTSIDE])}h")
    # print(f"Time spend on holidays or weekends: {time_delta_to_hours(parts[HOLIDAY])}h")
    print(f"Shifts during working hours: {time_delta_to_shifts(parts[WORK])}")
    print(f"Shifts outside of working hours: {time_delta_to_shifts(parts[NIGHT])}")
    print(f"Shifts on holidays or weekends: {time_delta_to_shifts(parts[HOLIDAY])}")

    return parts



def manual_shifts(file_path: Union[str, Path]):
    """Calculate the shifts from Shifts column of the first markdown table in a given file.

    Args:
        file_path (Union[str, Path]): Path to the markdown file.

    Returns:
        Dict[str, timedelta]: Dictionary of the total time deltas separated by 
        the type of hours (working hours, night hours, holidays or weekends).
    """
    file_path = Path(file_path)
    df = parse_file(file_path)

    parts = {
        WORK: 0.0,
        NIGHT: 0.0, 
        HOLIDAY: 0.0,
    }

    all_names = "".join(parts.keys())

    if COLUMN_SHIFTS not in df.columns:
        raise ValueError(f"No shift column found in {file_path.name}")

    for _, entry in df.iterrows():
        if not entry[COLUMN_SHIFTS]:
            continue

        shift_split = re.findall(fr"([\d.]+)([{all_names}])", entry[COLUMN_SHIFTS])         
        for value, key in shift_split:
            parts[key] += float(value)

    print(f"Shifts in File {file_path.name}") 
    # print(f"Time spend during working hours: {time_delta_to_hours(parts[WORK])}h")
    # print(f"Time spend outside of working hours: {time_delta_to_hours(parts[OUTSIDE])}h")
    # print(f"Time spend on holidays or weekends: {time_delta_to_hours(parts[HOLIDAY])}h")
    print(f"Shifts during working hours: {parts[WORK]}")
    print(f"Shifts outside of working hours: {parts[NIGHT]}")
    print(f"Shifts on holidays or weekends: {parts[HOLIDAY]}")

    return parts


def plot_results(parts, title: str = None, output_path: Union[str, Path] = None):
    """Plot the results of a calculation.

    Args:
        parts (Dict[str, timedelta]): Dictionary of the total time deltas separated by 
        the type of hours (working hours, outside working hours, holidays or weekends).
        output_path (Union[str, Path]): Path to the output file.
    """
    fig, ax = plt.subplots()
    name_map = {
        WORK: "Working hour shifts",
        NIGHT: "Night shifts",
        HOLIDAY: "Holidays or weekends",
    }

    data = [time_delta_to_shifts(value) if isinstance(value, timedelta) else value for value in parts.values() ]
    labels = [f"{name_map[k]}: {v:.1f}" for k, v in zip(parts.keys(), data)]

    ax.pie(data, labels=labels, autopct='%1.1f%%')

    if title:
        ax.set_title(title)

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
    print("\nFrom the Start/End Time Columns:")
    shift_c = calculate_shifts("/mnt/volume/jdilly/projects/pylhc.github.io/docs/resources/logbook/2023_lhc.md") 
    plot_results(shift_c, title="OMC Shifts LHC 2023")

    print("\nFrom the Shifts Columns:")
    shift_m = manual_shifts("/mnt/volume/jdilly/projects/pylhc.github.io/docs/resources/logbook/2023_lhc.md")
    plot_results(shift_m, title="OMC Shifts LHC 2023")

    plt.show()
