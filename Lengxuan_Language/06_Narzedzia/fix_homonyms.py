# -*- coding: utf-8 -*-
"""
Skrypt naprawiający homonimię w słowniku Lengxuan
Strategia:
1. Dla liczb, kolorów, anatomii - zostawić monosylaby
2. Dla pozostałych - preferować dwusylabowe złożenia
3. Zmienić fonetycznie najbardziej problematyczne
"""

import re
from collections import defaultdict

# Słownik poprawek homonimów
FIXES = {
    # er: dwa vs. ucho
    'er': {
        'ucho': 'er-duo',  # ucho-dziura
        'dwa': 'er',       # liczba - zostaw
    },

    # bai: sto vs. biały
    'bai': {
        'biały': 'bai',      # kolor - zostaw
        'sto': 'yi-bai',     # yi-bai (jeden-sto)
    },

    # wan: dziesięć tysięcy vs. miska vs. późno
    'wan': {
        'dziesięć tysięcy': 'wan',    # liczba - zostaw
        'miska': 'wan-zi',             # miska-rzecz
        'późno': 'wan-shang',          # późno-wieczór
    },

    # he: żuraw vs. rzeka vs. pić
    'he': {
        'żuraw': 'bai-he',      # biały-żuraw
        'rzeka': 'he-liu',      # rzeka-strumień
        'pić': 'he-shui',       # pić-woda (czasownik)
    },

    # nu: gniew vs. wnuczka
    'nu': {
        'gniew': 'fen-nu',      # gniew-wściekłość
        'wnuczka': 'sun-nu',    # wnuk-żeński
    },

    # fei: płuco vs. lecieć
    'fei': {
        'płuco': 'fei-zang',    # płuco-organ
        'lecieć': 'fei-xiang',  # lecieć-wznosić
    },

    # gu: kość vs. dolina
    'gu': {
        'kość': 'gu-tou',       # kość-głowa
        'dolina': 'shan-gu',    # góra-dolina
    },

    # pi: śledziona vs. skóra
    'pi': {
        'śledziona': 'pi-zang',  # śledziona-organ
        'skóra': 'pi-fu',        # skóra-powierzchnia
    },

    # tu: królik vs. ziemia (element)
    'tu': {
        'królik': 'tu-zi',       # królik-rzecz
        'ziemia': 'tu-xing',     # ziemia-element
    },

    # shi: mistrz vs. godzina vs. praktyka vs. czas
    'shi': {
        'mistrz': 'shi-fu',      # mistrz-ojciec
        'godzina': 'shi-chen',   # godzina-czas
        'praktyka': 'shi-jian',  # praktyka-doświadczenie
        'czas': 'shi-jian',      # czas-okres
    },

    # wu: pięć vs. droga (Wu-dao) vs. mgła vs. taniec
    'wu': {
        'pięć': 'wu',            # liczba - zostaw
        'droga': 'wu-dao',       # droga-wojownika (już złożone)
        'mgła': 'wu-qi',         # mgła-para
        'taniec': 'wu-dao',      # taniec-droga (kontekst rozróżni)
    },

    # da: uderzać vs. duży vs. odpowiadać
    'da': {
        'uderzać': 'da-ji',      # uderzać-atakować
        'duży': 'da',            # przymiotnik - zostaw
        'odpowiadać': 'hui-da',  # zwrotny-odpowiadać
    },

    # xue: śnieg vs. krew vs. uczyć się
    'xue': {
        'śnieg': 'xue-hua',      # śnieg-kwiat
        'krew': 'xue-ye',        # krew-płyn
        'uczyć się': 'xue-xi',   # uczyć-praktykować
    },

    # jiu: dziewięć vs. wujek (brat matki) vs. stary
    'jiu': {
        'dziewięć': 'jiu',       # liczba - zostaw
        'wujek': 'jiu-jiu',      # wujek-wujek
        'stary': 'jiu-de',       # stary-poprzedni
    },

    # xiao: synowska pobożność vs. śmiać się
    'xiao': {
        'synowska pobożność': 'xiao-dao',  # pobożność-droga
        'śmiać się': 'xiao-sheng',         # śmiać-dźwięk
    },

    # feng: Fengzhan vs. wiatr
    'feng': {
        'wiatr': 'feng-li',      # wiatr-siła
        'fengzhan': 'feng-zhan', # nazwa własna - zostaw
    },

    # gan-jue: czuć (zmysł) vs. uczucie (dotyk)
    'gan-jue': {
        'czuć': 'gan-jue',       # czasownik
        'uczucie (dotyk)': 'chu-jue',  # dotyk-zmysł
    },

    # bei: smutek vs. północ
    'bei': {
        'smutek': 'bei-shang',   # smutek-żal
        'północ': 'bei-fang',    # północ-kierunek
    },

    # xi: zazdrość vs. zachód
    'xi': {
        'zazdrość': 'du-ji',     # zazdrość (inne słowo)
        'zachód': 'xi-fang',     # zachód-kierunek
    },

    # men: my/wy/oni (partykuła) vs. drzwi
    'men': {
        'my': 'men',             # partykuła - zostaw
        'wy': 'men',             # partykuła - zostaw
        'oni/one': 'men',        # partykuła - zostaw
        'drzwi': 'men-hu',       # drzwi-wejście
    },
}

# Dodatkowe zasady:
# - Duplikaty (wielka/mała litera) -> jedna wersja
# - Słowa podstawowe (liczby 1-10, kolory, zaimki) -> monosylaby
# - Czasowniki -> preferować czasownik+obiekt lub czasownik+rezultat
# - Rzeczowniki -> preferować dwusylabowe

def load_dictionary_from_html(filepath):
    """Wczytuje słownik z pliku HTML"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Znajdź sekcję słownika
    dict_start = content.find('<h1 class="western">Słownik</h1>')
    if dict_start == -1:
        return []

    dict_content = content[dict_start:dict_start+100000]

    # Ekstrahuj wpisy
    pattern = r'([A-Za-zęóąśłżźćńĘÓĄŚŁŻŹĆŃüÜ-]+)\s*-\s*([^<\n]+)'
    entries = re.findall(pattern, dict_content)

    return entries

def normalize_entry(word, meaning):
    """Normalizuje wpis słownikowy"""
    word = word.strip()
    meaning = meaning.strip()

    # Usuń HTML artifacts
    if 'font' in word or 'weight' in word or 'margin' in word:
        return None

    # Usuń dziwne znaki
    meaning = re.sub(r'[&<>"]', '', meaning)
    meaning = meaning.replace('quot;', '')

    return (word, meaning)

def fix_dictionary(entries):
    """Naprawia słownik - eliminuje homonimię"""
    fixed = {}
    duplicates = defaultdict(list)

    # Zbierz wszystkie znaczenia dla każdego słowa
    for word, meaning in entries:
        normalized = normalize_entry(word, meaning)
        if not normalized:
            continue
        word, meaning = normalized

        word_lower = word.lower()
        duplicates[word_lower].append((word, meaning))

    # Napraw homonimы
    for word_lower, meanings in duplicates.items():
        if len(meanings) == 1:
            # Nie ma duplikatów
            word, meaning = meanings[0]
            fixed[word] = meaning
        else:
            # Są duplikaty - trzeba naprawić
            unique_meanings = {}
            for word, meaning in meanings:
                # Usuń duplikaty (ta sama definicja)
                if meaning.lower() not in [m.lower() for m in unique_meanings.values()]:
                    unique_meanings[word] = meaning

            if len(unique_meanings) == 1:
                # To były tylko duplikaty wielkości liter
                word, meaning = list(unique_meanings.items())[0]
                fixed[word] = meaning
            else:
                # Prawdziwe homonimы - użyj fixes
                if word_lower in FIXES:
                    for meaning, new_word in FIXES[word_lower].items():
                        # Znajdź odpowiednie znaczenie
                        for w, m in unique_meanings.items():
                            if meaning.lower() in m.lower():
                                fixed[new_word] = m
                                break
                else:
                    # Nie ma fix'a - zostaw wszystkie (oznacz jako TODO)
                    for w, m in unique_meanings.items():
                        fixed[f"{w} (TODO: {word_lower})"] = m

    return fixed

# Główna funkcja
if __name__ == '__main__':
    print("Ładowanie słownika...")
    entries = load_dictionary_from_html('../../Lengxuan.html')
    print(f"Znaleziono {len(entries)} wpisów")

    print("\nNaprawianie homonimów...")
    fixed_dict = fix_dictionary(entries)
    print(f"Po naprawie: {len(fixed_dict)} unikalnych słów")

    # Zapisz poprawiony słownik
    output = []
    for word in sorted(fixed_dict.keys()):
        meaning = fixed_dict[word]
        output.append(f"{word} - {meaning}")

    with open('../03_Slownik/slownik_lengxuan_polski.md', 'w', encoding='utf-8') as f:
        f.write("# Słownik Lengxuan - Poprawiony\n\n")
        f.write(f"**Liczba wpisów:** {len(fixed_dict)}\n\n")
        f.write("---\n\n")
        for line in output:
            f.write(f"- {line}\n")

    print(f"\n✅ Zapisano poprawiony słownik: {len(fixed_dict)} wpisów")
    print("   Lokalizacja: 03_Slownik/slownik_lengxuan_polski.md")
