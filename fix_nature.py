#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unify nature/weather words under consistent semantic roots
Strategy: Create clear semantic families for 5 categories
"""

def create_nature_mappings():
    """
    Create mappings for 149 nature/weather words
    New semantic families based on classical Chinese phonology but modified
    """
    
    mappings = {
        # POGODA - split into subcategories with clear roots
        
        # ATMOSPHERIC - 'tiano-' (天 tiān = sky, but modified)
        'xue': 'tiano',                    # niebo
        'tun-lian': 'tiano-lian',          # chmura
        'ao-gou': 'tiano-gou',             # częściowo pochmurnie
        'lei-peng': 'tiano-peng',          # pochmurny dzień
        
        # SUN/MOON/STARS - 'guango-' (光 guāng = light, modified)
        'yin': 'guango',                   # słońce
        'youo': 'guango-yo',               # księżyc
        'yuno': 'guango-no',               # gwiazda
        'wu-peng': 'guango-peng',          # kalendarz księżycowy
        'ka-qia': 'guango-qia',            # rozgwiazda
        'hang-sun': 'guango-sun',          # meteor
        'mie-die': 'guango-die',           # wega (gwiazda)
        'pin-ao': 'guango-ao',             # syriusz
        'ru-ku': 'guango-ku',              # altair
        
        # RAIN - 'yuo-' (雨 yǔ = rain, modified)
        'zao': 'yuo',                      # deszcz
        'miao-ke': 'yuo-ke',               # mały deszcz
        'keng-tong': 'yuo-tong',           # duży deszcz
        'qi-pang': 'yuo-pang',             # ulewny deszcz
        'qu-ben': 'yuo-ben',               # deszcz zbóż
        'geng-ming': 'yuo-ming',           # deszczowy dzień
        'chuai-nen': 'yuo-nen',            # padać (śnieg)
        
        # SNOW - 'xueo-' (雪 xuě = snow, modified)
        'zei': 'xueo',                     # śnieg
        'rong-bai': 'xueo-bai',            # mały śnieg
        
        # WIND - 'fengo-' (风 fēng = wind, modified)
        'zai': 'fengo',                    # wiatr
        'run-zei': 'fengo-zei',            # lekki wiatr
        'sao-tun': 'fengo-tun',            # silny wiatr
        'rui-kuo': 'fengo-kuo',            # prędkość wiatru
        'en-ei': 'fengo-ei',               # kierunek wiatru
        'ling-ni': 'fengo-ni',             # świst wiatru
        'jie-zhi': 'fengo-zhi',            # pod wiatr
        'liu-bi': 'fengo-bi',              # z wiatrem
        'bei-zhao': 'fengo-zhao',          # patogen wiatru
        
        # STORM - 'baoo-' (暴 bào = storm, modified)
        'ran-ka': 'baoo-ka',               # burza
        'sui-xu': 'baoo-xu',               # burza z piorunami
        
        # TEMPERATURE - 'weno-' (温 wēn = temperature, modified)
        'can-keng': 'weno-keng',           # temperatura
        'eng': 'weno-eng',                 # gorący
        'fei': 'weno-fei',                 # zimny
        'feno': 'weno-feno',               # ciepły
        'fou': 'weno-fou',                 # chłodny
        
        # WEATHER - 'qio-' (气 qì = air/weather, modified)
        'meng-tui': 'qio-tui',             # pogoda
        'qu-zhen': 'qio-zhen',             # klimat
        'yue-yu-en': 'qio-yu-en',          # globalne ocieplenie
        'zi-dao-na': 'qio-dao-na',         # zmiana klimatu
        
        # FOG/MIST - 'wuo-' (雾 wù = fog, modified)
        'gu-shi': 'wuo-shi',               # mgła i opary
        'gen-jiao': 'wuo-jiao',            # zimna rosa
        
        # Energy/syndrome - 'qio-' family extended
        'fa-gen': 'qio-gen',               # gorąca energia
        'neng-zui': 'qio-zui',             # wilgotna energia
        'ling-sou': 'qio-sou',             # sucha energia
        'yin-bao': 'qio-bao',              # zimna energia
        'tan-tong': 'qio-tong',            # syndrom zimna
        'pie-mian': 'qio-mian',            # syndrom gorąca
        'gei-song': 'qio-song',            # gorąco płuc
        'jin-shi': 'qio-shi',              # mieć gorączkę
        'liang-miao': 'qio-miao',          # patogen suchości
        
        # Wet/dry - 'shio-' (湿 shī = wet, modified)
        'bing-wai': 'shio-wai',            # wilgotny, mokry
        'si-ge': 'shio-ge',                # suchy
        'da-cheng': 'shio-cheng',          # smażyć do sucha
        'fo-sun': 'shio-sun',              # wytrzeć do sucha
        'han-wai': 'shio-han',             # dmuchać (na gorące)
        
        # ROŚLINY - split into clear categories
        
        # TREE - keep 'xiaoo-' as root (already exists)
        # (no changes needed - xiaoo is good)
        
        # FLOWER - keep 'xie-' as root (already exists)
        # Add variants:
        'dei-gun': 'xie-gun',              # kwiat brzoskwini
        'kua-bie': 'xie-bie',              # kwiat gruszy
        'tai-nuo': 'xie-nuo',              # kwiat moreli
        'xuan-die': 'xie-die',             # kwiat śliwy
        'ying-hua': 'xie-hua',             # kwiat wiśni
        'shai-ting': 'xie-ting',           # kwiat bambusa
        'huan-dei-long': 'xie-long',       # kwiat granatu
        'pu-feng': 'xie-feng',             # herbata kwiatowa
        'bie-ga': 'xie-ga',                # pyłek kwiatowy
        'geng-leng': 'xie-leng',           # kwiaty i trawy
        
        # LEAF - keep 'xiu-' as root
        # (no changes - xiu is good)
        
        # GRASS - keep 'xino-' as root
        # Extend:
        'nano-liu': 'xino-liu',            # zielona trawa
        'zao-piao': 'xino-piao',           # dzika trawa
        
        # FOREST - keep 'weno-' root BUT CONFLICT with weather 'weno'!
        # Change forest to 'lino-' (林 lín = forest, modified)
        'weno': 'lino',                    # las
        
        # FRUIT - keep 'duano-' as root
        # Extend:
        'zai-sai': 'duano-sai',            # miąższ owocu
        'duan-ri': 'duano-ri',             # skórka owocu
        'nu-meng': 'duano-meng',           # owocowy zapach
        
        # ROOT (botaniczny) - 'geno-' (根 gēn = root, modified)
        'cang-suo': 'geno-suo',            # korzeń
        'nao-du': 'geno-du',               # korzeń drzewa
        
        # SEED - 'zhono-' (种 zhǒng = seed, modified)
        'pian-chan': 'zhono-chan',         # nasiono
        'bi-qia': 'zhono-qia',             # nasiona lotosu
        
        # BRANCH - 'zhio-' (枝 zhī = branch, modified)
        'ming-ta': 'zhio-ta',              # gałąź
        
        # BAMBOO - 'zhuo-' (竹 zhú = bamboo, modified)
        'yi-ming': 'zhuo-ming',            # bambus
        'la-ce': 'zhuo-ce',                # flet bambusowy
        'men-gei': 'zhuo-gei',             # zagajnik bambusowy
        'qian-mang': 'zhuo-mang',          # bambusa rdzawa
        'rang-sun-que': 'zhuo-que',        # bambus łzawy
        
        # PINE - 'songo-' (松 sōng = pine, modified)
        'pian-jiu': 'songo-jiu',           # sosna
        
        # SANDAL TREE - 'tano-' (檀 tán = sandalwood, modified)
        'kun-kan': 'tano-kan',             # drzewo sandałowe
        
        # PLANT - 'zhio-' (植 zhí = plant, modified) - CONFLICT with branch!
        # Use 'cao-' (草 cǎo = grass/plant, modified) → 'caoo-'
        'keng-chui': 'caoo-chui',          # roślina
        'dao-cuo': 'caoo-cuo',             # indygo (roślina)
        'za-sun': 'caoo-sun',              # roślina ryżowa
        
        # Keep nano-hong as is (wapień = limestone, not plant)
        
        # KRAJOBRAZ
        
        # MOUNTAIN - 'shano-' (山 shān = mountain, modified)
        'tun': 'shano',                    # góra
        'shu-sun': 'shano-sun',            # brama góry (klasztoru)
        
        # RIVER - 'heo-' (河 hé = river, modified)
        'tuo': 'heo',                      # rzeka
        'sui-ha': 'heo-ha',                # jadeitowa Rzeka
        'mao-yue': 'heo-yue',              # brzeg rzeki
        
        # LAKE - 'huo-' (湖 hú = lake, modified)
        'wai': 'huo',                      # jezioro
        
        # SEA - 'haio-' (海 hǎi = sea, modified)
        'wei': 'haio',                     # morze
        'zan-ye': 'haio-ye',               # ocean
        'lou-dang': 'haio-dang',           # wyspa morska
        'nei-mei': 'haio-mei',             # wyspa
        'tu-lai': 'haio-lai',              # półwysep
        'yun-qin': 'haio-qin',             # wybrzeże
        'mie-ri': 'haio-ri',               # zatoka
        'meng-mo': 'haio-mo',              # plaża
        'mao-que': 'haio-que',             # dobić do brzegu
        
        # VALLEY - 'guo-' (谷 gǔ = valley, modified)
        'sa-guang': 'guo-guang',           # dolina
        
        # PLAIN - 'pingo-' (平 píng = plain, modified)
        'rao-qiang': 'pingo-qiang',        # równina
        
        # WATERFALL - 'puo-' (瀑 pù = waterfall, modified)
        'gou-liao': 'puo-liao',            # wodospad
        
        # SPRING/SOURCE - 'yuano-' (源 yuán = source, modified)
        'bian-seng': 'yuano-seng',         # źródło
        
        # CLIFF - 'yao-' (崖 yá = cliff, modified)
        'en-xiang': 'yao-xiang',           # urwisko
        
        # ROCK - 'shio-' (石 shí = rock/stone, modified) - CONFLICT with wet/dry!
        # Use 'yano-' (岩 yán = rock, modified)
        'jing-tian': 'yano-tian',          # skała
        
        # ZIEMIA
        
        # EARTH/LAND - keep 'yan-' as simple root
        # (no changes - yan is good)
        
        # STONE - keep 'zhio-' as root
        # Extend:
        'gao-jiao': 'zhio-jiao',           # kamień do rozcierania tuszu
        'zhe-chu-o': 'zhio-chu-o',         # cztery skarby gabinetu
        
        # SAND - 'shao-' (沙 shā = sand, modified)
        'zhu': 'shao',                     # piasek
        
        # ARABLE LAND - 'tiano-' - CONFLICT with sky!
        # Use 'diio-' (地 dì = earth/land, modified)
        'run-rui': 'diio-rui',             # ziemia orna
        
        # ZJAWISKA
        
        # LIGHTNING - 'diano-' (电 diàn = lightning/electricity, modified)
        'an-guo': 'diano-guo',             # błyskawica
        'chen-zu-qiong': 'diano-qiong',    # błyskawiczny
        
        # RAINBOW - 'hongo-' (虹 hóng = rainbow, modified)
        'pang-ang': 'hongo-ang',           # tęcza
        'zhi-mou': 'hongo-mou',            # podwójna tęcza
        
        # EARTHQUAKE - 'zheno-' (震 zhèn = shake/quake, modified)
        'lei-nuan': 'zheno-nuan',          # trzęsienie ziemi
        
        # VOLCANO - 'huoo-' (火 huǒ = fire, modified)
        'du-ying': 'huoo-ying',            # wulkan
        
        # TSUNAMI - 'haio-' family extended
        'niu-qu': 'haio-qu',               # tsunami
        
        # TYPHOON - 'fengo-' family extended (wind-related)
        'jiao-chou': 'fengo-chou',         # tajfun
        'luan-lou-de': 'fengo-de',         # tornado
        
        # FLOOD - 'shuo-' (水 shuǐ = water, modified)
        'sui-shuang': 'shuo-shuang',       # powódź
        
        # DROUGHT - 'hano-' (旱 hàn = drought, modified)
        'lue-tian': 'hano-tian',           # susza
    }
    
    return mappings

def apply_nature_fixes():
    """Apply nature/weather unification"""
    lp_path = 'Lengxuan_Language/03_Slownik/slownik_lengxuan_polski.md'
    pl_path = 'Lengxuan_Language/03_Slownik/slownik_polski_lengxuan.md'
    
    print("🌍 UNIFIKACJA PRZYRODY - ZADANIE 2/4\n")
    print("=" * 80)
    
    mappings = create_nature_mappings()
    
    # Load dictionary
    lp_entries = {}
    with open(lp_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('- '):
                parts = line.strip().rsplit(' - ', 1)
                if len(parts) == 2:
                    code, polish = parts[0][2:], parts[1]
                    lp_entries[code] = polish
    
    print(f"\n📋 Zastępuję {len(mappings)} kodów przyrody/pogody:\n")
    
    # Apply mappings
    changes_count = 0
    not_found = []
    
    for old_code, new_code in sorted(mappings.items()):
        if old_code in lp_entries:
            polish = lp_entries[old_code]
            del lp_entries[old_code]
            lp_entries[new_code] = polish
            changes_count += 1
            if changes_count <= 30:  # Show first 30
                print(f"  {old_code:20} → {new_code:20} | {polish[:50]}")
        else:
            not_found.append(old_code)
    
    if changes_count > 30:
        print(f"  ... (pokazano 30 z {changes_count} zmian)")
    
    if not_found:
        print(f"\n⚠️  NIE ZNALEZIONO {len(not_found)} kodów:")
        for code in not_found[:10]:
            print(f"    {code}")
        if len(not_found) > 10:
            print(f"    ... (i {len(not_found)-10} innych)")
    
    print(f"\n✅ Zastosowano {changes_count} zmian")
    
    # Save both dictionaries
    with open(lp_path, 'w', encoding='utf-8') as f:
        f.write("# Słownik Lengxuan → Polski\n\n")
        for code in sorted(lp_entries.keys()):
            f.write(f"- {code} - {lp_entries[code]}\n")
    
    with open(pl_path, 'w', encoding='utf-8') as f:
        f.write("# Słownik Polski → Lengxuan\n\n")
        for code, polish in sorted(lp_entries.items(), key=lambda x: x[1].lower()):
            f.write(f"- {polish} - {code}\n")
    
    print(f"\n✅ Zapisano oba słowniki")
    print(f"📊 Liczba wpisów: {len(lp_entries)}")
    
    print("\n" + "=" * 80)
    print("\n✅ PRZYRODA ZUNIFIKOWANA!")
    print("   Nowe rodziny semantyczne:")
    print("   POGODA:")
    print("     - tiano (niebo/chmury) - 4 słowa")
    print("     - guango (światło: słońce/księżyc/gwiazdy) - 9 słów")
    print("     - yuo (deszcz) - 7 słów")
    print("     - xueo (śnieg) - 2 słowa")
    print("     - fengo (wiatr) - 11 słów")
    print("     - baoo (burza) - 2 słowa")
    print("     - weno (temperatura) - 5 słów")
    print("     - qio (pogoda/klimat/energia) - 13 słów")
    print("     - wuo (mgła) - 2 słowa")
    print("     - shio (mokry/suchy) - 5 słów")
    print("   ROŚLINY:")
    print("     - xie (kwiat) - 10 słów")
    print("     - xino (trawa) - 3 słowa")
    print("     - lino (las) - 1 słowo")
    print("     - duano (owoc) - 4 słowa")
    print("     - geno (korzeń) - 2 słowa")
    print("     - zhono (nasiono) - 2 słowa")
    print("     - zhio (gałąź) - 1 słowo")
    print("     - zhuo (bambus) - 5 słów")
    print("     - songo (sosna) - 1 słowo")
    print("     - tano (sandał) - 1 słowo")
    print("     - caoo (roślina) - 3 słowa")
    print("   KRAJOBRAZ:")
    print("     - shano (góra) - 2 słowa")
    print("     - heo (rzeka) - 3 słowa")
    print("     - huo (jezioro) - 1 słowo")
    print("     - haio (morze/ocean/wyspa) - 9 słów")
    print("     - guo (dolina) - 1 słowo")
    print("     - pingo (równina) - 1 słowo")
    print("     - puo (wodospad) - 1 słowo")
    print("     - yuano (źródło) - 1 słowo")
    print("     - yao (urwisko) - 1 słowo")
    print("     - yano (skała) - 1 słowo")
    print("   ZIEMIA:")
    print("     - zhio (kamień) - 3 słowa")
    print("     - shao (piasek) - 1 słowo")
    print("     - diio (ziemia orna) - 1 słowo")
    print("   ZJAWISKA:")
    print("     - diano (błyskawica) - 2 słowa")
    print("     - hongo (tęcza) - 2 słowa")
    print("     - zheno (trzęsienie ziemi) - 1 słowo")
    print("     - huoo (wulkan) - 1 słowo")
    print("     - shuo (powódź) - 1 słowo")
    print("     - hano (susza) - 1 słowo")
    print("   + rozszerzono: haio (tsunami), fengo (tajfun/tornado)")

if __name__ == "__main__":
    apply_nature_fixes()
