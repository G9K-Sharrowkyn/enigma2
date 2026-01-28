# -*- coding: utf-8 -*-
"""
SPRAWDZANIE DUPLIKATÓW W SŁOWNIKU LENGXUAN
Wykrywa:
1. Dosłowne duplikaty (to samo słowo >1 raz)
2. Duplikaty wielkości liter (np. "Bai" i "bai")
3. Duplikaty znaczeń (różne słowa, to samo znaczenie)
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

def check_exact_duplicates(entries):
    """Sprawdza dosłowne duplikaty (to samo słowo, to samo znaczenie)"""
    seen = {}
    exact_duplicates = []

    for word, meaning in entries:
        key = (word.strip(), meaning.strip())
        if key in seen:
            exact_duplicates.append((word, meaning, seen[key]))
        else:
            seen[key] = len(exact_duplicates) + 1

    return exact_duplicates

def check_word_duplicates(entries):
    """Sprawdza duplikaty słów (to samo słowo, różne znaczenia)"""
    word_dict = defaultdict(list)

    for word, meaning in entries:
        word_dict[word.strip()].append(meaning.strip())

    # Znajdź słowa z >1 znaczeniem
    duplicates = {}
    for word, meanings in word_dict.items():
        if len(meanings) > 1:
            duplicates[word] = meanings

    return duplicates

def check_case_variants(entries):
    """Sprawdza warianty wielkości liter (np. Bai vs bai)"""
    word_dict = defaultdict(list)

    for word, meaning in entries:
        normalized = word.lower().strip()
        word_dict[normalized].append((word, meaning.strip()))

    # Znajdź warianty
    variants = {}
    for normalized, word_list in word_dict.items():
        if len(word_list) > 1:
            # Sprawdź czy są różne wersje wielkości liter
            unique_words = set(w[0] for w in word_list)
            if len(unique_words) > 1:
                variants[normalized] = word_list

    return variants

def check_meaning_duplicates(entries):
    """Sprawdza duplikaty znaczeń (różne słowa, podobne znaczenia)"""
    meaning_dict = defaultdict(list)

    for word, meaning in entries:
        # Normalizuj znaczenie (lowercase, usuń białe znaki)
        normalized_meaning = meaning.strip().lower()
        meaning_dict[normalized_meaning].append(word.strip())

    # Znajdź znaczenia z >1 słowem
    duplicates = {}
    for meaning, words in meaning_dict.items():
        if len(words) > 1:
            duplicates[meaning] = words

    return duplicates

def print_results(entries, exact_dups, word_dups, case_variants, meaning_dups):
    """Wypisuje wyniki"""
    total = len(entries)

    print("=" * 70)
    print("SPRAWDZANIE DUPLIKATOW - SLOWNIK LENGXUAN")
    print("=" * 70)

    print(f"\nCalkowita liczba wpisow: {total}")

    # 1. Dosłowne duplikaty
    print("\n" + "=" * 70)
    print("1. DOSLOWNE DUPLIKATY (to samo slowo + znaczenie):")
    print("=" * 70)

    if exact_dups:
        print(f"\nZNALEZIONO: {len(exact_dups)} dosłownych duplikatow!")
        for word, meaning, index in exact_dups:
            print(f"  - {word} = {meaning}")
    else:
        print("\nBRAK! Slownik czysty.")

    # 2. Duplikaty słów
    print("\n" + "=" * 70)
    print("2. DUPLIKATY SLOW (to samo slowo, rozne znaczenia = HOMONIMIA):")
    print("=" * 70)

    if word_dups:
        print(f"\nZNALEZIONO: {len(word_dups)} homonimow!")
        for word, meanings in sorted(word_dups.items()):
            print(f"\n  [{word}] - {len(meanings)} znaczen:")
            for meaning in meanings:
                print(f"    - {meaning}")
    else:
        print("\nBRAK! Slownik czysty.")

    # 3. Warianty wielkości liter
    print("\n" + "=" * 70)
    print("3. WARIANTY WIELKOSCI LITER (np. Bai vs bai):")
    print("=" * 70)

    if case_variants:
        print(f"\nZNALEZIONO: {len(case_variants)} wariantow!")
        for normalized, variants in sorted(case_variants.items()):
            print(f"\n  [{normalized}] - {len(variants)} wersji:")
            for word, meaning in variants:
                print(f"    - {word} = {meaning}")
    else:
        print("\nBRAK! Slownik konsekwentny.")

    # 4. Duplikaty znaczeń
    print("\n" + "=" * 70)
    print("4. DUPLIKATY ZNACZEN (rozne slowa, to samo znaczenie):")
    print("=" * 70)

    if meaning_dups:
        print(f"\nZNALEZIONO: {len(meaning_dups)} duplikatow znaczen!")
        print("(To moze byc OK - synonimy sa naturalne w jezykach)")

        # Pokaz tylko pierwsze 20 przykladow
        count = 0
        for meaning, words in sorted(meaning_dups.items()):
            if count >= 20:
                print(f"\n... i {len(meaning_dups) - 20} wiecej")
                break
            print(f"\n  [{meaning}] - {len(words)} slow:")
            for word in words:
                print(f"    - {word}")
            count += 1
    else:
        print("\nBRAK! Kazde slowo ma unikalne znaczenie.")

    # Podsumowanie
    print("\n" + "=" * 70)
    print("PODSUMOWANIE:")
    print("=" * 70)

    issues = []
    if exact_dups:
        issues.append(f"DOSLOWNE DUPLIKATY: {len(exact_dups)}")
    if word_dups:
        issues.append(f"HOMONIMIA: {len(word_dups)}")
    if case_variants:
        issues.append(f"WARIANTY LITER: {len(case_variants)}")

    if issues:
        print("\nZNALEZIONE PROBLEMY:")
        for issue in issues:
            print(f"  - {issue}")
        print("\nSTATUS: WYMAGA NAPRAWY")
    else:
        print("\nBRAK PROBLEMOW!")
        print("STATUS: SLOWNIK CZYSTY I KONSEKWENTNY")

        if meaning_dups:
            print(f"\nUWAGA: Znaleziono {len(meaning_dups)} duplikatow znaczen")
            print("(To moze byc naturalne - synonimy sa OK w jezykach)")

    print("=" * 70)

def main():
    dict_path = "../03_Slownik/slownik_lengxuan_polski.md"

    print("Ladowanie slownika...")
    entries = load_dict_from_markdown(dict_path)

    if not entries:
        print("Nie znaleziono wpisow!")
        return

    print(f"Zaladowano {len(entries)} wpisow\n")

    print("Sprawdzanie duplikatow...")
    exact_dups = check_exact_duplicates(entries)
    word_dups = check_word_duplicates(entries)
    case_variants = check_case_variants(entries)
    meaning_dups = check_meaning_duplicates(entries)

    print_results(entries, exact_dups, word_dups, case_variants, meaning_dups)

    # Zapisz raport
    report_path = "../05_Dokumentacja/raport_duplikatow.txt"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("RAPORT DUPLIKATOW - SLOWNIK LENGXUAN\n")
        f.write("=" * 70 + "\n\n")
        f.write(f"Calkowita liczba wpisow: {len(entries)}\n\n")

        f.write("DOSLOWNE DUPLIKATY: ")
        if exact_dups:
            f.write(f"{len(exact_dups)} znalezionych\n")
            for word, meaning, _ in exact_dups:
                f.write(f"  - {word} = {meaning}\n")
        else:
            f.write("BRAK\n")

        f.write("\nHOMONIMIA (to samo slowo, rozne znaczenia): ")
        if word_dups:
            f.write(f"{len(word_dups)} znalezionych\n")
            for word, meanings in sorted(word_dups.items()):
                f.write(f"\n  [{word}]:\n")
                for meaning in meanings:
                    f.write(f"    - {meaning}\n")
        else:
            f.write("BRAK\n")

        f.write("\nWARIANTY WIELKOSCI LITER: ")
        if case_variants:
            f.write(f"{len(case_variants)} znalezionych\n")
            for normalized, variants in sorted(case_variants.items()):
                f.write(f"\n  [{normalized}]:\n")
                for word, meaning in variants:
                    f.write(f"    - {word} = {meaning}\n")
        else:
            f.write("BRAK\n")

    print(f"\nRaport zapisany do: {report_path}")

if __name__ == "__main__":
    main()
