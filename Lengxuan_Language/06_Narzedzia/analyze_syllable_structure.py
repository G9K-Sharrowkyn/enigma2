# -*- coding: utf-8 -*-
"""
ANALIZA STRUKTURY SYLABICZNEJ SŁOWNIKA LENGXUAN
Sprawdza proporcje słów mono- vs dwusylabowych vs więcej
"""

import re
from collections import defaultdict

def load_dict_from_markdown(file_path):
    """Wczytuje słownik z pliku Markdown"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        pattern = r'^- ([A-Za-zęóąśłżźćńĘÓĄŚŁŻŹĆŃüÜ-]+) - (.+)$'
        entries = re.findall(pattern, content, re.MULTILINE)

        return entries
    except FileNotFoundError:
        print(f"[BLAD] Nie znaleziono pliku: {file_path}")
        return []

def count_syllables(word):
    """Liczy liczbę sylab w słowie (liczba segmentów oddzielonych myślnikiem + 1)"""
    # Usuń początkowy myślnik jeśli jest (dla partykuł jak -fu, -shi)
    word = word.lstrip('-')

    # Policz myślniki
    if '-' in word:
        return word.count('-') + 1
    else:
        return 1

def analyze_syllable_structure(entries):
    """Analizuje strukturę sylabiczną słownika"""
    syllable_counts = defaultdict(int)
    examples = defaultdict(list)

    for word, meaning in entries:
        syllables = count_syllables(word)
        syllable_counts[syllables] += 1

        # Zbierz przykłady (max 10 na kategorię)
        if len(examples[syllables]) < 10:
            examples[syllables].append((word, meaning))

    return syllable_counts, examples

def print_analysis(entries, syllable_counts, examples):
    """Wypisuje analizę"""
    total = len(entries)

    print("=" * 70)
    print("ANALIZA STRUKTURY SYLABICZNEJ SLOWNIKA LENGXUAN")
    print("=" * 70)

    print(f"\nCalkowita liczba slow: {total}")
    print("\n" + "-" * 70)
    print("ROZKLAD SYLAB:")
    print("-" * 70)

    # Sortuj według liczby sylab
    for syllables in sorted(syllable_counts.keys()):
        count = syllable_counts[syllables]
        percentage = (count / total) * 100

        if syllables == 1:
            label = "MONOSYLABICZNE (1 sylaba)"
        elif syllables == 2:
            label = "DWUSYLABOWE (2 sylaby)"
        elif syllables == 3:
            label = "TRÓJSYLABOWE (3 sylaby)"
        else:
            label = f"{syllables}-SYLABOWE"

        print(f"\n{label}:")
        print(f"  Liczba: {count} slow")
        print(f"  Procent: {percentage:.2f}%")
        print(f"  Przyklady:")

        for word, meaning in examples[syllables][:10]:
            print(f"    - {word} = {meaning}")

    print("\n" + "=" * 70)
    print("PODSUMOWANIE:")
    print("=" * 70)

    mono_count = syllable_counts.get(1, 0)
    di_count = syllable_counts.get(2, 0)
    tri_plus_count = sum(syllable_counts[s] for s in syllable_counts if s >= 3)

    mono_percent = (mono_count / total) * 100
    di_percent = (di_count / total) * 100
    tri_plus_percent = (tri_plus_count / total) * 100

    print(f"\nSLOWA MONOSYLABICZNE (1 sylaba): {mono_count} ({mono_percent:.2f}%)")
    print(f"SLOWA DWUSYLABOWE (2 sylaby): {di_count} ({di_percent:.2f}%)")
    print(f"SLOWA 3+ SYLAB: {tri_plus_count} ({tri_plus_percent:.2f}%)")

    print("\n" + "-" * 70)
    print("POROWNANIE Z PRAWDZIWYM CHINSKIM:")
    print("-" * 70)

    print("\nSTAROZYTNY CHINSKIM (klasyczny):")
    print("  - Monosylabiczne: ~60-70%")
    print("  - Dwusylabowe: ~25-35%")
    print("  - 3+ sylab: ~5-10%")

    print("\nNOWOCZESNY CHINSKIM (mandaryński):")
    print("  - Monosylabiczne: ~20-30%")
    print("  - Dwusylabowe: ~65-75%")
    print("  - 3+ sylab: ~5-10%")

    print("\nLENGXUAN (aktualnie):")
    print(f"  - Monosylabiczne: {mono_percent:.1f}%")
    print(f"  - Dwusylabowe: {di_percent:.1f}%")
    print(f"  - 3+ sylab: {tri_plus_percent:.1f}%")

    print("\n" + "-" * 70)
    print("OCENA:")
    print("-" * 70)

    if mono_percent >= 60:
        status = "STAROŻYTNY STYL (monosylaby dominują)"
        recommendation = "Dobry balans dla starozytnego chinskiego!"
    elif mono_percent >= 40:
        status = "ZRÓWNOWAŻONY (kompromis między starym a nowym)"
        recommendation = "Rozsądny kompromis - unika homonimii, zachowuje zwięzłość."
    elif mono_percent >= 20:
        status = "NOWOCZESNY STYL (dwusylaby dominują)"
        recommendation = "Przypomina nowoczesny mandaryński - bardzo bezpieczny dla homonimii."
    else:
        status = "PRZESADNIE ZŁOŻONY"
        recommendation = "Za dużo złożeń - rozważ uproszczenie."

    print(f"\nSTATUS: {status}")
    print(f"REKOMENDACJA: {recommendation}")

    print("\n" + "=" * 70)
    print("PROBLEM HOMONIMII vs ZWIĘZŁOŚĆ:")
    print("=" * 70)
    print("""
LENGXUAN NIE MA TONÓW LEKSYKALNYCH (jak mandaryński).
W mandaryńskim, "ma" może mieć 4 tony → 4 różne słowa.
W Lengxuan, "ma" = tylko 1 słowo.

OPCJE:
1. WIĘCEJ MONOSYLAB → ryzyko homonimii (ale starożytny styl)
2. WIĘCEJ DWUSYLAB → brak homonimii (ale mniej zwięźle)
3. WPROWADZIĆ TONY → jak mandaryński (ale zmienia system fonologiczny)

AKTUALNIE: Lengxuan używa strategii dwusylabowej, aby uniknąć homonimii.
    """)

    print("=" * 70)

def main():
    dict_path = "../03_Slownik/slownik_lengxuan_polski.md"

    print("Ladowanie slownika...")
    entries = load_dict_from_markdown(dict_path)

    if not entries:
        print("Nie znaleziono wpisow!")
        return

    print(f"Zaladowano {len(entries)} wpisow\n")

    print("Analizowanie struktury sylabicznej...")
    syllable_counts, examples = analyze_syllable_structure(entries)

    print_analysis(entries, syllable_counts, examples)

    # Zapisz raport
    report_path = "../05_Dokumentacja/raport_struktury_sylabicznej.txt"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("RAPORT STRUKTURY SYLABICZNEJ - SLOWNIK LENGXUAN\n")
        f.write("=" * 70 + "\n\n")
        f.write(f"Calkowita liczba slow: {len(entries)}\n\n")

        mono_count = syllable_counts.get(1, 0)
        di_count = syllable_counts.get(2, 0)
        tri_plus_count = sum(syllable_counts[s] for s in syllable_counts if s >= 3)
        total = len(entries)

        f.write(f"Monosylabiczne: {mono_count} ({(mono_count/total)*100:.2f}%)\n")
        f.write(f"Dwusylabowe: {di_count} ({(di_count/total)*100:.2f}%)\n")
        f.write(f"3+ sylab: {tri_plus_count} ({(tri_plus_count/total)*100:.2f}%)\n")

        f.write("\nSZCZEGOLY:\n")
        f.write("-" * 70 + "\n")

        for syllables in sorted(syllable_counts.keys()):
            count = syllable_counts[syllables]
            f.write(f"\n{syllables} sylaba/y: {count} slow\n")
            for word, meaning in examples[syllables]:
                f.write(f"  - {word} = {meaning}\n")

    print(f"\nRaport zapisany do: {report_path}")

if __name__ == "__main__":
    main()
