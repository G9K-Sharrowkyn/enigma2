#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unify animal words under consistent semantic roots
Only map actual animals, skip false positives
"""

def create_animal_mappings():
    """
    Create mappings for real animal words only
    """
    
    mappings = {
        # SSAKI - use 'shoo-' (兽 shòu = beast/mammal, modified)
        
        # DOG - 'gouo-' (狗 gǒu = dog, modified)
        'kuan': 'gouo',                    # pies
        
        # CAT - 'maoo-' (猫 māo = cat, modified)
        'lang': 'maoo',                    # kot
        
        # HORSE - 'mao-' root - CONFLICT with red!
        # Use 'pao-' (駢 pián horse, but modify to avoid confusion)
        'kuaio': 'pao',                    # koń
        'chao-shuo': 'pao-shuo',           # koń bojowy
        
        # PIG - 'zhuo-' (猪 zhū = pig, modified) - CONFLICT with bamboo!
        # Use 'tuno-' (豚 tún = pig/swine, modified)
        'dun-zhun': 'tuno-zhun',           # świnia
        
        # COW - 'niuo-' (牛 niú = cow/ox, modified)
        'fu-jun': 'niuo-jun',              # krowa
        'fang-wo': 'niuo-wo',              # bawół wodny
        
        # SHEEP/GOAT - 'yango-' (羊 yáng = sheep, modified)
        'neng-shang': 'yango-shang',       # owca
        'hai-sai': 'yango-sai',            # koza
        
        # RABBIT - 'tuo-' (兔 tù = rabbit, modified)
        'qian-jiang': 'tuo-jiang',         # królik (mięso)
        
        # MOUSE/RAT - 'shuo-' (鼠 shǔ = mouse/rat, modified) - CONFLICT with flood!
        # Use 'rao-' (鼠 shǔ but different mod)
        'die-mo': 'rao-mo',                # mysz, szczur
        'ca-fu': 'rao-fu',                 # szczur
        
        # MONKEY - 'houo-' (猴 hóu = monkey, modified)
        'he-nai': 'houo-nai',              # małpa
        
        # LION - 'shio-' (狮 shī = lion, modified) - CONFLICTS with wet/dry!
        # Use 'leo-' (different approach)
        'cun-run': 'leo-run',              # lew
        
        # TIGER - 'huo-' (虎 hǔ = tiger, modified) - CONFLICT with lake!
        # Use 'tigo-' (different)
        'miu-zen': 'tigo-zen',             # biały tygrys
        'xi-pai-lun': 'tigo-lun',          # lis używający tygrysiej siły
        'yao-ning-ge': 'tigo-ge',          # ukryty smok, czający się tygrys
        
        # BEAR - 'xiongo-' (熊 xióng = bear, modified)
        'mei-pei': 'xiongo-pei',           # niedźwiedź czarny
        
        # FOX - 'huo-' - CONFLICT!
        # Use 'hulo-' (狐 hú = fox, different mod)
        'du-bi': 'hulo-bi',                # lis
        
        # WOLF - 'lango-' (狼 láng = wolf, modified) - CONFLICT with cat!
        # Use 'laio-' (different)
        'yao-lie': 'laio-lie',             # wilk
        
        # DEER - 'luo-' (鹿 lù = deer, modified)
        'er-nie': 'luo-nie',               # jeleń
        
        # ELEPHANT - 'xio-' (象 xiàng = elephant, modified)
        'xiang': 'xio',                    # słoń
        
        # LIZARD - 'xio-' - CONFLICT with elephant!
        # Use 'sheo-' (蜥 xī = lizard, modified)
        'an-shi': 'sheo-shi',              # jaszczurka ścienna
        'mian-hua': 'sheo-hua',            # jaszczurka
        
        # PTAKI - use 'niao-' (鸟 niǎo = bird, modified)
        
        # General bird
        'leng': 'niao',                    # ptak
        'fu-xue': 'niao-xue',              # ptak latający
        
        # HAWK - 'yingo-' (鹰 yīng = hawk/eagle, modified)
        'ang-tou': 'yingo-tou',            # jastrząb, sokół
        
        # DUCK - 'yao-' (鸭 yā = duck, modified)
        'bi-ma': 'yao-ma',                 # kaczka mandarynka
        'chan-nong': 'yao-nong',           # kaczka
        
        # CHICKEN - 'jio-' (鸡 jī = chicken, modified)
        'du-nin': 'jio-nin',               # kurczak
        'zai-zhun': 'jio-zhun',            # kura
        'tan-ruan': 'jio-ruan',            # jajko kurze
        
        # DOVE - 'geo-' (鸽 gē = dove/pigeon, modified)
        'shu-ku': 'geo-ku',                # gołąb
        
        # CROW - 'wuo-' (乌 wū = crow, modified) - CONFLICT with fog!
        # Use 'yao-' (鸦 yā = crow, different from duck)
        'mei-bu': 'yao-bu',                # kruk czarny
        
        # SWALLOW - 'yano-' (燕 yàn = swallow, modified) - CONFLICT with rock!
        # Use 'yeno-' (different)
        'mo-cou': 'yeno-cou',              # jaskółka
        
        # PARROT - 'yingo-' (鹦 yīng = parrot, modified) - CONFLICT with hawk!
        # Use 'wuo-' (鹉 wǔ = parrot part, modified)
        'o-yong': 'wuo-yong',              # papuga
        
        # MAGPIE - 'quo-' (鹊 què = magpie, modified) - CONFLICT with love!
        # Use 'queo-' (different)
        'yue-zha': 'queo-zha',             # sroka
        
        # SPARROW - 'queo-' extended
        'zhua-ju': 'queo-ju',              # wróbel
        
        # OWL - 'xiao-' (鸮 xiāo = owl, modified) - CONFLICT with tree!
        # Use 'maoo-' (鸮 different reading) - CONFLICT with cat!
        # Use 'yao-' (鸮 yāo)
        'xia-neng-mao': 'yaoo-mao',        # sowa
        
        # RYBY - use 'yuo-' (鱼 yú = fish, modified) - CONFLICT with rain!
        # Use 'yü-' → 'yuo' but different tone marker → 'yüo'
        
        # General fish - keep 'dongo-' (already good root)
        
        # CARP - 'lino-' (鲤 lǐ = carp, modified) - CONFLICT with forest!
        # Use 'lio-' (different)
        'gao-de': 'lio-de',                # karp
        
        # MANDARIN FISH - extend dongo-
        'ai-kui': 'dongo-kui',             # ryba mandarynka
        
        # GOLDFISH - extend dongo-
        'dan-che': 'dongo-che',            # złota rybka
        
        # SHARK - 'shao-' (鲨 shā = shark, modified) - CONFLICT with sand!
        # Use 'sharo-' (different)
        'kua-zha': 'sharo-zha',            # rekin
        
        # LOBSTER - 'longo-' (龙 lóng = dragon/lobster, modified) - many conflicts!
        # Use 'xiao-' (虾 xiā = shrimp, modified) extended
        'bi-zhen': 'xiao-zhen',            # homar
        
        # JELLYFISH - 'zheo-' (蜇 zhé = jellyfish, modified)
        'diao-kua': 'zheo-kua',            # meduza
        
        # OCTOPUS - 'zhango-' (章 zhāng = octopus, modified)
        'ni-tong': 'zhango-tong',          # ośmiornica
        
        # DOLPHIN - 'tuno-' (豚 tún = dolphin, modified) - CONFLICT with pig!
        # Use 'haio-' extended (ocean family)
        'ning-qiu': 'haio-qiu',            # delfin
        
        # WHALE - 'haio-' extended
        'yang-kai': 'haio-kai',            # wieloryb
        
        # COD - 'xueo-' (雪 xuě = snow/cod, modified) - CONFLICT with snow!
        # Use 'dongo-' extended
        'nou-zhang-huan': 'dongo-huan',    # dorsz żółty
        
        # CRAB - 'xio-' (蟹 xiè = crab, modified) - CONFLICT with elephant!
        # Use 'paoo-' (螃 páng = crab part)
        'yi-ka': 'paoo-ka',                # krab
        
        # SHRIMP - use base 'xiao-'
        'zhua-lun': 'xiao-lun',            # krewetka
        
        # SHELL - 'beo-' (贝 bèi = shell, modified)
        'zhe-za': 'beo-za',                # muszla, skorupiak
        
        # FISHERMAN - 'haio-' extended
        'hai-seng': 'haio-seng',           # rybak
        'nun-men': 'haio-men',             # łódź rybacka
        'tan-wei': 'haio-wei',             # łowić ryby
        'gei-chen': 'haio-chen',           # sieć rybacka
        
        # OWADY - use 'chongo-' (虫 chóng = insect, modified)
        
        # General insect
        'jing-hang': 'chongo',             # owad
        
        # BEE - 'fengo-' (蜂 fēng = bee, modified) - CONFLICT with wind!
        # Use 'mio-' (蜜 mì = honey/bee)
        'fu-zou': 'mio-zou',               # pszczoła
        
        # WASP - 'fengo-' extended → 'mio-' extended
        'kuo-xiu': 'mio-xiu',              # osa
        
        # ANT - 'mao-' (蚂 mǎ = ant, modified) - CONFLICT with red!
        # Use 'yio-' (蚁 yǐ = ant)
        'ruan-qiong': 'yio-qiong',         # mrówka
        
        # BUTTERFLY - 'dieo-' (蝶 dié = butterfly, modified)
        'min-mao': 'dieo-mao',             # motyl
        
        # CRICKET - 'xio-' (蟋 xī = cricket, modified) - many conflicts!
        # Use 'shuo-' (蟀 shuài = cricket)
        'nin-reng': 'shuo-reng',           # świerszcz
        
        # SPIDER - 'zhio-' (蛛 zhū = spider, modified) - CONFLICT with stone/branch!
        # Use 'zhüo-' (different)
        'nun-ceng': 'zhüo-ceng',           # pająk
        
        # GADY - use 'sheo-' already used for lizard
        
        # SNAKE - 'sheo-' (蛇 shé = snake, modified)
        'cu-xie': 'sheo-xie',              # wąż
        'tou-shuo': 'sheo-shuo',           # jadowity wąż
        'mei-da': 'sheo-da',               # czarny wojownik, żółw i wąż
        
        # TURTLE - 'guio-' (龟 guī = turtle, modified)
        'xing-yao': 'guio-yao',            # żółw
        'cao-cuan': 'guio-cuan',           # żółw błotny
        'lian-chan': 'guio-chan',          # smoczy żółw
        'yang-ang': 'guio-ang',            # żółwia prędkość
        
        # DRAGON - keep 'lian-' (already exists and is good)
        # Extend:
        'bao-zei': 'lian-zei',             # lazurowy smok
        'yi-jue': 'lian-jue',              # król smoków
        
        # CROCODILE - 'eo-' (鳄 è = crocodile, modified)
        'liao-ca': 'eo-ca',                # krokodyl
        
        # PŁAZY - use 'wao-' (蛙 wā = frog, modified)
        'ca-fen': 'wao-fen',               # ropucha
        
        # INNE - animals general
        # Keep as is or use 'dongo-' (动 dòng = move/animal, modified)
        'nano-ta': 'dongo-ta',             # dzikie zwierzę
        'tao-bao': 'dongo-bao',            # zwierzę domowe
        'mang-kao-xiang': 'dongo-xiang',   # zwierzęta
        'chi-jing-shui': 'dongo-shui',     # dzikie zwierzęta
        'lin-xie-re': 'dongo-re',          # świat zwierząt
        'die-zhao-cheng': 'dongo-cheng',   # zwierzęta zagrożone
        'pen-nuo-lian': 'dongo-lian',      # zwierzęta wymarłe
        'zen-kao': 'dongo-kao',            # mityczne zwierzę
    }
    
    return mappings

def apply_animal_fixes():
    """Apply animal unification"""
    lp_path = 'Lengxuan_Language/03_Slownik/slownik_lengxuan_polski.md'
    pl_path = 'Lengxuan_Language/03_Slownik/slownik_polski_lengxuan.md'
    
    print("🐾 UNIFIKACJA ZWIERZĄT - ZADANIE 3/4\n")
    print("=" * 80)
    
    mappings = create_animal_mappings()
    
    # Load dictionary
    lp_entries = {}
    with open(lp_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('- '):
                parts = line.strip().rsplit(' - ', 1)
                if len(parts) == 2:
                    code, polish = parts[0][2:], parts[1]
                    lp_entries[code] = polish
    
    print(f"\n📋 Zastępuję {len(mappings)} kodów zwierząt:\n")
    
    # Apply mappings
    changes_count = 0
    not_found = []
    
    for old_code, new_code in sorted(mappings.items()):
        if old_code in lp_entries:
            polish = lp_entries[old_code]
            del lp_entries[old_code]
            lp_entries[new_code] = polish
            changes_count += 1
            if changes_count <= 30:
                print(f"  {old_code:20} → {new_code:20} | {polish[:50]}")
        else:
            not_found.append(old_code)
    
    if changes_count > 30:
        print(f"  ... (pokazano 30 z {changes_count} zmian)")
    
    if not_found:
        print(f"\n⚠️  NIE ZNALEZIONO {len(not_found)} kodów")
    
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
    print("\n✅ ZWIERZĘTA ZUNIFIKOWANE!")
    print("   Nowe rodziny semantyczne:")
    print("   SSAKI:")
    print("     - gouo (pies) - 1 słowo")
    print("     - maoo (kot) - 1 słowo")
    print("     - pao (koń) - 2 słowa")
    print("     - tuno (świnia) - 1 słowo")
    print("     - niuo (krowa/bawół) - 2 słowa")
    print("     - yango (owca/koza) - 2 słowa")
    print("     - tuo (królik) - 1 słowo")
    print("     - rao (mysz/szczur) - 2 słowa")
    print("     - houo (małpa) - 1 słowo")
    print("     - leo (lew) - 1 słowo")
    print("     - tigo (tygrys) - 3 słowa")
    print("     - xiongo (niedźwiedź) - 1 słowo")
    print("     - hulo (lis) - 1 słowo")
    print("     - laio (wilk) - 1 słowo")
    print("     - luo (jeleń) - 1 słowo")
    print("     - xio (słoń) - 1 słowo")
    print("     - sheo (jaszczurka) - 2 słowa")
    print("   PTAKI:")
    print("     - niao (ptak) - 2 słowa")
    print("     - yingo (jastrząb) - 1 słowo")
    print("     - yao (kaczka) - 2 słowa")
    print("     - jio (kurczak/kura) - 3 słowa")
    print("     - geo (gołąb) - 1 słowo")
    print("     - yao (kruk) - 1 słowo")
    print("     - yeno (jaskółka) - 1 słowo")
    print("     - wuo (papuga) - 1 słowo")
    print("     - queo (sroka/wróbel) - 2 słowa")
    print("     - yaoo (sowa) - 1 słowo")
    print("   RYBY:")
    print("     - dongo (ryba) - 3 słowa + rybacy")
    print("     - lio (karp) - 1 słowo")
    print("     - sharo (rekin) - 1 słowo")
    print("     - xiao (homar/krewetka) - 2 słowa")
    print("     - zheo (meduza) - 1 słowo")
    print("     - zhango (ośmiornica) - 1 słowo")
    print("     - haio (delfin/wieloryb) + rybactwo - 6 słów")
    print("     - paoo (krab) - 1 słowo")
    print("     - beo (muszla) - 1 słowo")
    print("   OWADY:")
    print("     - chongo (owad) - 1 słowo")
    print("     - mio (pszczoła/osa) - 2 słowa")
    print("     - yio (mrówka) - 1 słowo")
    print("     - dieo (motyl) - 1 słowo")
    print("     - shuo (świerszcz) - 1 słowo")
    print("     - zhüo (pająk) - 1 słowo")
    print("   GADY:")
    print("     - sheo (wąż) - 3 słowa")
    print("     - guio (żółw) - 4 słowa")
    print("     - lian (smok) - 3 słowa")
    print("     - eo (krokodyl) - 1 słowo")
    print("   PŁAZY:")
    print("     - wao (ropucha) - 1 słowo")
    print("   OGÓLNE:")
    print("     - dongo (zwierzę) - 8 słów")

if __name__ == "__main__":
    apply_animal_fixes()
