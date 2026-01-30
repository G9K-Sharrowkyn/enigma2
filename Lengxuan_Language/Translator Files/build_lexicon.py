#!/usr/bin/env python3
"""
Buduje maszynowe słowniki PL↔Lengxuan z:
- 03_Slownik/slownik_polski_lengxuan.md
- 03_Slownik/slownik_lengxuan_polski.md
- Translator Files/extra_terms.yaml (opcjonalne rozszerzenia)

Wyjście: TSV + JSONL + raport braków.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:
    yaml = None


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--root", default=".", help="katalog główny repo (domyślnie .)")
    p.add_argument("--out", required=True, help="katalog wyjściowy")
    return p.parse_args()


def load_md_lex(path: Path, order: str):
    """
    Parsuje linie typu '- polski - lengxuan' lub '- lengxuan - polski'
    order: 'pl2lx' albo 'lx2pl'
    """
    data = []
    pattern = re.compile(r"^-\s+(.*?)\s+-\s+(.*)$")
    for line in path.read_text(encoding="utf8").splitlines():
        m = pattern.match(line.strip())
        if not m:
            continue
        left, right = m.group(1).strip(), m.group(2).strip()
        if order == "pl2lx":
            for pl in expand_pl_lemmas(left):
                data.append({"lemma_pl": pl, "lemma_lx": right})
        else:
            data.append({"lemma_lx": left, "lemma_pl": right})
    return data


def expand_pl_lemmas(raw: str) -> list[str]:
    """
    Rozbija polskie hasła typu:
    - "przybyć, dotrzeć" -> ["przybyć", "dotrzeć"]
    - "pochodzić z, wywodzić się" -> ["pochodzić z", "wywodzić się"]
    - "z, od (źródło)" -> ["z", "od (źródło)", "od"]
    Zostawia też oryginał wśród wariantów (dla stabilności).
    """
    raw = raw.strip()
    out: set[str] = {raw}

    # Rozbij na warianty przez "/" (częste w opisach)
    slash_parts = [p.strip() for p in raw.split("/") if p.strip()]
    for part in slash_parts:
        out.add(part)

    # Rozbij na warianty przez przecinki (synonimy)
    for part in list(out):
        if "," in part:
            for sub in [p.strip() for p in part.split(",") if p.strip()]:
                out.add(sub)
                # alias bez doprecyzowań w nawiasach
                out.add(strip_parenthetical(sub))

    # alias bez nawiasów dla całości
    out.add(strip_parenthetical(raw))

    cleaned = [x.strip() for x in out if x.strip()]
    cleaned = sorted(set(cleaned), key=lambda s: (len(s), s))
    return cleaned


def strip_parenthetical(s: str) -> str:
    return re.sub(r"\s*\(.*?\)\s*", "", s).strip()


def merge_dicts(pl2lx, lx2pl):
    # indeksy pomocnicze
    idx_pl = {}
    for row in pl2lx:
        idx_pl.setdefault(row["lemma_pl"], set()).add(row["lemma_lx"])
    idx_lx = {}
    for row in lx2pl:
        idx_lx.setdefault(row["lemma_lx"], set()).add(row["lemma_pl"])
    return idx_pl, idx_lx


def apply_extra(idx_pl, idx_lx, extra_path: Path):
    if not extra_path.exists():
        return
    if yaml is None:
        print("Brak PyYAML — pomijam extra_terms.yaml", file=sys.stderr)
        return
    extra = yaml.safe_load(extra_path.read_text(encoding="utf8"))
    for entry in extra:
        pl = entry["pl"].strip()
        lx = entry["lx"].strip()
        idx_pl.setdefault(pl, set()).add(lx)
        idx_lx.setdefault(lx, set()).add(pl)
        # alias LX bez diakrytyków typu ǎ/ǒ (dla wygody pisania)
        lx_alias = lx.replace("ǎ", "a").replace("ǒ", "o")
        if lx_alias != lx:
            idx_lx.setdefault(lx_alias, set()).add(pl)


def write_outputs(idx_pl, idx_lx, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    # TSV
    with (out_dir / "lexicon_pl2lx.tsv").open("w", encoding="utf8") as f:
        for pl, lxs in sorted(idx_pl.items()):
            for lx in sorted(lxs):
                f.write(f"{pl}\t{lx}\n")
    with (out_dir / "lexicon_lx2pl.tsv").open("w", encoding="utf8") as f:
        for lx, pls in sorted(idx_lx.items()):
            for pl in sorted(pls):
                f.write(f"{lx}\t{pl}\n")
    # JSONL
    with (out_dir / "lexicon_pl2lx.jsonl").open("w", encoding="utf8") as f:
        for pl, lxs in sorted(idx_pl.items()):
            f.write(json.dumps({"pl": pl, "lx": sorted(lxs)}, ensure_ascii=False) + "\n")
    with (out_dir / "lexicon_lx2pl.jsonl").open("w", encoding="utf8") as f:
        for lx, pls in sorted(idx_lx.items()):
            f.write(json.dumps({"lx": lx, "pl": sorted(pls)}, ensure_ascii=False) + "\n")


def write_missing_report(idx_pl, idx_lx, out_dir: Path):
    # proste krzyżowe sprawdzenie: jeśli pl->lx, ale brak odwrotnego wpisu
    missing = []
    for pl, lxs in idx_pl.items():
        for lx in lxs:
            if lx not in idx_lx or pl not in idx_lx[lx]:
                missing.append((pl, lx))
    if not missing:
        return
    with (out_dir / "missing_report.txt").open("w", encoding="utf8") as f:
        f.write("# Hasła bez symetrycznego odwzorowania\n")
        for pl, lx in sorted(missing):
            f.write(f"{pl}\t{lx}\n")


def main():
    args = parse_args()
    root = Path(args.root)
    out_dir = Path(args.out)

    pl2lx_path = root / "03_Slownik" / "slownik_polski_lengxuan.md"
    lx2pl_path = root / "03_Slownik" / "slownik_lengxuan_polski.md"
    extra_path = root / "Translator Files" / "extra_terms.yaml"

    pl2lx = load_md_lex(pl2lx_path, "pl2lx")
    lx2pl = load_md_lex(lx2pl_path, "lx2pl")

    idx_pl, idx_lx = merge_dicts(pl2lx, lx2pl)
    apply_extra(idx_pl, idx_lx, extra_path)

    # alias LX bez diakrytyków ǎ/ǒ dla całego leksykonu (ü bez zmian)
    aliases: list[tuple[str, str]] = []
    for lx, pls in idx_lx.items():
        lx_alias = lx.replace("ǎ", "a").replace("ǒ", "o")
        if lx_alias != lx:
            for pl in pls:
                aliases.append((lx_alias, pl))
    for lx_alias, pl in aliases:
        idx_lx.setdefault(lx_alias, set()).add(pl)

    write_outputs(idx_pl, idx_lx, out_dir)
    write_missing_report(idx_pl, idx_lx, out_dir)


if __name__ == "__main__":
    main()
