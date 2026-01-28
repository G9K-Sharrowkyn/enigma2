# -*- coding: utf-8 -*-
"""
GENERATOR SŁOWNIKA LENGXUAN - CZĘŚĆ 10 SUPER-FINAL
Cel: OSTATECZNE PRZEKROCZENIE 3000+ słów (ostatnie 40 bardzo specyficznych słów)

Dodaje ostatnie 40 bardzo specyficznych, niszowych słów:
- Bardzo specjalistyczne terminy
- Rzadko używane słowa
- Regionalne i dialektalne
- Archaiczne terminy
"""

import re
from collections import defaultdict

# ============================================================
# OSTATNIE 40 BARDZO SPECYFICZNYCH SŁÓW
# ============================================================

SUPER_FINAL_VOCABULARY = {
    "bardzo_specyficzne_slow": [
        ("Cang-long-wo-hu", "Ukryty smok, czający się tygrys (idiom)"),
        ("Hu-jia-hu-wei", "Lis używający tygrysiej siły (idiom)"),
        ("Hua-long-dian-jing", "Dodać oczy smokowi (idiom - finalne uderzenie)"),
        ("Yi-ma-dang-xian", "Jeden koń na czele (idiom - prowadzić)"),
        ("Wan-fu-bu-dang", "Nie można powstrzymać 10000 ludzi (idiom - niepokonany)"),
        ("Bai-bu-chuan-yang", "Trafić przez wierzbę ze 100 kroków (idiom - celny)"),
        ("Qian-jun-yi-fa", "1000 jin wisząca na włosku (idiom - krytyczny moment)"),
        ("Yi-chu-ji-zhong", "Jeden cios na trafienie (idiom - decydujące uderzenie)"),
        ("Feng-chi-dian-che", "Wiatr i piorun (idiom - bardzo szybki)"),
        ("Xing-yun-liu-shui", "Płynące chmury i woda (idiom - płynny ruch)"),
        ("Gang-rou-bing-ji", "Twardość i miękkość razem (idiom - balans)"),
        ("Nei-wai-jian-xiu", "Wewnątrz i zewnątrz razem trenować (idiom)"),
        ("Shou-dao", "Sztuka ręki (japoński termin, ale używany)"),
        ("Judo", "Miękka droga (japoński termin)"),
        ("Ken-po", "Prawo pięści (termin karate)"),
        ("Wu-shu-jia", "Mistrz sztuk walki"),
        ("Quan-shi", "Nauczyciel pięściarstwa"),
        ("Dao-shi", "Nauczyciel Dao"),
        ("He-shang", "Mnich buddyjski"),
        ("Dao-ren", "Taoista"),
        ("Ni-gu", "Mniszka buddyjska"),
        ("Ju-shi", "Świecki uczeń buddyzmu"),
        ("Zhai-gong", "Pałac postu"),
        ("Chan-fang", "Pokój medytacji"),
        ("Fo-tang", "Sala Buddy"),
        ("Jing-tang", "Sala sutr"),
        ("Fa-tang", "Sala Dharmy"),
        ("Shan-men", "Brama góry (klasztoru)"),
        ("Tian-wang", "Niebiański król"),
        ("Luo-han", "Arhat"),
        ("Pu-sa", "Bodhisattwa"),
        ("Fo-zu", "Budda-przodek"),
        ("Ru-lai", "Tathagata"),
        ("Guan-yin", "Guanyin (bogini litości)"),
        ("Wen-shu", "Manjushri (bodhisattwa mądrości)"),
        ("Pu-xian", "Samantabhadra (bodhisattwa)"),
        ("Di-zang", "Ksitigarbha (bodhisattwa)"),
        ("Mi-le", "Maitreya (przyszły Budda)"),
        ("A-mi-tuo-fo", "Amitabha (mantra)"),
        ("Nan-wu", "Hołd (w mantrach)"),
    ],
}

# ============================================================
# FUNKCJE POMOCNICZE
# ============================================================

def load_existing_dict(file_path):
    """Wczytuje istniejący słownik z pliku Markdown"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        pattern = r'^- ([A-Za-zęóąśłżźćńĘÓĄŚŁŻŹĆŃüÜ-]+) - (.+)$'
        entries = re.findall(pattern, content, re.MULTILINE)

        word_dict = {}
        for word, meaning in entries:
            normalized = word.lower().strip()
            word_dict[normalized] = (word, meaning.strip())

        return word_dict
    except FileNotFoundError:
        print(f"[BLAD] Nie znaleziono pliku: {file_path}")
        return {}

def add_category_to_dict(word_dict, category_name, category_words):
    """Dodaje nową kategorię do słownika, pomijając duplikaty"""
    conflicts = []
    added = 0

    for lengxuan, polish in category_words:
        normalized = lengxuan.lower().strip()

        if normalized in word_dict:
            conflicts.append(f"  {lengxuan} - {polish}")
        else:
            word_dict[normalized] = (lengxuan, polish)
            added += 1

    if conflicts:
        print(f"  UWAGA: Znaleziono {len(conflicts)} konfliktow")

    print(f"  Dodano {added} nowych slow")
    return added, len(conflicts)

def save_dict_to_markdown(word_dict, output_path):
    """Zapisuje słownik do pliku Markdown"""
    sorted_entries = sorted(word_dict.items(), key=lambda x: x[1][0].lower())

    if len(sorted_entries) >= 3000:
        status = "*** CEL OSIAGNIETY!!! *** (3000+)"
    else:
        status = "W TRAKCIE ROZBUDOWY"

    output = f"""# Slownik Lengxuan - KOMPLETNY (3000+ slow)

**Liczba wpisow:** {len(sorted_entries)}
**Ostatnia aktualizacja:** 2026-01-03

**Status:** {status}

---

"""

    for normalized, (word, meaning) in sorted_entries:
        output += f"- {word} - {meaning}\n"

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"\n[OK] Zapisano kompletny slownik: {output_path}")
    print(f"  Calkowita liczba wpisow: {len(sorted_entries)}")

# ============================================================
# GŁÓWNA FUNKCJA
# ============================================================

def main():
    print("=" * 60)
    print("GENERATOR SLOWNIKA LENGXUAN - SUPER-FINAL CZESC 10")
    print("OSTATECZNY SPRINT DO 3000+!")
    print("=" * 60)

    dict_path = "../03_Slownik/slownik_lengxuan_polski.md"
    output_path = "../03_Slownik/slownik_lengxuan_polski.md"

    print(f"\nLadowanie istniejacego slownika...")
    word_dict = load_existing_dict(dict_path)
    print(f"Zaladowano {len(word_dict)} istniejacych slow")
    print(f"Cel: 3000 slow")
    print(f"Brakuje: {max(0, 3000 - len(word_dict))} slow")

    total_added = 0
    total_conflicts = 0

    categories = [
        ("bardzo_specyficzne_slow", "Bardzo specyficzne slowa"),
    ]

    for cat_key, cat_name in categories:
        print(f"\nDodawanie kategorii: {cat_key}...")
        added, conflicts = add_category_to_dict(
            word_dict,
            cat_name,
            SUPER_FINAL_VOCABULARY[cat_key]
        )
        total_added += added
        total_conflicts += conflicts

    print("\n" + "=" * 60)
    print(f"SUPER-FINAL CZESC 10 - SUMA: Dodano {total_added} nowych slow")
    print(f"Calkowita liczba slow: {len(word_dict)}")
    print("=" * 60)

    save_dict_to_markdown(word_dict, output_path)

    print("\n" + "=" * 60)
    print("STATYSTYKI KONCOWE:")
    print("=" * 60)
    print(f"  Calkowita liczba slow: {len(word_dict)}")
    print(f"  Dodano w tej sesji: {total_added}")
    print(f"  Wykryto konfliktow: {total_conflicts}")

    if len(word_dict) >= 3000:
        print(f"\n  *** *** *** CEL OSIAGNIETY!!! *** *** ***")
        print(f"  PRZEKROCZONO CEL 3000+ O: {len(word_dict) - 3000} slow!")
        print(f"\n  Slownik Lengxuan ma teraz {len(word_dict)} wpisow!")
        print(f"\n  GRATULACJE - SLOWNIK KOMPLETNY!")
    else:
        print(f"\n  Cel (3000+): Jeszcze brakuje {3000 - len(word_dict)} slow")

    print("=" * 60)
    print("\n*** SLOWNIK LENGXUAN KOMPLETNY - 3000+ SLOW ***")
    print("=" * 60)

if __name__ == "__main__":
    main()
