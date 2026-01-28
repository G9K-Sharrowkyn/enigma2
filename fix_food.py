#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unify food words under consistent semantic roots
Focus on real food items, skip false positives
"""

def create_food_mappings():
    """
    Create mappings for food words
    Keep mou- (cook) and da- (fry) families - they're already unified
    """
    
    mappings = {
        # MIĘSO - use 'rouo-' (肉 ròu = meat, modified)
        'ding': 'rouo',                    # mięso
        'yuan-piao': 'rouo-piao',          # wołowina
        'rua-cai': 'rouo-cai',             # wieprzowina
        'pen-de': 'rouo-de',               # baranina
        'rao-zeng': 'rouo-zeng',           # tłuste mięso
        # jio-nin (kurczak) - keep as animal family
        # tuo-jiang (królik mięso) - keep as animal family
        
        # WARZYWA - use 'cao-' (菜 cài = vegetable/dish, modified) → 'caio-'
        'fango': 'caio',                   # warzywo
        'zhao-dun': 'caio-dun',            # ziemniak
        'piao-ci-pian': 'caio-pian',       # marchew
        'guan-dou': 'caio-dou',            # kapusta chińska
        'kuai-zen': 'caio-zen',            # ogórek
        'pang-den': 'caio-den',            # pomidor
        'seng-zhong': 'caio-zhong',        # papryka chili
        'muo-kao': 'caio-kao',             # szpinak
        'de-zha': 'caio-zha',              # tofu
        'dong-er': 'caio-er',              # fasola, bob
        'shi-zi': 'caio-zi',               # fasola mung
        'xing-sheng': 'caio-sheng',        # fasola azuki
        'rui-huang': 'caio-huang',         # soja
        'yun-nen': 'caio-nen',             # ogórek morski
        
        # OWOCE - use 'guoo-' (果 guǒ = fruit, modified)
        'chi-shang': 'guoo-shang',         # jabłko
        'tuan-ye': 'guoo-ye',              # gruszka
        'mao-nuo': 'guoo-nuo',             # brzoskwinia
        'ga-biao': 'guoo-biao',            # morela
        'quan-long': 'guoo-long',          # wiśnia
        'zhang-le': 'guoo-le',             # truskawka
        'gua-gan': 'guoo-gan',             # banan
        'mi-can': 'guoo-can',              # arbuz
        'wen-ying': 'guoo-ying',           # melon zimowy
        'pa-en': 'guoo-en',                # pomarańcza/mandarynka
        'dui-gao': 'guoo-gao',             # skórka mandarynki
        'cang-ze': 'guoo-ze',              # cytryna
        # xie-long (kwiat granatu) - keep as flower family
        
        # ZBOŻA - Rice family: 'mio-' (米 mǐ = rice, modified) - CONFLICT with bee!
        # Use 'fano-' (饭 fàn = cooked rice/meal, modified)
        'dian': 'fano',                    # ryż
        'mou-jing': 'fano-jing',           # gotować ryż
        'mou-sheng': 'fano-sheng',         # gotowany ryż
        'de-jun': 'fano-jun',              # kongie, kleik ryżowy
        'guan-mou': 'fano-mou',            # pole ryżowe
        'ceng-ceng-dai': 'fano-dai',       # ryżowar
        # caoo-sun (roślina ryżowa) - keep as plant family
        
        # Bread/wheat - 'miano-' (面 miàn = flour/noodle, modified)
        'diao': 'miano',                   # chleb
        'cuan-piao': 'miano-piao',         # pszenica
        'lao-dui': 'miano-dui',            # makaron
        'mao-wu': 'miano-wu',              # makaron w zupie
        'da-zou': 'miano-zou',             # smażony makaron (keep da- prefix for frying)
        'diao-zhua': 'miano-zhua',         # siew ziarna
        
        # NABIAŁ - Milk: 'naio-' (奶 nǎi = milk, modified)
        'chao-ta': 'naio-ta',              # mleko
        'hang-bao': 'naio-bao',            # mleko sojowe
        
        # NAPOJE - keep individual words but unify families
        
        # Water - keep 'zhe' as is (good simple root)
        'zhan-heng': 'zhe-heng',           # wrzątek, gotowana woda
        
        # Tea - keep 'gango' as root, unify varieties
        'kuai-lao': 'gango-lao',           # zielona herbata
        'qiu-min': 'gango-min',            # czarna herbata
        'xia-eng': 'gango-eng',            # biała herbata
        'mai-suan-fa': 'gango-fa',         # herbata jaśminowa
        # xie-feng (herbata kwiatowa) - already in flower family
        
        # Wine - keep 'geng' as root
        'zeng-peng': 'geng-peng',          # alkohol, wino
        'xun-lian': 'geng-lian',           # winogrona
        
        # PRZYPRAWY - Spices: 'liao-' (料 liào = ingredient/spice, modified)
        'jue-rang': 'liao-rang',           # imbir
        'mie-nao': 'liao-nao',             # imbir świeży
        'da-yang': 'liao-yang',            # kora cynamonu
        'ou-shang': 'liao-shang',          # gałązki cynamonu
        'men-qia': 'liao-qia',             # anyż gwiaździsty
        'chuai-ci': 'liao-ci',             # goździk
        'zei-hua': 'liao-hua',             # pieprz syczuański
        
        # Sauce/oil - 'yoo-' (油 yóu = oil, modified)
        'que-xiao': 'yoo-xiao',            # sos sojowy
        'pi-biao': 'yoo-biao',             # ocet
        'rua-fang': 'yoo-fang',            # oleje
        'duo-zuo-a': 'yoo-a',              # olej sezamowy
        'xue-min-cuan': 'yoo-cuan',        # olej orzechowy
        'lang-xia': 'yoo-xia',             # dusić w sosie
        'tou-diao-xin': 'yoo-xin',         # słodki sos fasolowy
        
        # GOTOWANIE - keep mou- (cook) and da- (fry) families
        # Add cutting verbs - 'qiao-' (切 qiē = cut, modified)
        'cen-pao': 'qiao-pao',             # kroić
        'qi-ning': 'qiao-ning',            # kroić w paski
        'gou-zun': 'qiao-zun',             # kroić w plasterki
        'luan-hang': 'qiao-hang',          # kroić w kostkę
        'ban-xie': 'qiao-xie',             # siekać
        'hang-di': 'qiao-di',              # siekać na miazgę
        
        # Roasting - 'kaoo-' (烤 kǎo = roast, modified)
        'bin-jin': 'kaoo-jin',             # piec, grillować
        'rong-pai': 'kaoo-pai',            # pieczony
        
        # Braising - 'duo-' (炖 dùn = braise/stew, modified)
        'zong-ting': 'duo-ting',           # dusić powoli
        
        # Mix - 'bano-' (拌 bàn = mix, modified)
        'liang-xin': 'bano-xin',           # mieszać (składniki)
        
        # Prepare - 'beio-' (备 bèi = prepare, modified) - CONFLICT with sadness!
        # Use 'zhüo-' (准 zhǔn = prepare, modified) - CONFLICT with spider!
        # Use 'jio-' (备 different mod)
        'rang-diu': 'jio-diu',             # przygotowywać
        'jiu-shou': 'jio-shou',            # rezerwować, przygotować
        
        # Ready/fresh/raw
        'lou': 'zhüo',                     # gotowy (准 zhǔn)
        'pa-que': 'sheng',                 # surowy (生 shēng)
        # miao-seng (świeży) - already in fresh family
        
        # Meal types
        'nuan-sang': 'fano-sang',          # śniadanie (rice-family extended)
        'zhe-ni': 'fano-ni',               # kolacja
        'bian-chui': 'fano-chui',          # przekąska, przysmak
        
        # INNE - Food general
        'ji-deng': 'shio-deng',            # jedzenie (食 shí = food)
        'cai-dao': 'shio-dao',             # kuchnia
        
        # Taste - keep individual roots as they're basic adjectives
        # jun (słodki), kai (kwaśny), kano (gorzki), kao (słony), se-nu (pikantny)
        
        # Hunger - 'eo-' (饿 è = hungry, modified) - CONFLICT with crocodile!
        # Keep sen-zhua as is (already unique)
    }
    
    return mappings

def apply_food_fixes():
    """Apply food unification"""
    lp_path = 'Lengxuan_Language/03_Slownik/slownik_lengxuan_polski.md'
    pl_path = 'Lengxuan_Language/03_Slownik/slownik_polski_lengxuan.md'
    
    print("🍜 UNIFIKACJA JEDZENIA - ZADANIE 4/4\n")
    print("=" * 80)
    
    mappings = create_food_mappings()
    
    # Load dictionary
    lp_entries = {}
    with open(lp_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('- '):
                parts = line.strip().rsplit(' - ', 1)
                if len(parts) == 2:
                    code, polish = parts[0][2:], parts[1]
                    lp_entries[code] = polish
    
    print(f"\n📋 Zastępuję {len(mappings)} kodów jedzenia:\n")
    
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
                print(f"  {old_code:25} → {new_code:20} | {polish[:40]}")
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
    print("\n✅ JEDZENIE ZUNIFIKOWANE!")
    print("   Nowe rodziny semantyczne:")
    print("   MIĘSO:")
    print("     - rouo (mięso) - 5 słów")
    print("   WARZYWA:")
    print("     - caio (warzywo) - 14 słów")
    print("   OWOCE:")
    print("     - guoo (owoc) - 12 słów")
    print("   ZBOŻA:")
    print("     - fano (ryż) - 6 słów")
    print("     - miano (chleb/makaron) - 6 słów")
    print("   NABIAŁ:")
    print("     - naio (mleko) - 2 słowa")
    print("   NAPOJE:")
    print("     - zhe (woda) - 2 słowa")
    print("     - gango (herbata) - 5 słów")
    print("     - geng (wino) - 2 słowa")
    print("   PRZYPRAWY:")
    print("     - liao (przyprawa) - 7 słów")
    print("     - yoo (olej/sos) - 7 słów")
    print("   GOTOWANIE:")
    print("     + zachowano: mou (gotować) - 10 słów")
    print("     + zachowano: da (smażyć) - 5 słów")
    print("     - qiao (kroić) - 6 słów")
    print("     - kaoo (piec) - 2 słowa")
    print("     - duo (dusić) - 1 słowo")
    print("     - bano (mieszać) - 1 słowo")
    print("     - jio (przygotować) - 2 słowa")
    print("     - fano extended (posiłki) - 3 słowa")
    print("   INNE:")
    print("     - shio (jedzenie) - 2 słowa")

if __name__ == "__main__":
    apply_food_fixes()
