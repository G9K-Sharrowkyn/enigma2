#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

from translator_cli import load_lexicon, lx_to_pl, pl_to_lx


def parse_args():
    p = argparse.ArgumentParser(description="Smoke test dla tłumacza (seed-korpus)")
    p.add_argument("--lexdir", default="out", help="katalog z lexicon_*.tsv (domyślnie: out)")
    p.add_argument("--seed", default="parallel_seed.tsv", help="plik TSV (pl/lx/note)")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    base = Path(__file__).resolve().parent
    lexdir = Path(args.lexdir)
    if not lexdir.is_absolute():
        lexdir = base / lexdir
    seed = Path(args.seed)
    if not seed.is_absolute():
        seed = base / seed

    lex = load_lexicon(lexdir)

    failures = 0
    with seed.open("r", encoding="utf8", newline="") as f:
        r = csv.DictReader(f, delimiter="\t")
        for i, row in enumerate(r, start=1):
            pl = (row.get("pl") or "").strip()
            lx = (row.get("lx") or "").strip()
            if not pl or not lx:
                continue
            try:
                pl_out, _ = lx_to_pl(lx, lex, strict=True)
                lx_out, _ = pl_to_lx(pl, lex, strict=False)
            except ValueError as e:
                failures += 1
                print(f"[{i}] {e}", file=sys.stderr)
                continue
            # nie porównujemy 1:1 tekstów (to smoke), tylko brak unknown + brak crash
            _ = pl_out, lx_out

    if failures:
        print(f"FAIL ({failures})", file=sys.stderr)
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
