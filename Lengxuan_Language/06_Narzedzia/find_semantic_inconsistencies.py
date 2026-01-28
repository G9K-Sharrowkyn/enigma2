# -*- coding: utf-8 -*-
"""
FIND SEMANTIC INCONSISTENCIES IN LENGXUAN DICTIONARY

Identifies words that should share semantic roots but don't.

Target groups mentioned in the problem statement:
1. Directions/Geography (16 words) - east, west, north, south, etc.
2. Medical/Body Terms (~50 words) - body parts, illnesses, treatments
3. Nature/Weather - plants, animals, geological features
4. Food/Cooking - cooking methods, baking, roasting, boiling
5. Emotions/States (~35 words)
"""

import re
from collections import defaultdict

def load_dictionary(file_path):
    """Load dictionary entries"""
    entries = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        pattern = r'^- ([a-zęóąśłżźćńüA-Z-]+) - (.+)$'
        matches = re.findall(pattern, content, re.MULTILINE)
        
        for code, meaning in matches:
            entries.append({
                'code': code,
                'meaning': meaning.lower(),
                'root': code.split('-')[0] if '-' in code else code
            })
        
        return entries
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        return []

def find_semantic_groups(entries):
    """Find words in semantic groups"""
    
    # Define semantic keywords for each group
    groups = {
        'directions': [
            'wschód', 'zachód', 'północ', 'południe', 'północny', 'południowy',
            'wschodni', 'zachodni', 'północno-wschodni', 'północno-zachodni',
            'południowo-wschodni', 'południowo-zachodni', 'kierunek', 'strona świata'
        ],
        'medical_body': [
            'głowa', 'ręka', 'noga', 'oko', 'ucho', 'nos', 'usta', 'serce', 'płuco',
            'wątroba', 'nerka', 'żołądek', 'krew', 'kość', 'mięsień', 'skóra',
            'choroba', 'ból', 'leczenie', 'medycyna', 'lekarz', 'pacjent'
        ],
        'weather_nature': [
            'pogoda', 'słońce', 'deszcz', 'śnieg', 'wiatr', 'chmura', 'burza',
            'mgła', 'grad', 'mróz', 'ciepło', 'zimno', 'gorąco',
            'drzewo', 'kwiat', 'trawa', 'liść', 'korzeń', 'gałąź',
            'góra', 'rzeka', 'jezioro', 'morze', 'las', 'pole'
        ],
        'cooking_food': [
            'gotować', 'smażyć', 'piec', 'grillować', 'dusić', 'parować',
            'gotowany', 'smażony', 'pieczony', 'jedzenie', 'posiłek',
            'śniadanie', 'obiad', 'kolacja'
        ],
        'emotions': [
            'radość', 'smutek', 'gniew', 'strach', 'szczęście', 'miłość', 'nienawiść',
            'zadowolony', 'smutny', 'zły', 'przestraszony', 'szczęśliwy',
            'uczucie', 'emocja', 'nastrój'
        ],
        'professions': [
            'nauczyciel', 'uczeń', 'pisarz', 'malarz', 'muzyk', 'lekarz',
            'wojownik', 'kupiec', 'rzemieślnik', 'filozof', 'historyk'
        ],
        'colors': [
            'czerwony', 'zielony', 'niebieski', 'żółty', 'czarny', 'biały',
            'szary', 'brązowy', 'różowy', 'pomarańczowy', 'fioletowy', 'złoty'
        ],
        'family': [
            'matka', 'ojciec', 'brat', 'siostra', 'syn', 'córka', 'dziadek',
            'babcia', 'wuj', 'ciotka', 'rodzina', 'krewny'
        ]
    }
    
    # Find matches for each group
    results = defaultdict(list)
    
    for entry in entries:
        meaning = entry['meaning']
        
        for group_name, keywords in groups.items():
            for keyword in keywords:
                if keyword in meaning:
                    results[group_name].append(entry)
                    break  # Only add once per group
    
    return results, groups

def analyze_roots(group_entries):
    """Analyze root diversity in a semantic group"""
    roots = defaultdict(list)
    
    for entry in group_entries:
        roots[entry['root']].append(entry)
    
    return roots

def print_report(semantic_groups, groups):
    """Print semantic inconsistency report"""
    print("=" * 80)
    print("SEMANTIC INCONSISTENCIES - LENGXUAN DICTIONARY")
    print("=" * 80)
    
    print("\nThis tool identifies words that should share semantic roots but don't.")
    print("\nTarget: Related concepts should use common root morphemes for consistency.")
    
    total_inconsistencies = 0
    
    for group_name in sorted(semantic_groups.keys()):
        entries = semantic_groups[group_name]
        
        if not entries:
            continue
        
        roots = analyze_roots(entries)
        
        print("\n" + "=" * 80)
        print(f"{group_name.upper().replace('_', '/')} ({len(entries)} words)")
        print("=" * 80)
        
        if len(roots) > 1:
            print(f"\n⚠️  INCONSISTENT: {len(roots)} different roots for related concepts")
            total_inconsistencies += len(entries)
            
            print(f"\nRoot distribution:")
            for root, root_entries in sorted(roots.items(), key=lambda x: len(x[1]), reverse=True):
                print(f"\n  [{root}] - {len(root_entries)} words:")
                for entry in root_entries[:5]:
                    print(f"    • {entry['code']} - {entry['meaning']}")
                if len(root_entries) > 5:
                    print(f"    ... and {len(root_entries) - 5} more")
            
            # Recommendation
            print(f"\n  💡 RECOMMENDATION:")
            most_common_root = max(roots.items(), key=lambda x: len(x[1]))[0]
            print(f"     Consider unifying under '{most_common_root}' root")
            print(f"     Or create a new semantic root for this family")
        else:
            print(f"\n✓ CONSISTENT: All words share '{list(roots.keys())[0]}' root")
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    
    groups_with_issues = sum(1 for entries in semantic_groups.values() 
                            if len(analyze_roots(entries)) > 1 and len(entries) > 0)
    
    if groups_with_issues > 0:
        print(f"\n⚠️  ISSUES FOUND")
        print(f"\n  Semantic groups with inconsistent roots: {groups_with_issues}")
        print(f"  Total words needing review: {total_inconsistencies}")
        print("\n  STATUS: SEMANTIC ORGANIZATION NEEDS IMPROVEMENT")
        print("\n  ACTION ITEMS:")
        print("    1. Review each inconsistent group")
        print("    2. Choose or create a semantic root for each family")
        print("    3. Systematically update related words")
        print("    4. Re-run verification after changes")
    else:
        print("\n✓ EXCELLENT!")
        print("  All semantic groups are consistent")
        print("  STATUS: SEMANTIC ORGANIZATION IS GOOD")
    
    print("\n" + "=" * 80)

def save_detailed_report(semantic_groups, groups, output_path):
    """Save detailed report to file"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("SEMANTIC INCONSISTENCIES - LENGXUAN DICTIONARY\n")
        f.write("=" * 80 + "\n\n")
        
        f.write("Date: 2026-01-28\n\n")
        
        for group_name in sorted(semantic_groups.keys()):
            entries = semantic_groups[group_name]
            
            if not entries:
                continue
            
            roots = analyze_roots(entries)
            
            f.write(f"\n{group_name.upper().replace('_', '/')} ({len(entries)} words)\n")
            f.write("=" * 80 + "\n")
            
            if len(roots) > 1:
                f.write(f"\nINCONSISTENT: {len(roots)} different roots\n\n")
                
                for root, root_entries in sorted(roots.items(), key=lambda x: len(x[1]), reverse=True):
                    f.write(f"\n[{root}] - {len(root_entries)} words:\n")
                    for entry in root_entries:
                        f.write(f"  {entry['code']} - {entry['meaning']}\n")
            else:
                f.write(f"\nCONSISTENT: All use '{list(roots.keys())[0]}' root\n")

def main():
    dict_path = "../03_Slownik/slownik_lengxuan_polski.new.md"
    report_path = "../05_Dokumentacja/raport_semantic_inconsistencies.txt"
    
    print("Loading dictionary...")
    entries = load_dictionary(dict_path)
    
    if not entries:
        print("ERROR: Could not load dictionary!")
        return
    
    print(f"Loaded {len(entries)} entries\n")
    
    print("Finding semantic groups...")
    semantic_groups, groups = find_semantic_groups(entries)
    
    # Print report
    print_report(semantic_groups, groups)
    
    # Save detailed report
    save_detailed_report(semantic_groups, groups, report_path)
    print(f"\nDetailed report saved to: {report_path}")

if __name__ == "__main__":
    main()
