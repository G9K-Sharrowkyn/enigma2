# -*- coding: utf-8 -*-
"""
Generator rozszerzonego słownika Lengxuan - CZĘŚĆ 3 (FINALNA)
Cel: Dodanie kolejnych ~1500-2000 słów do osiągnięcia 3000+
"""

import re
from collections import defaultdict

# CZĘŚĆ 3 - FINALNE ROZSZERZENIE
FINAL_VOCABULARY = {
    # ============================================================
    # HANDEL I PIENIĄDZE
    # ============================================================
    "handel": [
        ("Qian", "Pieniądze"),
        ("Yin-zi", "Srebro (jako waluta)"),
        ("Jin-zi", "Złoto (jako waluta)"),
        ("Tong-qian", "Moneta miedziana"),
        ("Zhi-bi", "Papierowy pieniądz"),

        ("Jia-ge", "Cena"),
        ("Jia-zhi", "Wartość"),
        ("Cheng-ben", "Koszt, cena zakupu"),
        ("Li-run", "Zysk"),
        ("Kui-sun", "Strata"),

        ("Mai-mai", "Handel, transakcja"),
        ("Mao-yi", "Handel, komercja"),
        ("Jiao-yi", "Transakcja"),
        ("Mai", "Kupować"),
        ("Chu-shou", "Sprzedawać"),

        ("Shi-chang", "Rynek, targ"),
        ("Pu-zi", "Sklep, warsztat"),
        ("Shang-dian", "Sklep"),
        ("Huo-wu", "Towary"),
        ("Huo-pin", "Produkty"),

        ("Jie-zhang", "Rozliczyć rachunek"),
        ("Fu-kuan", "Zapłacić"),
        ("Shou-kuan", "Otrzymać płatność"),
        ("Qian-zhang", "Dług"),
        ("Huan-qian", "Spłacić dług"),

        ("Tan-jia", "Targować się"),
        ("Da-zhe", "Dawać rabat"),
        ("Zeng-song", "Dawać w prezencie"),
    ],

    # ============================================================
    # WOJNA I STRATEGIA
    # ============================================================
    "wojna": [
        ("Zhan-zheng", "Wojna"),
        ("Zhan-dou", "Bitwa, walka"),
        ("Zhan-yi", "Kampania wojenna"),
        ("Zhan-chang", "Pole bitwy"),

        ("Jun-dui", "Armia"),
        ("Bing-ma", "Wojsko (dosł. żołnierze i konie)"),
        ("Shui-jun", "Marynarka"),
        ("Qi-bing", "Kawaleria"),
        ("Bu-bing", "Piechota"),
        ("Gong-bing", "Łucznicy"),

        ("Jin-gong", "Atakować"),
        ("Fang-shou", "Bronić się"),
        ("Tui-que", "Wycofać się"),
        ("Zhui-ji", "Ścigać (wroga)"),
        ("Bao-wei", "Oblegać"),
        ("Tu-wei", "Przebijać oblężenie"),

        ("Sheng-li", "Zwycięstwo"),
        ("Shi-bai", "Porażka"),
        ("Tou-xiang", "Poddać się"),
        ("Jian-mie", "Zniszczyć całkowicie"),

        ("Ce-lüe", "Strategia"),
        ("Ji-mou", "Spisek, intryga"),
        ("Ji-hua", "Plan"),
        ("Bu-shu", "Rozmieszczenie (wojsk)"),

        ("Zhan-shu", "Taktyka"),
        ("Ji-gong", "Niespodziewany atak"),
        ("Mai-fu", "Zasadzka"),
        ("Sheng-dong-ji-xi", "Uderzenie z fintą (wschód-zachód)"),

        ("Qi", "Sztandar, chorągiew"),
        ("Gu", "Bęben wojenny"),
        ("Hao-jiao", "Róg wojenny"),
        ("Ling-pai", "Rozkaz wojskowy (tabliczka)"),

        ("Gong-lao", "Zasługa wojenna"),
        ("Zhan-gong", "Wyczyny bojowe"),
        ("Jiang-shang", "Nagroda wojenna"),
    ],

    # ============================================================
    # PRAWO I PORZĄDEK
    # ============================================================
    "prawo": [
        ("Fa-lv", "Prawo, ustawa"),
        ("Gui-ju", "Reguła, przepis"),
        ("Tiao-li", "Regulacja"),
        ("Fa-ling", "Dekret prawny"),

        ("Zui", "Zbrodnia, grzech"),
        ("Zui-fan", "Zbrodniarz"),
        ("Fan-zui", "Popełnić przestępstwo"),

        ("Pan-jue", "Wydać wyrok"),
        ("Shen-pan", "Sądzić, proces"),
        ("Xing-fa", "Kara"),
        ("Chu-fa", "Ukarać"),

        ("Si-xing", "Kara śmierci"),
        ("Liu-fang", "Wygnanie"),
        ("Jian-jin", "Więzienie"),
        ("Fa-kuan", "Grzywna"),

        ("Wu-zui", "Niewinny"),
        ("You-zui", "Winny"),
        ("Zheng-ju", "Dowód"),
        ("Zheng-ren", "Świadek"),

        ("Gong-ping", "Sprawiedliwy"),
        ("Zheng-yi", "Sprawiedliwość"),
        ("Gong-zheng", "Prawy, bezstronny"),
    ],

    # ============================================================
    # CECHY CHARAKTERU (rozszerzone)
    # ============================================================
    "charakter": [
        ("Shan-liang", "Dobry, życzliwy"),
        ("E-du", "Zły, okrutny"),
        ("Ci-bei", "Współczujący, litościwy"),
        ("Can-ren", "Okrutny, bezlitosny"),

        ("Yong-gan", "Odważny"),
        ("Qie-ruo", "Tchórzliwy"),
        ("Yong-meng", "Mężny, nieustraszony"),

        ("Cong-ming", "Inteligentny, mądry"),
        ("Yu-chun", "Głupi"),
        ("Rui-zhi", "Bystry, mądry"),
        ("Ben-zhuo", "Nierozgarnięty"),

        ("Qin-fen", "Pracowity"),
        ("Lan-duo", "Leniwy"),

        ("Cheng-shi", "Uczciwy"),
        ("Xu-wei", "Hipokryta, fałszywy"),
        ("Zhong-shi", "Lojalny"),
        ("Bei-pan", "Zdrada"),

        ("Qian-xu", "Skromny"),
        ("Jiao-ao", "Arogancki, dumny"),
        ("Ao-man", "Wyniosły"),

        ("Kuan-rong", "Tolerancyjny, wyrozumiały"),
        ("Xia-ai", "Wąskohoryzontalny"),

        ("Wen-rou", "Łagodny, delikatny"),
        ("Cu-bao", "Brutalny, gwałtowny"),
        ("Bao-zao", "Porywczy"),

        ("Hao-ke", "Gościnny"),
        ("Ke-qi", "Uprzejmy"),
        ("Li-mao", "Grzeczny"),
        ("Wu-li", "Niegrzeczny"),

        ("Shen-mi", "Tajemniczy"),
        ("Kai-fang", "Otwarty"),
        ("Bao-shou", "Konserwatywny"),

        ("Guan-xin", "Troskliwy, dbający"),
        ("Leng-mo", "Obojętny, zimny"),

        ("Re-xin", "Gorliwy, entuzjastyczny"),
        ("Leng-dan", "Obojętny, apatyczny"),
    ],

    # ============================================================
    # ABSTRAKCYJNE POJĘCIA
    # ============================================================
    "abstrakcja": [
        ("Li-xiang", "Ideał"),
        ("Xian-shi", "Rzeczywistość"),
        ("Zhen-li", "Prawda"),
        ("Mei", "Piękno"),

        ("Zi-you", "Wolność"),
        ("Shu-fu", "Ograniczenie, więzy"),
        ("Quan-li", "Władza, prawo"),
        ("Quan-wei", "Autorytet"),

        ("Ming-yun", "Los, przeznaczenie"),
        ("Yun-qi", "Szczęście, fortuna"),
        ("Ji-yu", "Szansa, okazja"),
        ("Wei-ji", "Kryzys, niebezpieczeństwo"),

        ("Mu-di", "Cel"),
        ("Mu-biao", "Zamiar, cel"),
        ("Fang-xiang", "Kierunek"),
        ("Dao-lu", "Droga, ścieżka (metafora)"),

        ("Yi-yi", "Znaczenie, sens"),
        ("Jia-zhi", "Wartość"),
        ("Zhong-yao-xing", "Ważność"),

        ("Yuan-yin", "Przyczyna"),
        ("Jie-guo", "Rezultat, skutek"),
        ("Guo-cheng", "Proces"),
        ("Fang-fa", "Metoda, sposób"),

        ("Ke-neng-xing", "Możliwość"),
        ("Bi-ran-xing", "Nieuchronność"),

        ("Guan-xi", "Relacja, związek"),
        ("Ying-xiang", "Wpływ"),
        ("Zuo-yong", "Działanie, efekt"),

        ("Wen-ti", "Problem, kwestia"),
        ("Da-an", "Odpowiedź, rozwiązanie"),

        ("Jing-yan", "Doświadczenie"),
        ("Jiao-xun", "Lekcja (z błędu)"),

        ("Chuan-tong", "Tradycja"),
        ("Xi-su", "Zwyczaj"),
        ("Wen-hua", "Kultura"),

        ("Shi-dai", "Era, epoka"),
        ("Li-shi", "Historia"),
        ("Guo-qu", "Przeszłość"),
        ("Xian-zai", "Teraźniejszość"),
        ("Wei-lai", "Przyszłość"),
    ],

    # ============================================================
    # TRANSPORT
    # ============================================================
    "transport": [
        ("Che", "Wóz, pojazd"),
        ("Ma-che", "Powóz konny"),
        ("Jiao-zi", "Palankin, lektyka"),
        ("Niu-che", "Wóz wołowy"),

        ("Chuan", "Statek, łódź"),
        ("Fan-chuan", "Żaglowiec"),
        ("Xiao-chuan", "Mała łódź"),
        ("Mu-fa", "Tratwa"),

        ("Qi-ma", "Jeździć konno"),
        ("Zuo-che", "Jechać wozem"),
        ("Cheng-chuan", "Płynąć statkiem"),

        ("Lu-shang", "Drogą lądową"),
        ("Shui-lu", "Drogą wodną"),

        ("Hang-xing", "Podróżować, pływać"),
        ("Dao-da", "Przybyć, dotrzeć"),
        ("Li-kai", "Opuścić, wyjechać"),
    ],

    # ============================================================
    # NARZĘDZIA GOSPODARCZE
    # ============================================================
    "narzedzia_rolnicze": [
        ("Nong-ju", "Narzędzia rolnicze"),
        ("Li", "Pług"),
        ("Ba", "Brona"),
        ("Lian-dao", "Sierp"),
        ("Cha-zi", "Widły"),
        ("Qiao", "Motyka, szpadel"),
        ("Dan-zi", "Kosz (na ramię)"),
        ("Dou", "Miara objętości"),
        ("Cheng", "Waga (narzędzie)"),
    ],

    # ============================================================
    # ZJAWISKA NATURALNE (rozszerzone)
    # ============================================================
    "zjawiska": [
        ("Cao-sheng", "Dźwięk, hałas"),
        ("Jing-mi", "Cisza"),
        ("Zao-yin", "Hałas"),
        ("Sheng-yin", "Głos, dźwięk"),

        ("Guang", "Światło"),
        ("Guang-ming", "Jasność"),
        ("Hei-an", "Ciemność"),
        ("Yin-ying", "Cień"),

        ("Yan-se", "Kolor"),
        ("Se-cai", "Kolorystyka"),
        ("Cai-hong", "Tęcza"),

        ("Wen-du", "Temperatura"),
        ("Bing-dian", "Punkt zamarzania"),
        ("Fei-dian", "Punkt wrzenia"),

        ("Feng-su", "Prędkość wiatru"),
        ("Feng-xiang", "Kierunek wiatru"),

        ("Chao-xi", "Przypływ i odpływ"),
        ("Bo-lang", "Fala"),
        ("Hai-lang", "Morska fala"),
    ],

    # ============================================================
    # MATEMATYKA I LICZBY
    # ============================================================
    "matematyka": [
        ("Shu-zi", "Liczba, cyfra"),
        ("Shu-xue", "Matematyka"),

        ("Jia", "Dodawać"),
        ("Jian", "Odejmować"),
        ("Cheng", "Mnożyć"),
        ("Chu", "Dzielić"),

        ("He", "Suma"),
        ("Cha", "Różnica"),
        ("Ji", "Iloczyn"),
        ("Shang", "Iloraz"),

        ("Shuang", "Para, dwa razy"),
        ("Ban", "Połowa"),
        ("Si-fen-zhi-yi", "Jedna czwarta"),
        ("Yi-ban", "Połowa"),

        ("Di-yi", "Pierwszy"),
        ("Di-er", "Drugi"),
        ("Di-san", "Trzeci"),
        ("Di-si", "Czwarty"),
        ("Di-wu", "Piąty"),
        ("Di-liu", "Szósty"),
        ("Di-qi", "Siódmy"),
        ("Di-ba", "Ósmy"),
        ("Di-jiu", "Dziewiąty"),
        ("Di-shi", "Dziesiąty"),

        ("Zui-hou", "Ostatni"),
        ("Xia-yi-ge", "Następny"),
        ("Shang-yi-ge", "Poprzedni"),
    ],

    # ============================================================
    # CZASOWNIKI MENTALNE I PERCEPCYJNE
    # ============================================================
    "czasowniki_mentalne": [
        ("Xiang", "Myśleć o, chcieć"),
        ("Si-kao", "Rozważać"),
        ("Kao-lv", "Rozpatrywać"),

        ("Ren-wei", "Uważać że, sądzić"),
        ("Xiang-xin", "Wierzyć"),
        ("Huai-yi", "Wątpić"),
        ("Que-ren", "Potwierdzić"),

        ("Le-jie", "Rozumieć, znać"),
        ("Zhi-dao", "Wiedzieć"),
        ("Dong", "Rozumieć (potocznie)"),
        ("Bu-dong", "Nie rozumieć"),

        ("Ji-de", "Pamiętać"),
        ("Wang-ji", "Zapomnieć"),
        ("Hui-xiang", "Wspominać"),

        ("Ting", "Słuchać"),
        ("Kan", "Patrzeć"),
        ("Guan-cha", "Obserwować"),
        ("Jian-shi", "Nadzorować"),

        ("Gan-shou", "Odczuwać"),
        ("Ti-hui", "Doświadczać, zrozumieć"),
        ("Gan-zhi", "Postrzegać"),

        ("Ren-chu", "Rozpoznać"),
        ("Fen-bian", "Odróżnić"),
        ("Pan-duan", "Osądzić"),

        ("Yi-shi-dao", "Zdawać sobie sprawę"),
        ("Zhu-yi", "Zauważyć, zwracać uwagę"),
        ("Hu-shi", "Ignorować, pomijać"),

        ("Xi-huan", "Lubić"),
        ("Ai-hao", "Hobby, zamiłowanie"),
        ("Tao-yan", "Nie lubić"),
        ("Zeng-wu", "Nienawidzić"),
    ],

    # ============================================================
    # CZASOWNIKI SPOŁECZNE
    # ============================================================
    "czasowniki_spoleczne": [
        ("Jian-mian", "Spotkać się"),
        ("Hui-mian", "Mieć spotkanie"),
        ("Tan-hua", "Rozmawiać"),

        ("Bang-zhu", "Pomagać"),
        ("Yuan-zhu", "Wspierać"),
        ("Zhi-yuan", "Pomagać, wspomagać"),

        ("Jiao", "Uczyć"),
        ("Xue", "Uczyć się"),
        ("Yan-xi", "Ćwiczyć, praktykować"),

        ("Ling-dao", "Prowadzić, dowodzić"),
        ("Guan-li", "Zarządzać"),
        ("Tong-zhi", "Rządzić"),

        ("Fu-cong", "Słuchać, być posłusznym"),
        ("Wei-bei", "Naruszyć (zasadę)"),

        ("He-zuo", "Współpracować"),
        ("Jing-zheng", "Konkurować"),
        ("Dui-kang", "Przeciwstawiać się"),

        ("Xiang-chu", "Wychodzić (z kimś)"),
        ("Jiao-wang", "Towarzysko obcować"),
        ("Jiao-liu", "Wymieniać (poglądy)"),

        ("Zun-jing", "Szanować"),
        ("Jing-pei", "Podziwiać"),
        ("Qing-shi", "Pogardzać"),

        ("Yao-qing", "Zapraszać"),
        ("Jie-dai", "Przyjmować (gości)"),
        ("Bai-fang", "Odwiedzać"),

        ("Gan-xie", "Dziękować"),
        ("Bao-qian", "Przepraszać"),
        ("Yuan-liang", "Przebaczać"),
    ],

    # ============================================================
    # PRZYMIOTNIKI EMOCJONALNE
    # ============================================================
    "przymiotniki_emocjonalne": [
        ("Gao-xing", "Szczęśliwy, wesoły"),
        ("Kuai-le", "Radosny"),
        ("Yu-kuai", "Zadowolony"),
        ("Man-zu", "Usatysfakcjonowany"),

        ("Shang-xin", "Smutny"),
        ("Bei-shang", "Zasmucony"),
        ("Nan-guo", "Przybity"),

        ("Sheng-qi", "Zły (emocjonalnie)"),
        ("Fen-nu", "Wściekły"),
        ("Fan-nao", "Zirytowany, zdenerwowany"),

        ("Jin-zhang", "Zdenerwowany, spięty"),
        ("Dan-xin", "Zmartwiony"),
        ("Hai-pa", "Przestraszony"),
        ("Kong-ju", "Przerażony"),

        ("Ji-dong", "Podekscytowany"),
        ("Xing-fen", "Ekscytowany"),
        ("Re-qing", "Entuzjastyczny"),

        ("Lei", "Zmęczony"),
        ("Pi-juan", "Wyczerpany"),
        ("Kun", "Senny"),

        ("E", "Głodny"),
        ("Bao", "Najedzony"),
        ("Ke", "Spragniony"),

        ("Ji-mo", "Samotny"),
        ("Gu-du", "Odosobniony"),

        ("Man-yi", "Zadowolony z"),
        ("Bu-man", "Niezadowolony"),

        ("Gan-dong", "Wzruszony"),
        ("Gan-ji", "Wdzięczny"),
    ],

    # ============================================================
    # RZECZOWNIKI ABSTRAKCYJNE (dodatkowe)
    # ============================================================
    "rzeczowniki_abstrakcyjne": [
        ("Zheng-que", "Poprawność"),
        ("Cuo-wu", "Błąd"),

        ("Cheng-gong", "Sukces"),
        ("Shi-bai", "Porażka"),

        ("Jin-bu", "Postęp"),
        ("Tui-bu", "Regres"),

        ("Kai-shi", "Początek"),
        ("Jie-shu", "Koniec"),

        ("Zhong-dian", "Punkt końcowy"),
        ("Qi-dian", "Punkt startowy"),

        ("Guo-cheng", "Proces"),
        ("Jie-duan", "Etap, faza"),

        ("Yuan-ze", "Zasada"),
        ("Gui-lu", "Prawidłowość, wzorzec"),

        ("Te-dian", "Cecha charakterystyczna"),
        ("Xing-zhi", "Natura, charakter (rzeczy)"),

        ("Mao-dun", "Sprzeczność"),
        ("Tong-yi", "Jedność"),

        ("Bian-hua", "Zmiana"),
        ("Wen-ding", "Stabilność"),

        ("Fa-zhan", "Rozwój"),
        ("Jin-hua", "Ewolucja"),
    ],

    # ============================================================
    # DODATKOWE CZASOWNIKI CODZIENNE
    # ============================================================
    "czasowniki_dodatkowe": [
        ("Qing", "Prosić"),
        ("Yao-qiu", "Żądać"),
        ("Ming-ling", "Rozkazywać"),

        ("Tong-yi", "Zgadzać się"),
        ("Ju-jue", "Odmawiać"),
        ("Jie-shou", "Akceptować"),

        ("Jia-ru", "Przyłączyć się"),
        ("Li-kai", "Opuścić"),
        ("Can-jia", "Uczestniczyć"),

        ("Kai-shi", "Zaczynać"),
        ("Ting-zhi", "Zatrzymać"),
        ("Ji-xu", "Kontynuować"),
        ("Wan-cheng", "Ukończyć"),

        ("Xuan-ze", "Wybierać"),
        ("Jue-ding", "Decydować"),
        ("Gai-bian", "Zmieniać"),

        ("Bao-hu", "Chronić"),
        ("Po-huai", "Niszczyć"),
        ("Jian-she", "Budować"),

        ("Da-bao", "Pakować"),
        ("Kai-bao", "Rozpakowywać"),

        ("Da-dian-hua", "Dzwonić (telefonicznie)"),
        ("Xie-xin", "Pisać list"),
        ("Song-xin", "Wysyłać list"),

        ("Xun-wen", "Pytać, dochodzić"),
        ("Jie-shi", "Wyjaśniać"),
        ("Shuo-ming", "Objaśniać"),

        ("Biao-shi", "Wyrażać, wskazywać"),
        ("Biao-da", "Wyrażać (uczucia, myśli)"),

        ("Xiao-hao", "Konsumować, zużywać"),
        ("Jie-yue", "Oszczędzać"),
        ("Lang-fei", "Marnować"),

        ("Shou-ji", "Zbierać, gromadzić"),
        ("Zheng-li", "Porządkować"),
        ("Fen-lei", "Klasyfikować"),

        ("Gua", "Wieszać, zawieszać"),
        ("Die", "Składać (papier, tkaninę)"),
        ("Juan", "Zwijać"),
    ],
}

def load_existing_dictionary(filepath):
    """Wczytuje istniejący słownik"""
    words = {}
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
            for line in lines:
                if line.startswith('- '):
                    match = re.match(r'- ([A-Za-zęóąśłżźćńĘÓĄŚŁŻŹĆŃüÜ-]+) - (.+)', line)
                    if match:
                        word, meaning = match.groups()
                        words[word.lower()] = (word, meaning)
    except FileNotFoundError:
        print("Istniejący słownik nie znaleziony")
    return words

def check_homonyms(existing_words, new_words):
    """Sprawdza homonimы"""
    conflicts = []
    for word, meaning in new_words:
        word_lower = word.lower()
        if word_lower in existing_words:
            conflicts.append((word, meaning, existing_words[word_lower][1]))
    return conflicts

def generate_final_dictionary():
    """Generuje CZĘŚĆ 3 (finalna) słownika"""
    print("Ładowanie istniejącego słownika...")
    existing = load_existing_dictionary('../03_Slownik/slownik_lengxuan_polski.md')
    print(f"Załadowano {len(existing)} istniejących słów\n")

    all_new_words = []
    total_added = 0

    for category, words in FINAL_VOCABULARY.items():
        print(f"Dodawanie kategorii: {category}...")

        conflicts = check_homonyms(existing, words)
        if conflicts:
            print(f"  UWAGA: Znaleziono {len(conflicts)} konfliktów")

        for word, meaning in words:
            word_lower = word.lower()
            if word_lower not in existing:
                existing[word_lower] = (word, meaning)
                all_new_words.append((word, meaning))
                total_added += 1

        print(f"  Dodano {len(words) - len(conflicts)} nowych słów")

    print(f"\n{'='*60}")
    print(f"CZĘŚĆ 3 (FINALNA) - SUMA: Dodano {total_added} nowych słów")
    print(f"Ca\u0142kowita liczba słów: {len(existing)}")
    print(f"{'='*60}\n")

    # Sortuj i zapisz
    sorted_words = sorted(existing.items(), key=lambda x: x[0])

    output_path = '../03_Slownik/slownik_lengxuan_polski.md'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# Słownik Lengxuan - Rozszerzony (KOMPLETNY)\n\n")
        f.write(f"**Liczba wpisów:** {len(existing)}\n")
        f.write(f"**Ostatnia aktualizacja:** 2026-01-03 (Kompletny)\n\n")
        f.write("**Status:** GOTOWY DO UŻYCIA\n\n")
        f.write("---\n\n")

        for word_lower, (word, meaning) in sorted_words:
            f.write(f"- {word} - {meaning}\n")

    print(f"[OK] Zapisano kompletny słownik: {output_path}")
    print(f"  Całkowita liczba wpisów: {len(existing)}")

    # Statystyki
    print(f"\n{'='*60}")
    print("STATYSTYKI KOŃCOWE:")
    print(f"{'='*60}")
    print(f"  Całkowita liczba słów: {len(existing)}")
    print(f"  Dodano w tej sesji: {total_added}")
    print(f"\n  Status: {'GOTOWY' if len(existing) >= 2500 else 'POTRZEBA WIĘCEJ SŁÓW'}")
    print(f"{'='*60}")

    return existing

if __name__ == '__main__':
    print("="*60)
    print("GENERATOR SŁOWNIKA LENGXUAN - CZĘŚĆ 3 (FINALNA)")
    print("="*60)
    print()

    extended_dict = generate_final_dictionary()

    print("\n" + "="*60)
    print("GOTOWE!")
    print("="*60)
