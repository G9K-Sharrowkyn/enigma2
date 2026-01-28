# -*- coding: utf-8 -*-
"""
CHECK CHINESE CONTAMINATION IN LENGXUAN DICTIONARY

Verifies that NO Lengxuan words match actual Chinese words.
This is CRITICAL for the language's authenticity.

Core Principle: "Sound Chinese, but BE original"

Checks:
1. Common Mandarin words (pinyin romanization)
2. Common Cantonese romanizations
3. Phonetic similarity (>70% match threshold)
"""

import re
from collections import defaultdict
import difflib

# Common Chinese words in pinyin romanization
# This is a sample list - in production, this should be much larger
COMMON_CHINESE_WORDS = [
    # Pronouns
    'wo', 'ni', 'ta', 'women', 'nimen', 'tamen',
    # Common verbs
    'shi', 'you', 'lai', 'qu', 'chi', 'he', 'shuo', 'kan', 'ting', 'zou',
    # Common nouns
    'ren', 'tian', 'di', 'shui', 'huo', 'feng', 'yue', 'ri',
    # Numbers
    'yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu', 'shi', 'bai', 'qian', 'wan',
    # Thank you and greetings
    'xie', 'xiexie', 'nihao', 'zaijian', 'duibuqi',
    # Common adjectives
    'da', 'xiao', 'hao', 'huai', 'chang', 'duan', 'gao', 'di',
    # Family
    'ba', 'ma', 'gege', 'jiejie', 'didi', 'meimei',
    # Colors
    'hong', 'huang', 'lan', 'lv', 'bai', 'hei',
    # More common words
    'shui', 'shan', 'mu', 'lin', 'cun', 'zhen', 'cheng', 'guo',
    # Time
    'nian', 'yue', 'ri', 'tian', 'xingqi', 'xiaoshi', 'fenzhong', 'miao',
    # Questions
    'shenme', 'shei', 'nar', 'zenme', 'weishenme', 'jige', 'duoshao',
    # Particles
    'de', 'le', 'ma', 'ne', 'ba', 'a',
    # Verbs
    'zuo', 'zhan', 'pao', 'tiao', 'xie', 'du', 'xue', 'jiao',
    # More nouns
    'shu', 'hua', 'men', 'chuang', 'zhuozi', 'yizi', 'che', 'fangzi',
]

# Cantonese romanizations (Jyutping/Yale)
COMMON_CANTONESE_WORDS = [
    'ngo', 'nei', 'keoi', 'ngodei', 'neidei', 'keoideoi',
    'hai', 'jau', 'mou', 'lai', 'heoi', 'sik', 'jam',
    'jan', 'tin', 'dei', 'seoi', 'fo', 'fung',
    # Numbers in Cantonese
    'jat', 'ji', 'saam', 'sei', 'ng', 'luk', 'cat', 'baat', 'gau', 'sap',
]

# Classical Chinese common particles and words
CLASSICAL_CHINESE_WORDS = [
    'zhi', 'ye', 'yi', 'er', 'yu', 'ze', 'qi', 'wei', 'bu', 'suo',
    'zhe', 'yan', 'hu', 'zai', 'fu', 'ruo', 'nai', 'ze', 'gu',
]

def load_lengxuan_codes(file_path):
    """Load all Lengxuan codes from dictionary"""
    codes = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        pattern = r'^- ([a-zęóąśłżźćńüA-Z-]+) - .+$'
        matches = re.findall(pattern, content, re.MULTILINE)
        codes = [m.lower() for m in matches]
        
        return codes
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        return []

def check_exact_matches(lengxuan_codes, chinese_words):
    """Check for exact matches with Chinese words"""
    matches = []
    chinese_set = set(w.lower() for w in chinese_words)
    
    for code in lengxuan_codes:
        # Check base code (without hyphens)
        base_code = code.replace('-', '')
        if base_code in chinese_set:
            matches.append((code, base_code, 'exact'))
        
        # Check individual syllables
        syllables = code.split('-')
        for syllable in syllables:
            if syllable in chinese_set and len(syllable) > 1:
                matches.append((code, syllable, 'syllable'))
    
    return matches

def check_phonetic_similarity(lengxuan_codes, chinese_words, threshold=0.7):
    """Check for phonetically similar words"""
    similar = []
    
    for code in lengxuan_codes:
        base_code = code.replace('-', '')
        
        for chinese in chinese_words:
            # Use difflib to calculate similarity
            ratio = difflib.SequenceMatcher(None, base_code, chinese.lower()).ratio()
            
            if ratio >= threshold and len(base_code) > 2:
                similar.append((code, chinese, ratio))
    
    return similar

def analyze_syllable_structure(lengxuan_codes):
    """Analyze syllable structure to verify it follows Chinese-like patterns"""
    stats = {
        'total_codes': len(lengxuan_codes),
        'single_syllable': 0,
        'two_syllable': 0,
        'three_syllable': 0,
        'four_plus_syllable': 0,
        'max_syllables': 0,
        'avg_syllables': 0,
    }
    
    syllable_counts = []
    
    for code in lengxuan_codes:
        syllables = code.split('-')
        count = len(syllables)
        syllable_counts.append(count)
        
        if count == 1:
            stats['single_syllable'] += 1
        elif count == 2:
            stats['two_syllable'] += 1
        elif count == 3:
            stats['three_syllable'] += 1
        else:
            stats['four_plus_syllable'] += 1
        
        stats['max_syllables'] = max(stats['max_syllables'], count)
    
    if syllable_counts:
        stats['avg_syllables'] = sum(syllable_counts) / len(syllable_counts)
    
    return stats

def print_report(lengxuan_codes, exact_matches, similar_words, syllable_stats):
    """Print comprehensive report"""
    print("=" * 80)
    print("CHINESE CONTAMINATION CHECK - LENGXUAN DICTIONARY")
    print("=" * 80)
    print("\nCore Principle: 'Sound Chinese, but BE original'")
    print("\nThis tool verifies that NO Lengxuan words match actual Chinese words.")
    print("=" * 80)
    
    print(f"\n[INFO] Total Lengxuan codes analyzed: {len(lengxuan_codes)}")
    
    # Exact matches
    print("\n" + "=" * 80)
    print("1. EXACT MATCHES WITH CHINESE WORDS")
    print("=" * 80)
    
    if exact_matches:
        print(f"\n⚠️  WARNING: Found {len(exact_matches)} potential exact matches!")
        
        # Group by type
        exact_full = [m for m in exact_matches if m[2] == 'exact']
        exact_syllable = [m for m in exact_matches if m[2] == 'syllable']
        
        if exact_full:
            print(f"\n  Full code matches ({len(exact_full)}):")
            for lengxuan, chinese, _ in exact_full:
                print(f"    • {lengxuan} → matches Chinese: {chinese}")
        
        if exact_syllable:
            print(f"\n  Syllable matches ({len(exact_syllable)}):")
            # Group by Lengxuan code
            by_code = defaultdict(list)
            for lengxuan, chinese, _ in exact_syllable:
                by_code[lengxuan].append(chinese)
            
            for lengxuan, chinese_list in sorted(by_code.items()):
                print(f"    • {lengxuan} → contains: {', '.join(set(chinese_list))}")
    else:
        print("\n✓ EXCELLENT! No exact matches found.")
        print("  All Lengxuan codes are distinct from common Chinese words.")
    
    # Phonetic similarity
    print("\n" + "=" * 80)
    print("2. PHONETICALLY SIMILAR WORDS (>70% similarity)")
    print("=" * 80)
    
    if similar_words:
        print(f"\n⚠️  WARNING: Found {len(similar_words)} phonetically similar words!")
        
        # Sort by similarity (highest first)
        similar_words.sort(key=lambda x: x[2], reverse=True)
        
        print("\n  Top 20 most similar:")
        for i, (lengxuan, chinese, ratio) in enumerate(similar_words[:20], 1):
            print(f"    {i}. {lengxuan} ↔ {chinese} (similarity: {ratio:.2%})")
        
        if len(similar_words) > 20:
            print(f"\n  ... and {len(similar_words) - 20} more")
    else:
        print("\n✓ EXCELLENT! No phonetically similar words found.")
        print("  All Lengxuan codes are sufficiently distinct.")
    
    # Syllable structure
    print("\n" + "=" * 80)
    print("3. SYLLABLE STRUCTURE ANALYSIS")
    print("=" * 80)
    
    print(f"\n  Total codes: {syllable_stats['total_codes']}")
    print(f"  Single syllable: {syllable_stats['single_syllable']} ({syllable_stats['single_syllable']/syllable_stats['total_codes']*100:.1f}%)")
    print(f"  Two syllables: {syllable_stats['two_syllable']} ({syllable_stats['two_syllable']/syllable_stats['total_codes']*100:.1f}%)")
    print(f"  Three syllables: {syllable_stats['three_syllable']} ({syllable_stats['three_syllable']/syllable_stats['total_codes']*100:.1f}%)")
    print(f"  Four+ syllables: {syllable_stats['four_plus_syllable']} ({syllable_stats['four_plus_syllable']/syllable_stats['total_codes']*100:.1f}%)")
    print(f"  Max syllables: {syllable_stats['max_syllables']}")
    print(f"  Average syllables: {syllable_stats['avg_syllables']:.2f}")
    
    print("\n  Note: Chinese words are typically 1-2 syllables (characters).")
    print("  Longer compounds in Lengxuan help differentiate from Chinese.")
    
    # Final summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    
    issues = []
    if exact_matches:
        issues.append(f"Exact matches: {len(exact_matches)}")
    if similar_words:
        issues.append(f"Similar words: {len(similar_words)}")
    
    if issues:
        print("\n⚠️  ISSUES FOUND:")
        for issue in issues:
            print(f"  • {issue}")
        print("\n  STATUS: REQUIRES REVIEW")
        print("  ACTION: Review flagged words and consider replacements if needed.")
    else:
        print("\n✓ EXCELLENT!")
        print("  STATUS: NO CONTAMINATION DETECTED")
        print("  All Lengxuan words are distinct from common Chinese vocabulary.")
    
    print("\n" + "=" * 80)
    print("\nNote: This check uses a limited set of common Chinese words.")
    print("For comprehensive verification, use larger Chinese dictionaries:")
    print("  • CC-CEDICT (Mandarin)")
    print("  • Cantonese dictionaries")
    print("  • Classical Chinese corpus")
    print("=" * 80)

def save_report(lengxuan_codes, exact_matches, similar_words, syllable_stats, output_path):
    """Save report to file"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("CHINESE CONTAMINATION CHECK - LENGXUAN DICTIONARY\n")
        f.write("=" * 80 + "\n\n")
        
        f.write(f"Date: 2026-01-28\n")
        f.write(f"Total codes analyzed: {len(lengxuan_codes)}\n\n")
        
        f.write("EXACT MATCHES:\n")
        if exact_matches:
            f.write(f"Found {len(exact_matches)} matches\n\n")
            for lengxuan, chinese, match_type in exact_matches:
                f.write(f"  {lengxuan} → {chinese} ({match_type})\n")
        else:
            f.write("None found\n")
        
        f.write("\n\nPHONETICALLY SIMILAR (>70%):\n")
        if similar_words:
            f.write(f"Found {len(similar_words)} similar words\n\n")
            for lengxuan, chinese, ratio in similar_words:
                f.write(f"  {lengxuan} ↔ {chinese} ({ratio:.2%})\n")
        else:
            f.write("None found\n")
        
        f.write("\n\nSYLLABLE STRUCTURE:\n")
        f.write(f"  Single: {syllable_stats['single_syllable']}\n")
        f.write(f"  Two: {syllable_stats['two_syllable']}\n")
        f.write(f"  Three: {syllable_stats['three_syllable']}\n")
        f.write(f"  Four+: {syllable_stats['four_plus_syllable']}\n")
        f.write(f"  Average: {syllable_stats['avg_syllables']:.2f}\n")

def main():
    dict_path = "../03_Slownik/slownik_lengxuan_polski.new.md"
    report_path = "../05_Dokumentacja/raport_chinese_contamination.txt"
    
    print("Loading Lengxuan dictionary...")
    lengxuan_codes = load_lengxuan_codes(dict_path)
    
    if not lengxuan_codes:
        print("ERROR: Could not load dictionary!")
        return
    
    print(f"Loaded {len(lengxuan_codes)} codes\n")
    
    # Combine all Chinese word lists
    all_chinese = COMMON_CHINESE_WORDS + COMMON_CANTONESE_WORDS + CLASSICAL_CHINESE_WORDS
    
    print("Checking for exact matches...")
    exact_matches = check_exact_matches(lengxuan_codes, all_chinese)
    
    print("Checking for phonetic similarity...")
    similar_words = check_phonetic_similarity(lengxuan_codes, all_chinese, threshold=0.7)
    
    print("Analyzing syllable structure...")
    syllable_stats = analyze_syllable_structure(lengxuan_codes)
    
    # Print report
    print_report(lengxuan_codes, exact_matches, similar_words, syllable_stats)
    
    # Save report
    save_report(lengxuan_codes, exact_matches, similar_words, syllable_stats, report_path)
    print(f"\nReport saved to: {report_path}")

if __name__ == "__main__":
    main()
