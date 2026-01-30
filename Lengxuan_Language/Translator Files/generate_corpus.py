#!/usr/bin/env python3
from __future__ import annotations

import argparse
import random
import re
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:
    yaml = None


def parse_args():
    p = argparse.ArgumentParser(description="Generator syntetycznego korpusu PL↔Lengxuan (do testów)")
    p.add_argument("--lexdir", default="out", help="katalog z lexicon_lx2pl.tsv (domyślnie: out)")
    p.add_argument("--vocab", default="core_vocab.yaml", help="plik YAML z listami tokenów")
    p.add_argument("--out", default="corpus/generated.tsv", help="plik wyjściowy TSV")
    p.add_argument("--count", type=int, default=5000, help="liczba par zdań (domyślnie 5000)")
    p.add_argument("--seed", type=int, default=13, help="seed losowania")
    p.add_argument("--auto-extra", type=int, default=300, help="ile dodatkowych tokenów LX dodać jako obiekty")
    return p.parse_args()


def load_tsv(path: Path) -> dict[str, list[str]]:
    d: dict[str, list[str]] = {}
    for raw in path.read_text(encoding="utf8").splitlines():
        raw = raw.strip()
        if not raw or raw.startswith("#"):
            continue
        a, b = raw.split("\t", 1)
        d.setdefault(a, [])
        if b not in d[a]:
            d[a].append(b)
    return d


def join_pl(tokens: list[str]) -> str:
    out: list[str] = []
    for t in tokens:
        if t in {".", ",", "!", "?", ";", ":"}:
            if out:
                out[-1] = out[-1] + t
            else:
                out.append(t)
        else:
            out.append(t)
    s = " ".join(out).strip()
    if s:
        s = s[0].upper() + s[1:]
    return s


def join_lx(tokens: list[str]) -> str:
    out: list[str] = []
    for t in tokens:
        if t in {".", ",", "!", "?", ";", ":"}:
            if out:
                out[-1] = out[-1] + t
            else:
                out.append(t)
        else:
            out.append(t)
    return " ".join(out).strip()


def lx_tokens_to_pl(tokens: list[str], lx2pl: dict[str, list[str]]) -> list[str]:
    pl: list[str] = []
    for t in tokens:
        if t in {".", ",", "!", "?", ";", ":"}:
            pl.append(t)
            continue
        pl.append(lx2pl.get(t, [t])[0])
    return pl


def _pick_extra_tokens(lx2pl: dict[str, list[str]], banned: set[str], limit: int) -> list[str]:
    # heuristic: bierzemy krótkie tokeny (żeby brzmiały "bazowo"), bez spacji
    ok = []
    token_re = re.compile(r"^[a-ząćęłńóśźżüǎǒ-]+$", re.IGNORECASE)
    for lx in lx2pl.keys():
        if lx in banned:
            continue
        if " " in lx:
            continue
        if len(lx) < 2 or len(lx) > 10:
            continue
        if not token_re.match(lx):
            continue
        ok.append(lx)
    ok = sorted(set(ok))
    random.shuffle(ok)
    return ok[:limit]


def generate_random_sentences(v, extra_objects: list[str], count: int, seed: int):
    random.seed(seed)
    pron = v["pronouns"]
    places = v["places"]
    nouns = list(v["nouns"]) + list(extra_objects)
    adjs = v["adjectives"]
    vin = v["verbs_intransitive"]
    vtr = v["verbs_transitive"]

    # generujemy "z powtórzeniami", ale staramy się maksymalizować unikalność
    seen: set[str] = set()
    out: list[list[str]] = []

    def emit(tokens: list[str]):
        s = " ".join(tokens)
        if s in seen:
            return False
        seen.add(s)
        out.append(tokens)
        return True

    attempts = 0
    max_attempts = count * 50
    while len(out) < count and attempts < max_attempts:
        attempts += 1
        kind = random.randint(1, 10)
        p = random.choice(pron)

        if kind == 1:
            tokens = [p, random.choice(vtr), random.choice(nouns), "."]
        elif kind == 2:
            tokens = [p, "daoo", random.choice(vtr), random.choice(nouns), "."]
        elif kind == 3:
            tokens = [p, "ai", random.choice(adjs), "."]
        elif kind == 4:
            tokens = [p, "zhai", random.choice(nouns), "."]
        elif kind == 5:
            tokens = [p, "ai", random.choice(places), "mo"]
        elif kind == 6:
            tokens = [p, "rǎo-ci", random.choice(places), "."]
        elif kind == 7:
            tokens = ["jiao", p, "ji", random.choice(nouns), ",", p, "ju", "zhe", "."]
        elif kind == 8:
            tokens = [random.choice(vin), random.choice(places), "."]
        elif kind == 9:
            tokens = [p, random.choice(vin), "."]
        else:
            tokens = [p, random.choice(vtr), random.choice(nouns), "mo"]

        emit(tokens)

    # jeśli zabrakło unikalnych, dobijamy powtórkami (żeby count zawsze był spełniony)
    if len(out) < count:
        random.shuffle(out)
        while len(out) < count and out:
            out.append(random.choice(out))
    return out


def main() -> int:
    if yaml is None:
        print("Brak PyYAML — nie mogę wczytać core_vocab.yaml", flush=True)
        return 1

    args = parse_args()
    base = Path(__file__).resolve().parent
    lexdir = Path(args.lexdir)
    if not lexdir.is_absolute():
        lexdir = base / lexdir
    vocab_path = Path(args.vocab)
    if not vocab_path.is_absolute():
        vocab_path = base / vocab_path
    out_path = Path(args.out)
    if not out_path.is_absolute():
        out_path = base / out_path

    lx2pl = load_tsv(lexdir / "lexicon_lx2pl.tsv")
    v = yaml.safe_load(vocab_path.read_text(encoding="utf8"))

    banned = set(v.get("pronouns", [])) | set(v.get("particles", [])) | {".", ",", "!", "?", ";", ":"}
    extra_objects = _pick_extra_tokens(lx2pl, banned=banned, limit=args.auto_extra)
    chosen = generate_random_sentences(v, extra_objects=extra_objects, count=args.count, seed=args.seed)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf8") as f:
        f.write("pl\tlx\tnote\n")
        for toks in chosen:
            lx = join_lx(toks)
            pl = join_pl(lx_tokens_to_pl([t for t in toks if t != "mo"], lx2pl))
            note = "synthetic"
            f.write(f"{pl}\t{lx}\t{note}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
