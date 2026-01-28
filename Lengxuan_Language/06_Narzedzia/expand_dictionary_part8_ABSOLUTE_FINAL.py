# -*- coding: utf-8 -*-
"""
GENERATOR SŁOWNIKA LENGXUAN - CZĘŚĆ 8 ABSOLUTE FINAL
Cel: DEFINITYWNE PRZEKROCZENIE 3000+ słów

Dodaje ostatnie ~300 słów w kategoriach:
- Dodatkowe czasowniki specjalistyczne
- Dodatkowe przymiotniki
- Dodatkowe zwierzęta
- Dodatkowe rośliny
- Dodatkowe zjawiska naturalne
- Dodatkowe stan przedmiotów
- Dodatkowe stany umysłowe
- Dodatkowe terminy filozoficzne
- Dodatkowe terminy medyczne TCM
- Dodatkowe terminy sztuk walki
"""

import re
from collections import defaultdict

# ============================================================
# SŁOWNICTWO ABSOLUTE FINAL - CZĘŚĆ 8 (~300 SŁÓW)
# ============================================================

ABSOLUTE_FINAL_VOCABULARY = {
    "czasowniki_specjalistyczne": [
        ("Shan", "Naprawiać"),
        ("Jiao-zheng", "Korygować"),
        ("Gai-zheng", "Poprawiać"),
        ("Tiao-zheng", "Dostosowywać"),
        ("Geng-gai", "Zmieniać, modyfikować"),
        ("Gai-bian", "Zmieniać, przekształcać"),
        ("Zhuan-bian", "Przekształcać się"),
        ("Zhuan-huan", "Konwertować"),
        ("Bian-hua", "Zmieniać się, ewoluować"),
        ("Fa-zhan", "Rozwijać się"),
        ("Jin-bu", "Postępować, czynić postępy"),
        ("Tui-bu", "Cofać się, regresować"),
        ("Shang-sheng", "Wzrastać"),
        ("Xia-jiang", "Spadać"),
        ("Zeng-jia", "Zwiększać"),
        ("Jian-shao", "Zmniejszać"),
        ("Kuo-da", "Powiększać"),
        ("Suo-xiao", "Pomniejszać"),
        ("Yan-chang", "Przedłużać"),
        ("Suo-duan", "Skracać"),
        ("Yan-shen", "Rozciągać, przedłużać"),
        ("Jia-qiang", "Wzmacniać"),
        ("Jian-ruo", "Osłabiać"),
        ("Jia-su", "Przyśpieszać"),
        ("Jian-man", "Zwalniać"),
        ("Ting-zhi", "Zatrzymywać"),
        ("Zan-ting", "Wstrzymywać"),
        ("Ji-xu", "Kontynuować"),
        ("Zhong-duan", "Przerywać"),
        ("Hui-fu", "Wznawiać, przywracać"),
        ("Chong-fu", "Powtarzać"),
        ("Fan-fu", "Wielokrotnie powtarzać"),
        ("Lian-xi", "Ćwiczyć, praktykować"),
        ("Xun-lian", "Trenować"),
        ("Pei-yang", "Kultywować, szkolić"),
        ("Jiao-yu", "Edukować"),
        ("Qi-fa", "Inspirować"),
        ("Gu-wu", "Zachęcać"),
        ("Mian-li", "Zachęcać, pobudzać"),
        ("Zu-zhi", "Powstrzymywać"),
        ("Fang-zhi", "Zapobiegać"),
        ("Jin-zhi", "Zakazywać"),
        ("Yun-xu", "Pozwalać"),
        ("Xu-ke", "Zezwalać"),
        ("Pi-zhun", "Zatwierdzać"),
        ("Ju-jue", "Odmawiać, odrzucać"),
        ("Fou-ren", "Zaprzeczać"),
        ("Cheng-ren", "Przyznawać, uznawać"),
        ("Que-ren", "Potwierdzać"),
        ("Fou-ding", "Negować"),
    ],

    "przymiotniki_dodatkowe": [
        ("Qing-song", "Lekki, łatwy"),
        ("Chen-zhong", "Ciężki, poważny"),
        ("Jian-dan", "Prosty"),
        ("Fu-za", "Skomplikowany"),
        ("Qing-chu", "Jasny, wyraźny"),
        ("Mo-hu", "Niewyraźny, zamglony"),
        ("Ming-que", "Wyraźny, określony"),
        ("Han-hu", "Niejasny, mglisty"),
        ("Xiang-xi", "Szczegółowy"),
        ("Cu-lue", "Prymitywny, zgrubny"),
        ("Jing-que", "Dokładny, precyzyjny"),
        ("Da-gai", "Przybliżony"),
        ("Wan-zheng", "Kompletny"),
        ("Bu-wan-zheng", "Niekompletny"),
        ("Zheng-que", "Poprawny"),
        ("Cuo-wu", "Błędny"),
        ("Zhen-shi", "Prawdziwy"),
        ("Jia", "Fałszywy"),
        ("Zhen-zheng", "Autentyczny"),
        ("Xu-jia", "Fałszywy, udawany"),
        ("Cheng-shi", "Szczery"),
        ("Xu-wei", "Hipokrytyczny"),
        ("Zhong-shi", "Lojalny"),
        ("Pan-ni", "Zdrajczy"),
        ("Yong-gan", "Odważny"),
        ("Qie-ruo", "Tchórzliwy"),
        ("Jian-qiang", "Silny, mocny"),
        ("Ruan-ruo", "Słaby"),
        ("Wen-ding", "Stabilny"),
        ("Bu-wen-ding", "Niestabilny"),
        ("Gu-ding", "Stały, nieruchomy"),
        ("Bian-dong", "Zmienny"),
        ("Heng-ding", "Stały, niezmien ny"),
        ("Lin-shi", "Tymczasowy"),
        ("Yong-jiu", "Permanentny"),
        ("Duan-zan", "Krótkotrwały"),
        ("Chang-jiu", "Długotrwały"),
        ("Ji-shi", "Natychmiastowy"),
        ("Yan-chi", "Opóźniony"),
        ("Ti-qian", "Wcześniejszy"),
    ],

    "zwierzeta_dodatkowe": [
        ("Lang", "Wilk"),
        ("Hu", "Lis"),
        ("Xiong", "Niedźwiedź"),
        ("Bao", "Lampart"),
        ("Shi", "Lew"),
        ("Xiang", "Słoń"),
        ("Lu", "Jeleń"),
        ("Zhang", "Sarna"),
        ("Ye-zhu", "Dzik"),
        ("Hou", "Małpa"),
        ("Yuan", "Gibbon"),
        ("Shu", "Mysz, szczur"),
        ("Song-shu", "Wiewiórka"),
        ("Tu", "Zając"),
        ("Ci-wei", "Jeż"),
        ("Bian-fu", "Nietoperz"),
        ("Diao", "Kuna"),
        ("Huan", "Borsuk"),
        ("Shui-ta", "Wydra"),
        ("E-yu", "Krokodyl"),
        ("She-jing", "Boa"),
        ("Mang-she", "Pyton"),
        ("Du-she", "Żmija jadowita"),
        ("Bi-hu", "Kobra"),
        ("Xi-yi", "Jaszczurka"),
        ("Bie", "Żółw błotny"),
        ("Gui", "Żółw"),
        ("Wa", "Żaba"),
        ("Ha-ma", "Ropucha"),
        ("Yuan-yang", "Kaczka mandarynka (para)"),
        ("Bai-lu", "Czapla biała"),
        ("Cang-lu", "Czapla szara"),
        ("Que", "Wróbel"),
        ("Yan", "Jaskółka"),
        ("Wu-ya", "Wrona"),
        ("Xi-que", "Sroka"),
        ("Ying", "Jastrząb"),
        ("Diao", "Orzeł"),
        ("Gong-ji", "Kogut"),
        ("Mu-ji", "Kura"),
        ("Xiao-ji", "Kurczę"),
    ],

    "rosliny_dodatkowe": [
        ("Cao", "Trawa"),
        ("Hua-cao", "Kwiaty i trawy"),
        ("Ye-cao", "Dzikie trawy"),
        ("Zhu-miao", "Sadzonka"),
        ("Gen", "Korzeń"),
        ("Jing", "Łodyga"),
        ("Zhi", "Gałąź"),
        ("Ye", "Liść"),
        ("Hua", "Kwiat"),
        ("Guo", "Owoc"),
        ("Zhong-zi", "Nasiono"),
        ("Gen-bu", "System korzeniowy"),
        ("Shu-gen", "Korzeń drzewa"),
        ("Shu-pi", "Kora drzewa"),
        ("Shu-ye", "Liście drzewa"),
        ("Hua-ban", "Płatek"),
        ("Hua-rui", "Pręcik"),
        ("Hua-fen", "Pyłek kwiatowy"),
        ("Mi", "Nektar"),
        ("Guo-pi", "Skórka owocu"),
        ("Guo-rou", "Miąższ owocu"),
        ("Guo-he", "Pestka"),
        ("Teng", "Pnącze"),
        ("Man", "Pnącze (rozgałęzione)"),
        ("Fu", "Paproć"),
        ("Tai", "Mech"),
        ("Jun", "Grzyb"),
        ("Du-jun", "Trujący grzyb"),
        ("Xiang-jun", "Jadalny grzyb"),
    ],

    "zjawiska_naturalne_dodatkowe": [
        ("Ri-shi", "Zaćmienie słońca"),
        ("Yue-shi", "Zaćmienie księżyca"),
        ("Liu-xing", "Meteor, spadająca gwiazda"),
        ("Yun-shi", "Meteoryt"),
        ("Hong", "Tęcza"),
        ("Shuang-hong", "Podwójna tęcza"),
        ("Wu-xia", "Mgła i opary"),
        ("Shui-qi", "Para wodna"),
        ("Ji-feng", "Wicher"),
        ("Kuang-feng", "Sztorm"),
        ("Xuan-feng", "Trąba powietrzna"),
        ("Feng-bao", "Burza"),
        ("Bing-bao", "Grad"),
        ("Bing-dong", "Zamarzanie"),
        ("Rong-hua", "Topnienie"),
        ("Zheng-fa", "Parowanie"),
        ("Ning-jie", "Kondensacja"),
        ("Di-zhen", "Trzęsienie ziemi"),
        ("Shan-崩", "Osunięcie się góry"),
        ("Hong-shui", "Powódź"),
        ("Gan-han", "Susza"),
        ("Huo-zai", "Pożar"),
        ("Huo-shan", "Wulkan"),
        ("Pen-fa", "Erupcja"),
    ],

    "stany_przedmiotow": [
        ("Xin", "Nowy"),
        ("Jiu", "Stary (przedmiot)"),
        ("Po", "Zniszczony"),
        ("Lan", "Zgniły"),
        ("Xiu", "Zardzewiały"),
        ("Hui", "Szary (od kurzu)"),
        ("Zang", "Brudny"),
        ("Jing", "Czysty"),
        ("Guang-liang", "Błyszczący"),
        ("Wu-ran", "Zabrudzony, zanieczyszczony"),
        ("Po-sun", "Uszkodzony"),
        ("Wan-hao", "Nienaruszony"),
        ("Wan-zheng", "Kompletny, cały"),
        ("Can-que", "Niekompletny, uszkodzony"),
        ("Lie", "Pęknięty"),
        ("Duan", "Złamany"),
        ("Sui", "Rozbity"),
        ("Fen", "Sproszkowany"),
        ("Rong", "Stopiony"),
        ("Dong", "Zamrożony"),
        ("Gan", "Suchy"),
        ("Shi-run", "Wilgotny"),
        ("Nen", "Świeży, młody"),
        ("Chen", "Stary, czerstwy"),
    ],

    "stany_umyslowe_dodatkowe": [
        ("Qing-xing", "Przytomny"),
        ("Hun-mi", "Nieprzytomny"),
        ("Mi-hu", "Oszołomiony"),
        ("Qing-chu", "Świadomy, jasny umysł"),
        ("Hun-luan", "Zamęt umysłowy"),
        ("Ji-zhong", "Skoncentrowany"),
        ("Fen-xin", "Rozkojarzony"),
        ("Zhuan-zhu", "Skupiony"),
        ("Man-bu-jing-xin", "Nieuważny"),
        ("Xing-fen", "Podekscytowany"),
        ("Ping-jing", "Spokojny"),
        ("An-xin", "Uspokojony"),
        ("Jiao-lü", "Niespokojny"),
        ("Jin-zhang", "Spięty, zestresowany"),
        ("Song-chi", "Rozluźniony"),
        ("Kun", "Zmęczony, senny"),
        ("Jing-shen", "Energiczny"),
        ("Pi-bei", "Wyczerpany"),
        ("Huo-li", "Energiczny, żywy"),
        ("Wu-liao", "Znudzony"),
        ("Gan-xing-qu", "Zainteresowany"),
        ("Re-qing", "Entuzjastyczny"),
        ("Leng-dan", "Obojętny"),
        ("Man-yi", "Zadowolony"),
        ("Bu-man", "Niezadowolony"),
        ("Shi-wang", "Rozczarowany"),
        ("Xi-wang", "Pełen nadziei"),
        ("Jue-wang", "Zdesperowany"),
    ],

    "filozofia_dodatkowa": [
        ("Dao-xue", "Nauka Dao"),
        ("Ru-xue", "Konfucjanizm"),
        ("Fo-xue", "Buddyzm"),
        ("Yin-yang-xue", "Nauka Yin-Yang"),
        ("Wu-xing-xue", "Teoria Pięciu Elementów"),
        ("Tian-ming", "Mandat Niebios"),
        ("Tian-dao", "Droga Nieba"),
        ("Ren-dao", "Droga Człowieka"),
        ("Zhong", "Lojalność"),
        ("Xiao", "Synowska pietyzm"),
        ("Ren", "Ludzkość, życzliwość"),
        ("Yi", "Sprawiedliwość, prawo"),
        ("Li", "Rytuał, przyzwoitość"),
        ("Zhi", "Mądrość"),
        ("Xin", "Wiara, zaufanie"),
        ("Jing", "Esencja"),
        ("Qi", "Energia życiowa"),
        ("Shen", "Duch"),
        ("Jing-qi-shen", "Esencja-energia-duch"),
        ("Yuan-qi", "Pierwotna energia"),
        ("Zheng-qi", "Praw a energia"),
        ("Xie-qi", "Zła energia"),
        ("Hun", "Dusza eteryczna"),
        ("Po", "Dusza cielesna"),
        ("Xin-xing", "Natura serca/umysłu"),
        ("Ben-xing", "Pierwotna natura"),
        ("Wu-chang", "Pięć stałości"),
        ("San-gang", "Trzy zasady"),
    ],

    "medycyna_tcm_dodatkowa": [
        ("Xu-zheng", "Syndrom niedoboru"),
        ("Shi-zheng", "Syndrom nadmiaru"),
        ("Han-zheng", "Syndrom zimna"),
        ("Re-zheng", "Syndrom gorąca"),
        ("Feng-xie", "Patogen wiatru"),
        ("Shi-xie", "Patogen wilgoci"),
        ("Zao-xie", "Patogen suchości"),
        ("Huo-xie", "Patogen ognia"),
        ("Qi-xu", "Niedobór Qi"),
        ("Xue-xu", "Niedobór krwi"),
        ("Yang-xu", "Niedobór Yang"),
        ("Yin-xu", "Niedobór Yin"),
        ("Qi-zhi", "Stagnacja Qi"),
        ("Xue-yu", "Staza krwi"),
        ("Tan-shi", "Flegma-wilgoć"),
        ("Gan-huo", "Ogień wątroby"),
        ("Xin-huo", "Ogień serca"),
        ("Fei-re", "Gorąco płuc"),
        ("Pi-xu", "Niedobór śledziony"),
        ("Shen-xu", "Niedobór nerek"),
        ("Jing-xu", "Niedobór esencji"),
        ("Gan-yang", "Yang wątroby"),
        ("Shen-yin", "Yin nerek"),
        ("Xin-shen", "Serce-umysł"),
    ],

    "sztuki_walki_dodatkowe": [
        ("Quan-fa", "Sztuka walki pięściami"),
        ("Jian-fa", "Sztuka walki mieczem"),
        ("Dao-fa", "Sztuka walki szablą"),
        ("Qiang-fa", "Sztuka walki włócznią"),
        ("Gun-fa", "Sztuka walki kijem"),
        ("Zhang-fa", "Sztuka walki laską"),
        ("Qing-gong", "Lekka umiejętność (latanie)"),
        ("Nei-gong", "Wewnętrzna siła"),
        ("Wai-gong", "Zewnętrzna siła"),
        ("Ying-gong", "Twarda siła"),
        ("Rou-gong", "Miękka siła"),
        ("Nei-li", "Wewnętrzna moc"),
        ("Wai-li", "Zewnętrzna moc"),
        ("Jin", "Siła wewnętrzna (jin)"),
        ("Dan-tian", "Pole elixiru"),
        ("Jing-mai", "Merydian"),
        ("Xue-wei", "Punkt akupunktury"),
        ("Dian-xue", "Uderzanie punktów"),
        ("Qin-na", "Chwytanie i kontrola"),
        ("Shuai-jiao", "Rzucanie"),
        ("Ti-tui", "Kopanie"),
        ("Shou-fa", "Techniki ręczne"),
        ("Bu-fa", "Techniki stóp"),
        ("Shen-fa", "Praca ciała"),
        ("Yan-fa", "Praca oczu"),
        ("Xin-fa", "Metoda serca/umysłu"),
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
            conflicts.append(f"  {lengxuan} - {polish} (istniejace: {word_dict[normalized][1]})")
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
        status = "CEL OSIAGNIETY! (3000+)"
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
    print("GENERATOR SLOWNIKA LENGXUAN - ABSOLUTE FINAL CZESC 8")
    print("CEL: DEFINITYWNE PRZEKROCZENIE 3000+ SLOW!")
    print("=" * 60)

    dict_path = "../03_Slownik/slownik_lengxuan_polski.md"
    output_path = "../03_Slownik/slownik_lengxuan_polski.md"

    print(f"\nLadowanie istniejacego slownika...")
    word_dict = load_existing_dict(dict_path)
    print(f"Zaladowano {len(word_dict)} istniejacych slow")

    total_added = 0
    total_conflicts = 0

    categories = [
        ("czasowniki_specjalistyczne", "Czasowniki specjalistyczne"),
        ("przymiotniki_dodatkowe", "Przymiotniki dodatkowe"),
        ("zwierzeta_dodatkowe", "Zwierzeta dodatkowe"),
        ("rosliny_dodatkowe", "Rosliny dodatkowe"),
        ("zjawiska_naturalne_dodatkowe", "Zjawiska naturalne dodatkowe"),
        ("stany_przedmiotow", "Stany przedmiotow"),
        ("stany_umyslowe_dodatkowe", "Stany umyslowe dodatkowe"),
        ("filozofia_dodatkowa", "Filozofia dodatkowa"),
        ("medycyna_tcm_dodatkowa", "Medycyna TCM dodatkowa"),
        ("sztuki_walki_dodatkowe", "Sztuki walki dodatkowe"),
    ]

    for cat_key, cat_name in categories:
        print(f"\nDodawanie kategorii: {cat_key}...")
        added, conflicts = add_category_to_dict(
            word_dict,
            cat_name,
            ABSOLUTE_FINAL_VOCABULARY[cat_key]
        )
        total_added += added
        total_conflicts += conflicts

    print("\n" + "=" * 60)
    print(f"ABSOLUTE FINAL CZESC 8 - SUMA: Dodano {total_added} nowych slow")
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
        print(f"\n  CEL OSIAGNIETY! (3000+)")
        print(f"  PRZEKROCZONO O: {len(word_dict) - 3000} slow!")
    else:
        print(f"\n  Cel (3000+): Brakuje {3000 - len(word_dict)} slow")

    print("=" * 60)
    print("\nSLOWNIK LENGXUAN KOMPLETNY!")
    print("=" * 60)

if __name__ == "__main__":
    main()
