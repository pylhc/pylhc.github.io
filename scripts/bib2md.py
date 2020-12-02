"""
Prints markdown for the Publications.md from .bib files.

Usage: Call `main` with the path to the script and a list of citekeys.
If no citekeys are given, all entries in the .bib are printed.
The boolean `add_year` can be set to "true" and prints the year with a '###' header.
This makes only sense, if you have your citekeys sorted by year!
(this is not done automatically, could be easily implemented though.)
"""
from pathlib import Path
from typing import Iterable
import re
from titlecase import titlecase

# Some tuning parameters:
ADMONITION = 'abstract'  # Admonition type
EXCLUDE_KEYS = ["file", "urldate", "abstract", "langid"]  # these are removed from bib-entry
MAX_AUTHORS = 5  # before writing "et al"
TO_REPLACE = {  # to be replaced in the title. First part (key) is case-insensitive regex
    "lhc": "LHC",
    "cern": "CERN",
    "fcc": "FCC",
    "fcc-ee": "FCC-ee",
    "fcc-hh": "FCC-hh",
    "fcc-he": "FCC-he",
    "he-lhc": "HE-LHC",
    'hllhc': "HLLHC",
    'hl-lhc': "HL-LHC",
    " ac ": " AC ",
    "ac-dipole": "AC-Dipole",
    " acdipole ": "ACDipole",
    " tev ": " TeV ",
    " kek ": " KEK ",
    " atf ": " ATF ",
    " atf2 ": " ATF2 ",
    " clic ": " CLIC "
}


# Patterns of bib-file:
type_citekey_pattern = "^\s*@(?P<type>.+){(?P<citekey>.+),\s*$"
key_value_pattern = "^\s*(?P<key>.*)\s*=\s*{(?P<value>.*)},?\s*$"


def main(bibfile: Path, citekeys: Iterable[str] = None, add_year: bool = False):
    """Prints markdown-admonitions for given bibfile and citekeys.
    If no citekeys are given, it prints all.
    """
    collection = read_bibfile(bibfile)
    print_markdown(collection, citekeys, add_year)


def read_bibfile(bibfile: Path) -> dict:
    """ Reads the bib-file and converts it's content to a dictionary.
    The entries are sorted by citekey and additional two entries
    `entrytype` (e.g. article, report etc.) and `rawtext` (the bib-raw text)
     are created.
    """
    with open(bibfile, 'r') as f:
        full_content = f.readlines()

    collection = dict()
    citekey = None

    type_citekey = re.compile(type_citekey_pattern)
    key_value = re.compile(key_value_pattern)

    for line in full_content:
        if not line.strip():
            continue

        match = re.match(type_citekey, line)
        if match:
            citekey = match.group('citekey')
            collection[citekey] = dict()
            collection[citekey]['entrytype'] = match.group('type')
            collection[citekey]['rawtext'] = line
            continue

        match = re.match(key_value, line)
        if match:
            key_ = match.group('key').strip()
            if key_ in EXCLUDE_KEYS:
                continue
            collection[citekey][key_] = match.group('value').replace("{", "").replace("}", "")

        if line.strip() == "}":
            collection[citekey]['rawtext'] = collection[citekey]['rawtext'].rstrip('\n').rstrip(",") + "\n"
        collection[citekey]['rawtext'] += line

    return collection


def print_markdown(collection: dict, citekeys: Iterable[str] = None, add_year: bool = False):
    """ Prints the markdown entries of the collection-dict of given citekeys.
    If citekeys is None, all are printed.
    `add_year` adds a year header, whenever the year changes between entries. """
    if citekeys is None:
        citekeys = collection.keys()

    last_year = None
    for citekey in citekeys:
        entry = collection[citekey]
        rawtext = entry["rawtext"].replace("\n", "\n    ").strip()

        doi = entry.get('doi')
        # replace citekey with doi-name, if it's of 13.231223/doi.name.323 format
        if doi and len(doi.split('/')) == 2:
            rawtext = rawtext.replace(citekey, doi.split('/')[-1])

        indented = "    " + rawtext

        # add year header if requested
        year = entry.get('year')
        if add_year and year and year != last_year:
            last_year = year
            print()
            print(f'### {year}')

        # Print the markdown admonition
        print()
        print(f'??? {ADMONITION} "{_format_description(entry)}"')
        print('    ```')
        print(indented)
        print("    ```")


def _format_description(entry):
    authors = entry.get("author", entry.get("editor", ""))
    author_str = ''
    if authors:
        author_str = f'`{_format_authors(authors)}`'

    title_str = titlecase(entry.get("title"))

    for key, val in TO_REPLACE.items():
        title_str = re.sub(key, val, title_str, flags=re.IGNORECASE)
    title_str = title_str.replace("\\", "")
    other_str = _format_other(entry)

    full_str = ''
    if author_str and title_str:
        full_str = f'{title_str}, {author_str}'
    elif author_str:
        full_str = author_str
    elif title_str:
        full_str = title_str

    if full_str and other_str:
        full_str = f'{full_str}, {other_str}'
    else:
        full_str = other_str

    return full_str


def _format_authors(raw):
    authors = raw.split(" and ")
    authors = [_switch_names(a) for a in authors]
    authors = [re.sub(r"\\'(\w)", lambda m: {"a": "á", "e": "é", "o": "ó", "i": "í", "c": "ć", "n": "ń"}[m.group(1)], a) for a in authors]
    authors = [re.sub(r'\\"(\w)', lambda m: {"a": "ä", "o": "ö", "u": "ü"}[m.group(1)], a) for a in authors]
    # authors = [re.sub(r"\\'(\w)", lambda m: f"&{m.group(1)}acute;", a) for a in authors]

    if len(authors) == 1:
        return authors[0]

    if len(authors) <= MAX_AUTHORS:
        return f'{", ".join(authors[:-1])}, and {authors[-1]}'

    return f'{authors[0]} et al.' 


def _switch_names(formal_name):
    parts = formal_name.split(", ")
    if len(parts) == 2:
        return f"{parts[1][0]}. {parts[0]}"
    return formal_name


def _format_other(entry):
    journal = entry.get('journal', entry.get('publisher', ''))
    volume = entry.get('volume')
    if volume:
        journal = f'{journal} **{volume}**'

    year = entry.get('year', entry.get('date', '    ')[:4]).strip()
    if journal and year:
        journal = f'{journal}, {year}'
    else:
        journal = year

    url = entry.get('url', '')
    if (journal != year) and url:
        return f'[{journal}]({url}){{target=_blank}}'

    if url:
        url = f'URL: [{url}]({url}){{target=_blank}}'

    if journal and url:
        return f"{journal}, {url}"

    if url:
        return url

    return journal


if __name__ == '__main__':
    main(bibfile=Path("path/to/bibfile"), citekeys=["citekeys", "touse"], add_year=True)