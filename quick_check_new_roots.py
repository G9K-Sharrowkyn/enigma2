#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quick check if new emotion roots match Chinese"""

common_chinese = [
    'wo', 'ni', 'ta', 'men', 'de', 'shi', 'zai', 'you', 'yi', 'er', 'san', 'si', 'wu',
    'liu', 'qi', 'ba', 'jiu', 'shi', 'bai', 'qian', 'wan', 'nian', 'yue', 'ri', 'tian',
    'ren', 'shui', 'huo', 'tu', 'jin', 'mu', 'da', 'xiao', 'shang', 'xia', 'zhong',
    'lai', 'qu', 'shuo', 'kan', 'ting', 'chi', 'he', 'zou', 'zuo', 'dou', 'xie', 'zhi',
    'dao', 'hui', 'neng', 'yao', 'xiang', 'guo', 'jia', 'ge', 'wei', 'bu', 'mei', 'hen',
    'zhe', 'le', 'ma', 'ne', 'ba', 'a', 'ya', 'o', 'ei', 'ai', 'hao', 'dui', 'wen', 'da',
    'sheng', 'xin', 'shou', 'yan', 'er', 'tou', 'jiao', 'lian', 'xiang', 'sheng', 'shuo',
    'hua', 'wen', 'yu', 'yan', 'wen', 'ti', 'wen', 'da', 'shu', 'zi', 'shu', 'xue',
    'ke', 'cheng', 'xue', 'xiao', 'lao', 'shi', 'xue', 'sheng', 'tong', 'xue', 'ban',
    'ji', 'kao', 'shi', 'wen', 'ti', 'da', 'an', 'cheng', 'ji', 'fen', 'shu'
]

new_roots = ['huano', 'beio', 'nuo', 'ru', 'ango', 'rongo']

print("🔍 SPRAWDZENIE NOWYCH ROOTÓW EMOCJI\n")
print("=" * 60)

contaminated = []
for root in new_roots:
    if root in common_chinese:
        contaminated.append(root)
        print(f"❌ {root:15} - KONTAMINACJA!")
    else:
        print(f"✅ {root:15} - OK")

print("\n" + "=" * 60)
if contaminated:
    print(f"\n⚠️  ZNALEZIONO {len(contaminated)} KONTAMINACJI: {', '.join(contaminated)}")
else:
    print("\n✅ WSZYSTKIE NOWE ROOTY CZYSTE - BRAK KONTAMINACJI CHIŃSKIEJ!")
