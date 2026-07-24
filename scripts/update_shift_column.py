# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""
Recompute the ``Shifts`` column of a logbook markdown table from its
``Start Date``/``End Date`` columns and write it back in place.

The shift model (work hours, weekend/holiday handling, shift length) is *not*
defined here: it is reused verbatim from ``shift_model.py`` via
``calculate_shift_parts``, so this stays the single
source of truth. Update the constants or ``CERN_HOLIDAYS`` there and re-run this.

Usage
-----
    uv run scripts/update_shift_column.py docs/logbook/LHC/2025_lhc.md ...
    uv run scripts/update_shift_column.py --check docs/logbook/LHC/*.md   # dry-run
    uv run scripts/update_shift_column.py --selftest   # run the built-in tests and exit
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import TYPE_CHECKING

# Reuse the canonical shift model + holidays (single source of truth). This is a
# sibling module: `uv run` puts this file's directory on sys.path automatically.
from shift_model import (
    COLUMN_END,
    COLUMN_SHIFTS,
    COLUMN_START,
    SHIFT_LENGTH,
    Shift,
    calculate_shift_parts,
    str_to_dt,
)

if TYPE_CHECKING:
    from datetime import timedelta

_ZERO_SHIFT = re.compile(
    r"(?:0+(?:\.0+)?(?:W|WN|H|HN))(?:\s+0+(?:\.0+)?(?:W|WN|H|HN))*"
)


def format_shift_string(parts: dict[Shift, timedelta], ndigits: int = 2) -> str:
    """Render the shift buckets as e.g. ``0.5W 0.6WN``, dropping empty buckets.

    Order follows ``Shift`` (W, WN, H, HN) as defined in ``shift_model``.
    """
    return " ".join(
        f"{value:g}{shift}"
        for shift in Shift
        if (value := round(parts[shift] / SHIFT_LENGTH, ndigits))
    )


def _split_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _is_separator(line: str) -> bool:
    return set(line.strip().strip("|")) <= set(":-| ")


def update_file(path: Path, *, check: bool = False) -> bool:
    """Recompute the Shifts column of the first markdown table in ``path``.

    Returns True if the file content changed (or would change, in ``check`` mode).
    """
    original = path.read_text()
    lines = original.splitlines()

    # First contiguous run of table lines only (ignore any later tables).
    try:
        first = next(i for i, line in enumerate(lines) if line.lstrip().startswith("|"))
    except StopIteration:
        raise ValueError(f"No markdown table found in {path.name}")
    last = first
    while last + 1 < len(lines) and lines[last + 1].lstrip().startswith("|"):
        last += 1

    # Header + data rows (skip the |:---:| separator), keeping their line indices.
    rows, row_idx, sep_idx = [], [], None
    for i in range(first, last + 1):
        if _is_separator(lines[i]):
            sep_idx = i
        else:
            rows.append(_split_row(lines[i]))
            row_idx.append(i)
    header, data = rows[0], rows[1:]
    malformed = next((row for row in data if len(row) != len(header)), None)
    if malformed is not None:
        raise ValueError(
            f"Malformed table row in {path.name}: "
            f"expected {len(header)} cells, found {len(malformed)}"
        )

    try:
        c_start = header.index(COLUMN_START)
        c_end = header.index(COLUMN_END)
        c_shift = header.index(COLUMN_SHIFTS)
    except ValueError as exc:
        raise ValueError(f"Missing expected column in {path.name}: {exc}") from exc

    for row in data:
        if (
            row[c_start]
            and row[c_end]
            and not _ZERO_SHIFT.fullmatch(row[c_shift])
        ):
            row[c_shift] = format_shift_string(
                calculate_shift_parts(str_to_dt(row[c_start]), str_to_dt(row[c_end]))
            )

    # Re-align the whole table (all columns centred, matching the existing style).
    widths = [max(3, *(len(cell) for cell in column)) for column in zip(*rows)]

    def fmt_row(cells: list[str]) -> str:
        return (
            "|"
            + "|".join(f" {cell.center(width)} " for cell, width in zip(cells, widths))
            + "|"
        )

    def fmt_sep() -> str:
        return "|" + "|".join(f":{'-' * width}:" for width in widths) + "|"

    new_lines = lines[:]
    for idx, row in zip(row_idx, rows):
        new_lines[idx] = fmt_row(row)
    if sep_idx is not None:
        new_lines[sep_idx] = fmt_sep()

    new_text = "\n".join(new_lines) + ("\n" if original.endswith("\n") else "")
    changed = new_text != original
    if changed and not check:
        path.write_text(new_text)
    return changed


# Tests ------------------------------------------------------------------------
# A valid shift for the model: 2025-04-01 is a Tuesday (weekday, non-holiday),
# 09:00 -> 17:30 = 8.5 work hours = 1.0625 shifts -> "1.06W".
_HEADER = f"| {COLUMN_START} | {COLUMN_END} | {COLUMN_SHIFTS} | Type |"
_SEP = "|:---:|:---:|:---:|:---:|"
_ROW = "| 2025-04-01 09:00 | 2025-04-01 17:30 | ? | test |"
_EXPECTED_SHIFT = "1.06W"


def _run(content: str) -> str:
    """Write ``content`` to a temp file, run ``update_file``, return the result."""
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "table.md"
        path.write_text(content)
        update_file(path)
        return path.read_text()


def test_recomputes_shift_column():
    out = _run(f"{_HEADER}\n{_SEP}\n{_ROW}\n")
    assert _EXPECTED_SHIFT in out.splitlines()[2]


def test_only_first_table_touched():
    second = f"{_HEADER}\n{_SEP}\n{_ROW.replace('?', 'KEEP')}\n"
    out = _run(f"{_HEADER}\n{_SEP}\n{_ROW}\n\nSome prose.\n\n{second}")
    # First table recomputed, second table left verbatim.
    assert _EXPECTED_SHIFT in out
    assert "KEEP" in out
    assert "Some prose." in out


def test_missing_start_or_end_left_alone():
    row = "| 2025-04-01 09:00 |  | UNTOUCHED | test |"
    out = _run(f"{_HEADER}\n{_SEP}\n{row}\n")
    assert "UNTOUCHED" in out


def test_explicit_zero_shift_left_alone():
    for zero in ("0W", "0.0W", "0WN", "0H", "0HN"):
        row = _ROW.replace("?", zero)
        out = _run(f"{_HEADER}\n{_SEP}\n{row}\n")
        assert zero in out.splitlines()[2]
        assert _EXPECTED_SHIFT not in out


def test_non_table_content_and_trailing_newline_preserved():
    prefix = "# Title\n\nIntro paragraph.\n\n"
    suffix = "\n\nFooter note.\n"
    out = _run(f"{prefix}{_HEADER}\n{_SEP}\n{_ROW}{suffix}")
    assert out.startswith(prefix)
    assert out.endswith(suffix)
    # No trailing newline in -> none out.
    assert not _run(f"{_HEADER}\n{_SEP}\n{_ROW}").endswith("\n")


def test_malformed_row_rejected():
    try:
        _run(f"{_HEADER}\n{_SEP}\n| too | few |\n")
    except ValueError as exc:
        assert "expected 4 cells, found 2" in str(exc)
    else:
        raise AssertionError("Malformed row was accepted")


def _selftest() -> int:
    test_recomputes_shift_column()
    test_only_first_table_touched()
    test_missing_start_or_end_left_alone()
    test_explicit_zero_shift_left_alone()
    test_non_table_content_and_trailing_newline_preserved()
    test_malformed_row_rejected()
    print("All update_shift_column tests passed.")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "files", nargs="*", type=Path, help="Markdown logbook files to update."
    )
    parser.add_argument(
        "--check", action="store_true", help="Report what would change without writing."
    )
    parser.add_argument("--selftest", action="store_true", help="Run the built-in tests and exit.")
    args = parser.parse_args(argv)

    if args.selftest:
        return _selftest()
    if not args.files:
        parser.error("the following arguments are required: files")

    any_changed = False
    for file_path in args.files:
        changed = update_file(file_path, check=args.check)
        any_changed |= changed
        state = ("would change" if args.check else "updated") if changed else "unchanged"
        print(f"{state}: {file_path}")

    # Non-zero exit in --check mode if anything is stale (handy for CI / pre-commit).
    return int(args.check and any_changed)


if __name__ == "__main__":
    raise SystemExit(main())
