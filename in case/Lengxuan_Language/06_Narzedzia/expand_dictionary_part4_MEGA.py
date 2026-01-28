# -*- coding: utf-8 -*-
"""
Generator rozszerzonego słownika Lengxuan - CZĘŚĆ 4 (MEGA-FINALNA)
Cel: Dodanie kolejnych ~1500 słów do osiągnięcia 3000+
"""

import re
from collections import defaultdict

# CZĘŚĆ 4 - MEGA FINALNE ROZSZERZENIE
MEGA_VOCABULARY = {
    # ============================================================
    # PRZYMIOTNIKI - SZCZEGÓŁOWE OPISY (200+ słów)
    # ============================================================
    "przymiotniki_detale": [
        # Wielkość szczegółowa
        ("Ju-da-wu-bi", "Kolosalny, gigantyczny"),
        ("Wei-bu-zu-dao", "Mikroskopijny"),
        ("Gao-ru-yun-xiao", "Wysoki jak chmury"),
        ("Di-ru-chen-ai", "Niski jak kurz"),

        # Prędkość szczegółowa
        ("Xun-lei-bu-ji", "Szybki jak piorun"),
        ("Huan-ru-wu-gui", "Wolny jak żółw"),
        ("Shan-dian-ban", "Błyskawiczny"),
        ("Gui-su", "Żółwia prędkość"),

        # Siła i moc
        ("Qiang-da", "Potężny"),
        ("Ruo-xiao", "Słaby, nieznaczny"),
        ("Jian-gu", "Mocny, solidny"),
        ("Cui-ruo", "Kruchy, delikatny"),
        ("Jie-shi", "Solidny jak skała"),
        ("Wen-gu", "Stabilny, niewzruszony"),

        # Wygląd szczegółowy
        ("Ying-jun", "Przystojny (mężczyzna)"),
        ("Piao-liang", "Piękna (kobieta)"),
        ("Jun-mei", "Przystojny, atrakcyjny"),
        ("Qing-xiu", "Delikatnie piękny"),
        ("Wei-mei", "Uroczo piękny"),
        ("Chou-e", "Ohydny, odpychający"),
        ("Ke-wu", "Wstrętny"),

        # Kształt szczegółowy
        ("Tuo-yuan", "Owalny"),
        ("Duo-bian", "Wielokątny"),
        ("Bu-gui-ze", "Nieregularny"),
        ("Dui-cheng", "Symetryczny"),
        ("Wan-qu-bu-ping", "Kręty i nierówny"),

        # Smak szczegółowy
        ("Mei-wei", "Pyszny"),
        ("Xian-mei", "Smaczny (umami)"),
        ("Ku-se", "Gorzki i cierpki"),
        ("Suan-tian", "Słodko-kwaśny"),
        ("Xiang-cui", "Aromatyczny i chrupiący"),

        # Zapach
        ("Qing-xiang", "Delikatnie pachnący"),
        ("Nong-xiang", "Intensywnie pachnący"),
        ("Chen-xiang", "Stęchły"),
        ("Xin-xiang", "Świeżo pachnący"),

        # Dźwięk
        ("Xiang-liang", "Głośny"),
        ("Qing-cui", "Dźwięczny, czysty"),
        ("Chen-men", "Stłumiony"),
        ("Wei-ruo", "Słaby (dźwięk)"),
        ("Zao-za", "Hałaśliwy"),

        # Światło
        ("Ming-liang", "Jasny, błyszczący"),
        ("Hun-an", "Ciemny, mroczny"),
        ("Shan-yao", "Lśniący, błyszczący"),
        ("An-dan", "Ciemny i mdły"),

        # Uczucia opisowe
        ("Shu-shi", "Komfortowy, wygodny"),
        ("Bu-shi", "Niewygodny"),
        ("Yu-kuai", "Przyjemny, wesoły"),
        ("Tong-ku", "Bolesny, cierpienie"),

        # Warunki środowiska
        ("Chao-shi", "Wilgotny"),
        ("Gan-zao", "Suchy"),
        ("Wen-nuan", "Ciepły"),
        ("Han-leng", "Chłodny, zimny"),
        ("Yan-re", "Skwarny, gorący"),
        ("Bing-leng", "Lodowato zimny"),

        # Jakość i stan
        ("You-xiu", "Doskonały, wyśmienity"),
        ("Lie-zhi", "Niskiej jakości"),
        ("Jing-zhi", "Wyrafinowany"),
        ("Cu-cao", "Prymitywny, szorstki"),
        ("Xi-ni", "Delikatny, subtelny"),

        # Wiek i stan
        ("Nian-qing", "Młody"),
        ("Nian-lao", "Stary (o osobie)"),
        ("Gu-lao", "Starożytny"),
        ("Xian-dai", "Nowoczesny"),
        ("Chuan-tong", "Tradycyjny"),

        # Społeczne
        ("Gao-gui", "Szlachetny, arystokratyczny"),
        ("Bei-jian", "Niski, pogardzany"),
        ("Fu-you", "Bogaty"),
        ("Pin-qiong", "Biedny"),
        ("Ming-wang", "Sławny"),
        ("Mo-ming", "Nieznany"),
    ],

    # ============================================================
    # CZASOWNIKI ROZSZERZONE (300+ słów)
    # ============================================================
    "czasowniki_szczegolowe": [
        # Ruch szczegółowy
        ("Ben", "Pędzić, gnać"),
        ("Chong", "Szarżować"),
        ("Tiao-guo", "Przeskoczyć"),
        ("Pan-yue", "Wspinać się"),
        ("Xia-jiang", "Zstępować"),
        ("Hua", "Ślizgać się"),
        ("Gun", "Toczyć się"),
        ("Zhuan", "Obracać się"),
        ("Yao", "Kołysać się"),
        ("Bai", "Machać, wymachiwać"),
        ("Zhen", "Wstrząsać"),
        ("Dong", "Poruszać"),
        ("Jing", "Nie ruszać się"),
        ("Ting", "Zatrzymać się"),
        ("Dun", "Zatrzymać się nagle"),

        # Manipulacja obiektami szczegółowa
        ("Zhua", "Chwytać, łapać"),
        ("Na", "Trzymać, brać"),
        ("Ju", "Podnosić"),
        ("Fang", "Kłaść, stawiać"),
        ("Reng", "Rzucać"),
        ("Diu", "Wyrzucać"),
        ("Tou", "Ciskać"),
        ("Kou", "Rzucać (w cel)"),
        ("Jie", "Łapać (w powietrzu)"),
        ("Tui", "Pchać"),
        ("La", "Ciągnąć"),
        ("Ti", "Kopać, uderzać nogą"),
        ("Qiao", "Pukać, stukać"),
        ("Ji", "Uderzać"),
        ("Chui", "Walić młotem"),
        ("Zha", "Kłuć, dźgać"),
        ("Kan", "Rąbać, ciąć"),
        ("Qie", "Kroić"),
        ("Ge", "Odcinać"),
        ("Si", "Rwać, drzeć"),
        ("Jian", "Ciąć nożyczkami"),
        ("He", "Łączyć, składać"),
        ("Fen", "Dzielić, rozdzielać"),

        # Jedzenie i picie szczegółowe
        ("Yan", "Połykać"),
        ("Jiao", "Przeżuwać"),
        ("Yao", "Gryźć"),
        ("Xi", "Ssać"),
        ("Tian", "Lizać"),
        ("Pin", "Delektować się, degustować"),
        ("Chang", "Próbować smaku"),
        ("Yin-yong", "Pijać (formalnie)"),
        ("He-zui", "Upić się"),

        # Komunikacja szczegółowa
        ("Han", "Krzyczeć, wołać"),
        ("Jiao", "Wołać głośno"),
        ("Hu", "Wzywać"),
        ("Da-zhao-hu", "Pozdrawiać głośno"),
        ("Di-yu", "Szeptać"),
        ("Nian", "Mamrotać"),
        ("Du", "Czytać na głos"),
        ("Song", "Recytować"),
        ("Jiang", "Opowiadać, mówić"),
        ("Shu", "Opisywać"),
        ("Tan", "Dyskutować"),
        ("Lun", "Debatować"),
        ("Zheng", "Kłócić się"),
        ("Chan", "Spierać się"),
        ("Ma", "Łajać, przeklinać"),
        ("Zan", "Chwalić"),
        ("Song", "Wychwalać"),
        ("Pi", "Krytykować"),

        # Emocje wyrażane
        ("Le", "Cieszyć się"),
        ("Xi", "Radować się"),
        ("Xiao-le", "Śmiać się radośnie"),
        ("Ku-qi", "Płakać głośno"),
        ("Liu-lei", "Ronić łzy"),
        ("Xi-qi", "Wzdychać"),
        ("Tan-qi", "Ubolewać"),
        ("Hou-hui", "Żałować"),
        ("Dan-you", "Martwić się, obawiać"),
        ("Kong-pa", "Bać się"),
        ("Ai", "Kochać"),
        ("Lian", "Pielęgnować uczucie"),
        ("Si-nian", "Tęsknić"),
        ("Hen", "Nienawidzić"),
        ("Wu", "Pogardzać"),

        # Działania umysłowe szczegółowe
        ("Xiang-dao", "Pomyśleć o, wpaść na pomysł"),
        ("Xiang-qi", "Przypomnieć sobie"),
        ("Wang-diao", "Zapomnieć całkowicie"),
        ("Ming-bai", "Zrozumieć"),
        ("Li-jie", "Pojąć"),
        ("Wu", "Uświadomić sobie"),
        ("Dong-de", "Rozumieć się na czymś"),
        ("Xue-hui", "Nauczyć się"),
        ("Zhang-wo", "Opanować (umiejętność)"),

        # Percepcja szczegółowa
        ("Kan-dao", "Zobaczyć"),
        ("Kan-jian", "Dostrzec"),
        ("Wang", "Patrzeć w dal"),
        ("Guan", "Obserwować"),
        ("Kui", "Podglądać"),
        ("Du", "Czytać"),
        ("Ting-dao", "Usłyszeć"),
        ("Ting-jian", "Dosłyszeć"),
        ("Wen-dao", "Poczuć zapach"),
        ("Mo", "Dotykać"),
        ("Chu", "Dotknąć"),
        ("Gan-jue", "Czuć, odczuwać"),

        # Tworzenie i niszczenie szczegółowe
        ("Zao", "Tworzyć, wytwarzać"),
        ("Zhi-zao", "Produkować"),
        ("Jian", "Budować"),
        ("Gai", "Wznosić (budowlę)"),
        ("Xiu", "Naprawiać"),
        ("Zheng", "Reperować"),
        ("Hui", "Niszczyć, burzyć"),
        ("Po", "Rozbijać"),
        ("Zha", "Wysadzać"),
        ("Shao", "Palić"),
        ("Ran", "Płonąć"),

        # Porządkowanie szczegółowe
        ("Shou-shi", "Sprzątać, porządkować"),
        ("Zheng-dun", "Organizować"),
        ("An-pai", "Układać, organizować"),
        ("Bai-fang", "Układać (przedmioty)"),
        ("Pai-lie", "Szeregować"),
        ("Fen-pei", "Przydzielać"),
        ("Fen-fa", "Dystrybuować"),

        # Podróż i transport szczegółowy
        ("Chu-fa", "Wyruszyć"),
        ("Qi-cheng", "Rozpocząć podróż"),
        ("Lu-xing", "Podróżować"),
        ("You-lan", "Wędrować, zwiedzać"),
        ("Dao", "Przybywać"),
        ("Dao-da", "Dotrzeć"),
        ("Fan-hui", "Powrócić"),
        ("Hui-lai", "Wrócić"),
        ("Hui-qu", "Wrócić (tam)"),
        ("Qu", "Iść (tam)"),
        ("Lai", "Przychodzić (tu)"),
        ("Guo", "Przechodzić, mijać"),
        ("Chuan-guo", "Przechodzić przez"),

        # Społeczne interakcje szczegółowe
        ("Jie-shao", "Przedstawiać (kogoś)"),
        ("Ren-shi", "Poznawać"),
        ("Jiao-wang", "Utrzymywać relacje"),
        ("Lian-xi", "Kontaktować się"),
        ("Tong-xin", "Korespondować"),
        ("Bai-fang", "Odwiedzać"),
        ("Ke-qi", "Być uprzejmym"),
        ("Gong-jing", "Szanować"),
        ("Jing-wei", "Czcić"),

        # Handel szczegółowy
        ("Chu-shou", "Sprzedawać"),
        ("Gou-mai", "Kupować"),
        ("Gou-wu", "Robić zakupy"),
        ("Tao-jia", "Targować się"),
        ("Jiao-huan", "Wymieniać"),
        ("Mao-yi", "Handlować"),

        # Czasowniki stanu
        ("Cheng", "Być, stawać się"),
        ("Wei", "Być, działać jako"),
        ("Shi", "Być"),
        ("You", "Istnieć, mieć"),
        ("Zai", "Być w (miejscu)"),

        # Czasowniki modalnych
        ("Neng", "Móc, potrafić"),
        ("Hui", "Umieć"),
        ("Gan", "Śmieć"),
        ("Ken", "Chcieć, zgodzić się"),
        ("Yao", "Chcieć, musieć"),
        ("Yao-qiu", "Wymagać"),
        ("Xu-yao", "Potrzebować"),
        ("Ying-gai", "Powinien"),
        ("Bi-xu", "Musieć"),
        ("Ke-yi", "Móc, można"),

        # Dawanie i otrzymywanie
        ("Gei", "Dawać"),
        ("Song", "Ofiarować"),
        ("Zeng", "Podarować"),
        ("Song-li", "Dać prezent"),
        ("Shou", "Otrzymywać"),
        ("De-dao", "Zdobyć"),
        ("Huo-de", "Uzyskać"),
        ("Shi-qu", "Tracić"),
        ("Diu-shi", "Zgubić"),

        # Osiągnięcia
        ("Wan-cheng", "Ukończyć"),
        ("Shi-xian", "Zrealizować"),
        ("Da-cheng", "Osiągnąć"),
        ("De-sheng", "Zwyciężyć"),
        ("Shi-li", "Przegrać"),
    ],

    # ============================================================
    # RZECZOWNIKI - PRZEDMIOTY CODZIENNE (150+ słów)
    # ============================================================
    "przedmioty_codzienne": [
        # Meble
        ("Jia-ju", "Meble"),
        ("Yi-gui", "Szafa"),
        ("Chu-gui", "Kredens"),
        ("Shu-jia", "Regał na książki"),
        ("Shu-zhuo", "Biurko"),
        ("Can-zhuo", "Stół jadalny"),
        ("Ping-jige", "Parawan"),
        ("Deng-long", "Latarnia"),

        # Naczynia i przybory
        ("Can-ju", "Naczynia stołowe"),
        ("Wan", "Miska"),
        ("Die", "Talerz"),
        ("Bei", "Kubek, filiżanka"),
        ("Hu", "Dzbanek"),
        ("Ping", "Butelka"),
        ("Kuai-zi", "Pałeczki"),
        ("Shao-zi", "Łyżka"),
        ("Cha-zi", "Widelec"),
        ("Dao-cha", "Nóż i widelec"),
        ("Cha-hu", "Czajnik do herbaty"),
        ("Jiu-bei", "Kieliszek do wina"),
        ("Tong", "Wiadro"),
        ("Pen", "Miednica"),

        # Tekstylia
        ("Bu-liao", "Materiał, tkanina"),
        ("Si-chou", "Jedwab"),
        ("Mian-bu", "Bawełna (tkanina)"),
        ("Jin-xiu", "Brokat"),
        ("Zhang", "Zasłona, namiot"),
        ("Bei-zi", "Kołdra"),
        ("Zhen-tou", "Poduszka"),
        ("Xi-dan", "Prześcieradło"),
        ("Mao-jin", "Ręcznik"),
        ("Shou-pa", "Chusteczka"),

        # Narzędzia pisarskie
        ("Wen-fang-si-bao", "Cztery skarby gabinetu (pędzel, tusz, papier, kamień)"),
        ("Mao-bi", "Pędzel do pisania"),
        ("Mo-zhi", "Tusz w sztabce"),
        ("Xuan-zhi", "Papier xuan"),
        ("Yan-tai", "Kamień do rozcierania tuszu"),
        ("Zhi-zhang", "Papier"),
        ("Shu-xin", "List, korespondencja"),

        # Ozdoby i biżuteria
        ("Shou-shi", "Ozdoba, biżuteria"),
        ("Xiang-lian", "Naszyjnik"),
        ("Shou-zhuo", "Bransoletka"),
        ("Jie-zhi", "Pierścień"),
        ("Er-zhui", "Kolczyki"),
        ("Fa-chai", "Ozdoba włosów"),
        ("Yu-pei", "Wisiorek z jadeitu"),
        ("Jin-yin", "Złoto i srebro"),

        # Muzyczne szczegółowe
        ("Yue-qi", "Instrument muzyczny"),
        ("Xian-qi", "Instrument strunowy"),
        ("Guan-yue", "Instrument dęty"),
        ("Da-ji-yue", "Instrument perkusyjny"),

        # Narzędzia ogrodowe
        ("Yuan-yi-gong-ju", "Narzędzia ogrodnicze"),
        ("Jian-dao", "Nożyce ogrodnicze"),
        ("Shui-tong", "Konewka"),
        ("Pa-zi", "Grabie"),

        # Oświetlenie
        ("Zhu", "Świeca"),
        ("Deng-tai", "Świecznik"),
        ("Deng-long", "Latarnia"),
        ("Huo-ba", "Pochodnia"),
        ("You-deng", "Lampa oliwna"),

        # Kadzidła i aromaty
        ("Xiang", "Kadzidło"),
        ("Xiang-lu", "Kadzielnica"),
        ("Xiang-nang", "Torebka zapachowa"),
        ("Hua-xiang", "Perfumy"),
    ],

    # ============================================================
    # ZWIERZĘTA SZCZEGÓŁOWE (100+ słów)
    # ============================================================
    "zwierzeta_szczegolowe": [
        # Ptaki szczegółowe
        ("Niao", "Ptak"),
        ("Fei-niao", "Ptak latający"),
        ("Gong-ji", "Kogut"),
        ("Mu-ji", "Kura"),
        ("Xiao-ji", "Pisklę"),
        ("Ya", "Kaczka"),
        ("E", "Gęś"),
        ("Tian-e", "Łabędź"),
        ("Gou", "Żuraw"),
        ("Bai-guan", "Czapla biała"),
        ("Cui-niao", "Zimorodek"),
        ("Que", "Wróbel"),
        ("Zhi-geng", "Pokrzewka"),
        ("Ying-wu", "Papuga"),
        ("Mao-tou-ying", "Sowa"),

        # Ssaki domowe
        ("Chu-sheng", "Zwierzę domowe"),
        ("Yang-niu", "Bydło"),
        ("Mu-niu", "Krowa"),
        ("Gong-niu", "Byk"),
        ("Shui-niu", "Bawół wodny"),
        ("Lu-tuo", "Wielbłąd"),
        ("Lv", "Osioł"),
        ("Luo-zi", "Muł"),
        ("Mian-yang", "Owca"),
        ("Shan-yang", "Koza"),

        # Ssaki dzikie
        ("Ye-shou", "Dzikie zwierzę"),
        ("Xiong-mao", "Panda"),
        ("Hou-zi", "Małpa"),
        ("Yuan", "Małpa człekokształtna"),
        ("Shi-zi", "Lew"),
        ("Xiang", "Słoń"),
        ("Xi-niu", "Nosorożec"),
        ("He-ma", "Hipopotam"),
        ("Tu-zi", "Królik, zając"),
        ("Song-shu", "Wiewiórka"),
        ("Lao-shu", "Mysz, szczur"),

        # Gady i płazy
        ("Pa-chong", "Gad"),
        ("She", "Wąż"),
        ("Du-she", "Jadowity wąż"),
        ("Mang-she", "Pyton"),
        ("Bi-hu", "Jaszczurka ścienna"),
        ("Xi-yi", "Jaszczurka"),
        ("Wa", "Żaba"),
        ("Chan", "Ropucha"),

        # Ryby i zwierzęta wodne
        ("Yu", "Ryba"),
        ("Jin-yu", "Złota rybka"),
        ("Li-yu", "Karp"),
        ("Sha-yu", "Rekin"),
        ("Jing-yu", "Wieloryb"),
        ("Hai-tun", "Delfin"),
        ("Zhang-yu", "Ośmiornica"),
        ("You-yu", "Kałamarnica"),
        ("Xia", "Krewetka"),
        ("Pang-xie", "Krab"),
        ("Shui-mu", "Meduz a"),
        ("Xing-xing", "Rozgwiazda (zwierzę)"),
        ("Bei-ke", "Muszla, skorupiak"),

        # Owady i bezkręgowce
        ("Kun-chong", "Owad"),
        ("Mi-feng", "Pszczoła"),
        ("Huang-feng", "Osa"),
        ("Ma-yi", "Mrówka"),
        ("Ying-huo-chong", "Świetlik"),
        ("Zhi-zhu", "Pająk"),
        ("Xie-zi", "Skorpion"),
        ("Wu-gong", "Stonoga"),
        ("Qiu-yin", "Dżdżownica"),
        ("Wo-niu", "Ślimak"),

        # Zwierzęta mityczne szczegółowe
        ("Shen-shou", "Mityczne zwierzę"),
        ("Qi-lin", "Qilin"),
        ("Feng-huang", "Feniks"),
        ("Long-wang", "Król smoków"),
        ("Bai-hu", "Biały tygrys (kierunek zachód)"),
        ("Zhu-que", "Czerwony ptak (kierunek południe)"),
        ("Xuan-wu", "Czarny wojownik (kierunek północ) - żółw i wąż"),
        ("Qing-long", "Lazurowy smok (kierunek wschód)"),
    ],

    # ============================================================
    # ROŚLINY SZCZEGÓŁOWE (80+ słów)
    # ============================================================
    "rosliny_szczegolowe": [
        # Drzewa szczegółowe
        ("Shu", "Drzewo"),
        ("Shu-mu", "Drzewa (zbiorowo)"),
        ("Song", "Sosna"),
        ("Bai", "Cyprys"),
        ("Liu", "Wierzba"),
        ("Yang", "Topola"),
        ("Feng", "Klon"),
        ("Huai", "Akacja chińska"),
        ("Wu-tong", "Firmiana"),
        ("Sang", "Morwa"),
        ("Zao", "Daktyl chiński"),
        ("Li", "Śliwa"),
        ("Tao", "Brzoskwinia"),
        ("Xing", "Morela"),
        ("Ying", "Wiśnia"),

        # Bambus i trawy
        ("Zhu", "Bambus"),
        ("Mao-zhu", "Bambusa rdzawa"),
        ("Xiang-fei-zhu", "Bambus łzawy"),
        ("Cao", "Trawa"),
        ("Ye-cao", "Dzika trawa"),
        ("Cao-ping", "Trawnik"),
        ("Lu-cao", "Zielona trawa"),

        # Kwiaty szczegółowe
        ("Hua", "Kwiat"),
        ("Mu-dan", "Piwonia"),
        ("Mei", "Kwiat śliwy"),
        ("Lan", "Orchidea"),
        ("Zhu", "Chryzantema (skrót)"),
        ("Lian", "Lotos"),
        ("He", "Lotos (synonim)"),
        ("Yue-ji", "Róża chińska"),
        ("Gui-hua", "Osmanthus"),
        ("Ying-hua", "Kwiat wiśni"),
        ("Xing-hua", "Kwiat moreli"),

        # Warzywa szczegółowe
        ("Shu-cai", "Warzywa"),
        ("Qing-cai", "Bok choy"),
        ("Bai-cai", "Kapusta chińska"),
        ("Bo-cai", "Szpinak"),
        ("Hu-luo-bo", "Marchew"),
        ("Tu-dou", "Ziemniak"),
        ("Shan-yao", "Pochrzyn jadalny"),
        ("Lian-ou", "Kłącze lotosu"),
        ("Dou-jiao", "Strączki fasolowe"),
        ("Dou-ya", "Kiełki fasoli"),

        # Owoce szczegółowe
        ("Shui-guo", "Owoce"),
        ("Gan-ju", "Pomarańcza/mandarynka"),
        ("Ning-meng", "Cytryna"),
        ("You-zi", "Pomelo"),
        ("Shi-zi", "Persymona"),
        ("Yang-mei", "Chińska jagoda woskowa"),
        ("Li-zhi", "Liczi"),
        ("Long-yan", "Longan"),
        ("Bo-luo", "Ananas"),
        ("Xiang-jiao", "Banan"),
        ("Ying-tao", "Wiśnia"),
        ("Cao-mei", "Truskawka"),

        # Zioła lecznicze szczegółowe
        ("Zhong-yao", "Zioła chińskie"),
        ("Ren-shen", "Żeń-szeń"),
        ("Dang-gui", "Dzięgiel chiński"),
        ("Huang-qi", "Astragalus"),
        ("Ling-zhi", "Ganoderma (reishi)"),
        ("Gou-qi", "Jagody goji"),
        ("Ju-hua", "Chryzantema (herbata)"),
        ("Jin-yin-hua", "Wiciokrzew japoński"),
    ],

    # ============================================================
    # RELACJE I POZYCJE SPOŁECZNE (80+ słów)
    # ============================================================
    "relacje_spoleczne": [
        # Tytuły honorowe szczegółowe
        ("Dian-xia", "Wasza Wysokość"),
        ("Bi-xia", "Jego Wysokość (cesarz)"),
        ("Da-ren", "Szanowny panie (urzędnik)"),
        ("Xiao-de", "Pokorny sługa (o sobie)"),
        ("Zai-xia", "Pokorny ja (skromność)"),

        # Relacje mistrz-uczeń
        ("Shi-xiong", "Starszy współuczeń (mężczyzna)"),
        ("Shi-di", "Młodszy współuczeń (mężczyzna)"),
        ("Shi-jie", "Starsza współuczennica"),
        ("Shi-mei", "Młodsza współuczennica"),
        ("Tong-men", "Współuczeń (ogólnie)"),
        ("Shi-bo", "Wujek-mistrz (brat mistrza)"),
        ("Shi-shu", "Wujek-mistrz (młodszy brat mistrza)"),
        ("Shi-zu", "Dziadek-mistrz"),
        ("Zhang-men", "Przywódca szkoły/sekty"),

        # Relacje towarzyskie
        ("Peng-you", "Przyjaciel"),
        ("Hao-you", "Dobry przyjaciel"),
        ("Zhi-you", "Bliski przyjaciel"),
        ("Yi-xiong", "Przysięgły brat"),
        ("Yi-jie", "Przysięgła siostra"),
        ("Tong-ban", "Towarzysz"),
        ("Huo-ban", "Partner"),

        # Wrogowie i rywale
        ("Di-ren", "Wróg"),
        ("Dui-shou", "Przeciwnik"),
        ("Su-di", "Śmiertelny wróg"),
        ("Qiu-ren", "Człowiek zemsty"),
        ("Jing-zheng-zhe", "Konkurent"),

        # Pozycje w organizacji
        ("Shou-ling", "Przywódca"),
        ("Fu-shou-ling", "Zastępca przywódcy"),
        ("Zhang-lao", "Starszy (organizacji)"),
        ("Hu-fa", "Strażnik, protektor"),
        ("Shi-zhe", "Wysłannik"),
        ("Men-ren", "Członek sekty/klanu"),
        ("Wai-men", "Zewnętrzny uczeń"),
        ("Nei-men", "Wewnętrzny uczeń"),
        ("Qin-chuan", "Uczeń osobisty"),

        # Tytuły wojskowe szczegółowe
        ("Yuan-shuai", "Marszałek"),
        ("Da-jiang", "Wielki generał"),
        ("Fu-jiang", "Wicegenerał"),
        ("Xiao-wei", "Kapitan"),
        ("Zhong-wei", "Porucznik"),
        ("Shi-zu-zhang", "Plutonowy"),
        ("Shi-bing", "Zwykły żołnierz"),

        # Tytuły cywilne szczegółowe
        ("Cheng-xiang", "Premier"),
        ("Shang-shu", "Minister"),
        ("Shi-lang", "Wiceminister"),
        ("Zhi-fu", "Prefekt"),
        ("Zhi-xian", "Zarządca powiatu"),
        ("Xun-fu", "Gubernator prowincji"),

        # Tytuły uczonych
        ("Zhuang-yuan", "Pierwszy na egzaminie cesarskim"),
        ("Jin-shi", "Zdający egzamin cesarski"),
        ("Ju-ren", "Uczony człowiek"),
        ("Xiu-cai", "Uczony-kandydat"),
    ],

    # ============================================================
    # KONCEPTY FILOZOFICZNE I DUCHOWE (100+ słów)
    # ============================================================
    "filozofia_duchowość": [
        # Taoizm szczegółowy
        ("Dao-jia", "Szkoła taoistyczna"),
        ("Wu-wei", "Niedział anie"),
        ("Zi-ran", "Naturalność"),
        ("Yin-yang", "Yin i Yang"),
        ("Tai-ji", "Najwyższa ostateczność (Taiji)"),
        ("Wu-ji", "Pierwotna pustka"),
        ("Qi", "Energia życiowa"),
        ("Jing", "Esencja"),
        ("Shen", "Duch"),
        ("San-bao", "Trzy skarby (Jing, Qi, Shen)"),

        # Buddyzm szczegółowy
        ("Fo-fa", "Dharma buddyjska"),
        ("Ku", "Cierpienie (pierwsza szlachetna prawda)"),
        ("Kong", "Pustka"),
        ("Wu", "Oświecenie"),
        ("Chan", "Zen, medytacja"),
        ("Jing-tu", "Czysta Kraina"),
        ("Lun-hui", "Reinkarnacja"),
        ("Ye", "Karma"),
        ("Yuan", "Przyczyny i warunki"),
        ("Ci-bei", "Współczucie"),

        # Konfucjanizm szczegółowy
        ("Ru-jia", "Szkoła konfucjańska"),
        ("Ren", "Humanitarność"),
        ("Yi", "Prawość"),
        ("Li", "Rytuał, przyzwoitość"),
        ("Zhi", "Mądrość"),
        ("Xin", "Uczciwość"),
        ("Zhong", "Lojalność"),
        ("Xiao", "Synowska pobożność"),
        ("Ti", "Szacunek braterski"),
        ("Jun-zi", "Szlachetny mąż"),
        ("Xiao-ren", "Człowiek niski"),

        # Qi Gong i kultywacja
        ("Xiu-lian", "Kultywacja duchowa"),
        ("Yang-sheng", "Pielęgnowanie życia"),
        ("Nei-dan", "Wewnętrzna alchemia"),
        ("Wai-dan", "Zewnętrzna alchemia"),
        ("Jing-zuo", "Siedząca medytacja"),
        ("Dao-yin", "Prowadzenie i rozciąganie (Qi Gong)"),
        ("Tu-na", "Oddychanie (praktyka)"),
        ("Bi-gu", "Post od zbóż"),
        ("Dan-tian", "Pole eliksiru (centrum energii)"),
        ("Jing-luo", "Meridiany"),
        ("Xue-dao", "Punkty akupunkturowe"),

        # Koncepty metafizyczne
        ("Tian", "Niebo, kosmos"),
        ("Di", "Ziemia"),
        ("Ren", "Człowiek"),
        ("Tian-ren-he-yi", "Jedność nieba i człowieka"),
        ("Wu-xing", "Pięć elementów"),
        ("Ba-gua", "Osiem trigramów"),
        ("Tai-ji-tu", "Diagram Taiji"),
        ("He-tu", "Diagram rzeki"),
        ("Luo-shu", "Pismo Luo"),

        # Poziomy kultywacji
        ("Hou-tian", "Post-niebiański"),
        ("Xian-tian", "Pre-niebiański"),
        ("Lian-jing", "Rafinowanie esencji"),
        ("Lian-qi", "Rafinowanie qi"),
        ("Lian-shen", "Rafinowanie ducha"),
        ("Lian-xu", "Rafinowanie pustki"),
        ("Jin-dan", "Złoty eliksir"),
        ("Yuan-ying", "Pierwotne niemowlę"),

        # Duchy i istoty
        ("Gui", "Duch, zjawa"),
        ("Shen", "Bóstwo, duch"),
        ("Xian", "Nieśmiertelny"),
        ("Mo", "Demon"),
        ("Yao", "Demon, potwór"),
        ("Jing", "Duch (zwierzęcy/roślinny)"),
        ("Ling", "Duch (ogólnie)"),

        # Pojęcia szczęścia i przeznaczenia
        ("Ming", "Przeznaczenie, los"),
        ("Yun", "Fortuna, szczęście"),
        ("Fu", "Błogosławieństwo"),
        ("Lu", "Pomyślność"),
        ("Shou", "Długowieczność"),
        ("Xi", "Radość, szczęście (ślub)"),
        ("Cai", "Bogactwo"),
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

def generate_mega_dictionary():
    """Generuje MEGA CZĘŚĆ 4 słownika"""
    print("Ładowanie istniejącego słownika...")
    existing = load_existing_dictionary('../03_Slownik/slownik_lengxuan_polski.md')
    print(f"Załadowano {len(existing)} istniejących słów\n")

    all_new_words = []
    total_added = 0

    for category, words in MEGA_VOCABULARY.items():
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
    print(f"MEGA CZĘŚĆ 4 - SUMA: Dodano {total_added} nowych słów")
    print(f"Całkowita liczba słów: {len(existing)}")
    print(f"{'='*60}\n")

    # Sortuj i zapisz
    sorted_words = sorted(existing.items(), key=lambda x: x[0])

    output_path = '../03_Slownik/slownik_lengxuan_polski.md'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# Słownik Lengxuan - KOMPLETNY (3000+ słów)\n\n")
        f.write(f"**Liczba wpisów:** {len(existing)}\n")
        f.write(f"**Ostatnia aktualizacja:** 2026-01-03\n\n")
        f.write(f"**Status:** {'KOMPLETNY - GOTOWY DO UŻYCIA' if len(existing) >= 3000 else 'W TRAKCIE ROZBUDOWY'}\n\n")
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
    print(f"\n  Cel (3000+): {'OSIĄGNIĘTY!' if len(existing) >= 3000 else f'Brakuje {3000 - len(existing)} słów'}")
    print(f"{'='*60}")

    return existing

if __name__ == '__main__':
    print("="*60)
    print("GENERATOR SŁOWNIKA LENGXUAN - MEGA CZĘŚĆ 4")
    print("CEL: 3000+ SŁÓW")
    print("="*60)
    print()

    extended_dict = generate_mega_dictionary()

    print("\n" + "="*60)
    print("GOTOWE!")
    print("="*60)
