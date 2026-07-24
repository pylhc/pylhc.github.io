# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "matplotlib >= 3.0",
#   "pandas >= 2.0",
# ]
# ///
"""
Aggregate and plot the shifts from the first markdown table in a given file,
e.g. for the end-of-year report.

The shift *model* (work hours, weekend/holiday handling, shift length) lives in
``shift_model.py`` and is reused here; this module only adds the pandas-based
table reading and the matplotlib plotting on top.
"""

from __future__ import annotations

import re
from datetime import timedelta
from pathlib import Path

import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib.figure import Figure

# Reuse the core shift model + table parser (single source of truth). These are
# sibling modules: `uv run` puts this file's directory on sys.path automatically.
from parse_md_table import parse_file
from shift_model import (
    COLUMN_END,
    COLUMN_SHIFTS,
    COLUMN_START,
    COLUMN_TYPE,
    SHIFT_LENGTH,
    SHIFT_NAMING,
    Shift,
    calculate_shift_parts,
    str_to_dt,
)


def calculate_shifts(
    file_path: str | Path, shift_type: str | None = None
) -> dict[Shift, timedelta]:
    """Calculate the shifts from Start/End Date columns of the first markdown table in a given file.

    Args:
        file_path (str | Path): Path to the markdown file.
        shift_type (str, optional): Regex to filter shift type.

    Returns:
        dict[Shift, timedelta]: Dictionary of the total time deltas separated by
        the type of hours (working hours, night hours, holidays or weekends).
    """
    file_path = Path(file_path)
    df = parse_file(file_path)

    if shift_type is not None:
        df = df.loc[df[COLUMN_TYPE].str.match(shift_type), :]

    parts = {shift: timedelta() for shift in Shift}

    if not {COLUMN_START, COLUMN_END} <= set(df.columns):
        raise ValueError(f"No start or end time column found in {file_path.name}")

    for start, end in df[[COLUMN_START, COLUMN_END]].itertuples(index=False, name=None):
        if not start or not end:
            continue

        for shift, duration in calculate_shift_parts(str_to_dt(start), str_to_dt(end)).items():
            parts[shift] += duration

    print(f"\nShifts from '{COLUMN_START}'/'{COLUMN_END}' columns in File {file_path.name}")
    for shift, name in SHIFT_NAMING.items():
        print(
            f"{name}: {parts[shift] / SHIFT_LENGTH:.1f} "
            f"({parts[shift] / timedelta(hours=1):.1f}h)"
        )

    return parts


def manual_shifts(file_path: str | Path, shift_type: str | None = None) -> dict[Shift, float]:
    """Calculate the shifts from Shifts column of the first markdown table in a given file.

    Args:
        file_path (str | Path): Path to the markdown file.
        shift_type (str): Regex to filter shift-type.

    Returns:
        dict[Shift, float]: Dictionary of the total shifts separated by
        the type of hours (working hours, night hours, holidays or weekends).
    """
    file_path = Path(file_path)
    df = parse_file(file_path)

    if shift_type is not None:
        df = df.loc[df[COLUMN_TYPE].str.match(shift_type), :]

    if COLUMN_SHIFTS not in df.columns:
        raise ValueError(f"No shift column found in {file_path.name}")

    parts = {
        shift: sum(
            float(amount)
            for value in df[COLUMN_SHIFTS]
            if value
            for amount, key in re.findall(r"([\d.]+)([WH]N?)", value)
            if key == shift
        )
        for shift in Shift
    }

    print(f"\nShifts from '{COLUMN_SHIFTS}' column in File {file_path.name}")
    for shift, name in SHIFT_NAMING.items():
        print(f"{name}: {parts[shift]}")

    return parts


def plot_results(parts, title: str = "", output_path: str | Path | None = None) -> Figure:
    """Plot the results of a calculation.

    Args:
        parts: Shift totals by category, either as timedeltas or shift counts.
        output_path (str | Path): Path to the output file.
    """
    fig, ax = plt.subplots()

    entries = [
        (index, shift, value / SHIFT_LENGTH if isinstance(value, timedelta) else value)
        for index, (shift, value) in enumerate(parts.items())
        if value
    ]
    data = [value for _, _, value in entries]
    labels = [f"{SHIFT_NAMING[shift]}: {value:.1f}" for _, shift, value in entries]
    colors = [f"C{index}" for index, _, _ in entries]
    explode = [0.1 * (shift == Shift.WORK) for _, shift, _ in entries]

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
        shift = calculate_shifts(file_path) if calculate else manual_shifts(file_path)
        times = [
            value / SHIFT_LENGTH if isinstance(value, timedelta) else value
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
    # The shift-model unit tests live in shift_model.py (run: uv run scripts/shift_model.py).

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
