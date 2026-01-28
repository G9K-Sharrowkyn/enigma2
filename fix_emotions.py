#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unify emotion words under consistent semantic roots
Strategy: Keep existing good families, unify scattered words
"""

def create_emotion_mappings():
    """
    Create mappings for emotion words
    Keep what works, unify what's scattered
    """
    
    mappings = {
        # SZCZĘŚCIE/RADOŚĆ - use 'huan-' root (but modify to avoid 欢 huān)
        # Keep: tao-* (śmiać się family - already unified)
        # Unify others under 'huano-' (modified to avoid contamination)
        'ca-zang': 'huano',              # szczęście
        'guan-wang': 'huano-wang',       # radość, szczęście
        'mang-tai': 'huano-tai',         # szczęśliwy, wesoły
        'jie-kui': 'huano-kui',          # zadowolenie, satysfakcja
        'miao-zhang': 'huano-zhang',     # zadowolony
        
        # SMUTEK/ŻAL - use 'beio-' root (modified from 悲 bēi = sorrow)
        'ke-zhang': 'beio-zhang',        # smutek, zmartwienie
        'ke-nian': 'beio-nian',          # smutny
        'ke-shuo': 'beio-shuo',          # żałoba
        'kan-mou': 'beio-mou',           # żal, skrucha
        'dia-dei': 'beio-dei',           # rozpacz
        'luan-miu': 'beio-miu',          # płakać, łkać
        'luan-zhua': 'beio-zhua',        # ronić łzy
        
        # GNIEW/ZŁOŚĆ - use 'nuo-' root (modified to avoid 怒 nù)
        'song-dun': 'nuo-dun',           # gniew
        'dei': 'nuo',                    # zły
        'zeng-dong': 'nuo-dong',         # irytacja
        
        # STRACH/LĘK - keep 'ru-' family (already consistent: ru, ru-she)
        # Unify others
        'dai-pin': 'ru-pin',             # obawa
        'shai-bie': 'ru-bie',            # panika
        
        # SPOKÓJ/HARMONIA - use 'ango-' root (modified from 安 ān = peace)
        'pai': 'ango',                   # spokojny
        'long-zhan': 'ango-zhan',        # spokój
        'shu': 'ango-shu',               # pokój
        'pen': 'ango-pen',               # cichy
        'kuang-jiu': 'ango-jiu',         # harmonia
        # Keep: hong-zen (równowaga - already good)
        
        # MIŁOŚĆ - keep 'qu/quo' family (already unified: quo, qu-zhou, qu-san)
        # Just ensure consistency
        
        # DUMA/HONOR - use 'rong-' root (modified from 荣 róng = honor/glory)
        'hei-pao': 'rongo-pao',          # duma
        'nai-che': 'rongo',              # honor, chwała  
        'shou-cao': 'rongo-cao',         # szacunek
    }
    
    return mappings

def apply_emotion_fixes():
    """Apply emotion unification"""
    lp_path = 'Lengxuan_Language/03_Slownik/slownik_lengxuan_polski.md'
    pl_path = 'Lengxuan_Language/03_Slownik/slownik_polski_lengxuan.md'
    
    print("😊 UNIFIKACJA EMOCJI - ZADANIE 1/4\n")
    print("=" * 80)
    
    mappings = create_emotion_mappings()
    
    # Load dictionary
    lp_entries = {}
    with open(lp_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('- '):
                parts = line.strip().rsplit(' - ', 1)
                if len(parts) == 2:
                    code, polish = parts[0][2:], parts[1]
                    lp_entries[code] = polish
    
    print(f"\n📋 Zastępuję {len(mappings)} kodów emocjonalnych:\n")
    
    # Apply mappings
    changes_count = 0
    for old_code, new_code in sorted(mappings.items()):
        if old_code in lp_entries:
            polish = lp_entries[old_code]
            del lp_entries[old_code]
            lp_entries[new_code] = polish
            changes_count += 1
            print(f"  {old_code:20} → {new_code:20} | {polish[:50]}")
        else:
            print(f"  ⚠️  {old_code:20} NOT FOUND")
    
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
    print("\n✅ EMOCJE ZUNIFIKOWANE!")
    print("   Nowe rodziny semantyczne:")
    print("   - huano (szczęście/radość) - 5 słów")
    print("   - beio (smutek/żal) - 7 słów")
    print("   - nuo (gniew/złość) - 3 słowa")
    print("   - ru (strach/lęk) - 4 słowa")
    print("   - ango (spokój/harmonia) - 5 słów")
    print("   - rongo (duma/honor) - 3 słowa")
    print("   + zachowano: tao (śmiać się), quo/qu (kochać)")

if __name__ == "__main__":
    apply_emotion_fixes()
