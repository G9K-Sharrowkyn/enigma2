#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Find nature/weather words for semantic unification"""

def find_nature_weather_words():
    lp_path = 'Lengxuan_Language/03_Slownik/slownik_lengxuan_polski.md'
    
    # Nature/weather keyword categories
    nature_keywords = {
        'POGODA': ['deszcz', 'śnieg', 'wiatr', 'burza', 'mgła', 'chmur', 'słońce', 'księżyc', 
                   'gwiazd', 'niebo', 'pogoda', 'klimat', 'temperatura', 'gorąc', 'zimn', 
                   'ciep', 'chłod', 'wilgotn', 'such'],
        'ROŚLINY': ['kwiat', 'drzewo', 'las', 'trawa', 'liść', 'korzeń', 'gałąź', 'pień', 
                    'owoc', 'nasion', 'roślin', 'bamboo', 'bambus', 'sosna', 'jodła'],
        'KRAJOBRAZ': ['góra', 'wzgórze', 'dolina', 'równina', 'urwisko', 'klifów', 'skał',
                      'rzeka', 'strumień', 'jezioro', 'morze', 'ocean', 'zatoka', 'wybrzeże',
                      'plaża', 'wyspa', 'półwysep', 'brzeg', 'wodospad', 'źródł'],
        'ZIEMIA': ['ziemia', 'gleba', 'piasek', 'kamień', 'skała', 'błoto', 'ląd', 'grunt'],
        'ZJAWISKA': ['tęcza', 'błyskawic', 'grom', 'piorun', 'powódź', 'susza', 'trzęsien',
                     'wulkan', 'lawa', 'tsunami', 'tajfun', 'tornado', 'huragan']
    }
    
    entries = {}
    with open(lp_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('- '):
                parts = line.strip().rsplit(' - ', 1)
                if len(parts) == 2:
                    code, polish = parts[0][2:], parts[1]
                    entries[code] = polish
    
    print("🌍 PRZYRODA I POGODA - ANALIZA\n")
    print("=" * 80)
    
    found_by_category = {}
    total_found = 0
    
    for category, keywords in nature_keywords.items():
        found_words = []
        for code, polish in sorted(entries.items()):
            polish_lower = polish.lower()
            for keyword in keywords:
                if keyword in polish_lower:
                    found_words.append((code, polish))
                    break
        
        if found_words:
            found_by_category[category] = found_words
            total_found += len(found_words)
            
            print(f"\n### {category} ({len(found_words)} words)")
            
            # Analyze roots
            roots = {}
            for code, polish in found_words:
                # Extract root (first part before -)
                root = code.split('-')[0] if '-' in code else code[:3]
                if root not in roots:
                    roots[root] = []
                roots[root].append(f"{code:20} → {polish}")
            
            # Show words grouped by root
            for root, words in sorted(roots.items()):
                if len(words) > 1:
                    print(f"\n  ROOT '{root}' ({len(words)} words):")
                    for word in words:
                        print(f"    {word}")
                else:
                    for word in words:
                        print(f"  {word}")
            
            if len(roots) > 1:
                print(f"\n  ⚠️ {len(roots)} różnych rootów w kategorii {category}")
    
    print("\n" + "=" * 80)
    print(f"\n📊 PODSUMOWANIE:")
    print(f"   Łączna liczba słów przyroda/pogoda: {total_found}")
    print(f"   Kategorie: {len(found_by_category)}")
    
    for category, words in found_by_category.items():
        roots = set()
        for code, _ in words:
            root = code.split('-')[0] if '-' in code else code[:3]
            roots.add(root)
        print(f"   - {category}: {len(words)} słów, {len(roots)} rootów")
    
    return found_by_category

if __name__ == "__main__":
    find_nature_weather_words()
