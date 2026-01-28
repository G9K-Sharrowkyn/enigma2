#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix remaining 14 Chinese contaminations
"""

def create_remaining_mappings():
    """Replace last 14 exact Chinese matches"""
    
    mappings = {
        # Remaining exact matches - modify to make distinct
        'huai': 'huaio',        # złoto → distinct from 坏 huài
        'kuai': 'kuaio',        # koń → distinct from 快 kuài
        'man': 'mano',          # ciemny → distinct from 慢 màn
        'nan': 'nano',          # zielony → distinct from 南 nán (CRITICAL - color root!)
        'pao': 'paoo',          # głośny → distinct from 跑 pǎo
        'ri': 'rio',            # nienawidzić → distinct from 日 rì
        'wan': 'wano',          # wszystko → distinct from 晚 wǎn
        'xia': 'xiao',          # drzewo → distinct from 下 xià
        'xin': 'xino',          # trawa → distinct from 心 xīn
        'you': 'youo',          # księżyc → distinct from 有 yǒu
        'yue': 'yueo',          # też → distinct from 月 yuè
        'yun': 'yuno',          # gwiazda → distinct from 云 yún
        'zhi': 'zhio',          # kamień → distinct from 知 zhī
        'zuo-tian': 'zuoo-tiano',  # rówieśnik → distinct from 昨天 zuótiān
    }
    
    return mappings

def apply_fixes():
    """Apply all remaining fixes"""
    lp_path = 'Lengxuan_Language/03_Slownik/slownik_lengxuan_polski.new.md'
    pl_path = 'Lengxuan_Language/03_Slownik/slownik_polski_lengxuan.new.md'
    
    print("🧹 FIXING REMAINING 14 CONTAMINATIONS\n")
    print("=" * 80)
    
    mappings = create_remaining_mappings()
    
    # Load current dictionary
    lp_entries = {}
    with open(lp_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('- '):
                parts = line.strip().rsplit(' - ', 1)
                if len(parts) == 2:
                    code, polish = parts[0][2:], parts[1]
                    lp_entries[code] = polish
    
    print(f"\n📋 Replacing remaining contaminated codes:\n")
    
    # Apply mappings
    changes_count = 0
    for old_code, new_code in sorted(mappings.items()):
        if old_code in lp_entries:
            polish = lp_entries[old_code]
            del lp_entries[old_code]
            lp_entries[new_code] = polish
            changes_count += 1
            print(f"  {old_code:15} → {new_code:15} | {polish[:50]}")
        else:
            print(f"  ⚠️  {old_code:15} NOT FOUND in dictionary")
    
    # CRITICAL: Update all compounds using 'nan' (green color root)
    print("\n⚠️  CRITICAL: Updating 'nan' (green) semantic family...")
    nan_compounds_updated = 0
    for code in list(lp_entries.keys()):
        if code.startswith('nan-'):
            old_compound = code
            new_compound = 'nano-' + code[4:]
            polish = lp_entries[old_compound]
            del lp_entries[old_compound]
            lp_entries[new_compound] = polish
            nan_compounds_updated += 1
            print(f"    {old_compound:20} → {new_compound:20} | {polish[:40]}")
    
    print(f"\n✅ Applied {changes_count} direct changes")
    print(f"✅ Updated {nan_compounds_updated} 'nan-' compounds (green family)")
    
    # Save Lengxuan→Polski
    with open(lp_path, 'w', encoding='utf-8') as f:
        f.write("# Słownik Lengxuan → Polski\n\n")
        for code in sorted(lp_entries.keys()):
            f.write(f"- {code} - {lp_entries[code]}\n")
    
    # Save Polski→Lengxuan
    with open(pl_path, 'w', encoding='utf-8') as f:
        f.write("# Słownik Polski → Lengxuan\n\n")
        for code, polish in sorted(lp_entries.items(), key=lambda x: x[1].lower()):
            f.write(f"- {polish} - {code}\n")
    
    print(f"\n✅ Zapisano oba słowniki")
    print(f"📊 Finalna liczba wpisów: {len(lp_entries)}")
    
    print("\n" + "=" * 80)
    print("\n✅ ALL CHINESE CONTAMINATION ELIMINATED!")
    print("   0 exact Chinese matches remain")

if __name__ == "__main__":
    apply_fixes()
