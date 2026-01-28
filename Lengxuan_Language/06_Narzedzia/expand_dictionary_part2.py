# -*- coding: utf-8 -*-
"""
Generator rozszerzonego słownika Lengxuan - CZĘŚĆ 2
Cel: Dodanie kolejnych ~2000 słów
"""

import re
from collections import defaultdict

# CZĘŚĆ 2 - ROZSZERZONE KATEGORIE
ADDITIONAL_VOCABULARY = {
    # ============================================================
    # CZASOWNIKI DZIAŁANIA (bardzo szczegółowe)
    # ============================================================
    "czasowniki_dzialania": [
        # Ruch podstawowy
        ("Zou-lu", "Chodzić, iść pieszo"),
        ("Pao-bu", "Biegać, jogging"),
        ("Ben-pao", "Pędzić, gnać"),
        ("Man-zou", "Iść wolno"),
        ("Kuai-zou", "Iść szybko"),
        ("Tiao-yue", "Skakać"),
        ("Pan-deng", "Wspinać się"),
        ("Xia-jiang", "Schodzić w dół"),
        ("Die-dao", "Upaść"),
        ("Zhan-qi", "Wstać (na nogi)"),

        # Pozycje i postawa
        ("Pan-tui", "Siedzieć ze skrzyżowanymi nogami"),
        ("Gui-xia", "Klęczeć"),
        ("Tang-xia", "Leżeć"),
        ("Fu-xia", "Leżeć na brzuchu"),
        ("Yang-xia", "Leżeć na plecach"),
        ("Dun-xia", "Przykucnąć"),

        # Manipulacja obiektami
        ("Na-qi", "Podnieść, wziąć"),
        ("Fang-xia", "Położyć, postawić"),
        ("Ju-qi", "Podnieść (w górę)"),
        ("Reng-diao", "Wyrzucić"),
        ("Diu-qi", "Porzucić"),
        ("Jie-shou", "Otrzymać, przyjąć"),
        ("Di-gei", "Przekazać, podać"),

        ("Tui-kai", "Odepchnąć"),
        ("La-jin", "Przyciągnąć"),
        ("Yao-dong", "Potrząsać, kiwać"),
        ("Zhuan-dong", "Obracać"),
        ("Fan-zhuan", "Przewrócić"),

        ("Da-kai", "Otworzyć"),
        ("Guan-shang", "Zamknąć"),
        ("Suo-shang", "Zamknąć na klucz"),
        ("Jie-kai", "Rozwiązać, otworzyć"),

        ("Xi", "Myć, prać"),
        ("Shua", "Szorować"),
        ("Ca-shi", "Wycierać"),
        ("Ca-gan", "Wytrzeć do sucha"),

        # Tworzenie i niszczenie
        ("Zao-jian", "Budować, konstruować"),
        ("Jian-zao", "Wznosić (budynki)"),
        ("Po-huai", "Niszczyć"),
        ("Chai-hui", "Burzyć, rozbierać"),
        ("Xiu-li", "Naprawiać"),
        ("Xiu-fu", "Restaurować"),

        # Łączenie i rozdzielanie
        ("Jie-he", "Łączyć, jednoczyć"),
        ("Fen-kai", "Oddzielać"),
        ("Fen-lie", "Dzielić, rozłupywać"),
        ("He-bing", "Scalać, łączyć"),
        ("Hun-he", "Mieszać"),

        # Zmiana stanu
        ("Bian-hua", "Zmieniać się"),
        ("Gai-bian", "Zmieniać (coś)"),
        ("Cheng-wei", "Stawać się, zostawać"),
        ("Zhuan-bian", "Przekształcać"),
        ("Fa-zhan", "Rozwijać się"),
        ("Jin-bu", "Postępować, rozwijać"),
        ("Tui-bu", "Cofać się, podupadać"),

        # Posiadanie i wymiana
        ("You-you", "Posiadać"),
        ("Suo-you", "Własność, posiadać"),
        ("De-dao", "Zdobyć, otrzymać"),
        ("Qu-de", "Uzyskać"),
        ("Shi-qu", "Stracić"),
        ("Diu-shi", "Zgubić"),
        ("Jie-gei", "Pożyczyć (komuś)"),
        ("Jie-lai", "Pożyczyć (od kogoś)"),
        ("Mai-chu", "Sprzedać"),
        ("Gou-mai", "Kupić, zakupić"),

        # Komunikacja niewerbal na
        ("Kan-jian", "Zobaczyć"),
        ("Ting-dao", "Usłyszeć"),
        ("Wen-dao", "Poczuć zapach"),
        ("Chang-dao", "Skosztować"),
        ("Mo-dao", "Dotknąć (poczuć)"),

        ("Zhi-shi", "Wskazywać"),
        ("Zhao-shou", "Machać ręką"),
        ("Dian-tou", "Kiwać głową"),
        ("Yao-tou", "Potrząsać głową (zaprzeczenie)"),
        ("Ju-shou", "Podnieść rękę"),

        # Emocje wyrażane działaniem
        ("Xiao-chu", "Uśmiechać się"),
        ("Da-xiao", "Śmiać się głośno"),
        ("Ku-qi", "Płakać, łkać"),
        ("Liu-lei", "Ronić łzy"),
        ("Tan-xi", "Wzdychać"),
        ("Jiao-han", "Krzyczeć, wołać"),
        ("Han-jiao", "Wrzeszczeć"),
        ("Di-sheng", "Szeptać"),

        # Jedzenie i picie szczegółowo
        ("Yan-xia", "Połykać"),
        ("Jue-jiao", "Żuć"),
        ("Zhuo", "Dmuchać (na gorące)"),
        ("Pin-chang", "Degustować"),
        ("Gan-bei", "Wznieść toast"),

        # Czynności umysłowe
        ("Si-nian", "Tęsknić za"),
        ("Dan-xin", "Martwić się"),
        ("Dan-you", "Obawiać się"),
        ("Xi-wang", "Mieć nadzieję"),
        ("Yuan-wang", "Pragnąć, życzyć sobie"),
        ("Qi-pan", "Oczekiwać z niecierpliwością"),

        # Porównanie i ocena
        ("Bi-jiao", "Porównywać"),
        ("Pan-duan", "Osądzać, oceniać"),
        ("Ping-jia", "Oceniać, wartościować"),
        ("Ce-liang", "Mierzyć"),
        ("Ji-suan", "Obliczać, liczyć"),

        # Planowanie i organizacja
        ("Ji-hua", "Planować"),
        ("An-pai", "Organizować, ustalać"),
        ("Zhun-bei", "Przygotowywać"),
        ("Yu-bei", "Rezerwować, przygotować z wyprzedzeniem"),
    ],

    # ============================================================
    # PRZYMIOTNIKI OPISOWE (rozszerzone)
    # ============================================================
    "przymiotniki": [
        # Rozmiar i wymiary
        ("Ju-da", "Ogromny, gigantyczny"),
        ("Wei-xiao", "Maleńki, drobny"),
        ("Zhong-deng", "Średni"),
        ("Gao-da", "Wysoki i wielki"),
        ("Di-xiao", "Niski i mały"),
        ("Chang", "Długi"),
        ("Duan", "Krótki"),
        ("Kuan", "Szeroki"),
        ("Zhai", "Wąski"),
        ("Hou", "Gruby"),
        ("Bao", "Cienki"),
        ("Shen", "Głęboki"),
        ("Qian", "Płytki"),

        # Kształt
        ("Yuan", "Okrągły"),
        ("Fang", "Kwadratowy"),
        ("Chang-fang", "Prostokątny"),
        ("San-jiao", "Trójkątny"),
        ("Ping", "Płaski"),
        ("Wan-qu", "Zakrzywiony"),
        ("Zhi", "Prosty"),

        # Tekstura i powierzchnia
        ("Hua", "Gładki"),
        ("Cu-cao", "Szorstki"),
        ("Ruan", "Miękki"),
        ("Ying", "Twardy"),
        ("Cui", "Kruchy"),
        ("Nian", "Kleisty, lepki"),
        ("Gan-zao", "Suchy"),
        ("Shi-run", "Wilgotny, mokry"),
        ("Wen-re", "Ciepły"),
        ("Liang-shuang", "Chłodny, orzeźwiający"),
        ("Yan-re", "Gorący, upalny"),
        ("Bing-leng", "Lodowaty, mroźny"),

        # Waga
        ("Zhong", "Ciężki"),
        ("Qing", "Lekki"),
        ("Chen-zhong", "Bardzo ciężki"),

        # Wygląd
        ("Piao-liang", "Piękny, ładny"),
        ("Mei-li", "Piękny, urok liwy"),
        ("Chou-lou", "Brzydki"),
        ("Pu-tong", "Zwykły, przeciętny"),
        ("Te-shu", "Specjalny, szczególny"),
        ("Qi-guai", "Dziwny, osobliwy"),
        ("Qi-te", "Niezwykły"),

        # Kolory (rozszerzone)
        ("Shen-hong", "Ciemnoczerwony"),
        ("Qian-hong", "Jasnoczerwony"),
        ("Ju-hong", "Pomarańczowy"),
        ("Huang-se", "Żółty"),
        ("Lu-se", "Zielony"),
        ("Lan-se", "Niebieski"),
        ("Zi-se", "Fioletowy"),
        ("Fen-se", "Różowy"),
        ("Zong-se", "Brązowy"),
        ("Hui-se", "Szary"),
        ("Jin-se", "Złoty"),
        ("Yin-se", "Srebrny"),
        ("Cai-se", "Kolorowy"),

        # Stan i jakość
        ("Xin-xian", "Świeży"),
        ("Lao-jiu", "Stary, przestarzały"),
        ("Po-jiu", "Zniszczony, zużyty"),
        ("Wan-zheng", "Kompletny, cały"),
        ("Can-que", "Niepełny, uszkodzony"),
        ("Wan-hao", "Doskonały, nienaruszony"),
        ("Sun-huai", "Uszkodzony, zepsuty"),

        # Czystość i porządek
        ("Zheng-qi", "Uporządkowany, schludny"),
        ("Luan", "Chaotyczny"),
        ("Qing-jie", "Czysty, schludny"),
        ("Wu-zhuo", "Brudny, zabrudzony"),

        # Prędkość
        ("Xun-su", "Szybki"),
        ("Ji-su", "Bardzo szybki"),
        ("Huan-man", "Powolny"),
        ("Chi-huan", "Opóźniony, spóźniony"),

        # Trudność
        ("Rong-yi", "Łatwy"),
        ("Kun-nan", "Trudny"),
        ("Jian-dan", "Prosty"),
        ("Fu-za", "Skomplikowany"),

        # Bezpieczeństwo
        ("An-quan", "Bezpieczny"),
        ("Wei-xian", "Niebezpieczny"),
        ("Ke-pa", "Straszny"),
        ("Ke-wei", "Budzący respekt"),

        # Wartość
        ("Gui", "Drogi, cenny"),
        ("Pian-yi", "Tani"),
        ("Zhen-gui", "Cenny, rzadki"),
        ("Wu-jia", "Bezcenny"),

        # Prawda i fałsz
        ("Zhen-shi", "Prawdziwy, autentyczny"),
        ("Jia-mao", "Fałszywy, podrobiony"),
        ("Que-shi", "Rzeczywisty, faktyczny"),
        ("Xu-jia", "Fałszywy, zmyślony"),

        # Emocjonalne (opisujące rzeczy)
        ("You-qu", "Ciekawy, interesujący"),
        ("Wu-qu", "Nudny"),
        ("Ke-ai", "Uroczy, słodki"),
        ("Ke-hen", "Nienawistny, wstrętny"),
    ],

    # ============================================================
    # PRZYSŁÓWKI
    # ============================================================
    "przyslowki": [
        # Czas
        ("Gang-gang", "Właśnie, dopiero co"),
        ("Gang-cai", "Przed chwilą"),
        ("Ma-shang", "Zaraz, natychmiast"),
        ("Li-ke", "Natychmiast"),
        ("Yi-jing", "Już"),
        ("Zheng-zai", "Właśnie (w trakcie)"),
        ("Hai-mei", "Jeszcze nie"),
        ("Jing-chang", "Często"),
        ("Tong-chang", "Zazwyczaj"),
        ("You-shi", "Czasami"),
        ("Ou-er", "Od czasu do czasu"),
        ("Zong-shi", "Zawsze"),
        ("Cong-bu", "Nigdy"),
        ("Ceng-jing", "Kiedyś, niegdyś"),
        ("Jiang-yao", "Wkrótce, za chwilę"),

        # Stopień
        ("Hen", "Bardzo"),
        ("Fei-chang", "Niezwyczajnie"),
        ("Tai", "Zbyt, za bardzo"),
        ("Geng", "Bardziej"),
        ("Zui", "Najbardziej"),
        ("Bi-jiao", "Dość, dosyć"),
        ("Xiang-dang", "Dość, całkiem"),
        ("Shi-fen", "Bardzo, nadzwyczaj"),
        ("Guo-fen", "Nadmiernie"),
        ("Shao-wei", "Trochę, nieco"),
        ("You-dian", "Trochę, nieco"),

        # Sposób
        ("Hao-hao", "Dobrze, porządnie"),
        ("Man-man", "Powoli, stopniowo"),
        ("Kuai-kuai", "Szybko"),
        ("Ren-zhen", "Poważnie, starannie"),
        ("Sui-bian", "Niedbale, od niechcenia"),
        ("Tu-ran", "Nagle"),
        ("Jiang-jiang", "Powoli, stopniowo"),

        # Zakres
        ("Quan-bu", "Całkowicie, wszystko"),
        ("Bu-fen", "Częściowo"),
        ("Zhi-you", "Tylko"),
        ("Jin-jin", "Tylko, jedynie"),
        ("Dou", "Wszyscy, wszystkie"),
        ("Ge-ge", "Każdy z osobna"),

        # Pewność
        ("Yi-ding", "Na pewno, koniecznie"),
        ("Ken-ding", "Zdecydowanie"),
        ("Ye-xu", "Może"),
        ("Ke-neng", "Możliwe"),
        ("Da-gai", "Prawdopodobnie"),
        ("Huo-xu", "Być może"),

        # Negacja wzmocniona
        ("Wan-quan", "Całkowicie (nie)"),
        ("Gen-ben", "W ogóle (nie)"),
        ("Yi-dian", "Ani trochę (nie)"),

        # Położenie
        ("Zhe-li", "Tutaj"),
        ("Na-li", "Tam"),
        ("Shang-mian", "Góra, na górze"),
        ("Xia-mian", "Dół, na dole"),
        ("Qian-mian", "Przód, z przodu"),
        ("Hou-mian", "Tył, z tyłu"),
        ("Li-mian", "Wewnątrz"),
        ("Wai-mian", "Na zewnątrz"),
        ("Pang-bian", "Obok, z boku"),
        ("Zhong-jian", "Pośrodku"),
    ],

    # ============================================================
    # BUDYNKI I ARCHITEKTURA
    # ============================================================
    "architektura": [
        ("Lou", "Budynek piętrowy"),
        ("Ta", "Pagoda, wieża"),
        ("Qiao", "Most"),
        ("Men-lou", "Brama (budowla)"),
        ("Cheng-qiang", "Mur miejski"),
        ("Cheng-bao", "Twierdza"),

        ("Gong-dian", "Pałac, hala pałacowa"),
        ("Miao", "Świątynia"),
        ("Ci-tang", "Sala przodków"),
        ("Shu-yuan", "Akademia konfucjańska"),

        ("Fang-zi", "Dom"),
        ("Fang-jian", "Pokój"),
        ("Ke-ting", "Salon"),
        ("Wo-shi", "Sypialnia"),
        ("Chu-fang", "Kuchnia"),
        ("Shu-fang", "Gabinet"),
        ("Yuan-zi", "Dziedziniec"),
        ("Ting-yuan", "Ogród wewnętrzny"),

        ("Fang-ding", "Dach"),
        ("Qiang-bi", "Ściana"),
        ("Di-ban", "Podłoga"),
        ("Lou-ti", "Schody"),
        ("Zhu-zi", "Filar, kolumna"),
        ("Liang-zi", "Belka"),

        ("Wa-pian", "Dachówka"),
        ("Zhuan-tou", "Cegła"),
        ("Mu-tou", "Drewno (materiał budowlany)"),
        ("Shi-tou", "Kamień (materiał budowlany)"),
    ],

    # ============================================================
    # JEDZENIE I PICIE (szczegółowe)
    # ============================================================
    "jedzenie": [
        # Posiłki
        ("Zao-fan", "Śniadanie"),
        ("Wu-fan", "Obiad"),
        ("Wan-fan", "Kolacja"),
        ("Dian-xin", "Przekąska, przysmak"),

        # Przygotowanie
        ("Sheng-de", "Surowy"),
        ("Shu-de", "Gotowany, ugotowany"),
        ("Kao-de", "Pieczony"),
        ("Zha-de", "Smażony (głębokie smażenie)"),
        ("Zheng-de", "Gotowany na parze"),
        ("Chao-de", "Smażony (stir-fry)"),

        # Smak
        ("Tian", "Słodki"),
        ("Suan", "Kwaśny"),
        ("Ku", "Gorzki"),
        ("La", "Ostry, pikantny"),
        ("Xian", "Słony, smaczny (umami)"),
        ("Dan", "Mdły"),
        ("Xiang", "Aromatyczny"),

        # Produkty zbożowe
        ("Zhou", "Kongie, kleik ryżowy"),
        ("Tang-mian", "Makaron w zupie"),
        ("Chao-mian", "Smażony makaron"),
        ("Bing-zi", "Placek, naleśnik"),

        # Mięso
        ("Zhu-rou", "Wieprzowina"),
        ("Niu-rou", "Wołowina"),
        ("Yang-rou", "Baranina"),
        ("Ji-rou", "Kurczak"),
        ("Ya-rou", "Kaczka"),
        ("Yu-rou", "Ryba (mięso)"),

        # Warzywa
        ("Qing-cai", "Zielone warzywa"),
        ("Dou-fu", "Tofu"),
        ("Qie-zi", "Bakłażan"),
        ("Huang-gua", "Ogórek"),
        ("Fan-qie", "Pomidor"),
        ("Cong", "Szczypior"),
        ("Suan", "Czosnek"),
        ("Jiang", "Imbir"),

        # Owoce
        ("Ping-guo", "Jabłko"),
        ("Li-zi", "Gruszka"),
        ("Tao-zi", "Brzoskwinia"),
        ("Xing-zi", "Morela"),
        ("Pu-tao", "Winogrona"),
        ("Ju-zi", "Mandarynka, pomarańcza"),
        ("Xi-gua", "Arbuz"),
        ("Li-zhi", "Liczi"),
        ("Long-yan", "Longan"),

        # Napoje
        ("Cha", "Herbata"),
        ("Jiu", "Alkohol, wino"),
        ("Nai", "Mleko"),
        ("Dou-jiang", "Mleko sojowe"),
        ("Kai-shui", "Wrzątek, gotowana woda"),

        # Przyprawy
        ("Yan", "Sól"),
        ("Tang", "Cukier"),
        ("Cu", "Ocet"),
        ("Jiang-you", "Sos sojowy"),
        ("Xiang-you", "Olej sezamowy"),
        ("La-jiao", "Papryka chili"),
    ],

    # ============================================================
    # UBRANIA I OZDOBY
    # ============================================================
    "ubrania": [
        ("Yi-fu", "Ubranie (ogólne)"),
        ("Chang-pao", "Długa szata"),
        ("Duan-ao", "Krótka kurtka"),
        ("Ku", "Spodnie"),
        ("Qun", "Spódnica"),

        ("Wai-yi", "Wierzchnie ubranie"),
        ("Nei-yi", "Bielizna"),
        ("Mao-yi", "Sweter wełniany"),
        ("Pi-ao", "Płaszcz skórzany"),

        ("Mao-zi", "Kapelusz, czapka"),
        ("Guan", "Korona, czapka urzędnicza"),
        ("Jin", "Chusta, szal"),
        ("Xie", "Buty"),
        ("Wa", "Skarpetki"),
        ("Dai-zi", "Pasek"),

        ("Shou-zhuo", "Bransoletka"),
        ("Xiang-lian", "Naszyjnik"),
        ("Er-huan", "Kolczyki"),
        ("Jie-zhi", "Pierścień"),
        ("Fa-zan", "Szpilka do włosów"),
        ("Yu-pei", "Wisiorek z jadeitu"),

        ("Si", "Jedwab"),
        ("Bu", "Tkanina, materiał"),
        ("Mian", "Bawełna"),
        ("Ma", "Len"),
        ("Mao", "Wełna"),
        ("Pi-ge", "Skóra"),
    ],

    # ============================================================
    # RODZINA ROZSZERZONA
    # ============================================================
    "rodzina_rozszerzona": [
        ("Zu-xian", "Przodek"),
        ("Hou-dai", "Potomek"),
        ("Bei-fen", "Pokolenie (starsze/młodsze)"),

        ("Bo-fu", "Wujek (starszy brat ojca)"),
        ("Bo-mu", "Ciotka (żona starszego brata ojca)"),
        ("Shu-fu", "Wujek (młodszy brat ojca)"),
        ("Shen-mu", "Ciotka (siostra ojca)"),
        ("Jiu-ma", "Ciotka (żona brata matki)"),
        ("Yi-mu", "Ciotka (siostra matki)"),

        ("Tang-xiong", "Kuzyn (starszy, od ojca)"),
        ("Tang-di", "Kuzyn (młodszy, od ojca)"),
        ("Biao-xiong", "Kuzyn (starszy, od matki)"),

        ("Er-zi", "Syn"),
        ("Nü-er", "Córka"),
        ("Zhang-zi", "Zięć"),
        ("Xi-fu", "Synowa"),

        ("Sun-zi", "Wnuk"),
        ("Sun-nü", "Wnuczka"),
        ("Wai-sun", "Wnuk (od córki)"),

        ("Qi-zi", "Żona"),
        ("Zhang-fu", "Mąż"),
        ("Fu-qi", "Małżeństwo (para)"),
    ],

    # ============================================================
    # MUZYKA I INSTRUMENTY
    # ============================================================
    "muzyka": [
        ("Yin-yue", "Muzyka"),
        ("Ge-qu", "Piosenka"),
        ("Qu-zi", "Melodia"),
        ("Yue-pu", "Nuty muzyczne"),

        ("Qin", "Guqin (cytra)"),
        ("Zheng", "Guzheng (cytra)"),
        ("Pi-pa", "Pipa (lutnia)"),
        ("Di-zi", "Flet bambusowy"),
        ("Xiao", "Flet wertykalny"),
        ("Sheng", "Sheng (organy ustne)"),
        ("Gu", "Bęben"),
        ("Luo", "Gong"),

        ("Tan-qin", "Grać na instrumencie strunowym"),
        ("Chui-di", "Grać na flecie"),
        ("Da-gu", "Bić w bęben"),

        ("Chang-ge", "Śpiewać"),
        ("Ge-sheng", "Głos śpiewu"),
        ("Yue-shi", "Muzyk"),
    ],

    # ============================================================
    # LITERATURA I SZTUKA
    # ============================================================
    "literatura": [
        ("Wen-xue", "Literatura"),
        ("Shi-ci", "Poezja (formalna)"),
        ("Shi-ren", "Poeta"),
        ("San-wen", "Proza"),
        ("Xiao-shuo", "Powieść, opowiadanie"),
        ("Zhuan-ji", "Biografia"),

        ("Shu-fa", "Kaligrafia"),
        ("Mo-bao", "Kaligraficzny skarb"),
        ("Bi-mo", "Pędzel i tusz"),

        ("Hua-hua", "Malować obrazy"),
        ("Shan-shui-hua", "Malarstwo pejzażowe"),
        ("Hua-juan", "Zwój malarzy"),

        ("Diao-ke", "Rzeźbienie"),
        ("Diao-su", "Rzeźba"),
        ("Tao-ci", "Ceramika"),
        ("Yu-qi", "Przedmioty z jadeitu"),
    ],

    # ============================================================
    # RELIGIA I OBRZĘDY
    # ============================================================
    "religia": [
        ("Dao-jiao", "Taoizm"),
        ("Fo-jiao", "Buddyzm"),
        ("Ru-jiao", "Konfucjanizm"),

        ("Shen-ming", "Bóstwo, bożek"),
        ("Gui-shen", "Duchy i bóstwa"),
        ("Yao-guai", "Demon, potwór"),
        ("Xian-ren", "Nieśmiertelny (taoist)"),

        ("Qi-dao", "Modlić się"),
        ("Ji-si", "Ofiarować, składać ofiary"),
        ("Bai", "Kłaniać się w hołdzie"),

        ("Jing-xiang", "Kadzidło"),
        ("Gong-pin", "Ofiara (przedmiot)"),
        ("Xiang-lu", "Kadzielnica"),

        ("Si-miao", "Świątynia, sanktuarium"),
        ("Fo-ta", "Pagoda buddyjska"),
        ("Dao-guan", "Świątynia taoistyczna"),

        ("Fa-hui", "Ceremonia buddyjska"),
        ("Fa-shi", "Ceremonia taoistyczna"),
        ("Ji-dian", "Festiwal, ceremonia"),

        ("Chuan-shuo", "Legenda"),
        ("Shen-hua", "Mit, mitologia"),
        ("Yu-yan", "Przepowiednia"),
        ("Zhan-bu", "Wróżbiarstwo"),
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

def generate_extended_dictionary():
    """Generuje CZĘŚĆ 2 słownika"""
    print("Ładowanie istniejącego słownika...")
    existing = load_existing_dictionary('../03_Slownik/slownik_lengxuan_polski.md')
    print(f"Załadowano {len(existing)} istniejących słów\n")

    all_new_words = []
    total_added = 0

    for category, words in ADDITIONAL_VOCABULARY.items():
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
    print(f"CZĘŚĆ 2 - SUMA: Dodano {total_added} nowych słów")
    print(f"Całkowita liczba słów: {len(existing)}")
    print(f"{'='*60}\n")

    # Sortuj i zapisz
    sorted_words = sorted(existing.items(), key=lambda x: x[0])

    output_path = '../03_Slownik/slownik_lengxuan_polski.md'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# Słownik Lengxuan - Rozszerzony (Część 2)\n\n")
        f.write(f"**Liczba wpisów:** {len(existing)}\n")
        f.write(f"**Ostatnia aktualizacja:** 2026-01-03 (Część 2)\n\n")
        f.write("---\n\n")

        for word_lower, (word, meaning) in sorted_words:
            f.write(f"- {word} - {meaning}\n")

    print(f"[OK] Zapisano rozszerzony słownik: {output_path}")
    print(f"  Całkowita liczba wpisów: {len(existing)}")

    return existing

if __name__ == '__main__':
    print("="*60)
    print("GENERATOR SŁOWNIKA LENGXUAN - CZĘŚĆ 2")
    print("="*60)
    print()

    extended_dict = generate_extended_dictionary()

    print("\n" + "="*60)
    print("GOTOWE!")
    print("="*60)
