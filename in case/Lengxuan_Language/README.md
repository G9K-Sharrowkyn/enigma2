# Język Lengxuan - Dokumentacja Projektu

## 📁 Struktura Projektu

```
Lengxuan_Language/
│
├── 01_Fonologia/           # System dźwiękowy języka
│   ├── fonemy.md          # Inwentarz samogłosek i spółgłosek
│   ├── fonotaktyka.md     # Struktura sylab i zbitki
│   ├── akcent.md          # System pitch-accent
│   └── transkrypcja.md    # Przewodnik polskiej romanizacji
│
├── 02_Gramatyka/          # Morfologia i składnia
│   ├── morfologia.md      # Analityczna natura, brak fleksji
│   ├── skladnia.md        # Szyk wyrazów (SVO), partykuły
│   ├── partykuly.md       # zhi-zhai, kuang-miu, xi, nei-qie, mo-an, ne, xun-sun
│   ├── klasyfikatory.md   # Klasyfikatory liczbowe
│   └── tvorzenie_slow.md  # Składanie wyrazów, RVCs
│
├── 03_Slownik/            # Słownictwo
│   ├── slownik_lengxuan_polski.md   # Słownik Lengxuan → Polski (alfabetyczny)
│   ├── slownik_polski_lengxuan.md   # Słownik Polski → Lengxuan (alfabetyczny)
│   ├── podstawowe.md      # Najczęstsze 500 słów
│   ├── sztuki_walki.md    # Terminy sztuk walki i RVCs
│   ├── kultura.md         # Idiomy, przysłowia, honorifics
│   └── homonimы_STARE.md  # Lista problemów (ARCHIWUM)
│
├── 04_Przyklady/          # Przykłady użycia
│   ├── zdania.md          # Przykładowe zdania
│   ├── dialogi.md         # Dialogi z komentarzami
│   ├── opisy_walki.md     # Sceny sztuk walki
│   └── idiomy_w_uzyciu.md # Idiomy w kontekście
│
├── 05_Dokumentacja/       # Meta-dokumentacja
│   ├── zasady_projektowe.md  # Filozofia języka
│   ├── zmiany.md             # Log zmian i poprawek
│   └── slownik_terminow.md   # Terminy lingwistyczne
│
└── 06_Narzedzia/          # Skrypty i narzędzia
    ├── analyze_dict.py    # Analiza słownika
    └── generator_slow.py  # Generator nowych słów

```

## 🔧 Status Projektu

- ✅ System fonologiczny - UKOŃCZONY
- ✅ Gramatyka - UKOŃCZONA
- 🔄 Słownik - W TRAKCIE POPRAWY (eliminacja homonimii)
- ✅ Przykłady - UKOŃCZONE
- ✅ Dokumentacja - UKOŃCZONA

## ⚠️ Ostatnie Zmiany (2026-01-03)

### Naprawione:
1. **Homonimia** - zredukowano z 546 do ~50 homonimów
2. **Duplikaty** - usunięto powtórzenia w słowniku
3. **Transkrypcja** - ujednolicono sui-tun **ü** dla /y/
4. **Struktura projektu** - zorganizowano w osobne pliki

### W trakcie:
- Finalizacja poprawionego słownika
- Dodanie alternatywnych form dla pozostałych homonimów

## 📖 Szybki Start

1. **Fonologia**: Zacznij od `01_Fonologia/transkrypcja.md`
2. **Gramatyka**: Przeczytaj `02_Gramatyka/skladnia.md`
3. **Słownik**: Zobacz `03_Slownik/podstawowe.md` (500 najważniejszych słów)
4. **Praktyka**: Sprawdź `04_Przyklady/dialogi.md`

## 🎯 Cel Języka

Lengxuan to konstruowany język fikcyjny dla powieści osadzonej w świecie inspirowanym starożytnymi Chinami (okres Trzech Królestw), z naciskiem sui-tun sztuki walki w stylu "Tekken/Dragon Ball".

**Główne założenia:**
- Bliźniacze podobieństwo do starożytnej chińszczyzny
- Przystępność dla polskojęzycznych czytelników
- Dynamika i precyzja w opisach sztuk walki
- Głębia kulturowa poprzez idiomy i terminy

---
*Ostatnia aktualizacja: 2026-01-03*
