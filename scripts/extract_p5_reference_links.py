#!/usr/bin/env python3
"""
Extract p5.js reference entries from Reference.md into a CSV.

Columns: H2, H3, Title, Description, Link
"""
from __future__ import annotations

import csv
import os
import re
import sys
from pathlib import Path

INPUT_PATH = Path(os.getenv("INPUT_PATH", "P5/Reference.md"))
OUTPUT_CSV = Path(os.getenv("OUTPUT_CSV", "P5/reference_links.csv"))

LINK_LINE_RE = re.compile(r"^\s*\[(.+?)\]\((https?://[^)]+)\)\s*$")
HEADING_RE = re.compile(r"^\s*(#{2,3})\s+(.*?)\s*$")
LINK_TEXT_RE = re.compile(r"^\[(.+?)\]\([^)]+\)$")


def strip_front_matter(lines: list[str]) -> list[str]:
    if lines and lines[0].strip() == "---":
        for idx in range(1, len(lines)):
            if lines[idx].strip() == "---":
                return lines[idx + 1 :]
    return lines


def normalize_line(line: str) -> str:
    if line.lstrip().startswith("#"):
        return line
    # Fix rare cases where a heading is appended to a link line.
    line = line.replace(")### ", ")\n### ")
    line = line.replace(")## ", ")\n## ")
    return line


def parse_entries(lines: list[str]) -> list[tuple[str, str, str, str, str]]:
    current_h2 = ""
    current_h3 = ""
    pending: tuple[str, str, str, str] | None = None
    rows: list[tuple[str, str, str, str, str]] = []

    for raw_line in lines:
        for line in normalize_line(raw_line).splitlines():
            heading_match = HEADING_RE.match(line)
            if heading_match:
                level = heading_match.group(1)
                heading_text = heading_match.group(2).strip()
                link_text_match = LINK_TEXT_RE.match(heading_text)
                if link_text_match:
                    heading_text = link_text_match.group(1).strip()
                if level == "##":
                    current_h2 = heading_text
                    current_h3 = ""
                else:
                    current_h3 = heading_text
                continue

            link_match = LINK_LINE_RE.match(line)
            if not link_match:
                continue

            text = link_match.group(1).strip()
            url = link_match.group(2).strip()
            if pending is None:
                pending = (current_h2, current_h3, text, url)
            else:
                h2, h3, title, title_url = pending
                rows.append((h2, h3, title, text, title_url or url))
                pending = None

    if pending is not None:
        h2, h3, title, title_url = pending
        print(
            f"Warning: unmatched title without description: {title} ({title_url})",
            file=sys.stderr,
        )

    return rows


def main() -> int:
    if not INPUT_PATH.exists():
        print(f"Missing input file: {INPUT_PATH}", file=sys.stderr)
        return 1

    lines = INPUT_PATH.read_text(encoding="utf-8").splitlines()
    lines = strip_front_matter(lines)
    rows = parse_entries(lines)

    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["H2", "H3", "Title", "Description", "Link"])
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {OUTPUT_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
