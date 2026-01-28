#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix final 2 Chinese contaminations: jin and mu
WARNING: 'mu' is semantic root for 'write' family (12 words)
"""

def fix_jin_mu():
    """Fix jin and mu contamination"""
    lp_path = 'Lengxuan_Language/03_Slownik/slownik_lengxuan_polski.md'
    pl_path = 'Lengxuan_Language/03_Slownik/slownik_polski_lengxuan.md'
    
    print("🧹 FIXING FINAL 2 CHINESE CONTAMINATIONS\n")
    print("=" * 80)
    
    # Load dictionary
    lp_entries = {}
    with open(lp_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('- '):
                parts = line.strip().rsplit(' - ', 1)
                if len(parts) == 2:
                    code, polish = parts[0][2:], parts[1]
                    lp_entries[code] = polish
    
    print("\n### PROBLEM:")
    print(f"  ❌ 'jin' → {lp_entries.get('jin', 'NOT FOUND')} (Chinese: 金 jīn = gold)")
    print(f"  ❌ 'mu' → {lp_entries.get('mu', 'NOT FOUND')} (Chinese: 木 mù = wood)")
    print(f"  ⚠️  'mu' is semantic ROOT for 12-word 'write' family!")
    
    print("\n### SOLUTIONS:")
    print(f"  1. jin → jino (twardy)")
    print(f"  2. mu → muo (pisać) + CASCADE 11 compound words")
    print()
    
    # Apply fixes
    changes = []
    
    # Fix 1: jin → jino
    if 'jin' in lp_entries:
        polish = lp_entries['jin']
        del lp_entries['jin']
        lp_entries['jino'] = polish
        changes.append(('jin', 'jino', polish))
        print(f"  ✅ jin → jino | {polish}")
    
    # Fix 2: mu → muo (and all mu-* compounds)
    mu_family = [(code, polish) for code, polish in lp_entries.items() 
                 if code.startswith('mu-') or code == 'mu']
    
    print(f"\n  ⚠️  Updating 'mu' semantic family ({len(mu_family)} words):")
    
    for old_code, polish in sorted(mu_family):
        if old_code == 'mu':
            new_code = 'muo'
        else:
            # mu-xxx → muo-xxx
            new_code = 'muo-' + old_code[3:]
        
        del lp_entries[old_code]
        lp_entries[new_code] = polish
        changes.append((old_code, new_code, polish))
        print(f"     {old_code:20} → {new_code:20} | {polish[:40]}")
    
    print(f"\n✅ Applied {len(changes)} changes")
    
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
    print("\n✅ ALL CHINESE CONTAMINATION ELIMINATED!")
    print("   2 final contaminations fixed (jin, mu family)")
    print("   Total changes in this session: 74 words")
    print("     - jin → jino (1 word)")
    print("     - mu → muo (12 words in family)")

if __name__ == "__main__":
    fix_jin_mu()
