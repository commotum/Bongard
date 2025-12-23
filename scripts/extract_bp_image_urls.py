#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin


class ImgSrcParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.srcs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "img":
            return
        for key, value in attrs:
            if key.lower() == "src" and value:
                self.srcs.append(value)


def extract_root_relative_srcs(html_text: str) -> list[str]:
    parser = ImgSrcParser()
    parser.feed(html_text)
    return [src for src in parser.srcs if src.startswith("/")]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract root-relative image URLs from Bongard Problem HTML files."
    )
    parser.add_argument(
        "--bps-dir",
        default="OEBP/BPs",
        help="Directory containing BP HTML files (default: OEBP/BPs).",
    )
    parser.add_argument(
        "--base-url",
        default="https://www.bongardproblems.com",
        help="Base URL to resolve root-relative image URLs.",
    )
    parser.add_argument(
        "--output",
        default="bp_image_urls.csv",
        help="Output CSV path (default: bp_image_urls.csv).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    bps_dir = Path(args.bps_dir)
    output_path = Path(args.output)
    base_url = args.base_url.rstrip("/") + "/"

    if not bps_dir.is_dir():
        raise SystemExit(f"BP directory not found: {bps_dir}")

    rows: list[tuple[str, str]] = []
    bp_name_re = re.compile(r"^BP\d+$")

    for html_path in sorted(bps_dir.glob("*.html")):
        bp_name = html_path.stem
        if not bp_name_re.match(bp_name):
            continue
        html_text = html_path.read_text(encoding="utf-8", errors="replace")
        for src in extract_root_relative_srcs(html_text):
            absolute_url = urljoin(base_url, src)
            rows.append((bp_name, absolute_url))

    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["bp", "image_url"])
        writer.writerows(rows)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
