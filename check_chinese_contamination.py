#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check for Chinese word contamination
Verify that NO Lengxuan words match actual Mandarin/Cantonese
"""

def load_dictionary(file_path):
    """Load Lengxuan→Polski dictionary"""
    entries = {}
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('- '):
                parts = line.strip().rsplit(' - ', 1)
                if len(parts) == 2:
                    code, polish = parts[0][2:], parts[1]
                    entries[code] = polish
    
    return entries

def check_chinese_contamination():
    """
    Check for potential Chinese word matches
    Common Mandarin syllables that should be avoided
    """
    
    # Common Mandarin words and phrases (pinyin romanization)
    # This is a sample list - comprehensive check would need full dictionary
    common_chinese = {
        # Greetings & basics
        'ni-hao', 'xie-xie', 'zai-jian', 'dui-bu-qi', 'qing',
        'shi', 'bu-shi', 'hao', 'hen-hao', 'xing',
        
        # Family
        'ma-ma', 'ba-ba', 'ge-ge', 'jie-jie', 'di-di', 'mei-mei',
        
        # Numbers
        'yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu', 'shi',
        
        # Common verbs
        'qu', 'lai', 'zou', 'pao', 'chi', 'he', 'shui', 'kan', 'ting',
        'shuo', 'wen', 'da', 'zuo', 'zhan', 'mai', 'mai', 'gei',
        
        # Common nouns
        'ren', 'tian', 'di', 'shui', 'huo', 'feng', 'yu', 'yun',
        'shan', 'he', 'lu', 'qiao', 'che', 'fang', 'men', 'chuang',
        
        # Colors (critical!)
        'hong', 'huang', 'lan', 'lü', 'bai', 'hei', 'hui',
        
        # Directions
        'dong', 'xi', 'nan', 'bei', 'shang', 'xia', 'zuo', 'you',
        
        # Time
        'nian', 'yue', 'ri', 'tian', 'xiao-shi', 'fen', 'miao',
        'jin-tian', 'ming-tian', 'zuo-tian',
        
        # Common adjectives
        'da', 'xiao', 'gao', 'di', 'chang', 'duan', 'kuai', 'man',
        'xin', 'jiu', 'duo', 'shao', 'hao', 'huai', 'piao-liang',
        
        # Measure words
        'ge', 'tiao', 'zhang', 'ben', 'zhi', 'kuai', 'wan', 'bei',
        
        # Common compounds (2-3 syllables)
        'zhong-guo', 'mei-guo', 'ri-ben', 'ying-guo', 'fa-guo',
        'bei-jing', 'shang-hai', 'guang-zhou', 'nan-jing',
        'xue-xiao', 'da-xue', 'lao-shi', 'xue-sheng',
        'peng-you', 'jia-ren', 'gong-si', 'gong-zuo',
    }
    
    lp_path = 'Lengxuan_Language/03_Slownik/slownik_lengxuan_polski.new.md'
    entries = load_dictionary(lp_path)
    
    print("🔍 CHINESE CONTAMINATION CHECK\n")
    print("=" * 80)
    print(f"\nChecking {len(entries)} Lengxuan words against {len(common_chinese)} common Chinese words...\n")
    
    # Check for exact matches
    exact_matches = []
    for code in entries:
        if code in common_chinese:
            exact_matches.append((code, entries[code]))
    
    # Check for similar single syllables (first part)
    single_syllable_chinese = {
        'ma', 'ba', 'ge', 'jie', 'di', 'mei',  # family
        'yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu', 'shi',  # numbers
        'qu', 'lai', 'zou', 'chi', 'he', 'kan', 'shuo', 'da', 'zuo',  # verbs
        'ren', 'tian', 'di', 'huo', 'feng', 'yu', 'shan', 'he', 'lu',  # nouns
        'hong', 'lan', 'bai', 'hei',  # colors
        'dong', 'xi', 'nan', 'bei',  # directions
        'da', 'xiao', 'gao', 'di', 'hao', 'xin', 'jiu',  # adjectives
    }
    
    single_syllable_matches = []
    for code in entries:
        # Check if code is single syllable or starts with Chinese syllable
        base = code.split('-')[0] if '-' in code else code
        if base in single_syllable_chinese:
            single_syllable_matches.append((code, entries[code], base))
    
    # Report results
    print("\n📊 RESULTS:\n")
    
    if exact_matches:
        print(f"❌ EXACT MATCHES FOUND: {len(exact_matches)}")
        print("   These codes are IDENTICAL to common Chinese words:\n")
        for code, polish in exact_matches[:20]:
            print(f"   {code:25} → {polish}")
        if len(exact_matches) > 20:
            print(f"   ... and {len(exact_matches) - 20} more")
    else:
        print("✅ NO EXACT MATCHES - No Lengxuan codes match common Chinese words exactly")
    
    print("\n" + "-" * 80 + "\n")
    
    if single_syllable_matches:
        print(f"⚠️  SINGLE-SYLLABLE MATCHES: {len(single_syllable_matches)}")
        print("   These codes START with common Chinese syllables:")
        print("   (May be acceptable if used in compounds)\n")
        
        # Group by root syllable
        by_root = {}
        for code, polish, root in single_syllable_matches:
            if root not in by_root:
                by_root[root] = []
            by_root[root].append((code, polish))
        
        for root in sorted(by_root.keys()):
            print(f"\n   Root '{root}' ({len(by_root[root])} words):")
            for code, polish in by_root[root][:5]:
                print(f"      {code:25} → {polish}")
            if len(by_root[root]) > 5:
                print(f"      ... and {len(by_root[root]) - 5} more")
    
    print("\n" + "=" * 80)
    print(f"\n📈 SUMMARY:")
    print(f"   Total Lengxuan words: {len(entries)}")
    print(f"   Exact Chinese matches: {len(exact_matches)}")
    print(f"   Single-syllable matches: {len(single_syllable_matches)}")
    
    contamination_rate = (len(exact_matches) + len(single_syllable_matches)) / len(entries) * 100
    print(f"   Potential contamination rate: {contamination_rate:.1f}%")
    
    if len(exact_matches) == 0:
        print("\n✅ PASS: No exact Chinese word matches!")
    else:
        print(f"\n❌ FAIL: {len(exact_matches)} exact matches need to be changed!")
    
    print("\n💡 RECOMMENDATION:")
    if len(exact_matches) > 0:
        print("   Priority: Change all exact matches immediately")
    if len(single_syllable_matches) > 50:
        print("   Consider: Review single-syllable matches (compound usage acceptable)")
    else:
        print("   Status: Single-syllable matches are acceptable in compounds")
    
    # Save report
    report_path = 'Lengxuan_Language/05_Dokumentacja/raport_chinese_contamination.txt'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("CHINESE CONTAMINATION REPORT\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Total Lengxuan words: {len(entries)}\n")
        f.write(f"Exact Chinese matches: {len(exact_matches)}\n")
        f.write(f"Single-syllable matches: {len(single_syllable_matches)}\n\n")
        
        if exact_matches:
            f.write("EXACT MATCHES (CRITICAL):\n")
            f.write("-" * 80 + "\n")
            for code, polish in exact_matches:
                f.write(f"{code:25} → {polish}\n")
            f.write("\n")
        
        if single_syllable_matches:
            f.write("SINGLE-SYLLABLE MATCHES (Review):\n")
            f.write("-" * 80 + "\n")
            for code, polish, root in single_syllable_matches:
                f.write(f"{code:25} → {polish:40} (root: {root})\n")
    
    print(f"\n📄 Report saved to: {report_path}")

if __name__ == "__main__":
    check_chinese_contamination()
