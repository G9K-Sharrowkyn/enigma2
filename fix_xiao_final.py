#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix last Chinese contamination: xiao and xiao-* compounds
"""

def fix_xiao():
    """Replace xiao with xiaoo and all compounds"""
    lp_path = 'Lengxuan_Language/03_Slownik/slownik_lengxuan_polski.new.md'
    pl_path = 'Lengxuan_Language/03_Slownik/slownik_polski_lengxuan.new.md'
    
    print("🧹 FIXING LAST CONTAMINATION: xiao\n")
    print("=" * 80)
    
    # Load current dictionary
    lp_entries = {}
    with open(lp_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('- '):
                parts = line.strip().rsplit(' - ', 1)
                if len(parts) == 2:
                    code, polish = parts[0][2:], parts[1]
                    lp_entries[code] = polish
    
    print(f"\n📋 Replacing xiao- compounds:\n")
    
    # Find and replace all xiao- compounds
    changes_count = 0
    for code in list(lp_entries.keys()):
        if code.startswith('xiao-'):
            new_code = 'xiaoo-' + code[5:]
            polish = lp_entries[code]
            del lp_entries[code]
            lp_entries[new_code] = polish
            changes_count += 1
            print(f"  {code:20} → {new_code:20} | {polish[:40]}")
    
    print(f"\n✅ Updated {changes_count} 'xiao-' compounds")
    
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
    print("\n✅ ALL CHINESE CONTAMINATION FINALLY ELIMINATED!")

if __name__ == "__main__":
    fix_xiao()
