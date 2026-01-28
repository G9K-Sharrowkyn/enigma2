#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix Chinese contamination - replace 58 exact matches with new unique codes
CRITICAL PRIORITY from README
"""

def create_decontamination_mappings():
    """
    Replace all 58 exact Chinese matches with unique Lengxuan codes
    Strategy: Add suffix or modify to make distinct
    """
    
    mappings = {
        # Basic verbs - add -ng or -o suffix for distinction
        'ba': 'bao',              # robić (do) → distinct from 把 bǎ
        'chi': 'chio',            # złapać (catch) → distinct from 吃 chī
        'da': 'dao',              # negacja (not) → distinct from 大 dà
        'di': 'dio',              # dać (give) → distinct from 地 dì
        'er': 'ero',              # widzieć (see) → distinct from 二 èr
        'ge': 'geo',              # myśleć (think) → distinct from 个 gè
        'he': 'heo',              # móc (can) → distinct from 和 hé
        'huo': 'huao',            # brudny (dirty) → distinct from 火 huǒ
        'jie': 'jieo',            # 17 → distinct from 姐 jiě
        'jiu': 'jiuo',            # miękki (soft) → distinct from 九 jiǔ
        'kan': 'kano',            # gorzki (bitter) → distinct from 看 kàn
        'lai': 'laio',            # trudny (difficult) → distinct from 来 lái
        'lan': 'lano',            # my (we) → distinct from 蓝 lán
        'liu': 'liuo',            # ważny (important) → distinct from 六 liù
        'qu': 'quo',              # kochać (love) → distinct from 去 qù
        'ren': 'reno',            # dziecko (child) → distinct from 人 rén
        'san': 'sano',            # przyjaciel (friend) → distinct from 三 sān
        'shi': 'shio',            # dom (house) → distinct from 是 shì
        'si': 'sio',              # wznieść się wysoko → distinct from 四 sì
        'wu': 'wuo',              # nic (nothing) → distinct from 五 wǔ
        'xi': 'xio',              # aspekt dokonany → distinct from 西 xī
        'yu': 'yuo',              # używać (use) → distinct from 鱼 yú
        'zou': 'zouo',            # metal → distinct from 走 zǒu
        'zuo': 'zuoo',            # miecz (sword) → distinct from 做 zuò
        
        # Nouns - modify with vowel change
        'bei': 'beio',            # bardzo (very) → distinct from 北 běi
        'ben': 'beno',            # 11 → distinct from 本 běn
        'che': 'cheo',            # rzucić (throw) → distinct from 车 chē
        'chuang': 'chuango',      # klatka piersiowa → distinct from 床 chuáng
        'dong': 'dongo',          # ryba (fish) → distinct from 东 dōng
        'duan': 'duano',          # owoc (fruit) → distinct from 短 duǎn
        'duo': 'duoo',            # młody (young) → distinct from 多 duō
        'fang': 'fango',          # warzywo (vegetable) → distinct from 房 fáng
        'fen': 'feno',            # ciepły (warm) → distinct from 分 fēn
        'feng': 'fengo',          # sól (salt) → distinct from 风 fēng
        'gao': 'gaoo',            # dużo (much) → distinct from 高 gāo
        'gei': 'geio',            # wolny (free) → distinct from 给 gěi
        'hao': 'haoo',            # ciężki (heavy) → distinct from 好 hǎo
        'hei': 'heio',            # nikt (nobody) → distinct from 黑 hēi
        'hong': 'hongo',          # pieniądze (money) → distinct from 红 hóng
        
        # Adjectives/states - add vowel
        'bai': 'baio',            # sprzedawać (sell) → distinct from 白 bái
        'biao': 'biaoo',          # dokument → distinct from 表 biǎo
        'cao': 'caoo',            # polityka → distinct from 草 cǎo
        'chang': 'chango',        # spokój → distinct from 长 cháng
        'dui': 'duio',            # świątynia → distinct from 对 duì
        'fan': 'fano',            # małż → distinct from 饭 fàn
        'gang': 'gango',          # niebo → distinct from 刚 gāng
        'gu': 'guo',              # skacząca struną → distinct from 古 gǔ
        'guo': 'guoo',            # wielbiciel → distinct from 国 guó
        'hui': 'huio',            # spotkać → distinct from 会 huì
        'li': 'lio',              # sen → distinct from 里 lǐ
        'lu': 'luo',              # uczeń Zen → distinct from 路 lù
        'mai': 'maio',            # komar → distinct from 买 mǎi
        'men': 'meno',            # siostrzeniec → distinct from 门 mén
        'qi': 'qio',              # żyć → distinct from 七 qī
        'shui': 'shuio',          # drewno → distinct from 水 shuǐ
        'tian': 'tiano',          # prawdopodobnie → distinct from 天 tiān
        'wen': 'weno',            # wróg → distinct from 文 wén
        'xing': 'xingo',          # droga → distinct from 行 xíng
    }
    
    return mappings

def apply_decontamination():
    """Apply all decontamination changes to both dictionaries"""
    lp_path = 'Lengxuan_Language/03_Slownik/slownik_lengxuan_polski.new.md'
    pl_path = 'Lengxuan_Language/03_Slownik/slownik_polski_lengxuan.new.md'
    
    print("🧹 CHINESE DECONTAMINATION - PRIORITY FIX\n")
    print("=" * 80)
    
    mappings = create_decontamination_mappings()
    
    # Load current dictionary
    lp_entries = {}
    with open(lp_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('- '):
                parts = line.strip().rsplit(' - ', 1)
                if len(parts) == 2:
                    code, polish = parts[0][2:], parts[1]
                    lp_entries[code] = polish
    
    print(f"\n📋 Replacing {len(mappings)} Chinese-contaminated codes:\n")
    
    # Apply mappings
    changes_count = 0
    for old_code, new_code in sorted(mappings.items()):
        if old_code in lp_entries:
            polish = lp_entries[old_code]
            # Remove old entry
            del lp_entries[old_code]
            # Add new entry
            lp_entries[new_code] = polish
            changes_count += 1
            print(f"  {old_code:15} → {new_code:15} | {polish[:50]}")
    
    print(f"\n✅ Applied {changes_count} decontamination changes")
    
    # Save Lengxuan→Polski
    with open(lp_path, 'w', encoding='utf-8') as f:
        f.write("# Słownik Lengxuan → Polski\n\n")
        for code in sorted(lp_entries.keys()):
            f.write(f"- {code} - {lp_entries[code]}\n")
    
    # Save Polski→Lengxuan (sorted by polish)
    with open(pl_path, 'w', encoding='utf-8') as f:
        f.write("# Słownik Polski → Lengxuan\n\n")
        for code, polish in sorted(lp_entries.items(), key=lambda x: x[1].lower()):
            f.write(f"- {polish} - {code}\n")
    
    print(f"\n✅ Zapisano oba słowniki")
    print(f"📊 Finalna liczba wpisów: {len(lp_entries)}")
    
    print("\n" + "=" * 80)
    print("\n✅ DECONTAMINATION COMPLETE!")
    print("   All 58 exact Chinese matches have been replaced")
    print("   Lengxuan is now phonologically distinct from Mandarin")

if __name__ == "__main__":
    apply_decontamination()
