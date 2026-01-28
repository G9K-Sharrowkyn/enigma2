#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Find emotion/psychological state words for semantic unification
"""

def find_emotions():
    lp_path = 'Lengxuan_Language/03_Slownik/slownik_lengxuan_polski.md'
    
    lp_entries = {}
    with open(lp_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('- '):
                parts = line.strip().rsplit(' - ', 1)
                if len(parts) == 2:
                    code, polish = parts[0][2:], parts[1]
                    lp_entries[code] = polish
    
    print("😊 EMOCJE I STANY PSYCHICZNE - ANALIZA\n")
    print("=" * 80)
    
    # Emotion categories
    emotion_keywords = {
        'SZCZĘŚCIE/RADOŚĆ': [
            'szczęście', 'szczęśliwy', 'radość', 'radosny', 'wesół', 'zadowol',
            'uśmiech', 'śmiech', 'śmiać'
        ],
        'SMUTEK/ŻAL': [
            'smutek', 'smutny', 'żal', 'rozpacz', 'płacz', 'płakać', 'łzy'
        ],
        'GNIEW/ZŁOŚĆ': [
            'gniew', 'zły', 'złość', 'wściekł', 'irytacja', 'rozgniewany'
        ],
        'STRACH/LĘK': [
            'strach', 'lęk', 'obawa', 'panika', 'przerażenie', 'bać się'
        ],
        'SPOKÓJ/HARMONIA': [
            'spokój', 'spokojny', 'cisza', 'cichy', 'harmonia', 'równowaga', 'pokój'
        ],
        'MIŁOŚĆ/UCZUCIA': [
            'miłość', 'kochać', 'uczucie', 'serce', 'pragn', 'tęsknota'
        ],
        'DUMA/HONOR': [
            'duma', 'dumny', 'honor', 'szacunek', 'godność', 'chwała'
        ]
    }
    
    results = {}
    
    for category, keywords in emotion_keywords.items():
        matches = []
        for code, polish in lp_entries.items():
            polish_lower = polish.lower()
            for keyword in keywords:
                if keyword in polish_lower:
                    matches.append((code, polish))
                    break
        
        if matches:
            results[category] = matches
    
    # Display results
    total_words = 0
    for category in sorted(results.keys()):
        matches = results[category]
        print(f"\n### {category}")
        print(f"Znaleziono {len(matches)} słów:\n")
        
        for code, polish in sorted(matches, key=lambda x: x[1]):
            print(f"  {code:20} → {polish[:60]}")
            total_words += 1
        
        # Analyze roots
        roots = {}
        for code, polish in matches:
            root = code.split('-')[0]
            if root not in roots:
                roots[root] = []
            roots[root].append(polish)
        
        if len(roots) > 2:
            print(f"\n  ⚠️  {len(roots)} różnych rootów:")
            for root in sorted(roots.keys())[:5]:
                print(f"     - {root}: {len(roots[root])} słów")
    
    print("\n" + "=" * 80)
    print(f"\n📊 PODSUMOWANIE:")
    print(f"   Łączna liczba słów emocjonalnych: {total_words}")
    print(f"   Kategorie: {len(results)}")
    
    return results

if __name__ == "__main__":
    find_emotions()
