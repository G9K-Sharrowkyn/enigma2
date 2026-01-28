#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Check specifically for 'jin' and 'mu' contamination"""

lp_path = 'Lengxuan_Language/03_Slownik/slownik_lengxuan_polski.md'

lp_entries = {}
with open(lp_path, 'r', encoding='utf-8') as f:
    for line in f:
        if line.startswith('- '):
            parts = line.strip().rsplit(' - ', 1)
            if len(parts) == 2:
                code, polish = parts[0][2:], parts[1]
                lp_entries[code] = polish

print("Checking 'jin' and 'mu' specifically:")
print()

if 'jin' in lp_entries:
    print(f"❌ FOUND: jin → {lp_entries['jin']}")
    print(f"   Chinese: 金 (jīn) = gold/metal")
    print(f"   PROBLEM: This is a common Chinese word!")
else:
    print(f"✅ 'jin' NOT FOUND")

print()

if 'mu' in lp_entries:
    print(f"❌ FOUND: mu → {lp_entries['mu']}")
    print(f"   Chinese: 木 (mù) = wood/tree")
    print(f"   PROBLEM: This is a common Chinese word!")
    print(f"   NOTE: 'mu' is also our semantic root for 'write' family (12 words)")
else:
    print(f"✅ 'mu' NOT FOUND")

print()

# Check all mu- family
mu_family = {code: polish for code, polish in lp_entries.items() if code.startswith('mu-') or code == 'mu'}
print(f"'mu' family ({len(mu_family)} words):")
for code in sorted(mu_family.keys())[:10]:
    print(f"  {code:20} → {mu_family[code][:50]}")
