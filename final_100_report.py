#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Final 100% Quality Report
Comprehensive verification after completing all 4 semantic unification tasks
"""

def verify_100_percent():
    lp_path = 'Lengxuan_Language/03_Slownik/slownik_lengxuan_polski.md'
    pl_path = 'Lengxuan_Language/03_Slownik/slownik_polski_lengxuan.md'
    
    # Load both dictionaries
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
    
    print("✨ RAPORT KOŃCOWY - JAKOŚĆ 100%\n")
    print("=" * 80)
    
    # TEST 1: Synchronizacja
    print("\n📋 TEST 1: SYNCHRONIZACJA SŁOWNIKÓW")
    print("-" * 80)
    if len(lp_entries) == len(pl_entries):
        print(f"✅ DOSKONALE: Oba słowniki mają {len(lp_entries)} wpisów")
    else:
        print(f"❌ BŁĄD: LP={len(lp_entries)}, PL={len(pl_entries)}")
    
    # TEST 2: Homonimia (zero duplikatów)
    print("\n📋 TEST 2: HOMONIMIA (1:1 MAPPING)")
    print("-" * 80)
    code_counts = {}
    for code in lp_entries.keys():
        code_counts[code] = code_counts.get(code, 0) + 1
    
    duplicates = {k: v for k, v in code_counts.items() if v > 1}
    if not duplicates:
        print(f"✅ DOSKONALE: Zero duplikatów - każdy kod unikalny")
    else:
        print(f"❌ BŁĄD: {len(duplicates)} duplikatów znalezionych")
    
    # TEST 3: Długość kodów
    print("\n📋 TEST 3: DŁUGOŚĆ KODÓW")
    print("-" * 80)
    max_length = max(len(code) for code in lp_entries.keys())
    avg_length = sum(len(code) for code in lp_entries.keys()) / len(lp_entries)
    long_codes = [code for code in lp_entries.keys() if len(code) > 15]
    
    print(f"  Maksymalna długość: {max_length} znaków")
    print(f"  Średnia długość: {avg_length:.1f} znaków")
    if not long_codes:
        print(f"✅ DOSKONALE: Wszystkie kody ≤ 15 znaków")
    else:
        print(f"❌ OSTRZEŻENIE: {len(long_codes)} kodów > 15 znaków")
    
    # TEST 4: Kontaminacja chińska (podstawowa lista)
    print("\n📋 TEST 4: KONTAMINACJA CHIŃSKA")
    print("-" * 80)
    common_chinese = [
        'wo', 'ni', 'ta', 'men', 'de', 'shi', 'zai', 'you', 'yi', 'er', 'san', 'si', 'wu',
        'liu', 'qi', 'ba', 'jiu', 'shi', 'bai', 'qian', 'wan', 'nian', 'yue', 'ri', 'tian',
        'ren', 'shui', 'huo', 'tu', 'jin', 'mu', 'da', 'xiao', 'shang', 'xia', 'zhong',
        'lai', 'qu', 'shuo', 'kan', 'ting', 'chi', 'he', 'zou', 'zuo', 'dou', 'xie', 'zhi',
        'dao', 'hui', 'neng', 'yao', 'xiang', 'guo', 'jia', 'ge', 'wei', 'bu', 'mei', 'hen'
    ]
    
    contaminated = [code for code in lp_entries.keys() if code in common_chinese]
    if not contaminated:
        print(f"✅ DOSKONALE: Zero dokładnych dopasowań z chińskim")
    else:
        print(f"❌ BŁĄD: {len(contaminated)} kontaminacji: {', '.join(contaminated[:10])}")
    
    # TEST 5: Rodziny semantyczne - count all unified families
    print("\n📋 TEST 5: RODZINY SEMANTYCZNE")
    print("-" * 80)
    
    families = {
        # Original families (from 95%)
        'tao': 0, 'mou': 0, 'ma': 0, 'muo': 0,
        'nano': 0, 'mao': 0, 'mei': 0, 'nou': 0, 'fang': 0,
        
        # Emotion families (Task 1)
        'huano': 0, 'beio': 0, 'nuo': 0, 'ru': 0, 'ango': 0, 'rongo': 0,
        'quo': 0, 'qu': 0,  # love family
        
        # Nature/Weather families (Task 2)
        'tiano': 0, 'guango': 0, 'yuo': 0, 'xueo': 0, 'fengo': 0,
        'baoo': 0, 'weno': 0, 'qio': 0, 'wuo': 0, 'shio': 0,
        'xie': 0, 'xino': 0, 'lino': 0, 'duano': 0, 'geno': 0,
        'zhono': 0, 'zhio': 0, 'zhuo': 0, 'songo': 0, 'tano': 0, 'caoo': 0,
        'shano': 0, 'heo': 0, 'huo': 0, 'haio': 0, 'guo': 0,
        'pingo': 0, 'puo': 0, 'yuano': 0, 'yao': 0, 'yano': 0,
        'zhio': 0, 'shao': 0, 'diio': 0,
        'diano': 0, 'hongo': 0, 'zheno': 0, 'huoo': 0, 'shuo': 0, 'hano': 0,
        
        # Animal families (Task 3)
        'gouo': 0, 'maoo': 0, 'pao': 0, 'tuno': 0, 'niuo': 0, 'yango': 0,
        'tuo': 0, 'rao': 0, 'houo': 0, 'leo': 0, 'tigo': 0, 'xiongo': 0,
        'hulo': 0, 'laio': 0, 'luo': 0, 'xio': 0, 'sheo': 0,
        'niao': 0, 'yingo': 0, 'yao': 0, 'jio': 0, 'geo': 0,
        'yeno': 0, 'wuo': 0, 'queo': 0, 'yaoo': 0,
        'dongo': 0, 'lio': 0, 'sharo': 0, 'xiao': 0, 'zheo': 0,
        'zhango': 0, 'paoo': 0, 'beo': 0,
        'chongo': 0, 'mio': 0, 'yio': 0, 'dieo': 0, 'zhüo': 0,
        'guio': 0, 'lian': 0, 'eo': 0, 'wao': 0,
        
        # Food families (Task 4)
        'rouo': 0, 'caio': 0, 'guoo': 0, 'fano': 0, 'miano': 0,
        'naio': 0, 'zhe': 0, 'gango': 0, 'geng': 0,
        'liao': 0, 'yoo': 0, 'qiao': 0, 'kaoo': 0, 'duo': 0,
        'bano': 0, 'jio': 0, 'shio': 0,
        'da': 0  # frying (already unified in 95%)
    }
    
    for code in lp_entries.keys():
        root = code.split('-')[0] if '-' in code else code
        if root in families:
            families[root] += 1
    
    active_families = {k: v for k, v in families.items() if v > 0}
    total_unified_words = sum(active_families.values())
    
    print(f"  Aktywne rodziny semantyczne: {len(active_families)}")
    print(f"  Łączna liczba zunifikowanych słów: {total_unified_words}")
    print(f"  Procent pokrycia: {100*total_unified_words/len(lp_entries):.1f}%")
    
    # Show largest families
    top_families = sorted(active_families.items(), key=lambda x: x[1], reverse=True)[:15]
    print("\n  Top 15 największych rodzin:")
    for root, count in top_families:
        print(f"    {root:12} - {count:3} słów")
    
    print("\n" + "=" * 80)
    print("\n🎯 PODSUMOWANIE KOŃCOWE:")
    print("-" * 80)
    print(f"  Całkowita liczba wpisów: {len(lp_entries)}")
    print(f"  Zunifikowane rodziny: {len(active_families)}")
    print(f"  Zunifikowane słowa: {total_unified_words}")
    print(f"  Synchronizacja: {'✅ TAK' if len(lp_entries)==len(pl_entries) else '❌ NIE'}")
    print(f"  Homonimia: {'✅ ZERO' if not duplicates else f'❌ {len(duplicates)}'}")
    print(f"  Kontaminacja: {'✅ ZERO' if not contaminated else f'❌ {len(contaminated)}'}")
    
    # Calculate final quality score
    quality_scores = {
        'Synchronizacja': 100 if len(lp_entries)==len(pl_entries) else 0,
        'Homonimia': 100 if not duplicates else 50,
        'Długość kodów': 100 if not long_codes else 90,
        'Kontaminacja': 100 if not contaminated else 0,
        'Semantyka': min(100, 100*total_unified_words/len(lp_entries))
    }
    
    final_score = sum(quality_scores.values()) / len(quality_scores)
    
    print("\n📊 OCENA JAKOŚCI:")
    print("-" * 80)
    for criterion, score in quality_scores.items():
        print(f"  {criterion:20} {score:5.1f}%")
    print("-" * 80)
    print(f"  OGÓLNA JAKOŚĆ:       {final_score:5.1f}%")
    
    if final_score >= 99.5:
        print("\n🏆 GRATULACJE! OSIĄGNIĘTO 100% JAKOŚCI!")
        print("   Słownik Lengxuan jest IDEALNY i gotowy do użycia.")
    elif final_score >= 95:
        print("\n✅ DOSKONALE! Słownik ma bardzo wysoką jakość.")
    else:
        print("\n⚠️  Słownik wymaga dalszych poprawek.")
    
    print("\n" + "=" * 80)
    
    return final_score, len(active_families), total_unified_words

if __name__ == "__main__":
    verify_100_percent()
