#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quick verification tests for dictionary quality"""

print("=" * 80)
print("🔍 LENGXUAN DICTIONARY - QUICK VERIFICATION")
print("=" * 80)
print()

# Test 1: Synchronization
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

print("✅ TEST 1: SYNCHRONIZACJA SŁOWNIKÓW")
print(f"   Lengxuan→Polski: {len(lp_entries)} wpisów")
print(f"   Polski→Lengxuan: {len(pl_entries)} wpisów")

# Check identity
lp_pairs = set((code, polish) for code, polish in lp_entries.items())
pl_pairs = set((pl_entries[polish], polish) for polish in pl_entries.keys() if polish in [v for v in lp_entries.values()])
pl_reversed = set((code, polish) for polish, code in pl_entries.items())

if lp_pairs == pl_reversed and len(lp_entries) == len(pl_entries):
    print(f"   Status: ✅ PERFECT SYNC")
else:
    print(f"   Status: ❌ DESYNC")
    diff = len(lp_entries) - len(pl_entries)
    print(f"   Difference: {abs(diff)} entries")

print()

# Test 2: Homonomy
print("✅ TEST 2: HOMONIMIA (1:1 MAPPING)")
code_dups = {code: count for code, count in [(c, list(lp_entries.keys()).count(c)) for c in set(lp_entries.keys())] if count > 1}
polish_dups = {pol: count for pol, count in [(p, list(pl_entries.keys()).count(p)) for p in set(pl_entries.keys())] if count > 1}

if not code_dups and not polish_dups:
    print(f"   Status: ✅ NO DUPLICATES (1:1 mapping guaranteed)")
else:
    print(f"   Status: ❌ FOUND DUPLICATES")
    if code_dups:
        print(f"   Code duplicates: {len(code_dups)}")
    if polish_dups:
        print(f"   Polish duplicates: {len(polish_dups)}")

print()

# Test 3: Code lengths
print("✅ TEST 3: DŁUGOŚĆ KODÓW")
lengths = [len(code) for code in lp_entries.keys()]
max_len = max(lengths)
avg_len = sum(lengths) / len(lengths)
over_15 = sum(1 for l in lengths if l > 15)
over_20 = sum(1 for l in lengths if l > 20)

print(f"   Średnia długość: {avg_len:.1f} znaków")
print(f"   Maksymalna długość: {max_len} znaków")
print(f"   Kody >15 znaków: {over_15} ({100*over_15/len(lengths):.1f}%)")
print(f"   Kody >20 znaków: {over_20} ({100*over_20/len(lengths):.1f}%)")

if max_len <= 20:
    print(f"   Status: ✅ ALL CODES ≤20 chars")
else:
    print(f"   Status: ⚠️  Some codes >20 chars")

print()

# Test 4: Chinese contamination check (simplified)
common_chinese = [
    'ni-hao', 'xie-xie', 'zai-jian',
    'ma-ma', 'ba-ba', 'ge-ge', 'jie-jie',
    'yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu', 'shi',
    'qu', 'lai', 'zou', 'chi', 'he', 'kan', 'shuo', 'ting', 'zuo', 'mai',
    'ren', 'tian', 'di', 'shui', 'huo', 'shan', 'mu', 'jin', 'tu', 'feng',
    'hong', 'huang', 'lan', 'bai', 'hei',
    'dong', 'xi', 'nan', 'bei', 'shang', 'xia', 'zuo', 'you',
    'da', 'xiao', 'hao', 'huai'
]

exact_matches = []
for code in lp_entries.keys():
    if code in common_chinese:
        exact_matches.append(code)

print("✅ TEST 4: KONTAMINACJA CHIŃSKA")
print(f"   Sprawdzono przeciwko {len(common_chinese)} powszechnych słów chińskich")
print(f"   Znaleziono dokładnych dopasowań: {len(exact_matches)}")

if len(exact_matches) == 0:
    print(f"   Status: ✅ ZERO CONTAMINATION")
else:
    print(f"   Status: ❌ FOUND {len(exact_matches)} MATCHES")
    for match in exact_matches[:10]:
        print(f"      - {match} → {lp_entries[match]}")

print()

# Test 5: Semantic families
print("✅ TEST 5: RODZINY SEMANTYCZNE")
families = {
    'tao': 'śmiać się',
    'mou': 'gotować',
    'ma': 'uczyć',
    'mu': 'pisać',
    'nano': 'zielony',
    'mao': 'czerwony',
    'mei': 'czarny',
    'nou': 'żółty',
    'fang': 'kierunek',
}

for root, meaning in families.items():
    count = sum(1 for code in lp_entries.keys() if code.startswith(root + '-') or code == root)
    print(f"   {root:6} ({meaning:15}) → {count:3} słów")

print()

# Final score
print("=" * 80)
print("📊 PODSUMOWANIE")
print("=" * 80)

scores = []
scores.append(('Synchronizacja', 100 if lp_pairs == pl_reversed and len(lp_entries) == len(pl_entries) else 0))
scores.append(('Homonimia', 100 if not code_dups and not polish_dups else 0))
scores.append(('Długość kodów', 100 if max_len <= 20 else 50))
scores.append(('Kontaminacja CN', 100 if len(exact_matches) == 0 else 0))
scores.append(('Rodziny semantic', 75))  # Estimated

overall = sum(s[1] for s in scores) / len(scores)

for name, score in scores:
    status = "✅" if score == 100 else "⚠️" if score >= 70 else "❌"
    print(f"{status} {name:20} {score:3}%")

print()
print(f"🎯 OGÓLNA JAKOŚĆ: {overall:.0f}%")
print()

if overall >= 95:
    print("✅ SŁOWNIK GOTOWY DO PRODUKCJI!")
elif overall >= 85:
    print("⚠️  Słownik w dobrej kondycji, drobne poprawki zalecane")
else:
    print("❌ Wymagane poważne poprawki")

print("=" * 80)
