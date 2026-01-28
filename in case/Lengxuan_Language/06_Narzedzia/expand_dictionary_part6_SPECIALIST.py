# -*- coding: utf-8 -*-
"""
GENERATOR SŁOWNIKA LENGXUAN - CZĘŚĆ 6 (SPECJALISTYCZNA)
Cel: Osiągnięcie 3000+ słów w słowniku

Dodaje ~700 nowych słów w specjalistycznych kategoriach:
- Szczegółowe owady i ryby
- Szczegółowe rośliny i zioła
- Choroby i symptomy
- Ruchy ciała i gesty
- Szczegóły pogody
- Rolnictwo szczegółowe
- Łowiectwo i rybołówstwo
- Tekstylia szczegółowe
- Czynności domowe
- Dzieci i rodzina
- Festiwale i ceremonie
- Przesądy i wierzenia ludowe
- Poezja i literatura
- Kaligrafia
- Ceremonia herbaty
- Taktyki wojenne
- Szczegóły broni
- Zbroja i ochrona
- Konie i jazda konna
- Statki i żegluga
- Pieniądze i waluta
- Gry i hazard
"""

import re
from collections import defaultdict

# ============================================================
# SŁOWNICTWO SPECJALISTYCZNE - CZĘŚĆ 6 (~700 SŁÓW)
# ============================================================

SPECIALIST_VOCABULARY = {
    "owady_ryby": [
        ("Chong", "Robak, owad"),
        ("Kun-chong", "Owad"),
        ("Ying", "Mucha"),
        ("Wen", "Komar"),
        ("Feng", "Pszczoła"),
        ("Mi-feng", "Pszczoła miodna"),
        ("Huang-feng", "Osa"),
        ("Die", "Motyl"),
        ("E", "Ćma"),
        ("Qing-ting", "Ważka"),
        ("Ma-yi", "Mrówka"),
        ("Zhi-zhu", "Pająk"),
        ("Xie-zi", "Skorpion"),
        ("Wu-gong", "Skolopendra"),
        ("Chan", "Cykada"),
        ("Guo-guo", "Świerszcz"),
        ("Huang-chong", "Szarańcza"),
        ("Zao", "Pchła"),
        ("Shi-zi", "Wesz"),
        ("Bi", "Pcheł"),
        ("Yu", "Ryba"),
        ("Li", "Karp"),
        ("Qing-yu", "Makrel"),
        ("Gui-yu", "Ryba mandarynka"),
        ("Huang-shan-yu", "Dorsz żółty"),
        ("Xia", "Krewetka"),
        ("Pang-xie", "Krab"),
        ("Long-xia", "Homar"),
        ("You-yu", "Kałamarnica"),
        ("Zhang-yu", "Ośmiornica"),
        ("Bei", "Skorupiak"),
        ("Mu-li", "Ostryga"),
        ("Ge", "Małż"),
        ("Tian-luo", "Ślimak wodny"),
        ("Hai-shen", "Ogórek morski"),
        ("Hai-zhe", "Meduza"),
        ("Shan-hu", "Koral"),
        ("Hai-xing", "Rozgwiazda"),
    ],

    "rosliny_ziola_szczegoly": [
        ("Ren-shen", "Żeń-szeń"),
        ("Huang-qi", "Astragalus"),
        ("Dang-gui", "Angelica chińska"),
        ("Chuan-xiong", "Ligusticum"),
        ("Bai-shao", "Piwonia biała"),
        ("Gan-cao", "Lukrecja"),
        ("Fu-ling", "Poria"),
        ("Bai-zhu", "Atractylodes"),
        ("Sheng-jiang", "Imbir świeży"),
        ("Da-zao", "Daktyl chiński"),
        ("Gou-qi", "Jagody goji"),
        ("Ju-hua", "Chryzantema"),
        ("Bo-he", "Mięta"),
        ("Gui-zhi", "Gałązki cynamonu"),
        ("Rou-gui", "Kora cynamonu"),
        ("Ding-xiang", "Goździk"),
        ("Ba-jiao", "Anyż gwiaździsty"),
        ("Hua-jiao", "Pieprz syczuański"),
        ("Zi-su", "Perilla"),
        ("Chen-pi", "Skórka mandarynki"),
        ("Lian-zi", "Nasiona lotosu"),
        ("Bai-he", "Lilia"),
        ("Shan-yao", "Ignam chiński"),
        ("He-shou-wu", "Rdest chiński"),
        ("Dong-chong-xia-cao", "Cordyceps"),
        ("Ling-zhi", "Reishi"),
        ("Mu-er", "Uszko Judasza"),
        ("Yin-er", "Grzybek srebrny"),
        ("Xiang-gu", "Shiitake"),
        ("Jin-zhen-gu", "Enoki"),
    ],

    "choroby_symptomy": [
        ("Bing", "Choroba"),
        ("Ji", "Dolegliwość"),
        ("Zheng", "Symptom"),
        ("Teng", "Ból"),
        ("Tou-teng", "Ból głowy"),
        ("Ya-teng", "Ból zęba"),
        ("Du-teng", "Ból brzucha"),
        ("Yao-teng", "Ból pleców"),
        ("Shao", "Gorączka"),
        ("Fa-shao", "Mieć gorączkę"),
        ("Han", "Pot"),
        ("Chu-han", "Pocić się"),
        ("Ke", "Kaszel"),
        ("Ke-sou", "Kaszleć"),
        ("Pen-ti", "Kichać"),
        ("Liu-ti", "Katar"),
        ("Yan", "Zapalenie"),
        ("Zhong", "Obrzęk"),
        ("Yang", "Swędzenie"),
        ("Fa-yang", "Swędzieć"),
        ("Yun", "Zawroty głowy"),
        ("Tou-yun", "Zawroty głowy"),
        ("E", "Nudności"),
        ("Fan-e", "Mdłości"),
        ("Tu", "Wymioty"),
        ("Ou-tu", "Wymiotować"),
        ("Xie", "Biegunka"),
        ("La-du-zi", "Mieć biegunkę"),
        ("Bian-mi", "Zaparcia"),
        ("Shang", "Rana"),
        ("Shang-kou", "Rana (otwarta)"),
        ("Chu-xue", "Krwawić"),
        ("Yu-xue", "Zastój krwi"),
        ("Gu-zhe", "Złamanie"),
        ("Nuo-shang", "Zwichnięcie"),
        ("Cuo-shang", "Skręcenie"),
        ("Shao-shang", "Oparzenie"),
        ("Dong-shang", "Odmrożenie"),
        ("Du", "Trucizna"),
        ("Zhong-du", "Zatrucie"),
        ("Feng", "Wiatr (TCM patogen)"),
        ("Han", "Zimno (TCM patogen)"),
        ("Shi", "Wilgoć (TCM patogen)"),
        ("Zao", "Suchość (TCM patogen)"),
        ("Huo", "Ogień (TCM patogen)"),
        ("Tan", "Flegma"),
        ("Xu", "Niedobór (TCM)"),
        ("Shi", "Nadmiar (TCM)"),
    ],

    "ruchy_gesty": [
        ("Zou", "Iść, chodzić"),
        ("Pao", "Biec"),
        ("Tiao", "Skakać"),
        ("Tiao-yue", "Podskakiwać"),
        ("Qi-lai", "Wstawać"),
        ("Zhan", "Stać"),
        ("Zuo", "Siedzieć"),
        ("Tang", "Leżeć"),
        ("Gui", "Klękać"),
        ("Bai", "Kłaniać się"),
        ("Fu", "Kłaniać się nisko"),
        ("Kou-tou", "Bić pokłony"),
        ("Dian-tou", "Kiwać głową"),
        ("Yao-tou", "Kręcić głową"),
        ("Hui-shou", "Machać ręką"),
        ("Zhao-shou", "Machać (witając)"),
        ("Zhi", "Wskazywać"),
        ("Dian", "Wskazywać palcem"),
        ("Na", "Brać, chwytać"),
        ("Zhua", "Chwytać, łapać"),
        ("Wo", "Trzymać (w dłoni)"),
        ("Bao", "Obejmować"),
        ("Yong", "Przytulać"),
        ("Tui", "Pchać"),
        ("La", "Ciągnąć"),
        ("Reng", "Rzucać"),
        ("Diu", "Wyrzucać"),
        ("Jie", "Łapać (w powietrzu)"),
        ("Ti", "Kopać"),
        ("Da", "Uderzać"),
        ("Ji", "Bić"),
        ("Pai", "Klepać"),
        ("Mo", "Głaskać"),
        ("Nuo", "Przenosić"),
        ("Tai", "Podnosić (razem)"),
        ("Ban", "Przenosić"),
        ("Kang", "Dźwigać (na ramieniu)"),
        ("Bei", "Nosić (na plecach)"),
        ("Wan", "Zginać"),
        ("Shen", "Wyciągać"),
        ("Shou", "Kurczyć"),
        ("Zhan", "Rozpościerać"),
        ("Juan", "Zwijać"),
        ("Zhe", "Składać"),
        ("Die", "Składać (warstwami)"),
    ],

    "pogoda_szczegoly": [
        ("Qing", "Słonecznie, pogodnie"),
        ("Yin", "Pochmurno"),
        ("Yun", "Chmura"),
        ("Duo-yun", "Częściowo pochmurnie"),
        ("Yu", "Deszcz"),
        ("Xiao-yu", "Mały deszcz"),
        ("Da-yu", "Duży deszcz"),
        ("Bao-yu", "Ulewny deszcz"),
        ("Mao-mao-yu", "Mżawka"),
        ("Lei", "Grzmot"),
        ("Shan-dian", "Błyskawica"),
        ("Lei-yu", "Burza z piorunami"),
        ("Xue", "Śnieg"),
        ("Xiao-xue", "Lekki śnieg"),
        ("Da-xue", "Obfity śnieg"),
        ("Bao-xue", "Zamieć"),
        ("Bing", "Lód"),
        ("Bing-bao", "Grad"),
        ("Shuang", "Szron"),
        ("Lu", "Rosa"),
        ("Wu", "Mgła"),
        ("Mai", "Smog, zadymka"),
        ("Feng", "Wiatr"),
        ("Wei-feng", "Lekki wiatr"),
        ("Qiang-feng", "Silny wiatr"),
        ("Bao-feng", "Huragan"),
        ("Long-juan-feng", "Tornado"),
        ("Tai-feng", "Tajfun"),
        ("Han", "Zimno"),
        ("Leng", "Chłód"),
        ("Re", "Gorąco"),
        ("Wen-nuan", "Ciepło"),
        ("Liang-kuai", "Chłodno"),
        ("Yan-re", "Upał"),
        ("Ku-re", "Skwar"),
        ("Chao-shi", "Wilgotno"),
        ("Gan-zao", "Sucho"),
    ],

    "rolnictwo": [
        ("Geng", "Orać"),
        ("Li", "Pług"),
        ("Bo", "Siać"),
        ("Zhong", "Sadzić"),
        ("Jiao", "Podlewać"),
        ("Guan-gai", "Nawadniać"),
        ("Chu-cao", "Pielić"),
        ("Shi-fei", "Nawozić"),
        ("Fei-liao", "Nawóz"),
        ("Shou", "Zbierać plony"),
        ("Shou-ge", "Żniwa"),
        ("Ge", "Żąć, kosić"),
        ("Lian", "Młócić"),
        ("Shai", "Suszyć (zboże)"),
        ("Cang", "Magazynować"),
        ("Gu-cang", "Spichlerz"),
        ("Dao", "Ryż (niełuskany)"),
        ("Mai", "Pszenica"),
        ("Shu", "Proso"),
        ("Liang", "Zboże"),
        ("Dou", "Fasola, bob"),
        ("Huang-dou", "Soja"),
        ("Lu-dou", "Fasola mung"),
        ("Hong-dou", "Fasola azuki"),
        ("Hua-sheng", "Orzeszki ziemne"),
        ("Zhi-ma", "Sezam"),
        ("Gua", "Melon, ogórek"),
        ("Huang-gua", "Ogórek"),
        ("Xi-gua", "Arbuz"),
        ("Dong-gua", "Melon zimowy"),
        ("Nan-gua", "Dynia"),
        ("Qie-zi", "Bakłażan"),
        ("Luo-bo", "Rzepa, rzodkiew"),
        ("Hu-luo-bo", "Marchew"),
        ("Bai-luo-bo", "Rzodkiew biała"),
    ],

    "lowiectwo_rybolowstwo": [
        ("Lie", "Polować"),
        ("Da-lie", "Polowanie"),
        ("Lie-ren", "Myśliwy"),
        ("Shou-lie", "Łowy"),
        ("Zhui", "Ścigać (zwierzynę)"),
        ("Gong", "Łuk"),
        ("Jian", "Strzała"),
        ("Nu", "Kusza"),
        ("She", "Strzelać"),
        ("She-jian", "Strzelać z łuku"),
        ("Quan-tao", "Sidła, pułapka"),
        ("Xian-jing", "Pułapka na zwierzynę"),
        ("Quan", "Pies myśliwski"),
        ("Ying", "Jastrząb, sokół"),
        ("Xun-ying", "Sokół treser"),
        ("Diao", "Wędkować"),
        ("Diao-yu", "Łowić ryby"),
        ("Yu-ren", "Rybak"),
        ("Yu-chuan", "Łódź rybacka"),
        ("Yu-wang", "Sieć rybacka"),
        ("Yu-gan", "Wędka"),
        ("Yu-gou", "Haczyk"),
        ("Er", "Przynęta"),
        ("Lu", "Połów"),
        ("Bu-lao", "Wyciągać sieć"),
        ("Sa-wang", "Zarzucać sieć"),
    ],

    "tekstylia_szczegoly": [
        ("Fang", "Przęść"),
        ("Fang-che", "Kołowrotek"),
        ("Sha", "Przędza"),
        ("Zhi", "Tkać"),
        ("Zhi-bu", "Tkać tkaninę"),
        ("Zhi-ji", "Krosno"),
        ("Ran", "Farbować"),
        ("Ran-se", "Barwienie"),
        ("Ran-liao", "Barwnik"),
        ("Lan-cao", "Indygo (roślina)"),
        ("Xiu", "Haftować"),
        ("Ci-xiu", "Haft"),
        ("Zhen-xian", "Nici do haftu"),
        ("Feng", "Szyć"),
        ("Feng-ren", "Krawiec"),
        ("Feng-zhen", "Igła do szycia"),
        ("Zhen-xian", "Nić"),
        ("Bu-liao", "Materiał"),
        ("Si-chou", "Jedwab (tkanina)"),
        ("Jin", "Brokat"),
        ("Duan", "Satyna"),
        ("Sha", "Gaza"),
        ("Luo", "Muślin jedwabny"),
        ("Ge", "Ramia (tkanina)"),
        ("Ma-bu", "Płótno lniane"),
        ("Mian-bu", "Bawełna (tkanina)"),
        ("Mao-pi", "Futro"),
    ],

    "czynnosci_domowe": [
        ("Sao", "Zamiatać"),
        ("Sao-di", "Zamiatać podłogę"),
        ("Mo", "Wycierać"),
        ("Ca", "Szorować"),
        ("Xi", "Prać"),
        ("Xi-yi", "Prać ubrania"),
        ("Shai", "Suszyć (na słońcu)"),
        ("Die", "Składać (ubrania)"),
        ("Shou-shi", "Sprzątać, porządkować"),
        ("Zheng-li", "Organizować"),
        ("Bai", "Ustawiać"),
        ("Fang", "Kłaść, umieszczać"),
        ("Gua", "Wieszać"),
        ("Diao", "Zawieszać"),
        ("Qu", "Brać, zdejmować"),
        ("Na-zou", "Zabierać"),
        ("Duan", "Nosić (dwoma rękami)"),
        ("Ti", "Nosić (w ręku)"),
        ("Shao-shui", "Gotować wodę"),
        ("Sheng-huo", "Rozpalać ogień"),
        ("Mie-huo", "Gasić ogień"),
        ("Tian-chai", "Dokładać drewna"),
        ("Dao-shui", "Nalewać wodę"),
        ("Qing-xi", "Czyścić, myć"),
    ],

    "dzieci_rodzina": [
        ("Huai-yun", "Ciąża"),
        ("Sheng", "Rodzić"),
        ("Ying-er", "Niemowlę"),
        ("Bao-bao", "Dziecko (pieszczotliwie)"),
        ("Xiao-hai", "Małe dziecko"),
        ("Nai", "Mleko matki"),
        ("Bu-ru", "Karmić piersią"),
        ("Yao", "Kołysać"),
        ("Bao", "Nosić (dziecko)"),
        ("Wan", "Bawić się"),
        ("Wan-ju", "Zabawka"),
        ("You-xi", "Gra, zabawa"),
        ("Pao", "Biegać (bawić się)"),
        ("Tiao", "Skakać (bawić się)"),
        ("Chang-ge", "Śpiewać"),
        ("Tiao-wu", "Tańczyć"),
        ("Ku", "Płakać"),
        ("Xiao", "Śmiać się"),
        ("Nao", "Hałasować"),
        ("Pian", "Oszukiwać, łudzić"),
        ("Qi-fu", "Dręczyć"),
        ("Jiao", "Nauczać"),
        ("Xue", "Uczyć się"),
        ("Ting-hua", "Być posłusznym"),
        ("Tao-qi", "Niegrzeczny, psotny"),
    ],

    "festiwale_ceremonie": [
        ("Jie", "Festiwal, święto"),
        ("Jie-ri", "Dzień świąteczny"),
        ("Chun-jie", "Nowy Rok Księżycowy"),
        ("Yuan-xiao", "Festiwal Latarni"),
        ("Qing-ming-jie", "Festiwal Qingming"),
        ("Duan-wu", "Festiwal Smoczych Łodzi"),
        ("Zhong-qiu", "Festiwal Środka Jesieni"),
        ("Chong-yang", "Festiwal Podwójnej Dziewiątki"),
        ("Ji", "Składać ofiarę"),
        ("Ji-si", "Ceremonia ofiarna"),
        ("Bai", "Czcić, oddawać pokłon"),
        ("Bai-shen", "Czcić bogów"),
        ("Bai-zu", "Czcić przodków"),
        ("Xiang", "Kadzidło"),
        ("Shao-xiang", "Palić kadzidło"),
        ("Zhu", "Świeca"),
        ("Dian-zhu", "Zapalać świece"),
        ("Gong", "Gong"),
        ("Gu", "Bęben"),
        ("Qiao", "Bić (w gong/bęben)"),
        ("Yan", "Uczta"),
        ("Yan-hui", "Bankiet"),
        ("Jiu-xi", "Przyjęcie (z alkoholem)"),
        ("Hun-li", "Ceremonia ślubna"),
        ("Tang-li", "Ceremonia pogrzebowa"),
    ],

    "przesady_wierzenia": [
        ("Yun", "Szczęście, fortuna"),
        ("Hao-yun", "Dobra fortuna"),
        ("E-yun", "Zła fortuna"),
        ("Ji", "Szczęśliwy, pomyślny"),
        ("Ji-xiang", "Auspicyjny"),
        ("Xiong", "Niepomyślny"),
        ("Bu-xiang", "Niefortunny"),
        ("Ling", "Magiczny, duchowy"),
        ("Shen-ling", "Bóstwo"),
        ("Gui", "Duch, widmo"),
        ("Yao", "Demon"),
        ("Yao-guai", "Potwór"),
        ("Xian", "Nieśmiertelny"),
        ("Shen-xian", "Bóg, nieśmiertelny"),
        ("Long", "Smok"),
        ("Feng", "Feniks"),
        ("Qi-lin", "Qilin"),
        ("Fu", "Nietoperz (symbol szczęścia)"),
        ("Fu-lu-shou", "Fortuna, dobrobyt, długowieczność"),
        ("Zhan-bu", "Wróżenie"),
        ("Suan-ming", "Wróżenie z losu"),
        ("Feng-shui", "Feng shui"),
        ("Zhou", "Klątwa, zaklęcie"),
        ("Fu", "Talizman"),
        ("Hu-shen-fu", "Amulet ochronny"),
    ],

    "poezja_literatura": [
        ("Shi", "Poezja"),
        ("Shi-ren", "Poeta"),
        ("Ci", "Liryka (forma poetycka)"),
        ("Fu", "Oda"),
        ("Ge", "Pieśń, ballada"),
        ("Yun", "Rym"),
        ("Lü", "Metrum, rytm"),
        ("Ju", "Werset, zdanie"),
        ("Hang", "Linia, wiersz"),
        ("Zhang", "Rozdział"),
        ("Pian", "Artykuł, utwór"),
        ("Wen", "Literatura, tekst"),
        ("Wen-zhang", "Artykuł literacki"),
        ("Gu-shi", "Historia, opowieść"),
        ("Xiao-shuo", "Powieść"),
        ("Chuan-shuo", "Legenda"),
        ("Shen-hua", "Mit"),
        ("Yu-yan", "Bajka"),
        ("Dian-gu", "Aluzja klasyczna"),
        ("Bi-yu", "Metafora"),
    ],

    "kaligrafia": [
        ("Shu", "Pisać"),
        ("Shu-fa", "Kaligrafia"),
        ("Bi", "Pędzel"),
        ("Mao-bi", "Pędzel kaligraficzny"),
        ("Mo", "Tusz"),
        ("Yan", "Kamień do tuszu"),
        ("Zhi", "Papier"),
        ("Xuan-zhi", "Papier ryżowy"),
        ("Mo-zhi", "Rozcierać tusz"),
        ("Dian", "Kropka (kreska)"),
        ("Heng", "Pozioma kreska"),
        ("Shu", "Pionowa kreska"),
        ("Pie", "Ukośna w lewo"),
        ("Na", "Ukośna w prawo"),
        ("Ti", "Haczyk"),
        ("Gou", "Hak"),
        ("Zhe", "Załamanie"),
    ],

    "ceremonia_herbaty": [
        ("Cha", "Herbata"),
        ("Cha-ye", "Liście herbaty"),
        ("Lü-cha", "Zielona herbata"),
        ("Hong-cha", "Czarna herbata"),
        ("Wu-long", "Oolong"),
        ("Pu-er", "Pu-erh"),
        ("Bai-cha", "Biała herbata"),
        ("Hua-cha", "Herbata kwiatowa"),
        ("Mo-li-hua-cha", "Herbata jaśminowa"),
        ("Cha-hu", "Czajniczek do herbaty"),
        ("Cha-bei", "Filiżanka do herbaty"),
        ("Cha-wan", "Czarka do herbaty"),
        ("Cha-pan", "Taca do herbaty"),
        ("Cha-jin", "Ściereczka do herbaty"),
        ("Pao-cha", "Zaparzać herbatę"),
        ("Dao-cha", "Nalewać herbatę"),
        ("Pin-cha", "Degustować herbatę"),
        ("Wen-xiang", "Wąchać aromat"),
    ],

    "taktyki_wojenne": [
        ("Zhan", "Walka, bitwa"),
        ("Zhan-dou", "Walczyć"),
        ("Zhan-yi", "Kampania"),
        ("Zhan-lue", "Strategia"),
        ("Zhan-shu", "Taktyka"),
        ("Jin-gong", "Atakować"),
        ("Fang-shou", "Bronić się"),
        ("Xi-ji", "Zaatakować"),
        ("Tu-xi", "Zasadzka"),
        ("Mai-fu", "Czaić się w zasadzce"),
        ("Wei-gong", "Oblężenie"),
        ("Chong-feng", "Szarża"),
        ("Tui-que", "Odwrót"),
        ("Che-tui", "Wycofać się"),
        ("Tou-xiang", "Poddać się"),
        ("Sheng-li", "Zwycięstwo"),
        ("Bai", "Porażka"),
        ("Zhen", "Formacja bojowa"),
        ("Dui-xing", "Szyk bojowy"),
        ("Jun-dui", "Armia"),
        ("Bing", "Żołnierz"),
        ("Jiang-jun", "Generał"),
        ("Xiao-wei", "Kapitan"),
    ],

    "bron_szczegoly": [
        ("Jian", "Miecz prosty"),
        ("Dao", "Szabla"),
        ("Qiang", "Włócznia"),
        ("Ji", "Halabarda"),
        ("Fu", "Topór bojowy"),
        ("Yue", "Topór (szeroki)"),
        ("Chui", "Buzdygan"),
        ("Bian", "Bicz (broń)"),
        ("Jiu-jie-bian", "Bicz dziewięcioczłonowy"),
        ("Gun", "Kij"),
        ("Bang", "Pałka"),
        ("Gou", "Hak"),
        ("Shuang-gou", "Podwójne haki"),
        ("Sheng-biao", "Lina z grotem"),
        ("An-qi", "Ukryta broń"),
        ("Fei-dao", "Latający nóż"),
        ("Biao", "Rzutka"),
        ("Zhen", "Igły (broń)"),
    ],

    "zbroja_ochrona": [
        ("Jia", "Zbroja"),
        ("Kai-jia", "Zbroja (kompletna)"),
        ("Hu-xiong-jia", "Napierśnik"),
        ("Tou-kui", "Hełm"),
        ("Mian-ju", "Maska"),
        ("Hu-shou", "Naramienniki"),
        ("Hu-bi", "Naręcznice"),
        ("Hu-tui", "Nagolennice"),
        ("Dun", "Tarcza"),
        ("Pao", "Płaszcz (ochronny)"),
        ("Pi-feng", "Peleryna"),
    ],

    "konie_jazda": [
        ("Ma", "Koń"),
        ("Jun-ma", "Rumak"),
        ("Zhan-ma", "Koń bojowy"),
        ("Mu-ma", "Klacz"),
        ("Gong-ma", "Ogier"),
        ("Xiao-ma", "Źrebię"),
        ("Qi", "Jeździć (konno)"),
        ("Qi-ma", "Jeździć konno"),
        ("An", "Siodło"),
        ("Ma-an", "Siodło"),
        ("Jiang", "Wodze"),
        ("Ma-jiang", "Lejce"),
        ("Deng", "Strzemię"),
        ("Ma-deng", "Strzemiona"),
        ("Bian", "Bat"),
        ("Ma-bian", "Bat jeździecki"),
        ("Pao", "Biec galopem"),
        ("Chi", "Pędzić"),
        ("Man-zou", "Stępa"),
        ("Kuai-pao", "Kłus"),
    ],

    "statki_zegluga": [
        ("Chuan", "Łódź, statek"),
        ("Fan-chuan", "Żaglowiec"),
        ("Zhan-chuan", "Okręt wojenny"),
        ("Shang-chuan", "Statek handlowy"),
        ("Fan", "Żagiel"),
        ("Wei", "Ster"),
        ("Mao", "Kotwica"),
        ("Sheng", "Lina, cumowina"),
        ("Jiang", "Wiosło"),
        ("Hua", "Wiosłować"),
        ("Bo", "Cumować"),
        ("Qi-hang", "Wypłynąć"),
        ("Kao-an", "Dobić do brzegu"),
        ("Cheng-feng-po-lang", "Pływać po wietrze i falach"),
    ],

    "pieniadze_waluta": [
        ("Qian", "Pieniądze"),
        ("Yin", "Srebro"),
        ("Jin", "Złoto"),
        ("Tong", "Miedź"),
        ("Qian-bi", "Moneta"),
        ("Yin-piao", "Banknot srebrny"),
        ("Yuan-bao", "Sztabka srebra"),
        ("Tong-qian", "Moneta miedziana"),
        ("Wen", "Wen (drobna moneta)"),
        ("Liang", "Tael (jednostka srebra)"),
        ("Fu", "Bogaty"),
        ("Pin", "Biedny"),
        ("Cai-fu", "Bogactwo"),
    ],

    "gry_hazard": [
        ("Wan", "Bawić się, grać"),
        ("You-xi", "Gra"),
        ("Qi", "Weiqi (go)"),
        ("Xiang-qi", "Szachy chińskie"),
        ("Pai", "Karta do gry"),
        ("Ma-jiang", "Mahjong"),
        ("Tou-zi", "Kości"),
        ("Du", "Hazard"),
        ("Du-bo", "Uprawiać hazard"),
        ("Shu", "Przegrać"),
        ("Ying", "Wygrać"),
        ("Cai", "Zgadywać"),
        ("Cai-mi", "Zgadywanie zagadek"),
    ],
}

# ============================================================
# FUNKCJE POMOCNICZE (TAKIE SAME JAK W PART 5)
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

**Status:** {'✓ CEL OSIĄGNIĘTY!' if len(sorted_entries) >= 3000 else 'W TRAKCIE ROZBUDOWY'}

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
    print("GENERATOR SŁOWNIKA LENGXUAN - SPECJALISTYCZNA CZĘŚĆ 6")
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
        ("owady_ryby", "Owady i ryby"),
        ("rosliny_ziola_szczegoly", "Rośliny i zioła - Szczegóły"),
        ("choroby_symptomy", "Choroby i symptomy"),
        ("ruchy_gesty", "Ruchy i gesty"),
        ("pogoda_szczegoly", "Pogoda - Szczegóły"),
        ("rolnictwo", "Rolnictwo"),
        ("lowiectwo_rybolowstwo", "Łowiectwo i rybołówstwo"),
        ("tekstylia_szczegoly", "Tekstylia - Szczegóły"),
        ("czynnosci_domowe", "Czynności domowe"),
        ("dzieci_rodzina", "Dzieci i rodzina"),
        ("festiwale_ceremonie", "Festiwale i ceremonie"),
        ("przesady_wierzenia", "Przesądy i wierzenia"),
        ("poezja_literatura", "Poezja i literatura"),
        ("kaligrafia", "Kaligrafia"),
        ("ceremonia_herbaty", "Ceremonia herbaty"),
        ("taktyki_wojenne", "Taktyki wojenne"),
        ("bron_szczegoly", "Broń - Szczegóły"),
        ("zbroja_ochrona", "Zbroja i ochrona"),
        ("konie_jazda", "Konie i jazda konna"),
        ("statki_zegluga", "Statki i żegluga"),
        ("pieniadze_waluta", "Pieniądze i waluta"),
        ("gry_hazard", "Gry i hazard"),
    ]

    for cat_key, cat_name in categories:
        print(f"\nDodawanie kategorii: {cat_key}...")
        added, conflicts = add_category_to_dict(
            word_dict,
            cat_name,
            SPECIALIST_VOCABULARY[cat_key]
        )
        total_added += added
        total_conflicts += conflicts

    # Zapisz kompletny słownik
    print("\n" + "=" * 60)
    print(f"SPECJALISTYCZNA CZĘŚĆ 6 - SUMA: Dodano {total_added} nowych słów")
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
    else:
        print(f"\n  Cel (3000+): Brakuje {3000 - len(word_dict)} słów")

    print("=" * 60)
    print("\n" + "=" * 60)
    print("GOTOWE!")
    print("=" * 60)

if __name__ == "__main__":
    main()
