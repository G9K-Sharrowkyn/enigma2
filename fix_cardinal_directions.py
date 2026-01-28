#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix core cardinal directions to use consistent 'fang-' root
Lengxuan inspiration: 方 (fāng) = direction/side
"""

def create_direction_mappings():
    """
    Unify cardinal directions under 'fang-' root
    """
    
    mappings = {
        # CARDINAL DIRECTIONS - use fang- root
        'chao-mo': 'fang-dong',       # wschód → east
        'gou-ka': 'fang-xi',          # zachód → west
        'che-tao': 'fang-bei',        # północ → north
        'pu-miao': 'fang-nan',        # południe → south
        
        # PRECISE DIRECTIONS - keep fang- + modifier
        'chan-tao': 'fang-bei-zheng',   # dokładnie północ → exact north
        're-nong': 'fang-dong-zheng',   # dokładnie wschód → exact east
        'sou-fei': 'fang-nan-zheng',    # dokładnie południe → exact south
        'ya-piao': 'fang-xi-zheng',     # dokładnie zachód → exact west
        
        # INTERMEDIATE DIRECTIONS - fang- + compound
        'mao-chi': 'fang-bei-dong',     # północny wschód → northeast
        'yi-fo': 'fang-bei-xi',         # północny zachód → northwest
        'dang-sen': 'fang-nan-dong',    # południowy wschód → southeast
        'zhuang-mi': 'fang-nan-xi',     # południowy zachód → southwest
        
        # SUN-RELATED DIRECTIONS - keep separate (time-based)
        # 'keng-la': keep as is → wschód słońca (sunrise)
        # 'yin-dia': keep as is → zachód słońca (sunset)
        
        # TIME OF DAY - keep separate (not spatial directions)
        # 'he-sang': keep as is → przed południem (AM)
        # 'shuai-fang': keep as is → popołudnie (PM)
        
        # SYMBOLIC/COLOR DIRECTIONS - these are from wuxing system
        # 'bao-zei': keep as is → lazurowy smok (wschód) - this is mythology
        # 'mao-ban': keep as is → czerwony ptak (południe) - mythology
        # 'mei-da': keep as is → czarny wojownik (północ) - mythology
        # These are NOT simple directions, they're cultural concepts
    }
    
    return mappings

def apply_direction_fixes():
    """Apply directional consistency fixes"""
    lp_path = 'Lengxuan_Language/03_Slownik/slownik_lengxuan_polski.new.md'
    pl_path = 'Lengxuan_Language/03_Slownik/slownik_polski_lengxuan.new.md'
    
    print("🧭 FIXING CARDINAL DIRECTIONS (fang- root)\n")
    print("=" * 80)
    
    mappings = create_direction_mappings()
    
    # Load dictionary
    lp_entries = {}
    with open(lp_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('- '):
                parts = line.strip().rsplit(' - ', 1)
                if len(parts) == 2:
                    code, polish = parts[0][2:], parts[1]
                    lp_entries[code] = polish
    
    print(f"\n📋 Replacing {len(mappings)} cardinal direction codes:\n")
    
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
    
    print(f"\n✅ Applied {changes_count} direction changes")
    
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
    print(f"📊 Finalna liczba wpisów: {len(lp_entries)}")
    
    print("\n" + "=" * 80)
    print("\n✅ CARDINAL DIRECTIONS UNIFIED!")
    print("   All basic directions now use 'fang-' root")
    print("\n💡 KEPT SEPARATE (by design):")
    print("   - keng-la, yin-dia (time-based: sunrise/sunset)")
    print("   - he-sang, shuai-fang (temporal: AM/PM)")
    print("   - bao-zei, mao-ban, mei-da (mythological symbols)")

if __name__ == "__main__":
    apply_direction_fixes()
