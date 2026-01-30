# Specyfikacja tłumacza PL↔Lengxuan (wersja startowa)

## 1) Tokenizacja
- Oddzielamy interpunkcję `.,?!;:` jako osobne tokeny.
- Apostrof i łącznik traktujemy jako część tokenu (np. „nie‑”, „re-mang”).
- Diakrytyki (ü, ǎ, ǒ) zachowujemy; normalizacja do NFC.
- Liczby arabskie można pozostawić lub rozwijać słownie (opcjonalny tryb).

## 2) Morfoskładnia Lengxuan (skrót)
- Szyk podstawowy **SVO**.
- Partykuły:
  - `zhai` (POS/określenie)
  - `mo` (pytanie)
  - `daoo` (negacja), `nai` (samodzielne „nie”)
  - `nei` (aspekt trwający)
  - `ban` (sugestia / tag)
  - `lo` (temat)
  - `sen` (marker liczby mnogiej)
  - `jiao` (jeśli)
- Pytanie = zdanie + `mo`.
- Negacja = `daoo` + czasownik.
- Posiadanie = X `zhai` Y.
- Czas przez słowa czasu przed czasownikiem.

## 3) Fonologia / zapis
- Romanizacja bez tonów; używamy 26 podstawowych liter + diakrytyki dla kolizji lub „chińskiego smaku”:
  - Ü/ü zachowana jak w słowniku.
  - Dodatkowe opcjonalne znaki: ǎ, ǒ (użyte w nowych hasłach, patrz `extra_terms.yaml`), nie zmieniają wymowy bazowej, tylko rozróżniają lemat.
- Brak bezpośrednich zapożyczeń z chińskiego — formy mogą być podobne, ale nie identyczne.

## 4) Mapowanie słów
- Źródło prawdy: `03_Slownik/slownik_polski_lengxuan.md` oraz `slownik_lengxuan_polski.md`.
- Nowe/missing hasła trzymamy w `extra_terms.yaml`; skrypt je scala.
- W słowniku maszynowym każde hasło ma pola: `lemma_pl`, `lemma_lx`, `pos` (jeśli możliwe), `gloss`, `flags`.

## 5) Reguły translacji (rdzeń regułowy)
- **PL→LX:**
  - Mapuj lematy przez słownik; przy wieloznaczności wybieraj najczęstsze (freq tag) albo wypisz kilka wariantów (tryb wielowariantowy).
  - Zachowuj szyk SVO; przy czasownikach modalnych (musieć, móc) → `hu`, `pao-he`.
  - Warunek „jeśli” → `jiao [klauzula], [skutek]`.
  - „Nie” zdaniowe → `daoo` przed czasownikiem; samotne „nie” → `nai`.
  - Liczba mnoga rzeczownika → dodaj `sen` (opcjonalnie, gdy w PL jawne “-owie/-y/-e”).
  - Posiadanie „X-y Y” → `X zhai Y`.
  - Pytania → dopisz `mo` na końcu.
  - „skąd/z (źródło)” wspiera przyimek `rǎo` oraz zaimek pyt. `hen-rǎo`.
- **LX→PL:**
  - Rozpoznaj partykuły i zdejmij `mo` (pytanie), `daoo` (negacja), `nei` (aspekt).
  - `zhai` → „(X) of/’s” → w PL dopełniacz lub przymiotnikowa fraza.
  - `sen` → liczba mnoga, jeśli brak innego wskazania.
  - `ban` → „czyż nie / prawda / zróbmy”.
  - `lo` → przesunięcie tematu: w PL zwykle „a X?” lub pauza.

## 6) Priorytety jakości
1. Poprawność leksykalna (zgodność z bazą + `extra_terms`).
2. Spójność składni (partykuły na właściwych pozycjach).
3. Deterministyczność: ten sam input → ten sam output w trybie „strict”.
4. Szybkość: czysto lokalne reguły + tablice; brak modelu = natychmiastowy wynik.
5. Rozszerzalność: możliwość podpięcia modelu ML jako „rerankera” wariantów.

## 7) Reprezentacje wyjściowe
- **TSV** do prostych lookupów.
- **JSONL** (pole `analysis`) dla debugowania: tokeny, lemat, pozycja, zastosowane reguły.

## 8) Testy i ewaluacja (propozycja)
- Smoke: przetłumacz `parallel_seed.tsv` w obie strony → oczekiwane ≈ oryginał.
- Coverage: raport `missing_report.txt` z budowy słownika.
- Regresja: zatrzaski na stałe przykłady (dialogi Ryujin, szybki start).
