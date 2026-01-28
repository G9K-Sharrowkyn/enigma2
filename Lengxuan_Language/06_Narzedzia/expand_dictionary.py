# -*- coding: utf-8 -*-
"""
Generator rozszerzonego słownika Lengxuan
Cel: Rozszerzenie z ~1000 do ~3500 słów
Strategia: Dwusylabowe złożenia, brak homonimii, styl starożytny chiński
"""

import re
from collections import defaultdict

# Kategorie tematyczne do dodania
NEW_VOCABULARY = {
    # ============================================================
    # UCZUCIA I EMOCJE (rozszerzone)
    # ============================================================
    "emocje": [
        ("Xi-yue", "Radość, szczęście"),
        ("Man-zu", "Zadowolenie, satysfakcja"),
        ("Yu-kuai", "Wesołość"),
        ("Xing-fen", "Ekscytacja, podekscytowanie"),
        ("Re-qing", "Entuzjazm, zapał"),
        ("An-wei", "Pocieszenie, ukojenie"),
        ("Gan-dong", "Wzruszenie"),
        ("Gan-ji", "Wdzięczność (głęboka)"),
        ("Xin-shang", "Podziw, uznanie"),

        ("You-chou", "Smutek, zmartwienie"),
        ("Shi-wang", "Rozczarowanie"),
        ("Hou-hui", "Żal, skrucha"),
        ("Ku-men", "Cierpienie wewnętrzne"),
        ("Bei-ai", "Żałoba, głęboki smutek"),
        ("Ji-mo", "Samotność"),
        ("Wu-liao", "Nuda"),
        ("Yan-juan", "Znudzenie, zmęczenie"),

        ("Fen-nu", "Gniew, wściekłość"),
        ("Sheng-qi", "Złość"),
        ("Bu-man", "Niezadowolenie"),
        ("Chou-hen", "Nienawiść (głęboka)"),
        ("Yuan-hen", "Uraza, pretensja"),
        ("Ji-du", "Zazdrość, zawiść"),

        ("Kong-ju", "Strach, lęk"),
        ("Wei-ju", "Obawa"),
        ("Dan-xin", "Zmartwienie, niepokój"),
        ("Jing-huang", "Panika"),
        ("Dan-qie", "Tchórzostwo"),
        ("Yong-gan", "Odwaga, śmiałość"),

        ("Ai-mu", "Miłość, uczucie"),
        ("Qing-ai", "Umiłowanie"),
        ("Lian-ai", "Miłość romantyczna"),
        ("Qin-qing", "Uczucie rodzinne"),
        ("You-yi", "Przyjaźń"),
        ("Zhong-cheng", "Lojalność, oddanie"),
        ("Xin-ren", "Zaufanie"),
        ("Huai-yi", "Podejrzliwość"),

        ("Jiao-ao", "Duma, pycha"),
        ("Qian-xu", "Skromność"),
        ("Xiu-chi", "Wstyd"),
        ("Can-kui", "Poczucie winy"),
        ("Zi-hao", "Duma (pozytywna)"),
        ("Zi-bei", "Kompleks niższości"),
    ],

    # ============================================================
    # MYŚLENIE I POZNANIE
    # ============================================================
    "poznanie": [
        ("Si-kao", "Myślenie, rozważanie"),
        ("Si-wei", "Sposób myślenia"),
        ("Li-jie", "Rozumienie, pojmowanie"),
        ("Ming-bai", "Zrozumieć, pojąć"),
        ("Dong-de", "Wiedzieć jak"),
        ("Ren-shi", "Poznać, rozpoznać"),
        ("Zhi-dao", "Wiedzieć (fakt)"),
        ("Xue-wen", "Wiedza, nauka"),
        ("Xue-shi", "Uczony, scholar"),

        ("Ji-yi", "Pamięć, wspomnienie"),
        ("Wang-ji", "Zapomnieć"),
        ("Hui-yi", "Wspominać"),
        ("Xiang-qi", "Przypominać sobie"),

        ("Xiang-xiang", "Wyobrażać sobie"),
        ("Meng-xiang", "Marzenie, sen (aspiracja)"),
        ("Huan-xiang", "Fantazja, iluzja"),
        ("Chuang-yi", "Kreatywność"),

        ("Pan-duan", "Osądzać, oceniać"),
        ("Jue-ding", "Decydować"),
        ("Xuan-ze", "Wybór, selekcja"),
        ("Kao-lü", "Rozważać, przemyśleć"),

        ("Huai-yi", "Wątpić, podejrzewać"),
        ("Xin-yang", "Wiara, przekonanie"),
        ("Que-xin", "Pewność"),
        ("Kun-huo", "Zagubienie, konfuzja"),

        ("Yan-jiu", "Badanie, studia"),
        ("Fa-xian", "Odkrycie"),
        ("Fa-ming", "Wynalazek"),
        ("Tan-suo", "Eksploracja, poszukiwanie"),
    ],

    # ============================================================
    # KOMUNIKACJA I JĘZYK
    # ============================================================
    "komunikacja": [
        ("Shuo-hua", "Mówić, rozmawiać"),
        ("Jiang-hua", "Przemawiać, wygłaszać"),
        ("Tan-hua", "Konwersować"),
        ("Dui-hua", "Dialog"),
        ("Wen-da", "Pytanie i odpowiedź"),
        ("Hui-da", "Odpowiadać"),
        ("Wen-hou", "Pozdrawiać"),

        ("Ting-shuo", "Słyszeć (informacje)"),
        ("Chuan-wen", "Plotka, pogłoska"),
        ("Xiao-xi", "Wiadomość, informacja"),
        ("Tong-zhi", "Zawiadomienie"),
        ("Gao-su", "Poinformować, powiedzieć"),

        ("Jiao-tan", "Negocjacje"),
        ("Shang-liang", "Konsultować, omawiać"),
        ("Zheng-lun", "Debata, spór"),
        ("Bi-lun", "Argumentować"),
        ("Tong-yi", "Zgadzać się"),
        ("Fan-dui", "Sprzeciwiać się"),

        ("Cheng-nuo", "Obietnica"),
        ("Bao-zheng", "Gwarancja"),
        ("Shi-yan", "Przysięga"),
        ("Qi-pian", "Oszukiwać"),
        ("Huang-yan", "Kłamstwo"),

        ("Zan-mei", "Chwalić"),
        ("Pi-ping", "Krytykować"),
        ("Ze-bei", "Ganić, łajać"),
        ("Quan-gao", "Ostrzegać"),

        ("Xie-zuo", "Pisać (tekst)"),
        ("Ji-lu", "Zapisywać, rejestrować"),
        ("Miao-shu", "Opisywać"),
        ("Jiang-shu", "Narracja, opowiadanie"),
    ],

    # ============================================================
    # DZIAŁANIA CODZIENNE (rozszerzone)
    # ============================================================
    "dzialania": [
        ("Qi-chuang", "Wstać z łóżka"),
        ("Shui-jiao", "Spać"),
        ("Xing-lai", "Obudzić się"),
        ("Xi-lian", "Myć twarz"),
        ("Shu-tou", "Czesać włosy"),
        ("Chuan-yi", "Ubierać się"),
        ("Tuo-yi", "Rozbierać się"),

        ("Zuo-fan", "Gotować"),
        ("Peng-ren", "Kucharzyć (profesjonalnie)"),
        ("Zhu-fan", "Gotować ryż"),
        ("Chao-cai", "Smażyć warzywa"),
        ("Zheng-bao", "Gotować na parze bułeczki"),

        ("Xi-wan", "Zmywać naczynia"),
        ("Sao-di", "Zamiatać podłogę"),
        ("Mo-di", "Myć podłogę"),
        ("Zheng-li", "Porządkować, organizować"),
        ("Da-sao", "Sprzątać"),

        ("Gou-wu", "Robić zakupy"),
        ("Mai-dong-xi", "Kupować rzeczy"),
        ("Chu-shou", "Sprzedawać"),
        ("Jiao-huan", "Wymieniać"),
        ("Song-gei", "Dawać w prezencie"),

        ("Xi-zao", "Kąpać się"),
        ("Yu-xi", "Brać kąpiel"),
        ("Gan-jing", "Czysty, czystość"),
        ("Zang", "Brudny"),

        ("Xiu-xi", "Odpoczywać"),
        ("Fang-song", "Relaksować się"),
        ("Xiao-qian", "Drzemka"),
    ],

    # ============================================================
    # PRZYRODA - ROŚLINY
    # ============================================================
    "rosliny": [
        ("Song-shu", "Sosna"),
        ("Bai-shu", "Cyprys"),
        ("Liu-shu", "Wierzba"),
        ("Zhu-zi", "Bambus"),
        ("Mei-hua", "Kwiat śliwy"),
        ("Lan-hua", "Orchidea"),
        ("Ju-hua", "Chryzantema"),
        ("He-hua", "Lotos"),
        ("Tao-hua", "Kwiat brzoskwini"),
        ("Li-hua", "Kwiat gruszy"),

        ("Cao-yao", "Zioła lecznicze"),
        ("Ren-shen", "Żeń-szeń"),
        ("Ling-zhi", "Reishi (grzyb nieśmiertelności)"),
        ("Gan-cao", "Lukrecja"),

        ("Mi-fan", "Gotowany ryż"),
        ("Dao-gu", "Roślina ryżowa"),
        ("Mai-zi", "Pszenica"),
        ("Dou-zi", "Fasola, bob"),
        ("Bai-cai", "Kapusta chińska"),
        ("Luo-bo", "Rzepa, rzodkiew"),

        ("Shu-ye", "Liść drzewa"),
        ("Shu-gen", "Korzeń drzewa"),
        ("Shu-zhi", "Gałąź"),
        ("Shu-pi", "Kora drzewa"),
        ("Guo-shi", "Owoc (formalnie)"),
    ],

    # ============================================================
    # PRZYRODA - ZWIERZĘTA (rozszerzone)
    # ============================================================
    "zwierzeta": [
        ("Bai-hu", "Biały tygrys"),
        ("Hei-xiong", "Niedźwiedź czarny"),
        ("Lang", "Wilk"),
        ("Hu-li", "Lis"),
        ("Lu", "Jeleń"),
        ("Bao", "Lampart, pantera"),

        ("Ying", "Jastrząb, sokół"),
        ("Wu-ya", "Wrona"),
        ("Xi-que", "Sroka"),
        ("Yan-zi", "Jaskółka"),
        ("Ge-zi", "Gołąb"),

        ("Yu-er", "Ryba (mała)"),
        ("Li-yu", "Karp"),
        ("Jin-yu", "Złota rybka"),

        ("She-jing", "Duch węża"),
        ("Gui-hun", "Duch żółwia"),

        ("Kun-chong", "Owad"),
        ("Hu-die", "Motyl"),
        ("Mi-feng", "Pszczoła"),
        ("Qing-ting", "Ważka"),
        ("Zhi-zhu", "Pająk"),
    ],

    # ============================================================
    # GEOGRAFIA I KRAJOBRAZY
    # ============================================================
    "geografia": [
        ("Shan-mai", "Pasmo górskie"),
        ("Shan-feng", "Szczyt góry"),
        ("Shan-gu", "Dolina górska"),
        ("Shan-dong", "Jaskinia w górze"),
        ("Shan-lu", "Górska ścieżka"),

        ("He-liu", "Rzeka, strumień"),
        ("He-an", "Brzeg rzeki"),
        ("He-kou", "Ujście rzeki"),
        ("Pu-bu", "Wodospad"),
        ("Quan-shui", "Źródło, strumyk"),

        ("Hu-po", "Jezioro"),
        ("Chi-tang", "Staw"),
        ("Shui-ze", "Bagno, mokradła"),

        ("Hai-yang", "Ocean, morze"),
        ("Hai-an", "Wybrzeże"),
        ("Hai-wan", "Zatoka"),
        ("Hai-dao", "Wyspa morska"),
        ("Sha-tan", "Plaża"),

        ("Ping-yuan", "Równina"),
        ("Cao-yuan", "Step, preria"),
        ("Huang-ye", "Pustkowie"),
        ("Sha-mo", "Pustynia"),

        ("Sen-lin", "Las"),
        ("Shu-lin", "Zagajnik"),
        ("Cong-lin", "Dżungla"),
    ],

    # ============================================================
    # POGODA I ZJAWISKA NATURALNE
    # ============================================================
    "pogoda": [
        ("Tian-qi", "Pogoda"),
        ("Qi-hou", "Klimat"),

        ("Qing-tian", "Pogodny dzień"),
        ("Yin-tian", "Pochmurny dzień"),
        ("Yu-tian", "Deszczowy dzień"),

        ("Xia-yu", "Padać (deszcz)"),
        ("Xia-xue", "Padać (śnieg)"),
        ("Xia-bing-bao", "Grad"),

        ("Feng-bao", "Burza"),
        ("Lei-dian", "Burza z piorunami"),
        ("Shan-dian", "Błyskawica"),
        ("Lei-sheng", "Grzmot"),

        ("Hong-shui", "Powódź"),
        ("Han-zai", "Susza"),
        ("Di-zhen", "Trzęsienie ziemi"),
        ("Huo-shan", "Wulkan"),

        ("Chun-tian", "Wiosna"),
        ("Xia-tian", "Lato"),
        ("Qiu-tian", "Jesień"),
        ("Dong-tian", "Zima"),

        ("Ri-chu", "Wschód słońca"),
        ("Ri-luo", "Zachód słońca"),
        ("Zhong-wu", "Południe (pora dnia)"),
        ("Wu-ye", "Północ (pora nocy)"),
        ("Huang-hun", "Zmierzch"),
        ("Li-ming", "Świt"),
    ],

    # ============================================================
    # SPOŁECZEŃSTWO - ROLE I HIERARCHIA
    # ============================================================
    "spoleczenstwo": [
        ("Jun-zhu", "Władca, monarcha"),
        ("Huang-shang", "Jego Wysokość (cesarz)"),
        ("Tai-hou", "Cesarzowa wdowa"),
        ("Huang-zi", "Książę (syn cesarza)"),
        ("Gong-zhu", "Księżniczka"),

        ("Zai-xiang", "Premier, kanclerz"),
        ("Da-chen", "Wielki minister"),
        ("Tai-shi", "Wielki nauczyciel (tytuł)"),
        ("Tai-bao", "Wielki opiekun (tytuł)"),

        ("Jiang-jun", "Generał"),
        ("Jun-shi", "Dowódca wojskowy"),
        ("Xiao-wei", "Kapitan"),
        ("Shi-zu", "Plutonowy"),

        ("Wen-ren", "Uczony, literat"),
        ("Wu-ren", "Wojownik"),
        ("Nong-fu", "Rolnik"),
        ("Gong-ren", "Rzemieślnik"),
        ("Shang-ren", "Kupiec"),

        ("Dao-shi", "Taoistyczny kapłan"),
        ("He-shang", "Mnich buddyjski"),
        ("Ni-gu", "Zakonnica"),

        ("Chang-zhe", "Starszy (wiekiem)"),
        ("Qian-bei", "Senior (hierarchia)"),
        ("Hou-bei", "Junior (hierarchia)"),
        ("Tong-ling", "Rówieśnik"),
    ],

    # ============================================================
    # RZEMIOSŁO I PROFESJE
    # ============================================================
    "rzemioslo": [
        ("Tie-jiang", "Kowal"),
        ("Mu-jiang", "Stolarz, cieśla"),
        ("Tao-jiang", "Garncarz"),
        ("Zhi-jiang", "Tkacz"),

        ("Jin-jiang", "Złotnik"),
        ("Yin-jiang", "Srebrnik"),
        ("Yu-jiang", "Kamieniarz (jade)"),

        ("Hua-jiang", "Malarz (rzemieślnik)"),
        ("Shu-fa-jia", "Kaligraf"),
        ("Diao-ke-shi", "Rzeźbiarz"),

        ("Yi-shi", "Lekarz"),
        ("Yao-shi", "Aptekarz"),
        ("Zhen-jiu-shi", "Akupunkturzysta"),

        ("Chu-shi", "Kucharz"),
        ("Mian-shi", "Piekarz (ciasto)"),
        ("Jiu-shi", "Browarnik, gorzelnik"),

        ("Shang-ren", "Kupiec"),
        ("Xing-shang", "Podróżny kupiec"),
        ("Dian-zhu", "Właściciel sklepu"),

        ("Yu-fu", "Rybak"),
        ("Lie-hu", "Myśliwy"),
        ("Mu-ren", "Pasterz"),
        ("Qiao-fu", "Drwal"),
    ],

    # ============================================================
    # NARZĘDZIA I PRZEDMIOTY
    # ============================================================
    "narzedzia": [
        ("Gong-ju", "Narzędzie (ogólne)"),
        ("Qi-ju", "Naczynie, przyrząd"),

        ("Chui-zi", "Młotek"),
        ("Fu-tou", "Siekiera"),
        ("Ju-zi", "Piła"),
        ("Dao-zi", "Nóż"),
        ("Jian-dao", "Nożyce"),

        ("Qiang", "Włócznia"),
        ("Dao", "Szabla, miecz"),
        ("Jian", "Miecz (prosty)"),
        ("Gong", "Łuk"),
        ("Jian-shi", "Strzała"),
        ("Nu", "Kusza"),
        ("Gun", "Kij, pałka"),
        ("Bian", "Bicz"),

        ("Dun", "Tarcza"),
        ("Kui-jia", "Zbroja, pancerz"),
        ("Tou-kui", "Hełm"),

        ("Hoe-zi", "Motyka"),
        ("Li", "Pług"),
        ("Lian-dao", "Sierp"),
        ("Shan-zi", "Wachlarz"),
        ("Yu-san", "Parasol"),

        ("Bi", "Pędzel (do pisania)"),
        ("Mo", "Tusz"),
        ("Zhi", "Papier"),
        ("Yan", "Kamień do rozcierania tuszu"),
    ],

    # ============================================================
    # MEDYCYNA TCM
    # ============================================================
    "medycyna": [
        ("Zhong-yi", "Tradycyjna medycyna chińska"),
        ("Yi-shu", "Sztuka leczenia"),
        ("Yi-dao", "Droga medyczna"),

        ("Bing", "Choroba"),
        ("Ji-bing", "Choroba (formalne)"),
        ("Zheng-zhuang", "Symptom"),
        ("Teng-tong", "Ból"),

        ("Zhen-duan", "Diagnoza"),
        ("Zhi-liao", "Leczenie"),
        ("Yi-liao", "Terapia medyczna"),

        ("Yao", "Lekarstwo, zioła"),
        ("Cao-yao", "Zioła lecznicze"),
        ("Tang-yao", "Odwar lekarski"),
        ("Yao-wan", "Pigułka"),

        ("Zhen-jiu", "Akupunktura i moksybucja"),
        ("An-mo", "Masaż"),
        ("Tui-na", "Terapia manipulacyjna"),

        ("Qi-xue", "Qi i krew"),
        ("Yin-yang", "Yin i Yang"),
        ("Wu-xing", "Pięć elementów"),

        ("Re-qi", "Gorąca energia"),
        ("Han-qi", "Zimna energia"),
        ("Shi-qi", "Wilgotna energia"),
        ("Zao-qi", "Sucha energia"),

        ("Jing-luo", "Meridiany"),
        ("Xue-wei", "Punkt akupunkturowy"),

        ("Yang-sheng", "Pielęgnowanie życia"),
        ("Bao-jian", "Ochrona zdrowia"),
    ],

    # ============================================================
    # ASTRONOMIA I KOSMOS
    # ============================================================
    "astronomia": [
        ("Tian-wen", "Astronomia"),
        ("Tian-ti", "Niebo i Ziemia"),
        ("Yu-zhou", "Kosmos, wszechświat"),

        ("Ri-yue", "Słońce i Księżyc"),
        ("Xing-chen", "Gwiazdy"),
        ("Xing-xiu", "Konstelacja"),

        ("Bei-dou", "Wielki Wóz (konstelacja)"),
        ("Tian-lang", "Syriusz (gwiazda)"),
        ("Zhi-nü", "Wega (tkaczka, gwiazda)"),
        ("Niu-lang", "Altair (pasterz wołów, gwiazda)"),

        ("Yin-li", "Kalendarz księżycowy"),
        ("Yang-li", "Kalendarz słoneczny"),
        ("Jie-qi", "Terminy solarne (24)"),

        ("Chun-fen", "Równonoc wiosenna"),
        ("Xia-zhi", "Przesilenie letnie"),
        ("Qiu-fen", "Równonoc jesienna"),
        ("Dong-zhi", "Przesilenie zimowe"),
    ],

    # ============================================================
    # FILOZOFIA I WARTOŚCI
    # ============================================================
    "filozofia": [
        ("Dao", "Droga, Tao"),
        ("De", "Cnota, moc"),
        ("Li", "Rytuał, zasady"),
        ("Yi", "Prawość"),
        ("Ren", "Życzliwość"),
        ("Xiao", "Synowska pobożność"),
        ("Zhong", "Lojalność"),
        ("Xin", "Uczciwość"),
        ("Zhi", "Mądrość"),

        ("Tian-ming", "Mandat Niebios"),
        ("Tian-li", "Zasady Niebios"),

        ("Wu-wei", "Działanie przez niedziałanie"),
        ("Zi-ran", "Naturalność"),

        ("Zhong-yong", "Środek, umiarkowanie"),
        ("He-xie", "Harmonia"),
        ("Ping-heng", "Równowaga"),

        ("Jing-shen", "Duch, energia duchowa"),
        ("Ling-hun", "Dusza"),
        ("Xin-ling", "Umysł duchowy"),
    ],

    # ============================================================
    # SZTUKI WALKI (dodatkowe)
    # ============================================================
    "sztuki_walki": [
        ("Wu-gong", "Kung fu, sztuka walki"),
        ("Quan-fa", "Technika pięści"),
        ("Tui-fa", "Technika kopnięć"),
        ("Shen-fa", "Technika ciała"),
        ("Bu-fa", "Technika kroków"),

        ("Nei-jin", "Wewnętrzna siła"),
        ("Wai-jin", "Zewnętrzna siła"),
        ("Jing-li", "Siła sprężynująca"),

        ("Zhao-shi", "Technika, ruch"),
        ("Tao-lu", "Forma, kata"),
        ("Dui-lian", "Sparring z partnerem"),

        ("Zhan-zhuang", "Pozycja słupowa"),
        ("Ma-bu", "Pozycja konia"),
        ("Gong-bu", "Pozycja łuku"),

        ("Fa-jin", "Wypuszczenie siły"),
        ("Ting-jin", "Słuchanie siły"),
        ("Dong-jin", "Zrozumienie siły"),

        ("Dian-xue", "Uderzanie w punkty"),
        ("Qin-na", "Chwytanie i kontrola"),
        ("Shuai-jiao", "Rzuty"),
    ],
}

def load_existing_dictionary(filepath):
    """Wczytuje istniejący słownik"""
    words = {}
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Pomiń nagłówek
            lines = content.split('\n')
            for line in lines:
                if line.startswith('- '):
                    # Format: - Word - Meaning
                    match = re.match(r'- ([A-Za-zęóąśłżźćńĘÓĄŚŁŻŹĆŃüÜ-]+) - (.+)', line)
                    if match:
                        word, meaning = match.groups()
                        words[word.lower()] = (word, meaning)
    except FileNotFoundError:
        print("Istniejący słownik nie znaleziony, tworzę nowy...")
    return words

def check_homonyms(existing_words, new_words):
    """Sprawdza czy nowe słowa nie kolidują z istniejącymi"""
    conflicts = []
    for word, meaning in new_words:
        word_lower = word.lower()
        if word_lower in existing_words:
            conflicts.append((word, meaning, existing_words[word_lower][1]))
    return conflicts

def generate_extended_dictionary():
    """Generuje rozszerzony słownik"""
    print("Ładowanie istniejącego słownika...")
    existing = load_existing_dictionary('../03_Slownik/slownik_lengxuan_polski.md')
    print(f"Załadowano {len(existing)} istniejących słów\n")

    all_new_words = []
    total_added = 0

    # Dodaj wszystkie kategorie
    for category, words in NEW_VOCABULARY.items():
        print(f"Dodawanie kategorii: {category}...")

        # Sprawdź homonimы
        conflicts = check_homonyms(existing, words)
        if conflicts:
            print(f"  UWAGA: Znaleziono {len(conflicts)} konfliktów:")
            for word, new_meaning, old_meaning in conflicts[:5]:
                print(f"    - {word}: '{new_meaning}' vs '{old_meaning}'")

        # Dodaj słowa
        for word, meaning in words:
            word_lower = word.lower()
            if word_lower not in existing:
                existing[word_lower] = (word, meaning)
                all_new_words.append((word, meaning))
                total_added += 1

        print(f"  Dodano {len(words)} słów z kategorii '{category}'")

    print(f"\n{'='*60}")
    print(f"SUMA: Dodano {total_added} nowych słów")
    print(f"Całkowita liczba słów: {len(existing)}")
    print(f"{'='*60}\n")

    # Sortuj i zapisz
    sorted_words = sorted(existing.items(), key=lambda x: x[0])

    # Zapisz rozszerzony słownik
    output_path = '../03_Slownik/slownik_lengxuan_polski.md'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# Słownik Lengxuan - Rozszerzony\n\n")
        f.write(f"**Liczba wpisów:** {len(existing)}\n")
        f.write(f"**Ostatnia aktualizacja:** 2026-01-03\n\n")
        f.write("---\n\n")

        for word_lower, (word, meaning) in sorted_words:
            f.write(f"- {word} - {meaning}\n")

    print(f"✓ Zapisano rozszerzony słownik: {output_path}")
    print(f"  Całkowita liczba wpisów: {len(existing)}")

    # Zapisz listę nowych słów osobno
    new_words_path = '../03_Slownik/nowe_slowa_2026-01-03.md'
    with open(new_words_path, 'w', encoding='utf-8') as f:
        f.write("# Nowe Słowa - 2026-01-03\n\n")
        f.write(f"**Dodano:** {total_added} nowych słów\n\n")
        f.write("---\n\n")

        current_category = None
        for category, words in NEW_VOCABULARY.items():
            f.write(f"\n## {category.upper()}\n\n")
            for word, meaning in words:
                if word.lower() not in [w[0].lower() for w in all_new_words]:
                    continue  # Skip conflicts
                f.write(f"- **{word}** - {meaning}\n")

    print(f"✓ Zapisano listę nowych słów: {new_words_path}")

    return existing

if __name__ == '__main__':
    print("="*60)
    print("GENERATOR ROZSZERZONEGO SŁOWNIKA LENGXUAN")
    print("="*60)
    print()

    extended_dict = generate_extended_dictionary()

    print("\n" + "="*60)
    print("GOTOWE!")
    print("="*60)
