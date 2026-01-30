#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
import warnings
from collections import Counter
from pathlib import Path

warnings.filterwarnings("ignore", message="CUDA path could not be detected*", category=UserWarning)

try:
    import spacy  # type: ignore
except Exception:
    spacy = None


def parse_args():
    p = argparse.ArgumentParser(description="Analiza pokrycia PL przez leksykon (na podstawie plików repo)")
    p.add_argument("--lexdir", default="out", help="katalog z lexicon_pl2lx.tsv")
    p.add_argument("--root", default="..", help="katalog do skanowania (domyślnie: .. czyli Lengxuan_Language)")
    p.add_argument("--out", default="out/coverage_pl_missing.tsv", help="plik wynikowy TSV")
    p.add_argument("--top", type=int, default=200, help="ile brakujących lematów wypisać")
    return p.parse_args()


def load_pl_lexicon(path: Path) -> set[str]:
    known = set()
    for raw in path.read_text(encoding="utf8").splitlines():
        raw = raw.strip()
        if not raw or raw.startswith("#"):
            continue
        pl, _ = raw.split("\t", 1)
        known.add(pl.strip().lower())
    return known


def load_lx_lexicon(path: Path) -> set[str]:
    known = set()
    for raw in path.read_text(encoding="utf8").splitlines():
        raw = raw.strip()
        if not raw or raw.startswith("#"):
            continue
        lx, _ = raw.split("\t", 1)
        known.add(lx.strip().lower())
    return known


def iter_text_files(root: Path):
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        if p.suffix.lower() not in {".md", ".txt", ".html", ".tsv"}:
            continue
        # pomijamy słowniki i generaty
        if "03_Slownik" in str(p):
            continue
        if "Translator Files" in str(p):
            continue
        yield p


def main() -> int:
    args = parse_args()
    base = Path(__file__).resolve().parent
    lexdir = Path(args.lexdir)
    if not lexdir.is_absolute():
        lexdir = base / lexdir
    root = Path(args.root)
    if not root.is_absolute():
        root = (base / args.root).resolve()
    out_path = Path(args.out)
    if not out_path.is_absolute():
        out_path = base / out_path

    known = load_pl_lexicon(lexdir / "lexicon_pl2lx.tsv")
    known_lx = load_lx_lexicon(lexdir / "lexicon_lx2pl.tsv")

    if spacy is None:
        raise SystemExit("Brak spaCy — nie da się policzyć lematów PL.")
    nlp = spacy.load("pl_core_news_sm")

    freq: Counter[str] = Counter()
    word_re = re.compile(r"[A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż-]+")
    fenced_code_re = re.compile(r"```.*?```", re.DOTALL)
    inline_code_re = re.compile(r"`[^`]*`")

    for path in iter_text_files(root):
        text = path.read_text(encoding="utf8", errors="ignore")
        # wytnij code-blocki i inline-code (często zawierają Lengxuan)
        text = fenced_code_re.sub(" ", text)
        text = inline_code_re.sub(" ", text)
        # szybkie odfiltrowanie: tylko linie z literami
        if not word_re.search(text):
            continue
        doc = nlp(text)
        for t in doc:
            if t.is_space or t.is_punct:
                continue
            lemma = (t.lemma_ or t.text).lower()
            if lemma == "-pron-":
                lemma = t.text.lower()
            if not word_re.fullmatch(lemma):
                continue
            if lemma in known_lx:
                continue
            freq[lemma] += 1

    missing = [(w, c) for (w, c) in freq.most_common() if w not in known]
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf8", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["lemma_pl", "count"])
        for lemma, count in missing[: args.top]:
            w.writerow([lemma, count])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
