# Normalizacja tekstu (PL↔Lengxuan)

## Wejście PL
- Lowercase do lematyzacji, ale zachowuj oryginalną wielkość liter przy składaniu wyniku.
- Zamieniaj „ą/ę/ó/ł/ś/ć/ń/ż/ź” na odpowiedniki bez zmian (słownik zawiera diakrytyki PL).
- Usuwaj podwójne spacje, standaryzuj cudzysłowy na „”.
- Tokenizuj interpunkcję jako osobne tokeny.

## Wejście Lengxuan
- Normalizuj do NFC, zachowaj diakrytyki (ü, ǎ, ǒ).
- Obniżaj litery; nazwy własne rozpoznawaj z kontekstu (lista w słowniku).
- `sen`, `mo`, `ban`, `nei`, `daoo`, `lo`, `zhai`, `jiao` traktuj jako odrębne tokeny (nie łącz).
- Rozpoznawaj „re-mang” i inne z łącznikiem jako jeden token.

## Wyjście
- PL: kapitalizacja zdaniowa, interpunkcja przyklejona z prawej.
- LX: brak kapitalizacji obowiązkowej; w trybie „pretty” kapitalizuj nazwy własne (z listy).

## Nie zmieniamy
- Liczb, dat ani nazw własnych już otagowanych w słowniku (np. `ashikagama`, `heijiro`).

