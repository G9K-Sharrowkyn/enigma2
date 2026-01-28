#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Find medical/body terms that should share semantic roots
Focus on: body parts, organs, medical conditions, treatments
"""

def find_medical_inconsistencies():
    """Find medical/anatomical words with different roots"""
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
    
    print("🩺 MEDICAL/ANATOMICAL SEMANTIC INCONSISTENCIES\n")
    print("=" * 80)
    
    # Keyword groups for medical terms
    medical_keywords = {
        'CZĘŚCI CIAŁA ZEWNĘTRZNE (external body parts)': [
            'głowa', 'twarz', 'oczy', 'oko', 'uszy', 'ucho', 'nos', 'usta', 'język (organ)',
            'szyja', 'ramię', 'ramiona', 'ręka', 'ręce', 'dłoń', 'palec', 'noga', 'stopa',
            'kolano', 'łokieć', 'plecy', 'brzuch', 'klatka piersiowa', 'pierś',
            'head', 'face', 'eyes', 'ears', 'nose', 'mouth', 'tongue', 'neck',
            'arm', 'hand', 'finger', 'leg', 'foot', 'knee', 'back', 'chest'
        ],
        'ORGANY WEWNĘTRZNE (internal organs)': [
            'serce', 'płuco', 'płuca', 'wątroba', 'nerki', 'nerka', 'żołądek', 'jelito',
            'mózg', 'kość', 'krew', 'mięsień', 'ścięgno',
            'heart', 'lung', 'liver', 'kidney', 'stomach', 'brain', 'bone', 'blood', 'muscle'
        ],
        'STANY MEDYCZNE (medical conditions)': [
            'ból', 'choroba', 'chory', 'zdrowie', 'zdrowy', 'zmęczenie', 'zmęczony',
            'gorączka', 'kaszel', 'rana', 'uraz', 'infekcja', 'zespół',
            'pain', 'illness', 'disease', 'health', 'healthy', 'sick', 'fever', 'wound', 'injury'
        ],
        'TERAPIA I LECZENIE (therapy and treatment)': [
            'leczyć', 'leczenie', 'medycyna', 'lek', 'zioła', 'akupunktura', 'masaż', 'terapia',
            'heal', 'medicine', 'treatment', 'herb', 'therapy', 'acupuncture', 'massage'
        ]
    }
    
    # Find matches
    results = {}
    
    for category, keywords in medical_keywords.items():
        matches = []
        for code, polish in lp_entries.items():
            polish_lower = polish.lower()
            # Exact word matching for common words
            for keyword in keywords:
                # Check for exact match or word boundary
                if keyword.lower() in polish_lower:
                    # Avoid false positives like "podobny" matching "ból"
                    if keyword in ['ból', 'nos', 'oko', 'ucho']:
                        # These need exact match
                        words_in_polish = polish_lower.split()
                        if keyword.lower() in words_in_polish:
                            matches.append((code, polish))
                            break
                    else:
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
        
        for code, polish in sorted(matches, key=lambda x: x[1]):
            print(f"  {code:20} → {polish}")
            total_words += 1
        
        # Analyze roots
        roots = {}
        for code, polish in matches:
            root = code.split('-')[0]
            if root not in roots:
                roots[root] = []
            roots[root].append((code, polish))
        
        if len(roots) > 3:  # Only show if significant inconsistency
            print(f"\n  ⚠️  {len(roots)} different roots found (showing top 5):")
            sorted_roots = sorted(roots.items(), key=lambda x: len(x[1]), reverse=True)[:5]
            for root, words in sorted_roots:
                print(f"     - {root}: {len(words)} words")
    
    print("\n" + "=" * 80)
    print(f"\n📊 SUMMARY:")
    print(f"   Total medical/anatomical words: {total_words}")
    print(f"   Categories with inconsistencies: {len(results)}")
    
    print("\n💡 RECOMMENDATIONS:")
    print("   1. BODY PARTS: Consider anatomical grouping")
    print("      - Head/face: use 'tou-' or 'mian-' prefix")
    print("      - Limbs: use 'zhi-' prefix")
    print("      - Torso: use 'shen-' prefix")
    print("   2. ORGANS (TCM): Use 'zang-' for organs (Five Zang organs)")
    print("   3. CONDITIONS: Use 'bing-' for diseases/conditions")
    print("   4. TREATMENT: Use 'yi-' for medical/healing")

if __name__ == "__main__":
    find_medical_inconsistencies()
