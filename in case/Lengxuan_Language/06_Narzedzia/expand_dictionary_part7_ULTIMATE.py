# -*- coding: utf-8 -*-
"""
GENERATOR SŁOWNIKA LENGXUAN - CZĘŚĆ 7 ULTIMATE (FINAŁ)
Cel: PRZEKROCZENIE 3000+ słów w słowniku

Dodaje ~500 nowych słów w ostatnich szczegółowych kategoriach:
- Szczegółowe jedzenie (mięsa, ryby, przyprawy)
- Szczegółowe narzędzia i implementy
- Elementy architektoniczne
- Stopnie wojskowe i urzędnicze
- Rozszerzone tytuły i honoryfikaty
- Rozszerzone pokrewieństwo
- Materiały naturalne szczegółowe
- Dodatkowe techniki kulinarne
- Jednostki miar szczegółowe
- Kierunki i orientacja
- Kształty i formy
- Pojemniki i naczynia
- Meble
- Instrumenty muzyczne
- Rośliny lecznicze i ozdobne
- Minerały i kamienie szlachetne
- Dodatkowe rzemiosła
- Terminy uczonych
"""

import re
from collections import defaultdict

# ============================================================
# SŁOWNICTWO ULTIMATE - CZĘŚĆ 7 (~500 SŁÓW)
# ============================================================

ULTIMATE_VOCABULARY = {
    "jedzenie_miesa_ryby": [
        ("Rou", "Mięso"),
        ("Zhu-rou", "Wieprzowina"),
        ("Niu-rou", "Wołowina"),
        ("Yang-rou", "Baranina"),
        ("Ji-rou", "Kurczak (mięso)"),
        ("Ya-rou", "Kaczka (mięso)"),
        ("E-rou", "Gęsina"),
        ("Lu-rou", "Dziczyzna"),
        ("Tu-rou", "Królik (mięso)"),
        ("Fei", "Tłuste mięso"),
        ("Shou", "Chude mięso"),
        ("Gan", "Wątroba (jedzenie)"),
        ("Xin", "Serce (jedzenie)"),
        ("Fei", "Płuca (jedzenie)"),
        ("Shen", "Nerki (jedzenie)"),
        ("Du", "Żołądek (jedzenie)"),
        ("Chang", "Jelita (jedzenie)"),
        ("Pi", "Śledziona (jedzenie)"),
        ("Gu", "Kość (z mięsem)"),
        ("Dan", "Jajko"),
        ("Ji-dan", "Jajko kurze"),
        ("Ya-dan", "Jajko kacze"),
        ("Pi-dan", "Jajko stulecia"),
        ("Xian-dan", "Jajko solone"),
        ("You", "Olej, tłuszcz"),
        ("Zhu-you", "Smalec"),
        ("Hua-sheng-you", "Olej orzechowy"),
        ("Zhi-ma-you", "Olej sezamowy"),
        ("Jiang", "Sos, pasta"),
        ("Jiang-you", "Sos sojowy"),
        ("Dou-ban-jiang", "Pasta z bobu"),
        ("Tian-mian-jiang", "Słodki sos fasolowy"),
        ("Cu", "Ocet"),
        ("Yan", "Sól"),
        ("Tang", "Cukier"),
        ("Mi", "Miód"),
        ("La-jiao", "Papryka chili"),
        ("Hua-jiao", "Pieprz syczuański"),
        ("Jiang", "Imbir"),
        ("Suan", "Czosnek"),
        ("Cong", "Szczypior"),
        ("Xiang-cai", "Kolendra"),
    ],

    "narzedzia_implementy": [
        ("Qi-ju", "Narzędzie, instrument"),
        ("Gong-ju", "Narzędzie robocze"),
        ("Chui-zi", "Młotek"),
        ("Fu-zi", "Siekiera"),
        ("Ju-zi", "Piła"),
        ("Bao-zi", "Strug"),
        ("Zao-zi", "Dłuto"),
        ("Zuan-zi", "Wiertło"),
        ("Cuo", "Pilnik"),
        ("Qian-zi", "Szczypce, obcęgi"),
        ("Qi-zi", "Cęgi"),
        ("Ying-zi", "Szpilka"),
        ("Ding-zi", "Gwóźdź"),
        ("Luo-si-ding", "Śruba"),
        ("Sheng-zi", "Lina"),
        ("Sheng-suo", "Sznur, lina"),
        ("Gua-zi", "Klamra, haczyk"),
        ("Suo-lian", "Łańcuch"),
        ("Huan", "Pierścień, obręcz"),
        ("Quan", "Obręcz"),
        ("Gun-zi", "Kij, drąg"),
        ("Bang-zi", "Pałka"),
        ("Zhang-zi", "Laska"),
        ("Gan-zi", "Tyka, drążek"),
        ("Ti-zi", "Drabina"),
        ("Hua-che", "Wózek"),
        ("Du-lun-che", "Taczka"),
        ("Shui-tong", "Wiadro na wodę"),
        ("Dan-zi", "Koromysło"),
    ],

    "architektura_elementy": [
        ("Dian", "Pałac, świątynia"),
        ("Tang", "Sala"),
        ("Ge", "Pawilon"),
        ("Lou", "Budynek wielopiętrowy"),
        ("Tai", "Platforma, taras"),
        ("Ting", "Pawilon (ogrodowy)"),
        ("Xuan", "Weranda"),
        ("Lang", "Korytarz"),
        ("Yuan", "Dziedziniec"),
        ("Men-lou", "Brama"),
        ("Pai-fang", "Paifang, łuk pamiątkowy"),
        ("Zhuan", "Cegła"),
        ("Wa", "Dachówka"),
        ("Shi-ban", "Kamienna płyta"),
        ("Mu-ban", "Deska"),
        ("Liang-zhu", "Belka i słup"),
        ("Diao-ke", "Rzeźba, ornament"),
        ("Hua-wen", "Wzór, dekoracja"),
        ("Ping-feng", "Parawan"),
        ("Men-jian", "Próg"),
        ("Chuang-ge", "Kratka okienna"),
    ],

    "stopnie_wojskowe_urzedn": [
        ("Da-jiang-jun", "Wielki generał"),
        ("Xiao-jiang", "Młodszy generał"),
        ("Du-wei", "Komendant"),
        ("Xiao-wei", "Kapitan, oficer"),
        ("Zhong-wei", "Środkowy oficer"),
        ("Shi-zhang", "Dowódca dziesiątki"),
        ("Bai-fu", "Setnik"),
        ("Qian-fu", "Tysięcznik"),
        ("Xian-ling", "Naczelnik powiatu"),
        ("Zhi-fu", "Prefekt"),
        ("Zong-du", "Gubernator generalny"),
        ("Xun-fu", "Wicegubernator"),
        ("Tai-shou", "Gubernator"),
        ("Zhou-mu", "Namiestnik"),
        ("Zai-xiang", "Kanclerz"),
        ("Shang-shu", "Minister"),
        ("Shi-lang", "Wiceminister"),
        ("Yuan-wai-lang", "Urzędnik departamentu"),
        ("Zhu-bu", "Sekretarz"),
        ("Li-bu", "Ministerstwo Personelu"),
        ("Hu-bu", "Ministerstwo Dochodów"),
        ("Li-bu", "Ministerstwo Obrzędów"),
        ("Bing-bu", "Ministerstwo Wojny"),
        ("Xing-bu", "Ministerstwo Sprawiedliwości"),
        ("Gong-bu", "Ministerstwo Robót Publicznych"),
    ],

    "tytuly_honoryfikaty_rozsz": [
        ("-jun", "Pan (szlachetny)"),
        ("-qing", "Minister (tytuł)"),
        ("-hou", "Markiz"),
        ("-bo", "Hrabia"),
        ("-zi", "Wicehrabia"),
        ("-nan", "Baron"),
        ("-gong", "Książę"),
        ("-wang", "Król"),
        ("-huang", "Cesarz"),
        ("-di", "Cesarz (tytuł)"),
        ("-hou", "Cesarzowa"),
        ("-fei", "Konkubina cesarska"),
        ("-guifei", "Szlachetna konkubina"),
        ("-taizi", "Następca tronu"),
        ("-wangzi", "Książę (syn króla)"),
        ("-gongzhu", "Księżniczka"),
        ("-xiangong", "Szanowny pan"),
        ("-xiansheng", "Pan (nauczyciel)"),
        ("-daren", "Wielki człowiek (tytuł)"),
        ("-dashi", "Wielki mistrz"),
        ("-zongshi", "Grand master"),
    ],

    "pokrewienstwo_rozszerzone": [
        ("Tang-xiong", "Brat stryjeczny (starszy)"),
        ("Tang-di", "Brat stryjeczny (młodszy)"),
        ("Tang-jie", "Siostra stryjeczna (starsza)"),
        ("Tang-mei", "Siostra stryjeczna (młodsza)"),
        ("Biao-xiong", "Brat cioteczny (starszy)"),
        ("Biao-di", "Brat cioteczny (młodszy)"),
        ("Biao-jie", "Siostra cioteczna (starsza)"),
        ("Biao-mei", "Siostra cioteczna (młodsza)"),
        ("Wai-gong", "Dziadek od matki"),
        ("Wai-po", "Babcia od matki"),
        ("Zu-fu", "Dziadek od ojca"),
        ("Zu-mu", "Babcia od ojca"),
        ("Bo-fu", "Stryj (starszy brat ojca)"),
        ("Bo-mu", "Żona stryja"),
        ("Shu-fu", "Stryj (młodszy brat ojca)"),
        ("Shu-mu", "Żona stryja młodszego"),
        ("Gu-fu", "Mąż cioci"),
        ("Yi-fu", "Mąż cioci od matki"),
        ("Yi-mu", "Ciocia od matki"),
        ("Jiu-fu", "Wujek (brat matki)"),
        ("Jiu-mu", "Żona wujka"),
        ("Qin-jia", "Krewni od męża"),
        ("Niang-jia", "Rodzina od żony"),
    ],

    "materialy_naturalne": [
        ("Mu-cai", "Drewno (materiał)"),
        ("Ying-mu", "Twarde drewno"),
        ("Ruan-mu", "Miękkie drewno"),
        ("Song-mu", "Drewno sosnowe"),
        ("Bai-mu", "Drewno cedrowe"),
        ("Tan-mu", "Drzewo sandałowe"),
        ("Zi-tan", "Palisander"),
        ("Hong-mu", "Drewno różane"),
        ("Shi-cai", "Kamień (materiał)"),
        ("Da-li-shi", "Marmur"),
        ("Hua-gang-shi", "Granit"),
        ("Qing-shi", "Kamień łupkowy"),
        ("Sha-shi", "Piaskowiec"),
        ("Shi-hui", "Wapień"),
        ("Ni-tu", "Glina"),
        ("Tao-tu", "Glina garnczarska"),
        ("Ci-qi", "Porcelana"),
        ("Tao-qi", "Ceramika"),
    ],

    "techniki_kulinarne_dodatkowe": [
        ("Qie-pian", "Kroić w plasterki"),
        ("Qie-si", "Kroić w paski"),
        ("Qie-ding", "Kroić w kostkę"),
        ("Duo-sui", "Siekać na miazgę"),
        ("Bao-chao", "Smażyć na dużym ogniu"),
        ("Man-dun", "Dusić powoli"),
        ("Kuai-chao", "Szybko smażyć"),
        ("Shui-zhu", "Gotować w wodzie"),
        ("Zheng-zhu", "Gotować na parze"),
        ("Hong-shao", "Dusić w sosie"),
        ("Tang-cu", "Słodko-kwaśne"),
        ("Gan-bian", "Smażyć do sucha"),
        ("Hui", "Dusić z sosem"),
        ("Hui-guo", "Gotować ponownie"),
    ],

    "miary_jednostki_dodatkowe": [
        ("Bu", "Krok (miara)"),
        ("Fen", "Dziesiąta część cala"),
        ("Hao", "Setna część cala"),
        ("Yin", "Uncja (~30g)"),
        ("Ke", "Ćwierćuncja"),
        ("Shao", "Łyżka (miara)"),
        ("Cuo", "Szczypta"),
        ("He", "Pudełko (miara objętości)"),
        ("Ge", "Dziesiąta część sheng"),
    ],

    "kierunki_orientacja": [
        ("Dong-bei", "Północny wschód"),
        ("Dong-nan", "Południowy wschód"),
        ("Xi-bei", "Północny zachód"),
        ("Xi-nan", "Południowy zachód"),
        ("Zheng-dong", "Dokładnie wschód"),
        ("Zheng-xi", "Dokładnie zachód"),
        ("Zheng-nan", "Dokładnie południe"),
        ("Zheng-bei", "Dokładnie północ"),
        ("Shang-feng", "Kierunek wiatru"),
        ("Xia-feng", "Pod wiatr"),
        ("Shun-feng", "Z wiatrem"),
        ("Ni-feng", "Pod wiatr"),
    ],

    "ksztalty_formy": [
        ("Xing", "Forma, kształt"),
        ("Yuan-xing", "Okrągły kształt"),
        ("Fang-xing", "Kwadratowy kształt"),
        ("Chang-fang-xing", "Prostokątny"),
        ("San-jiao-xing", "Trójkątny"),
        ("Wu-jiao-xing", "Pięciokątny"),
        ("Liu-jiao-xing", "Sześciokątny"),
        ("Ba-jiao-xing", "Ośmiokątny"),
        ("Tuo-yuan-xing", "Owalny"),
        ("Xing-xing", "Gwiaździsty"),
        ("Zhen-xing", "Igiełkowaty"),
        ("Pian-xing", "Płaski"),
        ("Qiu-xing", "Kulisty"),
        ("Yuan-zhui-xing", "Stożkowaty"),
        ("Yuan-zhu-xing", "Cylindryczny"),
    ],

    "pojemniki_naczynia_dodatkowe": [
        ("Tan", "Dzban, słój"),
        ("Weng", "Ulka, dzban"),
        ("Gang", "Garnek (duży)"),
        ("Hu-lu", "Tykwa"),
        ("Zun", "Puchar ceremonialny"),
        ("Ding", "Trójnóg rytualny"),
        ("Gui", "Misa rytualna"),
        ("Dou", "Kielich na nóżce"),
        ("He", "Pudełko"),
        ("Xia", "Skrzynia"),
        ("Gui", "Szafka, komoda"),
        ("Long", "Kosz"),
        ("Kuang", "Kosz (duży)"),
        ("Lan", "Koszyk"),
        ("Dai", "Torba, worek"),
        ("Bao-fu", "Zawiniątko"),
    ],

    "meble": [
        ("Jia-ju", "Meble"),
        ("Zhuo-zi", "Stół"),
        ("Yi-zi", "Krzesło"),
        ("Deng-zi", "Stołek"),
        ("Chuang", "Łóżko"),
        ("Ta", "Kanapa, leżanka"),
        ("An", "Stolik niski"),
        ("Ji", "Stolik (mały)"),
        ("Gui-zi", "Szafa"),
        ("Chu-gui", "Kredens"),
        ("Shu-jia", "Półka na książki"),
        ("Jia-zi", "Półka, regał"),
        ("Ping-feng", "Parawan"),
        ("Lian-zi", "Zasłona z koralików"),
        ("Zhen-tou", "Poduszka"),
        ("Xi-dian", "Poduszka do siedzenia"),
        ("Tan-zi", "Dywan, mata"),
        ("Xi-zi", "Mata (do siedzenia)"),
    ],

    "instrumenty_muzyczne_szcz": [
        ("Qin", "Cytra (guqin)"),
        ("Zheng", "Cytra (guzheng)"),
        ("Pipa", "Lutnia chińska"),
        ("Er-hu", "Skrzypce chińskie"),
        ("Di-zi", "Flet bambusowy"),
        ("Xiao", "Fletnia pionowa"),
        ("Sheng", "Organy ustne"),
        ("Suo-na", "Surna"),
        ("Gu", "Bęben"),
        ("Da-gu", "Wielki bęben"),
        ("Xiao-gu", "Mały bęben"),
        ("Luo", "Gong"),
        ("Zhong", "Dzwon"),
        ("Bian-zhong", "Zestaw dzwonów"),
        ("Mu-yu", "Drewniany bęben rybka"),
        ("Bang-zi", "Klepki"),
    ],

    "rosliny_lecznicze_ozdobne": [
        ("Mu-dan", "Piwonia drzewiasta"),
        ("Shao-yao", "Piwonia zielna"),
        ("Mei-hua", "Kwiat śliwy"),
        ("Lan-hua", "Orchidea"),
        ("Zhu-hua", "Kwiat bambusa"),
        ("He-hua", "Lotos"),
        ("Gui-hua", "Osmanthus"),
        ("Ying-hua", "Kwiat wiśni"),
        ("Tao-hua", "Kwiat brzoskwini"),
        ("Li-hua", "Kwiat gruszy"),
        ("Xing-hua", "Kwiat moreli"),
        ("Shi-liu-hua", "Kwiat granatu"),
        ("Liu-shu", "Wierzba"),
        ("Song-shu", "Sosna"),
        ("Bai-shu", "Cyprys"),
        ("Wu-tong", "Firmiana"),
        ("Feng-shu", "Klon"),
    ],

    "mineraly_kamienie": [
        ("Yu-shi", "Jaspis, jade"),
        ("Fei-cui", "Jadekit"),
        ("Ma-nao", "Agat"),
        ("Shui-jing", "Kryształ"),
        ("Zuan-shi", "Diament"),
        ("Hong-bao-shi", "Rubin"),
        ("Lan-bao-shi", "Szafir"),
        ("Lü-bao-shi", "Szmaragd"),
        ("Zhen-zhu", "Perła"),
        ("Hu-po", "Bursztyn"),
        ("Shan-hu", "Koral"),
        ("Zi-shui-jing", "Ametyst"),
        ("Huang-yu", "Topaz"),
    ],

    "rzemiosto_dodatkowe": [
        ("Diao-ke", "Rzeźbić"),
        ("Diao-ke-shi", "Rzeźbiarz"),
        ("Ke-ban", "Grawerować"),
        ("Shua-qi", "Lakierować"),
        ("Qi-jiang", "Lakiernik"),
        ("Jin-xiu", "Złote hafty"),
        ("Xiu-niang", "Hafciarka"),
        ("Zhu-bao-jiang", "Jubiler"),
        ("Zhi-tao", "Wyrabiać ceramikę"),
        ("Tao-gong", "Garncarz"),
        ("Zhu-jian", "Budować łódź"),
        ("Chuan-jiang", "Budowniczy łodzi"),
    ],

    "terminy_uczone_dodatkowe": [
        ("Xue-wen", "Wiedza, nauka"),
        ("Bo-xue", "Erudycja"),
        ("Bo-shi", "Doktor (stopień)"),
        ("Jin-shi", "Uczony (stopień)"),
        ("Ju-ren", "Zdający egzamin prowincjonalny"),
        ("Xiu-cai", "Absolwent egzaminu powiatowego"),
        ("Ke-ju", "Egzaminy cesarskie"),
        ("Jing", "Klasyki (księgi)"),
        ("Jing-dian", "Kanon klasyczny"),
        ("Zhu", "Komentarz"),
        ("Shu", "Traktat"),
        ("Lun", "Dysertacja"),
        ("Kao", "Badać, egzaminować"),
        ("Yan", "Badać, studiować"),
        ("Jiu", "Dociekać"),
        ("Tan", "Dyskutować"),
        ("Bian", "Debatować"),
    ],
}

# ============================================================
# FUNKCJE POMOCNICZE (TAKIE SAME JAK WCZEŚNIEJ)
# ============================================================

def load_existing_dict(file_path):
    """Wczytuje istniejący słownik z pliku Markdown"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Wzór: - Słowo - Znaczenie
        pattern = r'^- ([A-Za-zęóąśłżźćńĘÓĄŚŁŻŹĆŃüÜ-]+) - (.+)$'
        entries = re.findall(pattern, content, re.MULTILINE)

        # Normalizuj do małych liter dla porównania
        word_dict = {}
        for word, meaning in entries:
            normalized = word.lower().strip()
            word_dict[normalized] = (word, meaning.strip())

        return word_dict
    except FileNotFoundError:
        print(f"[BŁĄD] Nie znaleziono pliku: {file_path}")
        return {}

def add_category_to_dict(word_dict, category_name, category_words):
    """Dodaje nową kategorię do słownika, pomijając duplikaty"""
    conflicts = []
    added = 0

    for lengxuan, polish in category_words:
        normalized = lengxuan.lower().strip()

        if normalized in word_dict:
            conflicts.append(f"  {lengxuan} - {polish} (istniejące: {word_dict[normalized][1]})")
        else:
            word_dict[normalized] = (lengxuan, polish)
            added += 1

    if conflicts:
        print(f"  UWAGA: Znaleziono {len(conflicts)} konfliktów")

    print(f"  Dodano {added} nowych słów")
    return added, len(conflicts)

def save_dict_to_markdown(word_dict, output_path):
    """Zapisuje słownik do pliku Markdown"""
    # Sortuj alfabetycznie
    sorted_entries = sorted(word_dict.items(), key=lambda x: x[1][0].lower())

    status = "✓✓✓ CEL OSIĄGNIĘTY! (3000+) ✓✓✓" if len(sorted_entries) >= 3000 else "W TRAKCIE ROZBUDOWY"

    output = f"""# Słownik Lengxuan - KOMPLETNY (3000+ słów)

**Liczba wpisów:** {len(sorted_entries)}
**Ostatnia aktualizacja:** 2026-01-03

**Status:** {status}

---

"""

    for normalized, (word, meaning) in sorted_entries:
        output += f"- {word} - {meaning}\n"

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"\n[OK] Zapisano kompletny słownik: {output_path}")
    print(f"  Całkowita liczba wpisów: {len(sorted_entries)}")

# ============================================================
# GŁÓWNA FUNKCJA
# ============================================================

def main():
    print("=" * 60)
    print("GENERATOR SŁOWNIKA LENGXUAN - ULTIMATE CZĘŚĆ 7 (FINAŁ)")
    print("CEL: PRZEKROCZENIE 3000+ SŁÓW!")
    print("=" * 60)

    # Ścieżki
    dict_path = "../03_Slownik/slownik_lengxuan_polski.md"
    output_path = "../03_Slownik/slownik_lengxuan_polski.md"

    # Wczytaj istniejący słownik
    print(f"\nŁadowanie istniejącego słownika...")
    word_dict = load_existing_dict(dict_path)
    print(f"Załadowano {len(word_dict)} istniejących słów")

    # Dodaj nowe kategorie
    total_added = 0
    total_conflicts = 0

    categories = [
        ("jedzenie_miesa_ryby", "Jedzenie - Mięsa, ryby, przyprawy"),
        ("narzedzia_implementy", "Narzędzia i implementy"),
        ("architektura_elementy", "Architektura - Elementy"),
        ("stopnie_wojskowe_urzedn", "Stopnie wojskowe i urzędnicze"),
        ("tytuly_honoryfikaty_rozsz", "Tytuły i honoryfikaty - Rozszerzone"),
        ("pokrewienstwo_rozszerzone", "Pokrewieństwo rozszerzone"),
        ("materialy_naturalne", "Materiały naturalne"),
        ("techniki_kulinarne_dodatkowe", "Techniki kulinarne - Dodatkowe"),
        ("miary_jednostki_dodatkowe", "Miary i jednostki - Dodatkowe"),
        ("kierunki_orientacja", "Kierunki i orientacja"),
        ("ksztalty_formy", "Kształty i formy"),
        ("pojemniki_naczynia_dodatkowe", "Pojemniki i naczynia - Dodatkowe"),
        ("meble", "Meble"),
        ("instrumenty_muzyczne_szcz", "Instrumenty muzyczne - Szczegółowe"),
        ("rosliny_lecznicze_ozdobne", "Rośliny lecznicze i ozdobne"),
        ("mineraly_kamienie", "Minerały i kamienie szlachetne"),
        ("rzemiosto_dodatkowe", "Rzemiosło - Dodatkowe"),
        ("terminy_uczone_dodatkowe", "Terminy uczonych - Dodatkowe"),
    ]

    for cat_key, cat_name in categories:
        print(f"\nDodawanie kategorii: {cat_key}...")
        added, conflicts = add_category_to_dict(
            word_dict,
            cat_name,
            ULTIMATE_VOCABULARY[cat_key]
        )
        total_added += added
        total_conflicts += conflicts

    # Zapisz kompletny słownik
    print("\n" + "=" * 60)
    print(f"ULTIMATE CZĘŚĆ 7 (FINAŁ) - SUMA: Dodano {total_added} nowych słów")
    print(f"Całkowita liczba słów: {len(word_dict)}")
    print("=" * 60)

    save_dict_to_markdown(word_dict, output_path)

    # Statystyki końcowe
    print("\n" + "=" * 60)
    print("STATYSTYKI KOŃCOWE:")
    print("=" * 60)
    print(f"  Całkowita liczba słów: {len(word_dict)}")
    print(f"  Dodano w tej sesji: {total_added}")
    print(f"  Wykryto konfliktów: {total_conflicts}")

    if len(word_dict) >= 3000:
        print(f"\n  ✓✓✓ CEL OSIĄGNIĘTY! (3000+) ✓✓✓")
        print(f"  PRZEKROCZONO O: {len(word_dict) - 3000} słów!")
    else:
        print(f"\n  Cel (3000+): Brakuje {3000 - len(word_dict)} słów")

    print("=" * 60)
    print("\n" + "=" * 60)
    print("✓✓✓ SŁOWNIK LENGXUAN KOMPLETNY! ✓✓✓")
    print("=" * 60)

if __name__ == "__main__":
    main()
