# -*- coding: utf-8 -*-
"""
Dodaje brakujące słowa z dialogów Lao Longa do słownika
"""

import re

def load_dict(path):
    """Wczytuje słownik"""
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'^- ([A-Za-zęóąśłżźćńĘÓĄŚŁŻŹĆŃüÜ-]+) - (.+)$'
    entries = re.findall(pattern, content, re.MULTILINE)

    word_dict = {}
    for word, meaning in entries:
        normalized = word.lower().strip()
        word_dict[normalized] = (word, meaning.strip())

    return word_dict

def add_new_words():
    """Dodaje nowe słowa do słownika"""
    new_words = [
        ("Fan-yi", "Tłumacz"),
        ("Jian-nan", "Trudność, próba"),
        ("Jian-nan-shi", "Próby, trudne testy"),
        ("Jin-ru", "Wejść, wkroczyć"),
        ("Ming-bai", "Rozumieć, być jasnym"),
        ("Rao", "Niepokoić, przeszkadzać"),
        ("Shou-tu", "Przyjmować uczniów"),
        ("Ye-suan", "W porządku, też dobrze"),
        ("Ying-gai", "Powinien, należy"),
    ]

    return new_words

def save_dict(word_dict, output_path):
    """Zapisuje słownik"""
    sorted_entries = sorted(word_dict.items(), key=lambda x: x[1][0].lower())

    output = f"""# Slownik Lengxuan - KOMPLETNY (3000+ slow)

**Liczba wpisow:** {len(sorted_entries)}
**Ostatnia aktualizacja:** 2026-01-04

**Status:** *** CEL OSIAGNIETY!!! *** (3000+)

---

"""

    for normalized, (word, meaning) in sorted_entries:
        output += f"- {word} - {meaning}\n"

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"Zapisano slownik: {len(sorted_entries)} slow")

def main():
    print("Dodawanie brakujacych slow do slownika...")

    dict_path = "../03_Slownik/slownik_lengxuan_polski.md"
    output_path = "../03_Slownik/slownik_lengxuan_polski.md"

    # Wczytaj słownik
    word_dict = load_dict(dict_path)
    print(f"Zaladowano: {len(word_dict)} slow")

    # Dodaj nowe słowa
    new_words = add_new_words()
    added = 0

    for word, meaning in new_words:
        normalized = word.lower().strip()
        if normalized not in word_dict:
            word_dict[normalized] = (word, meaning)
            added += 1
            print(f"  + Dodano: {word} - {meaning}")
        else:
            print(f"  ~ Juz jest: {word}")

    print(f"\nDodano {added} nowych slow")
    print(f"Laczna liczba slow: {len(word_dict)}")

    # Zapisz
    save_dict(word_dict, output_path)
    print("\nGotowe!")

if __name__ == "__main__":
    main()
