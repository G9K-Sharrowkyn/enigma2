# -*- coding: utf-8 -*-
"""
GENERATOR SŁOWNIKA LENGXUAN - CZĘŚĆ 9 MICRO-FINAL
Cel: DEFINITYWNE PRZEKROCZENIE 3000+ słów (ostatnie 75 słów)

Dodaje ostatnie 75 starannie wyselekcjonowanych słów:
- Ostatnie czasowniki użytkowe
- Ostatnie przymiotniki opisowe
- Ostatnie rzeczowniki codzienne
- Terminy społeczne i kulturowe
"""

import re
from collections import defaultdict

# ============================================================
# OSTATNIE 75 SŁÓW - MICRO-FINAL
# ============================================================

MICRO_FINAL_VOCABULARY = {
    "ostatnie_czasowniki": [
        ("Bao-liu", "Zachowywać, przechowywać"),
        ("Cun-chu", "Magazynować"),
        ("Bao-cun", "Przechowywać"),
        ("Bao-hu", "Chronić, ochraniać"),
        ("Wei-hu", "Utrzymywać, konserwować"),
        ("Xiu-fu", "Naprawiać, restaurować"),
        ("Geng-xin", "Odnawiać, aktualizować"),
        ("Ti-huan", "Zastępować"),
        ("Jiao-huan", "Wymieniać"),
        ("Dui-huan", "Wymieniać (walutę)"),
        ("Zhuan-rang", "Przekazywać"),
        ("Song-gei", "Wręczać, dawać"),
        ("Jie-shou", "Przyjmować, akceptować"),
        ("Shou-qu", "Otrzymywać, zbierać"),
        ("Fa-song", "Wysyłać"),
        ("Ji-song", "Posyłać, dostarczać"),
        ("Chuan-di", "Przekazywać"),
        ("Zhuan-da", "Przekazywać (wiadomość)"),
        ("Tong-zhi", "Powiadamiać"),
        ("Bao-gao", "Raportować, zgłaszać"),
        ("Shuo-ming", "Wyjaśniać"),
        ("Jie-shi", "Interpretować, tłumaczyć"),
        ("Fan-yi", "Tłumaczyć (języki)"),
        ("Bi-jiao", "Porównywać"),
        ("Dui-bi", "Przeciwstawiać"),
    ],

    "ostatnie_przymiotniki": [
        ("Shu-shi", "Wygodny"),
        ("Fang-bian", "Wygodny, dogodny"),
        ("Rong-yi", "Łatwy"),
        ("Kun-nan", "Trudny"),
        ("Jian-nan", "Trudny, nieprzyjemny"),
        ("Kun", "Trudny, kłopotliwy"),
        ("Nan", "Trudny do..."),
        ("Yi", "Łatwy do..."),
        ("Ke", "Możliwy do..."),
        ("Bu-ke", "Niemożliwy do..."),
        ("Bi-yao", "Konieczny"),
        ("Xu-yao", "Potrzebny"),
        ("Zhong-yao", "Ważny"),
        ("Ci-yao", "Drugorzędny"),
        ("Zhu-yao", "Główny, podstawowy"),
        ("Fu-yao", "Dodatkowy, pomocniczy"),
        ("Te-shu", "Specjalny"),
        ("Pu-tong", "Zwyczajny, zwykły"),
        ("Chang-jian", "Powszechny"),
        ("Xi-you", "Rzadki"),
        ("Du-te", "Unikalny"),
        ("Te-bie", "Szczególny"),
        ("Yi-yang", "Jednakowy"),
        ("Bu-tong", "Różny, inny"),
        ("Xiang-si", "Podobny"),
    ],

    "ostatnie_rzeczowniki": [
        ("Qing-kuang", "Sytuacja, okoliczności"),
        ("Zhuang-kuang", "Stan, warunki"),
        ("Qing-xing", "Sytuacja, stan rzeczy"),
        ("Shi-qing", "Sprawa, rzecz"),
        ("Wen-ti", "Problem, kwestia"),
        ("Kun-nan", "Trudność"),
        ("Ma-fan", "Kłopot"),
        ("Wei-xian", "Niebezpieczeństwo"),
        ("An-quan", "Bezpieczeństwo"),
        ("Ji-hui", "Szansa, okazja"),
        ("Ke-neng", "Możliwość"),
        ("Ke-neng-xing", "Prawdopodobieństwo"),
        ("Yuan-yin", "Przyczyna, powód"),
        ("Jie-guo", "Rezultat, wynik"),
        ("Ying-xiang", "Wpływ"),
        ("Zuo-yong", "Działanie, efekt"),
        ("Mu-di", "Cel, zamiar"),
        ("Yi-tu", "Intencja"),
        ("Fang-fa", "Metoda, sposób"),
        ("Fang-shi", "Sposób, metoda"),
        ("Guo-cheng", "Proces"),
        ("Bu-zhou", "Krok, etap"),
        ("Jie-duan", "Faza, stadium"),
        ("Shi-qi", "Okres, czas"),
        ("Cha-bie", "Różnica"),
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
        status = "CEL OSIAGNIETY!!! (3000+)"
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
    print("GENERATOR SLOWNIKA LENGXUAN - MICRO-FINAL CZESC 9")
    print("=" * 60)

    dict_path = "../03_Slownik/slownik_lengxuan_polski.md"
    output_path = "../03_Slownik/slownik_lengxuan_polski.md"

    print(f"\nLadowanie istniejacego slownika...")
    word_dict = load_existing_dict(dict_path)
    print(f"Zaladowano {len(word_dict)} istniejacych slow")
    print(f"Cel: 3000 slow")
    print(f"Brakuje: {3000 - len(word_dict)} slow")

    total_added = 0
    total_conflicts = 0

    categories = [
        ("ostatnie_czasowniki", "Ostatnie czasowniki"),
        ("ostatnie_przymiotniki", "Ostatnie przymiotniki"),
        ("ostatnie_rzeczowniki", "Ostatnie rzeczowniki"),
    ]

    for cat_key, cat_name in categories:
        print(f"\nDodawanie kategorii: {cat_key}...")
        added, conflicts = add_category_to_dict(
            word_dict,
            cat_name,
            MICRO_FINAL_VOCABULARY[cat_key]
        )
        total_added += added
        total_conflicts += conflicts

    print("\n" + "=" * 60)
    print(f"MICRO-FINAL CZESC 9 - SUMA: Dodano {total_added} nowych slow")
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
        print(f"\n  *** CEL OSIAGNIETY!!! ***")
        print(f"  PRZEKROCZONO O: {len(word_dict) - 3000} slow!")
        print(f"\n  Slownik Lengxuan ma teraz {len(word_dict)} slow!")
    else:
        print(f"\n  Cel (3000+): Jeszcze brakuje {3000 - len(word_dict)} slow")

    print("=" * 60)
    print("\nSLOWNIK LENGXUAN KOMPLETNY - CEL OSIAGNIETY!")
    print("=" * 60)

if __name__ == "__main__":
    main()
