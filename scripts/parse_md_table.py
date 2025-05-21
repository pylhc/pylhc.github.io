from collections.abc import Sequence
from pathlib import Path

import pandas as pd


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
