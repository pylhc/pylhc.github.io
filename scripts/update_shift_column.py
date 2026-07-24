# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""
Recompute the ``Shifts`` column of a logbook markdown table from its
``Start Date``/``End Date`` columns and write it back in place.

The shift model (work hours, weekend/holiday handling, shift length) is *not*
defined here: it is reused verbatim from ``shift_model.py`` via
``calculate_shift_parts`` / ``time_delta_to_shifts``, so this stays the single
source of truth. Update the constants or ``CERN_HOLIDAYS`` there and re-run this.

Usage
-----
    python -m scripts.update_shift_column docs/logbook/LHC/2025_lhc.md ...
    python -m scripts.update_shift_column --check docs/logbook/LHC/*.md   # dry-run
"""

from __future__ import annotations

import argparse
from pathlib import Path

# Reuse the canonical shift model + holidays (single source of truth). Run this
# as a module from the repo root, e.g. `python -m scripts.update_shift_column`.
from scripts.shift_model import (
    ALL_SHIFTS,
    COLUMN_END,
    COLUMN_SHIFTS,
    COLUMN_START,
    calculate_shift_parts,
    str_to_dt,
    time_delta_to_shifts,
)


def format_shift_string(parts: dict, ndigits: int = 2) -> str:
    """Render the shift buckets as e.g. ``0.5W 0.6WN``, dropping empty buckets.

    Order follows ``ALL_SHIFTS`` (W, WN, H, HN) as defined in ``shift_model``.
    """
    pieces = []
    for key in ALL_SHIFTS:
        value = round(time_delta_to_shifts(parts[key]), ndigits)
        if value > 0:
            pieces.append(f"{value:g}{key}")
    return " ".join(pieces)


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
    first = next((i for i, ln in enumerate(lines) if ln.lstrip().startswith("|")), None)
    if first is None:
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

    try:
        c_start = header.index(COLUMN_START)
        c_end = header.index(COLUMN_END)
        c_shift = header.index(COLUMN_SHIFTS)
    except ValueError as exc:
        raise ValueError(f"Missing expected column in {path.name}: {exc}") from exc

    for row in data:
        if not row[c_start] or not row[c_end]:
            continue
        parts = calculate_shift_parts(str_to_dt(row[c_start]), str_to_dt(row[c_end]))
        row[c_shift] = format_shift_string(parts)

    # Re-align the whole table (all columns centred, matching the existing style).
    ncol = len(header)
    widths = [max(3, max(len(r[c]) for r in rows)) for c in range(ncol)]

    def fmt_row(cells: list[str]) -> str:
        return "|" + "|".join(f" {cells[c].center(widths[c])} " for c in range(ncol)) + "|"

    def fmt_sep() -> str:
        return "|" + "|".join(f":{'-' * widths[c]}:" for c in range(ncol)) + "|"

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


def test_non_table_content_and_trailing_newline_preserved():
    prefix = "# Title\n\nIntro paragraph.\n\n"
    suffix = "\n\nFooter note.\n"
    out = _run(f"{prefix}{_HEADER}\n{_SEP}\n{_ROW}{suffix}")
    assert out.startswith(prefix)
    assert out.endswith(suffix)
    # No trailing newline in -> none out.
    assert not _run(f"{_HEADER}\n{_SEP}\n{_ROW}").endswith("\n")


def _selftest() -> int:
    test_recomputes_shift_column()
    test_only_first_table_touched()
    test_missing_start_or_end_left_alone()
    test_non_table_content_and_trailing_newline_preserved()
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
        any_changed = any_changed or changed
        state = ("would change" if args.check else "updated") if changed else "unchanged"
        print(f"{state}: {file_path}")

    # Non-zero exit in --check mode if anything is stale (handy for CI / pre-commit).
    return 1 if (args.check and any_changed) else 0


if __name__ == "__main__":
    raise SystemExit(main())
