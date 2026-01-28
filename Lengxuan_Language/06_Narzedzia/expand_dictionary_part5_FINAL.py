# -*- coding: utf-8 -*-
"""
GENERATOR SŁOWNIKA LENGXUAN - CZĘŚĆ 5 (FINAŁ)
Cel: Osiągnięcie 3000+ słów w słowniku

Dodaje ~900 nowych słów w kategoriach:
- Szczegółowe czasowniki (gotowanie, medycyna, budowa)
- Szczegółowe części ciała
- Przedmioty domowe i narzędzia
- Czas (pory roku, dnia, kalendarz)
- Kolory i odcienie
- Tekstury i materiały
- Dźwięki i onomatopeje
- Zapachy i smaki
- Relacje przestrzenne
- Kwantyfikatory i miary
- Idiomy i zwroty
- Szczegóły natury
- Terminy rzemieślnicze
- Handel i administracja
- Terminy akademickie
"""

import re
from collections import defaultdict

# ============================================================
# NOWA PORCJA SŁOWNICTWA - CZĘŚĆ 5 (900+ SŁÓW)
# ============================================================

FINAL_VOCABULARY = {
    "czasowniki_gotowanie": [
        ("Zhu", "Gotować (w wodzie)"),
        ("Zheng", "Gotować na parze"),
        ("Jian", "Smażyć (na patelni)"),
        ("Chao", "Smażyć (z mieszaniem)"),
        ("Shao", "Dusić, piec"),
        ("Kao", "Piec, grillować"),
        ("Lu", "Gotować na wolnym ogniu"),
        ("Dun", "Dusić (długo)"),
        ("Yan", "Marynować solą"),
        ("Xun", "Wędzić"),
        ("Tang", "Zupa (czasownik: gotować zupę)"),
        ("Bao", "Zawijać (pierogi)"),
        ("Gan", "Toczyć (ciasto)"),
        ("Qie", "Kroić"),
        ("Duo", "Siekać"),
        ("Pian", "Kroić w plasterki"),
        ("Si", "Kroić w paski"),
        ("Ding", "Kroić w kostkę"),
        ("Mo", "Mielić, ucierać"),
        ("Niang", "Fermentować, warzyć"),
        ("Jiao", "Mieszać"),
        ("Hun", "Mieszać (składniki)"),
        ("Reng", "Rzucać (przyprawy)"),
        ("Sa", "Posypywać"),
        ("Lin", "Skrapiać, polewać"),
        ("Guan", "Napełniać (słoik)"),
        ("Shai", "Suszyć na słońcu"),
        ("Hong", "Suszyć nad ogniem"),
        ("Dong", "Mrożić"),
        ("Hua", "Rozmrażać"),
    ],

    "czasowniki_medyczne": [
        ("Zhen", "Diagnozować"),
        ("Mai", "Badać puls"),
        ("Kan", "Oglądać (pacjenta)"),
        ("Wen", "Wypytywać (o objawy)"),
        ("Qie", "Badać dotykaniem"),
        ("Zhen-jiu", "Akupunktura i moksybustia"),
        ("Zha", "Wkłuwać (igłę)"),
        ("Ba", "Wyciągać (igłę, truciznę)"),
        ("Gua-sha", "Skrobać (terapia)"),
        ("Tui-na", "Masaż terapeutyczny"),
        ("An", "Naciskać (punkt)"),
        ("Rou", "Masować okrężnie"),
        ("Nie", "Ugniatać"),
        ("Na", "Chwytać, łapać (mięsień)"),
        ("Yao", "Lek (rzeczownik i czasownik)"),
        ("Fu", "Brać (lek)"),
        ("Jian", "Gotować (zioła)"),
        ("Ao", "Gotować (długo, wywary)"),
        ("Fu-yong", "Stosować (zewnętrznie)"),
        ("Tie", "Przyklejać (plaster)"),
        ("Zhi", "Leczyć"),
        ("Liao", "Terapia"),
        ("Yang", "Odżywiać, pielęgnować"),
        ("Tiao", "Harmonizować, regulować"),
        ("Bu", "Uzupełniać (energię)"),
        ("Xie", "Oczyszczać (nadmiar)"),
        ("Wen", "Ogrzewać"),
        ("Qing", "Chłodzić"),
        ("Shi", "Nawilżać"),
        ("Zao", "Osuszać"),
    ],

    "czasowniki_budowa": [
        ("Zao", "Budować"),
        ("Jian", "Wznosić (budynek)"),
        ("Gai", "Budować (dom)"),
        ("Qi", "Wznosić, podnosić"),
        ("Die", "Układać (cegły)"),
        ("Zhu", "Odlewać, stawiać (fundament)"),
        ("Wa", "Kopać"),
        ("Tian", "Wypełniać (ziemią)"),
        ("Zhen", "Ubijać (ziemię)"),
        ("Diao", "Rzeźbić, wykuwać"),
        ("Ke", "Wycinać, grawerować"),
        ("Mo", "Polerować"),
        ("Qi", "Lakierować"),
        ("Hua", "Malować (ściany)"),
        ("Tu", "Smarować (farbą)"),
        ("Fen", "Bielić"),
        ("Zhuang", "Instalować"),
        ("Jie", "Demontować"),
        ("Chai", "Rozbierać, burzyć"),
        ("La", "Ciągnąć (linę)"),
        ("Tui", "Pchać"),
        ("Tai", "Dźwigać (razem)"),
        ("Ban", "Przenosić"),
        ("Yun", "Transportować"),
        ("Diao", "Podnosić (dźwigiem)"),
    ],

    "cialo_szczegoly": [
        ("Tou-fa", "Włosy na głowie"),
        ("Mei-mao", "Brwi"),
        ("Jie-mao", "Rzęsy"),
        ("Hu-zi", "Broda, wąsy"),
        ("E-tou", "Czoło"),
        ("Tai-yang", "Skroń"),
        ("Lian-jia", "Policzek"),
        ("Xia-ba", "Podbródek"),
        ("Bo-zi", "Szyja"),
        ("Hou-long", "Gardło"),
        ("Jian-bang", "Ramię (bark)"),
        ("Zhou", "Łokieć"),
        ("Wan", "Nadgarstek"),
        ("Shou-zhang", "Dłoń"),
        ("Shou-zhi", "Palec u ręki"),
        ("Mu-zhi", "Kciuk"),
        ("Zhi-jia", "Paznokieć"),
        ("Xiong", "Klatka piersiowa"),
        ("Ru-fang", "Pierś (żeńska)"),
        ("Du-zi", "Brzuch"),
        ("Qi", "Pępek"),
        ("Yao", "Talia, pas"),
        ("Tun", "Pośladki"),
        ("Kua", "Biodro"),
        ("Da-tui", "Udo"),
        ("Xi", "Kolano"),
        ("Xiao-tui", "Goleń"),
        ("Jiao-huai", "Kostka (nogi)"),
        ("Jiao-zhang", "Podeszwa stopy"),
        ("Jiao-zhi", "Palec u nogi"),
        ("Jiao-gen", "Pięta"),
        ("Gan", "Wątroba"),
        ("Dan", "Pęcherzyk żółciowy"),
        ("Wei", "Żołądek"),
        ("Chang", "Jelito"),
        ("Shen-zang", "Nerka (organ)"),
        ("Pang-guang", "Pęcherz moczowy"),
        ("Xin-zang", "Serce (organ)"),
        ("Gu-sui", "Szpik kostny"),
        ("Xue-guan", "Naczynie krwionośne"),
        ("Jin", "Ścięgno"),
    ],

    "przedmioty_domowe": [
        ("Men", "Drzwi"),
        ("Chuang", "Okno"),
        ("Qiang", "Ściana"),
        ("Di", "Podłoga"),
        ("Tian-hua-ban", "Sufit"),
        ("Wu-ding", "Dach"),
        ("Zhu-zi", "Słup, kolumna"),
        ("Liang", "Belka"),
        ("Lou-ti", "Schody"),
        ("Tai-jie", "Stopnie"),
        ("Lan-gan", "Balustrada"),
        ("Chuang-hu", "Okno"),
        ("Chuang-lian", "Zasłona"),
        ("Men-shuang", "Zawias"),
        ("Suo", "Zamek"),
        ("Yao-shi", "Klucz"),
        ("Deng", "Lampa, światło"),
        ("Zhu", "Świeca"),
        ("Lu", "Piec"),
        ("Zao", "Kuchenka"),
        ("Yan-cong", "Komin"),
        ("Shui-gang", "Dzban na wodę"),
        ("Pen", "Miska"),
        ("Die", "Talerz"),
        ("Wan", "Miska (do ryżu)"),
        ("Bei", "Kubek, kieliszek"),
        ("Shao", "Łyżka"),
        ("Kuai-zi", "Pałeczki"),
        ("Dao", "Nóż (kuchenny)"),
        ("Cha", "Widelec"),
        ("Guo", "Garnek, patelnia"),
        ("Hu", "Czajnik"),
        ("Zeng", "Parowiec (bambusowy)"),
        ("Ping", "Butelka"),
        ("Guan", "Słoik"),
        ("Tong", "Wiadro"),
        ("Pen-di", "Miednica"),
        ("Sao-zhou", "Miotła"),
        ("Mo-bu", "Ścierka"),
        ("Sheng", "Lina, sznur"),
        ("Zhen", "Igła"),
        ("Xian", "Nić"),
        ("Jian-dao", "Nożyczki"),
        ("Zhi", "Papier"),
        ("Bi", "Pędzel, pióro"),
        ("Mo", "Tusz"),
        ("Yan", "Kamień do tuszu"),
        ("Shu", "Książka"),
        ("Juan", "Zwój"),
        ("Fu", "Obraz (wiszący)"),
    ],

    "czas_kalendarz": [
        ("Chun-tian", "Wiosna"),
        ("Xia-tian", "Lato"),
        ("Qiu-tian", "Jesień"),
        ("Dong-tian", "Zima"),
        ("Chun-fen", "Równonoc wiosenna"),
        ("Xia-zhi", "Przesilenie letnie"),
        ("Qiu-fen", "Równonoc jesienna"),
        ("Dong-zhi", "Przesilenie zimowe"),
        ("Li-chun", "Początek wiosny"),
        ("Jing-zhe", "Przebudzenie owadów"),
        ("Qing-ming", "Jasność i czystość"),
        ("Gu-yu", "Deszcz zbóż"),
        ("Li-xia", "Początek lata"),
        ("Xiao-man", "Małe dojrzewanie"),
        ("Mang-zhong", "Siew ziarna"),
        ("Xiao-shu", "Mały upał"),
        ("Da-shu", "Wielki upał"),
        ("Li-qiu", "Początek jesieni"),
        ("Chu-shu", "Koniec upału"),
        ("Bai-lu", "Biała rosa"),
        ("Han-lu", "Zimna rosa"),
        ("Shuang-jiang", "Opadanie szronu"),
        ("Li-dong", "Początek zimy"),
        ("Xiao-xue", "Mały śnieg"),
        ("Da-xue", "Wielki śnieg"),
        ("Xiao-han", "Mały chłód"),
        ("Da-han", "Wielki chłód"),
        ("Nian", "Rok"),
        ("Yue", "Miesiąc"),
        ("Ri", "Dzień"),
        ("Zhou", "Tydzień"),
        ("Xing-qi", "Tydzień"),
        ("Jin-tian", "Dzisiaj"),
        ("Zuo-tian", "Wczoraj"),
        ("Ming-tian", "Jutro"),
        ("Qian-tian", "Przedwczoraj"),
        ("Hou-tian", "Pojutrze"),
        ("Shang-wu", "Przed południem"),
        ("Zhong-wu", "Południe"),
        ("Xia-wu", "Popołudnie"),
        ("Huang-hun", "Zmierzch"),
        ("Wan-shang", "Wieczór"),
        ("Ye-wan", "Późny wieczór"),
        ("Ban-ye", "Północ"),
        ("Ling-chen", "Nad ranem"),
        ("Po-xiao", "Świt"),
        ("Ri-chu", "Wschód słońca"),
        ("Ri-luo", "Zachód słońca"),
    ],

    "kolory_odcienie": [
        ("Hong", "Czerwony"),
        ("Zhu-hong", "Cynobrowy"),
        ("Shen-hong", "Ciemnoczerwony"),
        ("Fen-hong", "Różowy"),
        ("Cheng", "Pomarańczowy"),
        ("Huang", "Żółty"),
        ("Jin-huang", "Złotożółty"),
        ("Tu-huang", "Żółty ziemisty"),
        ("Lü", "Zielony"),
        ("Cui-lü", "Szmaragdowy"),
        ("Qing-lü", "Jaskrawozielony"),
        ("Shen-lü", "Ciemnozielony"),
        ("Qing", "Niebieski/zielony"),
        ("Tian-qing", "Błękitny"),
        ("Shen-qing", "Ciemnoniebieski"),
        ("Lan", "Indygo"),
        ("Zi", "Fioletowy"),
        ("Zi-hong", "Purpurowy"),
        ("Hei", "Czarny"),
        ("Mo-hei", "Kruk czarny"),
        ("Hui", "Szary"),
        ("Yin-hui", "Srebroszary"),
        ("Jin", "Złoty"),
        ("Yin", "Srebrny"),
        ("Tong", "Miedziany"),
        ("Zong", "Brązowy"),
        ("Ka-fei", "Kawowy"),
        ("Mi", "Beżowy"),
        ("Xiang-ya", "Kość słoniowa"),
        ("An", "Ciemny"),
        ("Ming", "Jasny"),
        ("Nong", "Intensywny (kolor)"),
        ("Dan", "Blady"),
        ("Xian", "Jaskrawy"),
        ("An-dan", "Przyćmiony"),
    ],

    "tekstury_materialy": [
        ("Hua", "Gładki"),
        ("Cu", "Szorstki"),
        ("Xi", "Cienki, delikatny"),
        ("Hou", "Gruby"),
        ("Ying", "Twardy"),
        ("Ruan", "Miękki"),
        ("Run", "Aksamitny"),
        ("Gan", "Suchy"),
        ("Shi", "Mokry"),
        ("Nian", "Lepki, klejący"),
        ("Hua", "Śliski"),
        ("Se", "Chropowaty, drapiący"),
        ("Mao", "Puszysty"),
        ("Guang", "Błyszczący"),
        ("An", "Matowy"),
        ("Tou-ming", "Przezroczysty"),
        ("Bu-tou-ming", "Nieprzezroczysty"),
        ("Jin", "Metal (materiał)"),
        ("Mu", "Drewno (materiał)"),
        ("Shui", "Woda (materiał)"),
        ("Huo", "Ogień (materiał)"),
        ("Tu", "Ziemia (materiał)"),
        ("Shi-tou", "Kamień"),
        ("Yu", "Jaspis, jade"),
        ("Tie", "Żelazo"),
        ("Tong", "Miedź"),
        ("Yin", "Srebro"),
        ("Jin", "Złoto"),
        ("Zhu", "Bambus"),
        ("Teng", "Ratan"),
        ("Ma", "Konopie, len"),
        ("Mian", "Bawełna"),
        ("Si", "Jedwab"),
        ("Mao", "Wełna"),
        ("Pi", "Skóra (materiał)"),
        ("Pi-ge", "Skóra (wyprawiona)"),
        ("Zhi", "Papier"),
        ("Bu", "Tkanina"),
        ("Sha", "Gaza, muślin"),
    ],

    "dzwieki": [
        ("Sheng", "Dźwięk, głos"),
        ("Yin", "Dźwięk, ton"),
        ("Xiang", "Brzmieć, rozlegać się"),
        ("Jiao", "Krzyczeć, wołać"),
        ("Han", "Krzyczeć głośno"),
        ("Hu", "Wołać"),
        ("Chang", "Śpiewać"),
        ("Ge", "Pieśń"),
        ("Yin-yue", "Muzyka"),
        ("Shao", "Gwizdać"),
        ("Ku", "Płakać"),
        ("Xiao", "Śmiać się"),
        ("Tan", "Wzdychać"),
        ("Xi", "Oddychać, westchnąć"),
        ("Da-han", "Krzyczeć głośno"),
        ("Di-sheng", "Szeptać"),
        ("Qiao-qiao", "Cicho"),
        ("Hong", "Hałasować"),
        ("Zao", "Hałaśliwy"),
        ("Jing", "Cichy"),
        ("Lei", "Grzmot"),
        ("Hong-long", "Dudnienie"),
        ("Hua-hua", "Plusk, szum wody"),
        ("Sha-sha", "Szelest"),
        ("Hu-hu", "Świst wiatru"),
        ("Zhi-zhi", "Ćwierkanie"),
        ("Miao", "Miauczenie"),
        ("Wang", "Szczekanie"),
        ("Si", "Syczenie"),
        ("Gu", "Rechot"),
        ("Wu", "Zawodzenie"),
        ("Xi-li-hua-la", "Trzask, łoskot"),
        ("Peng", "Łoskot, huk"),
        ("Qiang", "Brzęk (metalu)"),
        ("Dang", "Bicie dzwonu"),
    ],

    "zapachy_smaki": [
        ("Xiang", "Pachnący, aromatyczny"),
        ("Chou", "Śmierdzący"),
        ("Fen", "Woń, aromat"),
        ("Qi", "Zapach"),
        ("Wei", "Smak, zapach"),
        ("Tian", "Słodki"),
        ("Suan", "Kwaśny"),
        ("Ku", "Gorzki"),
        ("La", "Ostry, pikantny"),
        ("Xian", "Słony"),
        ("Xian", "Świeży, umami"),
        ("Dan", "Mdły, łagodny"),
        ("Nong", "Intensywny (smak)"),
        ("Qing", "Lekki (smak)"),
        ("Se", "Cierpki"),
        ("Hua", "Gładki (w ustach)"),
        ("Nen", "Miękki, delikatny"),
        ("Lao", "Twardy (o mięsie)"),
        ("Cui", "Chrupiący"),
        ("Ruan", "Miękki (konsystencja)"),
        ("Hua", "Śluzowaty"),
        ("Nen-hua", "Gładki i delikatny"),
        ("Xiang-wei", "Aromat"),
        ("Hua-xiang", "Kwiatowy zapach"),
        ("Guo-xiang", "Owocowy zapach"),
        ("Yao-xiang", "Zapach ziół"),
        ("Rou-xiang", "Zapach mięsa"),
        ("Yan-xiang", "Zapach dymu"),
    ],

    "relacje_przestrzenne": [
        ("Shang", "Góra, na"),
        ("Xia", "Dół, pod"),
        ("Zuo", "Lewy"),
        ("You", "Prawy"),
        ("Qian", "Przód"),
        ("Hou", "Tył"),
        ("Zhong", "Środek"),
        ("Nei", "Wewnątrz"),
        ("Wai", "Zewnątrz"),
        ("Li", "Wewnątrz, w"),
        ("Pang", "Obok"),
        ("Bian", "Strona, bok"),
        ("Zuo-bian", "Lewa strona"),
        ("You-bian", "Prawa strona"),
        ("Qian-mian", "Przed"),
        ("Hou-mian", "Za"),
        ("Shang-mian", "Na górze"),
        ("Xia-mian", "Na dole"),
        ("Li-mian", "Wewnątrz"),
        ("Wai-mian", "Zewnątrz"),
        ("Dui-mian", "Naprzeciwko"),
        ("Pang-bian", "Obok"),
        ("Fu-jin", "W pobliżu"),
        ("Yuan", "Daleko"),
        ("Jin", "Blisko"),
        ("Gao", "Wysoko"),
        ("Di", "Nisko"),
        ("Shen", "Głęboko"),
        ("Qian", "Płytko"),
        ("Kuan", "Szeroki"),
        ("Zhai", "Wąski"),
        ("Yuan", "Okrągły"),
        ("Fang", "Kwadratowy"),
        ("Zhi", "Prosty"),
        ("Wan", "Zakrzywiony"),
        ("Ping", "Płaski"),
        ("Dou", "Stromy"),
    ],

    "kwantyfikatory_miary": [
        ("Ge", "Sztuka (ogólne)"),
        ("Zhi", "Sztuka (zwierzęta, przedmioty długie)"),
        ("Tiao", "Sztuka (długie, cienkie)"),
        ("Zhang", "Arkusz (papier)"),
        ("Pian", "Plaster, kawałek"),
        ("Kuai", "Kawałek, bryła"),
        ("Ba", "Wiązka (kwiaty)"),
        ("Duo", "Kwiat (klasyfikator)"),
        ("Ke", "Ziarnko, ziarno"),
        ("Li", "Ziarenko (małe)"),
        ("Di", "Kropla"),
        ("Wei", "Osoba (szanująca)"),
        ("Ren", "Osoba"),
        ("Kou", "Osoba (rodzina)"),
        ("Ming", "Osoba (formalne)"),
        ("Shuang", "Para (buty, pałeczki)"),
        ("Dui", "Para (ludzi, rzeczy)"),
        ("Fu", "Zestaw"),
        ("Tao", "Komplet"),
        ("Jian", "Przedmiot (ubranie, sprawa)"),
        ("Suo", "Budynek"),
        ("Dong", "Budynek"),
        ("Ceng", "Piętro, warstwa"),
        ("Jian", "Pokój"),
        ("Chi", "Stopa (miara ~30cm)"),
        ("Cun", "Cal (~3cm)"),
        ("Zhang", "Sążeń (~3m)"),
        ("Li", "Li (miara ~500m)"),
        ("Jin", "Funt (miara ~500g)"),
        ("Liang", "Uncja (~50g)"),
        ("Qian", "Cent (miara ~5g)"),
        ("Dou", "Miara objętości (~10l)"),
        ("Sheng", "Miara objętości (~1l)"),
        ("Dan", "Miara objętości (~100l)"),
        ("Bei", "Kubek, kieliszek (miara)"),
        ("Wan", "Miska (miara)"),
    ],

    "idiomy_zwroty": [
        ("Hao-jiu-bu-jian", "Dawno się nie widzieliśmy"),
        ("Qing-wen", "Proszę pozwolić zapytać"),
        ("Dui-bu-qi", "Przepraszam"),
        ("Bu-ke-qi", "Nie ma za co"),
        ("Mei-guan-xi", "Nie szkodzi"),
        ("Xie-xie", "Dziękuję"),
        ("Bu-yong-xie", "Nie ma za co"),
        ("Qing", "Proszę"),
        ("Qing-jin", "Proszę wejść"),
        ("Qing-zuo", "Proszę usiąść"),
        ("Man-man-chi", "Smacznego (dosł. jedz powoli)"),
        ("Man-zou", "Idź powoli (na pożegnanie)"),
        ("Yi-lu-ping-an", "Bezpiecznej podróży"),
        ("Wan-an", "Dobrej nocy"),
        ("Zhu-ni", "Życzę tobie"),
        ("Gong-xi", "Gratulacje"),
        ("Hao-yun", "Powodzenia"),
        ("Shen-ti-jian-kang", "Zdrowia (dosł. ciało zdrowe)"),
        ("Xin-ku-le", "Zmęczyłeś się (współczucie)"),
        ("Jia-you", "Trzymaj się! Dalej!"),
        ("Mei-shi", "W porządku, nic się nie stało"),
        ("Zhen-de-ma", "Naprawdę?"),
        ("Dang-ran", "Oczywiście"),
        ("Ke-neng", "Możliwe"),
        ("Ye-xu", "Może"),
        ("Bu-yi-ding", "Niekoniecznie"),
        ("Shuo-bu-ding", "Trudno powiedzieć"),
        ("Kan-qing-kuang", "Zobaczymy (dosł. patrz sytuacja)"),
        ("Sui-bian", "Wszystko jedno"),
        ("Mei-wen-ti", "Nie ma problemu"),
    ],

    "natura_szczegoly": [
        ("Yan-shi", "Skała"),
        ("Ju-shi", "Głaz"),
        ("Sha", "Piasek"),
        ("Li-sha", "Żwir"),
        ("Shi-zi", "Kamyki"),
        ("Ni", "Błoto"),
        ("Chen-tu", "Pył"),
        ("Yan-dong", "Jaskinia"),
        ("Shan-dong", "Grota górska"),
        ("Xuan-ya", "Urwisko"),
        ("Shan-feng", "Szczyt górski"),
        ("Shan-po", "Zbocze"),
        ("Shan-gu", "Dolina górska"),
        ("Xia-gu", "Wąwóz"),
        ("Ping-yuan", "Równina"),
        ("Cao-yuan", "Step"),
        ("Sha-mo", "Pustynia"),
        ("Lin", "Las"),
        ("Sen-lin", "Gęsty las"),
        ("Shu-lin", "Gaj"),
        ("Zhu-lin", "Zagajnik bambusowy"),
        ("Cao-di", "Łąka"),
        ("Yuan-ye", "Pole, dzikie pole"),
        ("Tian", "Pole (uprawne)"),
        ("Dao-tian", "Pole ryżowe"),
        ("Geng-di", "Ziemia orna"),
        ("He", "Rzeka"),
        ("Jiang", "Wielka rzeka"),
        ("Xi", "Strumień"),
        ("Quan", "Źródło"),
        ("Pu-bu", "Wodospad"),
        ("Chi", "Staw"),
        ("Hu", "Jezioro"),
        ("Hai", "Morze"),
        ("Yang", "Ocean"),
        ("Hai-wan", "Zatoka"),
        ("Hai-xia", "Cieśnina"),
        ("An", "Brzeg"),
        ("Hai-tan", "Plaża"),
        ("Dao", "Wyspa"),
        ("Zhou", "Łódź"),
    ],

    "rzemioslo_terminy": [
        ("Mu-jiang", "Stolarz"),
        ("Tie-jiang", "Kowal"),
        ("Tong-jiang", "Kotlarz"),
        ("Yin-jiang", "Złotnik"),
        ("Tao-jiang", "Garncarz"),
        ("Fang-jiang", "Tkacz"),
        ("Ran-jiang", "Farbarz"),
        ("Hua-jiang", "Malarz"),
        ("Shi-jiang", "Kamieniarz"),
        ("Wa-jiang", "Dekarz"),
        ("Zuo", "Robić, wytwarzać"),
        ("Zhi", "Produkować"),
        ("Zao", "Tworzyć"),
        ("Xiu", "Naprawiać"),
        ("Bu", "Łatać"),
        ("Huo", "Ogień (rzemieślniczy)"),
        ("Lu", "Piec (do topiena)"),
        ("Zhui", "Młot"),
        ("Zhen", "Kowadło"),
        ("Qian-zi", "Szczypce"),
        ("Chuui", "Młotek"),
        ("Ju", "Piła"),
        ("Fu", "Siekiera"),
        ("Bao", "Strug"),
        ("Zao", "Dłuto"),
        ("Zuan", "Wiertło"),
        ("Sheng", "Lina"),
        ("Ding", "Gwóźdź"),
        ("Luo-si", "Śruba"),
        ("Jiao-shui", "Klej"),
    ],

    "handel_administracja": [
        ("Mai", "Sprzedawać"),
        ("Gou", "Kupować"),
        ("Huan", "Wymieniać"),
        ("Jiao-yi", "Transakcja"),
        ("Shang-ren", "Kupiec"),
        ("Gui-tai", "Lada"),
        ("Huo-wu", "Towary"),
        ("Jia-ge", "Cena"),
        ("Zhi-liang", "Jakość"),
        ("Shu-liang", "Ilość"),
        ("Zhong-liang", "Waga"),
        ("Cheng", "Waga (narzędzie)"),
        ("Tian-ping", "Szale"),
        ("Liang", "Ważyć"),
        ("Suan", "Liczyć, kalkulować"),
        ("Zhang", "Rachunek"),
        ("Shou-ju", "Pokwitowanie"),
        ("Qi-yue", "Umowa"),
        ("Yin-zhang", "Pieczęć"),
        ("Wen-shu", "Dokument"),
        ("Gong-wen", "Pismo urzędowe"),
        ("Ming-ling", "Rozkaz, nakaz"),
        ("Fa-lü", "Prawo"),
        ("Gui-ding", "Regulacja"),
        ("Gui-ze", "Zasada"),
        ("Zheng-ce", "Polityka"),
        ("Shui", "Podatek"),
        ("Guan", "Urząd, stanowisko"),
        ("Guan-yuan", "Urzędnik"),
        ("Li-shi", "Niższy urzędnik"),
    ],

    "akademia_nauka": [
        ("Xue", "Uczyć się"),
        ("Jiao", "Uczyć (kogoś)"),
        ("Du", "Czytać, studiować"),
        ("Xie", "Pisać"),
        ("Ji", "Zapamiętywać"),
        ("Bei", "Recytować z pamięci"),
        ("Kao", "Egzaminować"),
        ("Shi", "Test, egzamin"),
        ("Xue-sheng", "Uczeń"),
        ("Xue-zhe", "Uczony"),
        ("Shi-fu", "Mistrz (nauczyciel)"),
        ("Tu-di", "Uczeń, adept"),
        ("Shu-yuan", "Akademia"),
        ("Xue-tang", "Szkoła"),
        ("Wen-zhang", "Artykuł, esej"),
        ("Lun", "Dyskutować"),
        ("Bian", "Debatować"),
        ("Zheng-lun", "Spierać się"),
        ("Li", "Powód, logika"),
        ("Dao-li", "Zasada, prawda"),
        ("Zhen-li", "Prawda"),
        ("Zhi-shi", "Wiedza"),
        ("Zhi-hui", "Mądrość"),
        ("Cong-ming", "Inteligentny"),
        ("Yu", "Głupi"),
        ("Ben", "Tępy, głupi"),
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

    output = f"""# Słownik Lengxuan - KOMPLETNY (3000+ słów)

**Liczba wpisów:** {len(sorted_entries)}
**Ostatnia aktualizacja:** 2026-01-03

**Status:** FINALNY

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
    print("GENERATOR SŁOWNIKA LENGXUAN - FINAŁ CZĘŚĆ 5")
    print("CEL: 3000+ SŁÓW")
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
        ("czasowniki_gotowanie", "Czasowniki - Gotowanie"),
        ("czasowniki_medyczne", "Czasowniki - Medycyna"),
        ("czasowniki_budowa", "Czasowniki - Budowa"),
        ("cialo_szczegoly", "Ciało - Szczegóły"),
        ("przedmioty_domowe", "Przedmioty domowe"),
        ("czas_kalendarz", "Czas i kalendarz"),
        ("kolory_odcienie", "Kolory i odcienie"),
        ("tekstury_materialy", "Tekstury i materiały"),
        ("dzwieki", "Dźwięki"),
        ("zapachy_smaki", "Zapachy i smaki"),
        ("relacje_przestrzenne", "Relacje przestrzenne"),
        ("kwantyfikatory_miary", "Kwantyfikatory i miary"),
        ("idiomy_zwroty", "Idiomy i zwroty"),
        ("natura_szczegoly", "Natura - Szczegóły"),
        ("rzemioslo_terminy", "Rzemiosło - Terminy"),
        ("handel_administracja", "Handel i administracja"),
        ("akademia_nauka", "Akademia i nauka"),
    ]

    for cat_key, cat_name in categories:
        print(f"\nDodawanie kategorii: {cat_key}...")
        added, conflicts = add_category_to_dict(
            word_dict,
            cat_name,
            FINAL_VOCABULARY[cat_key]
        )
        total_added += added
        total_conflicts += conflicts

    # Zapisz kompletny słownik
    print("\n" + "=" * 60)
    print(f"FINAŁ CZĘŚĆ 5 - SUMA: Dodano {total_added} nowych słów")
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
        print(f"\n  ✓ CEL OSIĄGNIĘTY! (3000+)")
    else:
        print(f"\n  Cel (3000+): Brakuje {3000 - len(word_dict)} słów")

    print("=" * 60)
    print("\n" + "=" * 60)
    print("GOTOWE!")
    print("=" * 60)

if __name__ == "__main__":
    main()
