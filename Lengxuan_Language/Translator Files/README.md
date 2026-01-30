# Translator Files — zestaw startowy

Cel: przygotować dane i zasady, by dało się zbudować **deterministyczny, natychmiastowy tłumacz PL↔Lengxuan**, zgodny z najnowszymi słownikami `03_Slownik/`, bez mieszania z chińskim źródłowym.

## Skład pakietu
- `spec.md` — zasady translacji (tokenizacja, partykuły, diakrytyki, brak tonów).
- `normalization_rules.md` — reguły normalizacji tekstu wejściowego/wyjściowego.
- `extra_terms.yaml` — propozycje nowych haseł (np. „skąd”, przyimki źródła), które są brakujące w `03_Slownik/`.
- `build_lexicon.py` — skrypt generujący maszynowe słowniki (TSV/JSONL) z `03_Slownik/` + `extra_terms.yaml`.
- `translator_cli.py` — proste CLI do tłumaczenia offline (regułowe, natychmiastowe).
- `pl_aliases.yaml` — aliasy lematów PL (np. „tu”→„tutaj”, przypadki zaimków) + lista lematów do pomijania.
- `parallel_seed.tsv` — startowy korpus równoległy (PL ↔ Lengxuan) do testów / ewaluacji.
- `generate_corpus.py` + `core_vocab.yaml` — generator syntetycznego korpusu (tysiące par zdań).
- `out/` — aktualne wygenerowane słowniki (po scaleniu extra_terms do głównych słowników).

## Jak wygenerować słowniki maszynowe
```
cd ..  # (katalog Lengxuan_Language)
python "Translator Files/build_lexicon.py" --out "Translator Files/out"
```
Powstanie:
- `out/lexicon_pl2lx.tsv`
- `out/lexicon_lx2pl.tsv`
- `out/lexicon_pl2lx.jsonl`
- `out/lexicon_lx2pl.jsonl`
- raport braków w `out/missing_report.txt` (jeśli są)

## Jak użyć tłumacza CLI (offline)
```
python "Translator Files/translator_cli.py" --pl2lx "Dziękuję."
python "Translator Files/translator_cli.py" --lx2pl "poye."
```
Uwagi:
- PL→LX używa lematyzacji przez `pl_core_news_sm` (spaCy), jeśli jest dostępna lokalnie.

## Jak wygenerować tysiące zdań do testów
```
cd "Translator Files"
python generate_corpus.py --count 5000
```

## Smoke test
```
cd "Translator Files"
python smoke_test.py
```

## Web (React)
Projekt React jest w `Translator Files/web/`.

Uruchomienie:
```
cd "Translator Files/web"
npm install
npm run dev
```

Aktualizacja słowników w aplikacji web (po zmianach w `03_Slownik/`):
```
cd "Translator Files/web"
powershell -ExecutionPolicy Bypass -File sync_lexicons.ps1
```

## Założenia jakości
- **Deterministyczność**: najpierw reguły i słownik; ewentualne AI tylko jako „post‑edit”.
- **Spójność**: bazą jest `03_Slownik/`; `extra_terms.yaml` jest strefą roboczą (jeśli chcesz dodać kolejne brakujące hasła).
- **Status**: bieżąca wersja słowników zawiera już nowe hasła (`rǎo`, `hen-rǎo`, `rǎo-ci`, `lie-xu`, `ying-shun`, `laio-shun`, `deo-re`, `wai-que`, `chen-zhang`); `out/` jest zregenerowane.
- **Brzmienie chińskie**: zachowujemy romanizację bez tonów; dodajemy diakrytyki tylko jako rozróżniki (np. ü, ǎ, ǒ) tam, gdzie wzbogaca brzmienie, ale nie łamiemy prostoty bazowych słów.
- **Brak kalek**: żadnych bezpośrednich kopiowań z chińskiego standardowego — formy mogą być podobne, ale nie identyczne.

## Co dalej?
- Rozszerzać `parallel_seed.tsv` i `corpus/generated.tsv` o kolejne przykłady (im więcej, tym lepsza ewaluacja).
- Wprowadzić kolejne reguły składniowe (np. lepsza obsługa negacji, pytań, „zhai” w złożeniach).
- (Opcjonalnie) dodać tryb „AI post-edit” jako osobny przełącznik, ale rdzeń offline zostawić deterministyczny.
