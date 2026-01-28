#!/usr/bin/env python3
# -*- coding: utf-8 -*-

lp_path = 'Lengxuan_Language/03_Slownik/slownik_lengxuan_polski.md'
pl_path = 'Lengxuan_Language/03_Slownik/slownik_polski_lengxuan.md'

# Method 1: Simple count
with open(lp_path, 'r', encoding='utf-8') as f:
    lp_simple = sum(1 for line in f if line.startswith('- '))

with open(pl_path, 'r', encoding='utf-8') as f:
    pl_simple = sum(1 for line in f if line.startswith('- '))

print(f"Simple count:")
print(f"  L→P: {lp_simple}")
print(f"  P→L: {pl_simple}")
print()

# Method 2: Parse with rsplit
lp_entries = []
with open(lp_path, 'r', encoding='utf-8') as f:
    for line in f:
        if line.startswith('- '):
            parts = line.strip().rsplit(' - ', 1)
            if len(parts) == 2:
                lp_entries.append(parts)
            else:
                print(f"L→P FAILED TO PARSE: {line.strip()[:80]}")

pl_entries = []
with open(pl_path, 'r', encoding='utf-8') as f:
    for line in f:
        if line.startswith('- '):
            parts = line.strip().rsplit(' - ', 1)
            if len(parts) == 2:
                pl_entries.append(parts)
            else:
                print(f"P→L FAILED TO PARSE: {line.strip()[:80]}")

print(f"Parsed count:")
print(f"  L→P: {len(lp_entries)}")
print(f"  P→L: {len(pl_entries)}")
print(f"  Difference: {abs(len(lp_entries) - len(pl_entries))}")
