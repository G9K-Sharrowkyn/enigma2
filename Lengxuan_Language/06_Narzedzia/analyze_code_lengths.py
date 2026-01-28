# -*- coding: utf-8 -*-
"""
ANALYZE CODE LENGTHS IN LENGXUAN DICTIONARY

Identifies excessively long compound codes that should be shortened.

Recommendation:
- Compound codes should be max 3-4 syllables
- Max length: 20 characters
- Idioms might need abbreviated forms
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
                'meaning': meaning,
                'length': len(code),
                'syllables': len(code.split('-'))
            })
        
        return entries
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        return []

def analyze_lengths(entries):
    """Analyze code lengths"""
    stats = {
        'total': len(entries),
        'short': 0,  # 1-10 chars
        'medium': 0,  # 11-20 chars
        'long': 0,  # 21-30 chars
        'very_long': 0,  # 31+ chars
        'max_length': 0,
        'avg_length': 0,
        'by_syllables': defaultdict(int),
    }
    
    total_length = 0
    long_codes = []
    very_long_codes = []
    
    for entry in entries:
        length = entry['length']
        syllables = entry['syllables']
        
        total_length += length
        stats['by_syllables'][syllables] += 1
        stats['max_length'] = max(stats['max_length'], length)
        
        if length <= 10:
            stats['short'] += 1
        elif length <= 20:
            stats['medium'] += 1
        elif length <= 30:
            stats['long'] += 1
            long_codes.append(entry)
        else:
            stats['very_long'] += 1
            very_long_codes.append(entry)
            long_codes.append(entry)
    
    if entries:
        stats['avg_length'] = total_length / len(entries)
    
    return stats, long_codes, very_long_codes

def print_report(entries, stats, long_codes, very_long_codes):
    """Print analysis report"""
    print("=" * 80)
    print("CODE LENGTH ANALYSIS - LENGXUAN DICTIONARY")
    print("=" * 80)
    
    print(f"\n[INFO] Total entries analyzed: {stats['total']}")
    
    # Length distribution
    print("\n" + "=" * 80)
    print("LENGTH DISTRIBUTION")
    print("=" * 80)
    
    print(f"\n  Short (1-10 chars): {stats['short']} ({stats['short']/stats['total']*100:.1f}%)")
    print(f"  Medium (11-20 chars): {stats['medium']} ({stats['medium']/stats['total']*100:.1f}%)")
    print(f"  Long (21-30 chars): {stats['long']} ({stats['long']/stats['total']*100:.1f}%)")
    print(f"  Very Long (31+ chars): {stats['very_long']} ({stats['very_long']/stats['total']*100:.1f}%)")
    
    print(f"\n  Max length: {stats['max_length']} characters")
    print(f"  Average length: {stats['avg_length']:.1f} characters")
    
    # Syllable distribution
    print("\n" + "=" * 80)
    print("SYLLABLE DISTRIBUTION")
    print("=" * 80)
    
    for syllables in sorted(stats['by_syllables'].keys()):
        count = stats['by_syllables'][syllables]
        percent = count / stats['total'] * 100
        print(f"  {syllables} syllable(s): {count} ({percent:.1f}%)")
    
    # Very long codes
    if very_long_codes:
        print("\n" + "=" * 80)
        print("⚠️  VERY LONG CODES (31+ characters)")
        print("=" * 80)
        print(f"\nFound {len(very_long_codes)} very long codes that should be shortened:\n")
        
        for entry in sorted(very_long_codes, key=lambda x: x['length'], reverse=True):
            print(f"  {entry['length']} chars, {entry['syllables']} syllables:")
            print(f"    {entry['code']} → {entry['meaning']}")
            print()
    else:
        print("\n✓ No very long codes (31+ chars) found.")
    
    # Long codes (21-30 chars)
    if stats['long'] > 0:
        print("\n" + "=" * 80)
        print("⚠️  LONG CODES (21-30 characters)")
        print("=" * 80)
        print(f"\nFound {stats['long']} long codes that might need shortening:\n")
        
        # Show only codes not already shown in very_long
        long_only = [e for e in long_codes if e['length'] <= 30]
        
        for entry in sorted(long_only, key=lambda x: x['length'], reverse=True)[:20]:
            print(f"  {entry['length']} chars, {entry['syllables']} syllables:")
            print(f"    {entry['code']} → {entry['meaning']}")
        
        if len(long_only) > 20:
            print(f"\n  ... and {len(long_only) - 20} more")
    else:
        print("\n✓ No long codes (21-30 chars) found.")
    
    # Recommendations
    print("\n" + "=" * 80)
    print("RECOMMENDATIONS")
    print("=" * 80)
    
    if very_long_codes or stats['long'] > 0:
        print("\n⚠️  ACTION NEEDED:")
        print("\n  Target lengths:")
        print("    • Single words: 2-8 characters (1-2 syllables)")
        print("    • Compounds: 9-15 characters (2-3 syllables)")
        print("    • Complex terms: 16-20 characters (3-4 syllables)")
        print("    • Maximum: 20 characters")
        
        print("\n  Strategies for shortening:")
        print("    1. Use abbreviations for common components")
        print("    2. Create base words for semantic families")
        print("    3. Replace long descriptive compounds with shorter roots")
        print("    4. For idioms, create abbreviated forms")
        
        if very_long_codes:
            print(f"\n  Priority: {len(very_long_codes)} codes over 30 characters (IMMEDIATE)")
        if stats['long'] > 0:
            print(f"  Review: {stats['long']} codes 21-30 characters (SOON)")
    else:
        print("\n✓ EXCELLENT!")
        print("  All codes are within reasonable length limits.")
    
    print("\n" + "=" * 80)

def save_report(entries, stats, long_codes, very_long_codes, output_path):
    """Save report to file"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("CODE LENGTH ANALYSIS - LENGXUAN DICTIONARY\n")
        f.write("=" * 80 + "\n\n")
        
        f.write(f"Date: 2026-01-28\n")
        f.write(f"Total entries: {stats['total']}\n")
        f.write(f"Max length: {stats['max_length']} characters\n")
        f.write(f"Average length: {stats['avg_length']:.1f} characters\n\n")
        
        f.write("LENGTH DISTRIBUTION:\n")
        f.write(f"  Short (1-10): {stats['short']}\n")
        f.write(f"  Medium (11-20): {stats['medium']}\n")
        f.write(f"  Long (21-30): {stats['long']}\n")
        f.write(f"  Very Long (31+): {stats['very_long']}\n\n")
        
        f.write("SYLLABLE DISTRIBUTION:\n")
        for syllables in sorted(stats['by_syllables'].keys()):
            count = stats['by_syllables'][syllables]
            f.write(f"  {syllables} syllable(s): {count}\n")
        
        if very_long_codes:
            f.write("\n\nVERY LONG CODES (31+ chars):\n")
            f.write("=" * 80 + "\n\n")
            for entry in sorted(very_long_codes, key=lambda x: x['length'], reverse=True):
                f.write(f"{entry['length']} chars, {entry['syllables']} syllables:\n")
                f.write(f"  {entry['code']} → {entry['meaning']}\n\n")
        
        if stats['long'] > 0:
            f.write("\n\nLONG CODES (21-30 chars):\n")
            f.write("=" * 80 + "\n\n")
            long_only = [e for e in long_codes if e['length'] <= 30]
            for entry in sorted(long_only, key=lambda x: x['length'], reverse=True):
                f.write(f"{entry['length']} chars, {entry['syllables']} syllables:\n")
                f.write(f"  {entry['code']} → {entry['meaning']}\n\n")

def main():
    dict_path = "../03_Slownik/slownik_lengxuan_polski.new.md"
    report_path = "../05_Dokumentacja/raport_code_lengths.txt"
    
    print("Loading dictionary...")
    entries = load_dictionary(dict_path)
    
    if not entries:
        print("ERROR: Could not load dictionary!")
        return
    
    print(f"Loaded {len(entries)} entries\n")
    
    print("Analyzing code lengths...")
    stats, long_codes, very_long_codes = analyze_lengths(entries)
    
    # Print report
    print_report(entries, stats, long_codes, very_long_codes)
    
    # Save report
    save_report(entries, stats, long_codes, very_long_codes, report_path)
    print(f"\nReport saved to: {report_path}")

if __name__ == "__main__":
    main()
