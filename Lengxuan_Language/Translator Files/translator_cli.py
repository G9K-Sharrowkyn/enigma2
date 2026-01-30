#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
import warnings
from dataclasses import dataclass
from pathlib import Path

warnings.filterwarnings("ignore", message="CUDA path could not be detected*", category=UserWarning)

try:
    import spacy  # type: ignore
except Exception:
    spacy = None

try:
    import yaml  # type: ignore
except Exception:
    yaml = None

PUNCT_RE = re.compile(r"([.,!?;:()\"“”])")
SPACE_RE = re.compile(r"\s+")

_PL_NLP = None
_PL_ALIASES = None


@dataclass(frozen=True)
class Lexicon:
    pl2lx: dict[str, list[str]]
    lx2pl: dict[str, list[str]]
    pl_phrases: dict[tuple[str, ...], list[str]]
    max_pl_len: int


def normalize_pl(text: str) -> str:
    text = text.strip()
    text = text.replace("„", "\"").replace("”", "\"").replace("“", "\"")
    text = PUNCT_RE.sub(r" \1 ", text)
    text = SPACE_RE.sub(" ", text)
    return text.strip().lower()


def normalize_lx(text: str) -> str:
    text = text.strip()
    text = text.replace("„", "\"").replace("”", "\"").replace("“", "\"")
    text = PUNCT_RE.sub(r" \1 ", text)
    text = SPACE_RE.sub(" ", text)
    return text.strip().lower()


def load_tsv(path: Path) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    for raw in path.read_text(encoding="utf8").splitlines():
        raw = raw.strip()
        if not raw or raw.startswith("#"):
            continue
        parts = raw.split("\t")
        if len(parts) != 2:
            continue
        rows.append((parts[0].strip(), parts[1].strip()))
    return rows


def load_lexicon(out_dir: Path) -> Lexicon:
    pl2lx_rows = load_tsv(out_dir / "lexicon_pl2lx.tsv")
    lx2pl_rows = load_tsv(out_dir / "lexicon_lx2pl.tsv")
    pl2lx: dict[str, list[str]] = {}
    lx2pl: dict[str, list[str]] = {}
    pl_phrases: dict[tuple[str, ...], list[str]] = {}
    max_pl_len = 1
    for pl, lx in pl2lx_rows:
        pl2lx.setdefault(pl, [])
        if lx not in pl2lx[pl]:
            pl2lx[pl].append(lx)
        pl_norm = normalize_pl(pl)
        if pl_norm:
            key = tuple(pl_norm.split(" "))
            pl_phrases.setdefault(key, [])
            if lx not in pl_phrases[key]:
                pl_phrases[key].append(lx)
            max_pl_len = max(max_pl_len, len(key))
    for lx, pl in lx2pl_rows:
        lx2pl.setdefault(lx, [])
        if pl not in lx2pl[lx]:
            lx2pl[lx].append(pl)
    return Lexicon(pl2lx=pl2lx, lx2pl=lx2pl, pl_phrases=pl_phrases, max_pl_len=max_pl_len)


def join_pl(tokens: list[str]) -> str:
    out: list[str] = []
    for t in tokens:
        if t in {".", ",", "!", "?", ";", ":", ")"}:
            if out:
                out[-1] = out[-1] + t
            else:
                out.append(t)
        elif t in {"(", "\""}:
            out.append(t)
        else:
            if out and out[-1] == "\"":
                out[-1] = out[-1] + t
            else:
                out.append(t)
    # poprawiamy cudzysłowy (prosto: sklejamy bez spacji po otwarciu)
    s = " ".join(out)
    s = s.replace("\" ", "\"").replace(" \"", "\"")
    # kapitalizacja zdaniowa (minimalna)
    if s:
        s = s[0].upper() + s[1:]
    return s


def join_lx(tokens: list[str]) -> str:
    out: list[str] = []
    for t in tokens:
        if t in {".", ",", "!", "?", ";", ":", ")"}:
            if out:
                out[-1] = out[-1] + t
            else:
                out.append(t)
        elif t in {"(", "\""}:
            out.append(t)
        else:
            if out and out[-1] == "\"":
                out[-1] = out[-1] + t
            else:
                out.append(t)
    s = " ".join(out)
    s = s.replace("\" ", "\"").replace(" \"", "\"")
    return s


def pl_to_lx(text: str, lex: Lexicon, strict: bool) -> tuple[str, dict]:
    tokens_surface: list[str]
    tokens_lemma: list[str]

    tokens_surface = normalize_pl(text).split()
    tokens_lemma = tokens_surface

    spacy_used = False
    aliases_used = False
    drop_lemmas: set[str] = set()
    lemma_aliases: dict[str, str] = {}
    pronoun_cases: dict[str, str] = {}

    if yaml is not None:
        try:
            global _PL_ALIASES
            if _PL_ALIASES is None:
                alias_path = Path(__file__).resolve().parent / "pl_aliases.yaml"
                if alias_path.exists():
                    _PL_ALIASES = yaml.safe_load(alias_path.read_text(encoding="utf8")) or {}
                else:
                    _PL_ALIASES = {}
            lemma_aliases = dict((_PL_ALIASES.get("lemma_aliases") or {}))
            pronoun_cases = dict((_PL_ALIASES.get("pronoun_cases") or {}))
            drop_lemmas = set((_PL_ALIASES.get("drop_lemmas") or []))
        except Exception:
            pass

    if spacy is not None:
        try:
            global _PL_NLP
            if _PL_NLP is None:
                _PL_NLP = spacy.load("pl_core_news_sm")
            doc = _PL_NLP(text)
            surface: list[str] = []
            lemma: list[str] = []
            for t in doc:
                if t.is_space:
                    continue
                if t.is_punct:
                    tok = normalize_pl(t.text)
                    if tok:
                        surface.extend(tok.split())
                        lemma.extend(tok.split())
                    continue
                surface.append(t.text.lower())
                l = (t.lemma_ or t.text).lower()
                if l == "-pron-":
                    l = t.text.lower()
                if l in pronoun_cases:
                    l = pronoun_cases[l]
                    aliases_used = True
                if l in lemma_aliases:
                    l = lemma_aliases[l]
                    aliases_used = True
                lemma.append(l)
            tokens_surface = surface
            tokens_lemma = lemma
            spacy_used = True
        except Exception:
            spacy_used = False

    out: list[str] = []
    unknown: list[str] = []

    i = 0
    while i < len(tokens_surface):
        tok = tokens_surface[i]
        if tok in {".", ",", "!", "?", ";", ":", "(", ")", "\""}:
            out.append(tok)
            i += 1
            continue

        # Heurystyka negacji: "nie" przed czasownikiem → daoo (zamiast nai)
        if tokens_lemma[i] == "nie" and i + 1 < len(tokens_lemma):
            nxt = tokens_lemma[i + 1]
            if nxt not in {".", ",", "!", "?", ";", ":", "(", ")", "\""}:
                out.append("daoo")
                aliases_used = True
                i += 1
                continue

        matched = False
        max_len = min(lex.max_pl_len, len(tokens_surface) - i)
        for l in range(max_len, 0, -1):
            key_surface = tuple(tokens_surface[i : i + l])
            cand = lex.pl_phrases.get(key_surface)
            if cand:
                chosen = cand[0]
                if l == 1 and key_surface[0] == "przyjmować" and "nong-ci" in cand:
                    look = tokens_lemma[i + 1 : i + 6]
                    if "uczeń" in look or "uczniowie" in look:
                        chosen = "nong-ci"
                out.append(chosen)
                i += l
                matched = True
                break
            key_lemma = tuple(tokens_lemma[i : i + l])
            cand = lex.pl_phrases.get(key_lemma)
            if cand:
                chosen = cand[0]
                if l == 1 and key_lemma[0] == "przyjmować" and "nong-ci" in cand:
                    look = tokens_lemma[i + 1 : i + 6]
                    if "uczeń" in look or "uczniowie" in look:
                        chosen = "nong-ci"
                out.append(chosen)
                i += l
                matched = True
                break
        if matched:
            continue

        # jeśli to "pusty" lemat (np. przyimek) i nie weszło w frazę, można pominąć
        if tokens_lemma[i] in drop_lemmas:
            aliases_used = True
            i += 1
            continue
        unknown.append(tok)
        out.append(f"[[{tok}]]" if strict else tok)
        i += 1

    analysis = {
        "direction": "pl2lx",
        "unknown": unknown,
        "strict": strict,
        "spacy": spacy_used,
        "aliases": aliases_used,
    }
    if strict and unknown:
        raise ValueError(f"Nieznane tokeny PL: {', '.join(unknown)}")
    return join_lx(out), analysis


def lx_to_pl(text: str, lex: Lexicon, strict: bool) -> tuple[str, dict]:
    norm = normalize_lx(text)
    tokens = norm.split() if norm else []
    out: list[str] = []
    unknown: list[str] = []

    # minimalne reguły: zdejmij końcowe mo -> pytajnik
    question = False
    if tokens and tokens[-1] == "?":
        question = True
        tokens = tokens[:-1]
    if tokens and tokens[-1] == "mo":
        question = True
        tokens = tokens[:-1]
    if tokens and len(tokens) >= 2 and tokens[-2] == "mo" and tokens[-1] == "?":
        question = True
        tokens = tokens[:-2]

    for tok in tokens:
        if tok in {".", ",", "!", "?", ";", ":", "(", ")", "\""}:
            out.append(tok)
            continue
        cand = lex.lx2pl.get(tok)
        if not cand:
            unknown.append(tok)
            out.append(f"[[{tok}]]" if strict else tok)
        else:
            out.append(cand[0])

    if question:
        out.append("?")

    analysis = {"direction": "lx2pl", "unknown": unknown, "strict": strict, "question": question}
    if strict and unknown:
        raise ValueError(f"Nieznane tokeny LX: {', '.join(unknown)}")
    return join_pl(out), analysis


def main() -> int:
    p = argparse.ArgumentParser(description="Szybki tłumacz PL↔Lengxuan (regułowy, offline)")
    p.add_argument("--dir", default="out", help="katalog z lexicon_*.tsv (domyślnie: out)")
    p.add_argument("--pl2lx", action="store_true", help="tłumacz z polskiego na Lengxuan")
    p.add_argument("--lx2pl", action="store_true", help="tłumacz z Lengxuan na polski")
    p.add_argument("--strict", action="store_true", help="błąd na nieznanych tokenach; inaczej przepuszcza")
    p.add_argument("--json", action="store_true", help="zwraca wynik + analizę w JSON")
    p.add_argument("text", nargs="*", help="tekst do tłumaczenia (gdy puste: czyta stdin)")
    args = p.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

    if args.pl2lx == args.lx2pl:
        print("Wybierz dokładnie jedno: --pl2lx albo --lx2pl", file=sys.stderr)
        return 2

    base = Path(__file__).resolve().parent
    out_dir = Path(args.dir)
    if not out_dir.is_absolute():
        out_dir = base / out_dir

    lex = load_lexicon(out_dir)

    text = " ".join(args.text).strip()
    if not text:
        text = sys.stdin.read().strip()

    try:
        if args.pl2lx:
            out, analysis = pl_to_lx(text, lex, args.strict)
        else:
            out, analysis = lx_to_pl(text, lex, args.strict)
    except ValueError as e:
        print(str(e), file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps({"input": text, "output": out, "analysis": analysis}, ensure_ascii=False))
    else:
        print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
