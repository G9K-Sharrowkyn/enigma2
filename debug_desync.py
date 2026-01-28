#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Debug desynchronization between dictionaries"""

lp_path = 'Lengxuan_Language/03_Slownik/slownik_lengxuan_polski.md'
pl_path = 'Lengxuan_Language/03_Slownik/slownik_polski_lengxuan.md'

lp_entries = {}
pl_entries = {}

with open(lp_path, 'r', encoding='utf-8') as f:
    for line in f:
        if line.startswith('- '):
            parts = line.strip().rsplit(' - ', 1)
            if len(parts) == 2:
                code, polish = parts[0][2:], parts[1]
                lp_entries[code] = polish

with open(pl_path, 'r', encoding='utf-8') as f:
    for line in f:
        if line.startswith('- '):
            parts = line.strip().rsplit(' - ', 1)
            if len(parts) == 2:
                polish, code = parts[0][2:], parts[1]
                pl_entries[polish] = code

print(f"LP entries: {len(lp_entries)}")
print(f"PL entries: {len(pl_entries)}")
print(f"\nDifference: {abs(len(lp_entries) - len(pl_entries))}")

# Find what's in LP but not in PL
lp_codes = set(lp_entries.keys())
pl_codes = set(pl_entries.values())

only_in_lp = lp_codes - pl_codes
only_in_pl = pl_codes - lp_codes

if only_in_lp:
    print(f"\n❌ Tylko w LP ({len(only_in_lp)}):")
    for code in sorted(only_in_lp):
        print(f"  {code} - {lp_entries[code]}")

if only_in_pl:
    print(f"\n❌ Tylko w PL ({len(only_in_pl)}):")
    for code in sorted(only_in_pl):
        for pol, cod in pl_entries.items():
            if cod == code:
                print(f"  {code} - {pol}")
                break
