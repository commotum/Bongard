#!/usr/bin/env python3
"""
Download images listed in a CSV (bp,image_url) with polite rate limiting.

Usage:
    pip install requests tqdm colorama
    python scripts/download_bp_images.py
"""
from __future__ import annotations

import argparse
import csv
import random
import sys
import time
from pathlib import Path
from typing import Iterable
from urllib.parse import urlparse

import requests
from colorama import Fore, Style
from tqdm import tqdm


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/125.0.0.0 Safari/537.36"
    ),
    "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download image URLs listed in a CSV (bp,image_url)."
    )
    parser.add_argument(
        "--csv",
        default="bp_image_urls.csv",
        help="Input CSV path (default: bp_image_urls.csv).",
    )
    parser.add_argument(
        "--url-column",
        default="image_url",
        help="CSV column name that contains the URL (default: image_url).",
    )
    parser.add_argument(
        "--output-dir",
        default="oebp_images",
        help="Directory to write downloaded images (default: oebp_images).",
    )
    parser.add_argument(
        "--delay-min",
        type=float,
        default=2.0,
        help="Minimum delay between requests in seconds (default: 2).",
    )
    parser.add_argument(
        "--delay-max",
        type=float,
        default=6.0,
        help="Maximum delay between requests in seconds (default: 6).",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=20.0,
        help="Request timeout in seconds (default: 20).",
    )
    parser.add_argument(
        "--max-files",
        type=int,
        default=0,
        help="Optional cap on number of downloads (default: 0 = no cap).",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing files (default: skip if present).",
    )
    return parser.parse_args()


def load_urls(csv_path: Path, url_column: str) -> list[str]:
    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or url_column not in reader.fieldnames:
            raise ValueError(
                f"CSV missing required column '{url_column}' (found: {reader.fieldnames})"
            )
        urls = [row[url_column].strip() for row in reader if row.get(url_column)]
    # Preserve order while deduping
    return list(dict.fromkeys(urls))


def output_path_for_url(output_dir: Path, url: str) -> Path:
    parsed = urlparse(url)
    path = parsed.path.lstrip("/")
    return output_dir / path


def download_file(
    session: requests.Session,
    url: str,
    dest: Path,
    timeout: float,
    overwrite: bool,
) -> bool:
    if dest.exists() and not overwrite:
        return False

    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = dest.with_suffix(dest.suffix + ".part")

    resp = session.get(url, timeout=timeout, stream=True, allow_redirects=True)
    if resp.status_code != 200:
        raise RuntimeError(f"HTTP {resp.status_code}")

    with tmp_path.open("wb") as handle:
        for chunk in resp.iter_content(chunk_size=8192):
            if chunk:
                handle.write(chunk)
    tmp_path.replace(dest)
    return True


def main() -> int:
    args = parse_args()
    csv_path = Path(args.csv)
    output_dir = Path(args.output_dir)

    if not csv_path.exists():
        print(f"{Fore.RED}Missing CSV: {csv_path}{Style.RESET_ALL}")
        return 1

    try:
        urls = load_urls(csv_path, args.url_column)
    except Exception as exc:
        print(f"{Fore.RED}Failed to read CSV: {exc}{Style.RESET_ALL}")
        return 1

    if args.max_files > 0:
        urls = urls[: args.max_files]

    session = requests.Session()
    session.headers.update(HEADERS)

    for url in tqdm(urls, unit="img", desc="Downloading"):
        dest = output_path_for_url(output_dir, url)
        try:
            changed = download_file(
                session=session,
                url=url,
                dest=dest,
                timeout=args.timeout,
                overwrite=args.overwrite,
            )
            if not changed:
                tqdm.write(f"{Fore.CYAN}skip {url}{Style.RESET_ALL}")
        except Exception as exc:
            tqdm.write(f"{Fore.RED}error {url}: {exc}{Style.RESET_ALL}")

        time.sleep(random.uniform(args.delay_min, args.delay_max))

    print(
        f"{Fore.GREEN}✓ Done. Images saved under {output_dir}{Style.RESET_ALL}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
