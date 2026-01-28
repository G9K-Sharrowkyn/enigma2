#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Find food words for semantic unification"""

def find_food_words():
    lp_path = 'Lengxuan_Language/03_Slownik/slownik_lengxuan_polski.md'
    
    # Food keyword categories
    food_keywords = {
        'MIĘSO': ['mięso', 'wołowin', 'wieprzow', 'baranin', 'kurczak', 'drób',
                  'szynka', 'boczek', 'kiełbasa'],
        'WARZYWA': ['warzywo', 'kapusta', 'marchew', 'ziemniak', 'cebula', 'czosnek',
                    'pomidor', 'ogórek', 'papryka', 'sałata', 'szpinak', 'brokuł',
                    'kalafior', 'fasola', 'groch', 'soja', 'tofu'],
        'OWOCE': ['jabłko', 'gruszka', 'brzoskwinia', 'morela', 'śliwa', 'wiśnia',
                  'truskawka', 'malina', 'borówka', 'arbuz', 'melon', 'banan',
                  'pomarańcz', 'cytryna', 'grejpfrut', 'mandaryn', 'granat'],
        'ZBOŻA': ['ryż', 'pszenica', 'jęczmień', 'owies', 'kukurydza', 'proso',
                  'kasza', 'makaron', 'chleb', 'bułka', 'pieczywo', 'mąka',
                  'ziarno', 'ziarna'],
        'NABIAŁ': ['mleko', 'ser', 'masło', 'śmietana', 'jogurt', 'kefir', 'twaróg'],
        'NAPOJE': ['woda', 'herbata', 'wino', 'piwo', 'sok', 'napój'],
        'PRZYPRAWY': ['sól', 'pieprz', 'cukier', 'miód', 'ocet', 'olej', 'sos',
                      'przyprawa', 'imbir', 'cynamon', 'gałka', 'goździk', 'anyż'],
        'GOTOWANIE': ['gotować', 'smażyć', 'piec', 'dusić', 'grillować', 'blanszować',
                      'marynować', 'kroić', 'siekać', 'trzeć', 'mieszać', 'ubijać',
                      'gotowany', 'smażony', 'pieczony', 'duszony', 'surowy', 'świeży',
                      'gotowy', 'posiłek', 'danie', 'przekąsk', 'przystawka', 'kolacja'],
        'INNE': ['jedzenie', 'żywność', 'pokarm', 'jadło', 'kuchnia', 'kulinarn',
                 'przepis', 'smak', 'słony', 'słodki', 'kwaśny', 'gorzki', 'pikantny',
                 'apetyt', 'głód', 'syt']
    }
    
    entries = {}
    with open(lp_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('- '):
                parts = line.strip().rsplit(' - ', 1)
                if len(parts) == 2:
                    code, polish = parts[0][2:], parts[1]
                    entries[code] = polish
    
    print("🍜 JEDZENIE - ANALIZA\n")
    print("=" * 80)
    
    found_by_category = {}
    total_found = 0
    
    for category, keywords in food_keywords.items():
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
                root = code.split('-')[0] if '-' in code else code[:3]
                if root not in roots:
                    roots[root] = []
                roots[root].append(f"{code:25} → {polish}")
            
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
    print(f"   Łączna liczba słów jedzenia: {total_found}")
    print(f"   Kategorie: {len(found_by_category)}")
    
    for category, words in found_by_category.items():
        roots = set()
        for code, _ in words:
            root = code.split('-')[0] if '-' in code else code[:3]
            roots.add(root)
        print(f"   - {category}: {len(words)} słów, {len(roots)} rootów")
    
    return found_by_category

if __name__ == "__main__":
    find_food_words()
