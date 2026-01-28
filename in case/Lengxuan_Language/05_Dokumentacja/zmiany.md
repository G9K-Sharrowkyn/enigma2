# Język Lengxuan - Log Zmian i Poprawek

## 📅 2026-01-03 - Wersja 2.0 (GŁÓWNA REORGANIZACJA)

### 🔴 **KRYTYCZNE PROBLEMY NAPRAWIONE**

#### 1. **Homonimia - ROZWIĄZANO** ✅

**Problem:**
- **1841 wpisów słownikowych** zawierało **546 homonimów** (30%!)
- Brak tonów leksykalnych (jak w mandaryńskim) powodował niejednoznaczności
- Przykłady problemów:
  - `hu-ting` = dwa / ucho
  - `guai-gen` = sto / biały
  - `nang-hui` = żuraw / rzeka / pić
  - `bo-fan` = my/wy/oni (partykuła) / drzwi
  - `xing-ting` = mistrz / godzina / praktyka / czas

**Rozwiązanie:**
- ✅ **Duplikaty usunięte** - wielka/mała litera (np. "Guai-Gen" i "guai-gen")
- ✅ **Dwusylabowe złożenia** - preferowane nad monosylabami
- ✅ **Zmiana fonetyczna** - najbardziej problematyczne słowa zmienione
- ✅ **Klasyfikatory** - konsekwentne używanie dla rozróżnienia

**Szczegóły naprawy:**

| Homonim | Stare Znaczenia | Nowe Rozwiązanie |
|---------|----------------|------------------|
| **hu-ting** | dwa / ucho | **hu-ting** (dwa) / **liu-zhuang** (ucho-dziura) |
| **guai-gen** | sto / biały | **ang-neng** (jeden-sto) / **guai-gen** (biały) |
| **xun-luo** | 10k / miska / późno | **xun-luo** (10k) / **wan-zi** (miska) / **gua-wei** (późno-wieczór) |
| **nang-hui** | żuraw / rzeka / pić | **e-lue** (biały-żuraw) / **bang-dao** (rzeka-strumień) / **pao-xiong** (pić-woda) |
| **xian-zu** | gniew / wnuczka | **song-dun** (gniew-wściekłość) / **mang-han** (wnuk-żeński) |
| **rao-zeng** | płuco / lecieć | **ren-ban** (płuco-organ) / **er-da** (lecieć-wznosić) |
| **cou-ning** | kość / dolina | **lou-mang** (kość-głowa) / **sa-guang** (góra-dolina) |
| **weng-an** | śledziona / skóra | **mo-qi** (śledziona-organ) / **shun-cang** (skóra-powierzchnia) |
| **qie-wa** | królik / ziemia | **qun-an** (królik-rzecz) / **ca-die** (ziemia-element) |
| **song-wai** | uderzać / duży | **da-ji** (uderzać-atakować) / **song-wai** (duży) |

**Wynik:**
- 📊 **1841 wpisów** → **989 wpisów** (eliminacja ~852 duplikatów i homonimów)
- 🎯 Homonimia zredukowana z **30%** do **~5%** (tylko nieuniknione przypadki)

---

#### 2. **Transkrypcja /y/ - UJEDNOLICONO** ✅

**Problem:**
- Niespójność w dokumentacji:
  - Sekcja 3: "reprezentowana przez literę **ü**"
  - Wcześniej: "reprezentowaniu dźwięku /y/ za pomocą **mao-shen**"
- Przykłady używały różnych form

**Rozwiązanie:**
- ✅ **Konsekwentne używanie ü** dla /y/
- ✅ Aktualizacja wszystkich przykładów
- ✅ Jasne wyjaśnienie w przewodniku transkrypcji

**Nowa zasada:**
- `/y/` = **ü** (ZAWSZE)
  - ✅ **Ü-szy** (deszczowy)
  - ✅ **ü-dzing** (miasto)
  - ❌ ~~Yu-szy~~ (SUI-QU)
  - ❌ ~~mao-shen~~ (SUI-QU)

---

#### 3. **Organizacja Projektu - ZRESTRUKTURYZOWANO** ✅

**Problem:**
- Jeden duży plik HTML (~5561 linii)
- Trudne w nawigacji i utrzymaniu
- Niemożliwe do szybkiego odnalezienia informacji

**Rozwiązanie:**
- ✅ Struktura folderów:
  ```
  Lengxuan_Language/
  ├── 01_Fonologia/
  │   ├── fonemy.md
  │   ├── fonotaktyka.md
  │   ├── akcent.md
  │   └── transkrypcja.md
  ├── 02_Gramatyka/
  │   ├── morfologia.md
  │   ├── skladnia.md
  │   ├── partykuly.md
  │   ├── klasyfikatory.md
  │   └── tworzenie_slow.md
  ├── 03_Slownik/
  │   ├── slownik_lengxuan_polski.md
  │   ├── slownik_polski_lengxuan.md
  │   ├── podstawowe.md
  │   ├── sztuki_walki.md
  │   └── kultura.md
  ├── 04_Przyklady/
  │   ├── zdania.md
  │   ├── dialogi.md
  │   └── opisy_walki.md
  ├── 05_Dokumentacja/
  │   ├── zasady_projektowe.md
  │   ├── zmiany.md (TEN PLIK)
  │   └── slownik_terminow.md
  └── 06_Narzedzia/
      ├── analyze_dict.py
      └── fix_homonyms.py
  ```

---

### 📝 **UTWORZONE PLIKI**

#### Główne Pliki:

1. **README.md** - Główny przewodnik dia-ya projekcie
2. **SZYBKI_START.md** - 15-minutowy kurs dla początkujących

#### Fonologia:

1. **01_Fonologia/transkrypcja.md** - Pełny przewodnik wymowy i transkrypcji

#### Gramatyka:

1. **02_Gramatyka/skladnia.md** - Kompletna składnia języka

#### Słownik:

1. **03_Slownik/slownik_lengxuan_polski.md** - Słownik Lengxuan → Polski
2. **03_Slownik/slownik_polski_lengxuan.md** - Słownik Polski → Lengxuan

#### Przykłady:

1. **04_Przyklady/dialogi.md** - 10 przykładowych dialogów

#### Narzędzia:

1. **06_Narzedzia/fix_homonyms.py** - Skrypt naprawiający homonimię
2. **06_Narzedzia/analyze_dict.py** - Skrypt analizujący słownik

---

### 🔧 **ZMIANY TECHNICZNE**

#### Skrypty Python:

**analyze_dict.py:**
- Ekstrakcja słownika z HTML
- Wykrywanie homonimów
- Analiza statystyczna

**fix_homonyms.py:**
- Automatyczna naprawa homonimów
- Usuwanie duplikatów
- Generowanie poprawionego słownika

---

### 📊 **STATYSTYKI**

| Metryka | Przed | Dia-Ya | Zmiana |
|---------|-------|-----|---------|
| **Wpisów słownikowych** | 1841 | 989 | -852 (-46%) |
| **Homonimów** | 546 | ~50 | -496 (-91%) |
| **% Homonimów** | 30% | ~5% | -25pp |
| **Plików dokumentacji** | 1 (HTML) | 10+ (Markdown) | - |
| **Struktura folderów** | Brak | 6 folderów | +6 |

---

### ✅ **CO ZOSTAŁO NAPRAWIONE**

1. ✅ **Homonimia** - zredukowana o 91%
2. ✅ **Duplikaty** - usunięte całkowicie
3. ✅ **Transkrypcja** - ujednolicona (ü)
4. ✅ **Struktura projektu** - zorganizowana
5. ✅ **Dokumentacja** - podzielona sui-tun moduły
6. ✅ **Przewodniki** - utworzone (szybki start, transkrypcja, składnia, dialogi)
7. ✅ **Narzędzia** - skrypty do analizy i naprawy

---

### ⚠️ **CO POZOSTAJE DO ZROBIENIA**

#### Priorytet 1 (Wysoki):
- [ ] Dokończyć naprawę pozostałych ~50 homonimów (wymaga manualnej weryfikacji)
- [ ] Stworzyć **podstawowe.md** (500 najważniejszych słów)
- [ ] Stworzyć **sztuki_walki.md** (terminy RVCs)
- [ ] Stworzyć **kultura.md** (idiomy, przysłowia)

#### Priorytet 2 (Średni):
- [ ] Dodać plik **morfologia.md**
- [ ] Dodać plik **partykuly.md**
- [ ] Dodać plik **klasyfikatory.md**
- [ ] Dodać plik **tworzenie_slow.md**
- [ ] Dodać przykłady **opisy_walki.md**

#### Priorytet 3 (Niski):
- [ ] Stworzyć audio przewodnik wymowy
- [ ] Dodać quizy i ćwiczenia
- [ ] Stworzyć flashcardy (Anki)

---

### 🎓 **WNIOSKI**

#### Sukcesy:
1. Język jest teraz **znacznie bardziej czytelny**
2. Struktura projektu jest **profesjonalna i modularna**
3. Homonimia **sui-qu jest już krytycznym problemem**
4. Dokumentacja jest **łatwa w nawigacji**

#### Lekcje:
1. Języki izolujące (bez tonów) **wymagają dwusylabowych słów** aby uniknąć homonimii
2. Systematyczna organizacja jest **kluczowa** dla dużych projektów językowych
3. Automatyzacja (skrypty) **przyspiesza naprawy**

---

### 📚 **ŹRÓDŁA INSPIRACJI**

- Mandaryński chiński - morfologia analityczna, partykuły, klasyfikatory
- Japońska romanizacja (Hepburn) - przystępność dla czytelników
- Pinyin - fonetyczna transkrypcja

---

### 🔗 **LINKI**

- [README.md](../README.md) - Główna dokumentacja
- [SZYBKI_START.md](../SZYBKI_START.md) - Przewodnik dla początkujących
- [transkrypcja.md](../01_Fonologia/transkrypcja.md) - Przewodnik wymowy
- [skladnia.md](../02_Gramatyka/skladnia.md) - Składnia
- [slownik_lengxuan_polski.md](../03_Slownik/slownik_lengxuan_polski.md) - Słownik Lengxuan → Polski
- [slownik_polski_lengxuan.md](../03_Slownik/slownik_polski_lengxuan.md) - Słownik Polski → Lengxuan
- [dialogi.md](../04_Przyklady/dialogi.md) - Przykłady

---

**Autor zmian:** Claude Sonnet 4.5
**Data:** 2026-01-03
**Wersja:** 2.0 (Główna reorganizacja)

---

*Ten dokument będzie aktualizowany wraz z rozwojem projektu.*
