#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Find direction/geography related words that should share roots
"""

def find_direction_inconsistencies():
    """Find words related to directions/geography with different roots"""
    lp_path = 'Lengxuan_Language/03_Slownik/slownik_lengxuan_polski.new.md'
    
    # Load dictionary
    lp_entries = {}
    with open(lp_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('- '):
                parts = line.strip().rsplit(' - ', 1)
                if len(parts) == 2:
                    code, polish = parts[0][2:], parts[1]
                    lp_entries[code] = polish
    
    print("🧭 DIRECTION/GEOGRAPHY SEMANTIC INCONSISTENCIES\n")
    print("=" * 80)
    
    # Keyword groups for directions/geography
    direction_keywords = {
        'KIERUNKI PODSTAWOWE (cardinal directions)': [
            'wschód', 'zachód', 'północ', 'południe',
            'east', 'west', 'north', 'south'
        ],
        'KIERUNKI POŚREDNIE (intermediate directions)': [
            'północny wschód', 'północny zachód', 'południowy wschód', 'południowy zachód',
            'northeast', 'northwest', 'southeast', 'southwest'
        ],
        'POZYCJE WZGLĘDNE (relative positions)': [
            'lewo', 'prawo', 'przód', 'tył', 'góra', 'dół',
            'z przodu', 'z tyłu', 'z boku', 'obok', 'nad', 'pod',
            'left', 'right', 'front', 'back', 'above', 'below', 'beside'
        ],
        'GEOGRAFIA (geography)': [
            'góra', 'dolina', 'rzeka', 'jezioro', 'morze', 'ocean', 'las', 'pustynia',
            'miasto', 'wieś', 'droga', 'ścieżka', 'most',
            'mountain', 'valley', 'river', 'lake', 'sea', 'forest', 'desert',
            'city', 'village', 'road', 'path', 'bridge'
        ],
        'ODLEGŁOŚCI (distances)': [
            'blisko', 'daleko', 'tutaj', 'tam', 'nigdzie', 'wszędzie',
            'w pobliżu', 'wewnątrz', 'zewnątrz', 'poza',
            'near', 'far', 'here', 'there', 'inside', 'outside'
        ]
    }
    
    # Find matches
    results = {}
    
    for category, keywords in direction_keywords.items():
        matches = []
        for code, polish in lp_entries.items():
            polish_lower = polish.lower()
            for keyword in keywords:
                if keyword.lower() in polish_lower:
                    matches.append((code, polish))
                    break
        
        if matches:
            results[category] = matches
    
    # Display results
    total_words = 0
    for category in sorted(results.keys()):
        matches = results[category]
        print(f"\n### {category}")
        print(f"Found {len(matches)} words:\n")
        
        for code, polish in sorted(matches):
            print(f"  {code:20} → {polish}")
            total_words += 1
        
        # Analyze roots
        roots = {}
        for code, polish in matches:
            root = code.split('-')[0]
            if root not in roots:
                roots[root] = []
            roots[root].append((code, polish))
        
        if len(roots) > 1:
            print(f"\n  ⚠️  {len(roots)} different roots found:")
            for root in sorted(roots.keys()):
                print(f"     - {root}: {len(roots[root])} words")
    
    print("\n" + "=" * 80)
    print(f"\n📊 SUMMARY:")
    print(f"   Total direction/geography words: {total_words}")
    print(f"   Categories with inconsistencies: {len(results)}")
    
    print("\n💡 RECOMMENDATIONS:")
    print("   1. KIERUNKI: Use 'fang-' prefix for all cardinal directions")
    print("   2. POZYCJE: Use 'wei-' or 'chu-' for relative positions")
    print("   3. GEOGRAFIA: Keep diverse roots (they're different concepts)")
    print("   4. ODLEGŁOŚCI: Use 'ju-' for distance-related words")

if __name__ == "__main__":
    find_direction_inconsistencies()
