# -*- coding: utf-8 -*-
"""
ANALIZA FINALNEGO SŁOWNIKA LENGXUAN
Sprawdza homonimię w finalnym słowniku 3000+ słów
"""

import re
from collections import defaultdict

def load_dict_from_markdown(file_path):
    """Wczytuje słownik z pliku Markdown"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Wzór: - Słowo - Znaczenie
        pattern = r'^- ([A-Za-zęóąśłżźćńĘÓĄŚŁŻŹĆŃüÜ-]+) - (.+)$'
        entries = re.findall(pattern, content, re.MULTILINE)

        return entries
    except FileNotFoundError:
        print(f"[BLAD] Nie znaleziono pliku: {file_path}")
        return []

def analyze_homonyms(entries):
    """Analizuje homonimię w słowniku"""
    # Grupuj według słów (case-insensitive)
    word_dict = defaultdict(list)

    for word, meaning in entries:
        normalized = word.lower().strip()
        word_dict[normalized].append((word, meaning.strip()))

    # Znajdź homonimyho
    homonyms = {}
    for normalized_word, meanings_list in word_dict.items():
        if len(meanings_list) > 1:
            homonyms[normalized_word] = meanings_list

    return word_dict, homonyms

def print_statistics(entries, word_dict, homonyms):
    """Wypisuje statystyki"""
    print("=" * 60)
    print("ANALIZA SLOWNIKA LENGXUAN - RAPORT FINALNY")
    print("=" * 60)

    print(f"\nCALKOWITA LICZBA WPISOW: {len(entries)}")
    print(f"UNIKALNE SLOWA (bez duplikatow): {len(word_dict)}")
    print(f"HOMONIMOW ZNALEZIONYCH: {len(homonyms)}")

    if homonyms:
        total_homonym_entries = sum(len(meanings) for meanings in homonyms.values())
        homonym_percentage = (len(homonyms) / len(word_dict)) * 100

        print(f"PROCENTOWO HOMONIMOW: {homonym_percentage:.2f}%")
        print(f"CALKOWITA LICZBA WPISOW HOMONIMICZNYCH: {total_homonym_entries}")

        print("\n" + "=" * 60)
        print("LISTA HOMONIMOW:")
        print("=" * 60)

        # Sortuj homonimyms według liczby znaczeń (malejąco)
        sorted_homonyms = sorted(homonyms.items(),
                                key=lambda x: len(x[1]),
                                reverse=True)

        for normalized_word, meanings_list in sorted_homonyms:
            print(f"\n[{normalized_word.upper()}] - {len(meanings_list)} znaczen:")
            for original_word, meaning in meanings_list:
                print(f"  - {original_word} = {meaning}")
    else:
        print("\nBRAK HOMONIMOW! Slownik jest czysty.")

    print("\n" + "=" * 60)
    print("PODSUMOWANIE:")
    print("=" * 60)

    if len(homonyms) == 0:
        status = "DOSKONALY"
        homonym_percentage = 0.0
    elif homonym_percentage < 5:
        status = "BARDZO DOBRY"
    elif homonym_percentage < 10:
        status = "DOBRY"
    elif homonym_percentage < 20:
        status = "ZADOWALAJACY"
    else:
        status = "WYMAGA POPRAWY"

    print(f"STATUS SLOWNIKA: {status}")
    print(f"Liczba slow: {len(word_dict)}")
    print(f"Homonimow: {len(homonyms)} ({homonym_percentage:.2f}%)")

    if len(entries) >= 3000:
        print(f"\nCEL 3000+ SLOW: OSIAGNIETY!")
        print(f"Przekroczono o: {len(entries) - 3000} slow")

    print("=" * 60)

def main():
    dict_path = "../03_Slownik/slownik_lengxuan_polski.md"

    print("Ladowanie slownika...")
    entries = load_dict_from_markdown(dict_path)

    if not entries:
        print("Nie znaleziono wpisow slownikowych!")
        return

    print(f"Zaladowano {len(entries)} wpisow")

    print("\nAnalizowanie homonimii...")
    word_dict, homonyms = analyze_homonyms(entries)

    print_statistics(entries, word_dict, homonyms)

    # Zapisz raport do pliku
    report_path = "../05_Dokumentacja/raport_homonimii_final.txt"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("RAPORT HOMONIMII - SLOWNIK LENGXUAN FINAL\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Calkowita liczba wpisow: {len(entries)}\n")
        f.write(f"Unikalne slowa: {len(word_dict)}\n")
        f.write(f"Homonimow: {len(homonyms)}\n\n")

        if homonyms:
            f.write("LISTA HOMONIMOW:\n")
            f.write("-" * 60 + "\n\n")

            sorted_homonyms = sorted(homonyms.items(),
                                    key=lambda x: len(x[1]),
                                    reverse=True)

            for normalized_word, meanings_list in sorted_homonyms:
                f.write(f"[{normalized_word.upper()}] - {len(meanings_list)} znaczen:\n")
                for original_word, meaning in meanings_list:
                    f.write(f"  - {original_word} = {meaning}\n")
                f.write("\n")
        else:
            f.write("BRAK HOMONIMOW!\n")

    print(f"\nRaport zapisany do: {report_path}")

if __name__ == "__main__":
    main()
