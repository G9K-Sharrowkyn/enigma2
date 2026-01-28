#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix core body parts to use consistent anatomical roots
Focus ONLY on primary body parts, not false positives
"""

def create_body_part_mappings():
    """
    Unify basic body parts under anatomical roots
    Lengxuan approach: Traditional Chinese Medicine (TCM) inspired
    """
    
    mappings = {
        # PRIMARY BODY PARTS - manual selection after verification
        
        # HEAD/FACE REGION - tou- root (head)
        # 'chao': 'tou',                # głowa → head (ALREADY tou in semantic)
        # 'chen': 'tou-yan',            # oko → eye
        # 'chou': 'tou-er',             # ucho → ear
        # 'chua': 'tou-bi',             # nos → nose
        # 'chui': 'tou-kou',            # usta → mouth
        
        # LIMBS - zhi- root (limbs)
        # 'cang': 'zhi-shou',           # ręka → hand
        # 'chai': 'zhi-jiao',           # noga → leg
        # 'chan': 'zhi-zu',             # stopa → foot
        # 'ceng': 'zhi-zhi',            # palec → finger
        
        # TORSO - shen- root (body)
        # 'chuango': 'shen-xiong',      # klatka piersiowa → chest
        # 'de-tian': 'shen-fu',         # brzuch → belly
        # 'eng-jin': 'shen-jing',       # szyja → neck
        # 'dang-ruo': 'shen-bi',        # ramię (bark) → shoulder
        
        # INTERNAL ORGANS (TCM) - zang- root
        # Keep existing TCM terms as-is (they're culturally specific):
        # - ren-ban (Płuco / Lung organ)
        # - jia-tui (Jelito cienkie / Small Intestine)
        # - zhui-wen (Jelito grube / Large Intestine)
        # - duan-cuan (nerka / kidney)
        # - kuo-jiong (żołądek / stomach)
        
        # Actually, let me check what we have first...
    }
    
    return mappings

def analyze_body_parts():
    """Just analyze what we have for body parts - don't change yet"""
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
    
    print("🩺 BODY PARTS ANALYSIS (Primary Only)\n")
    print("=" * 80)
    
    # Core body parts we want to unify
    core_body_parts = {
        'głowa': [],
        'oko': [],
        'oczy': [],
        'ucho': [],
        'nos': [],
        'usta': [],
        'język (organ)': [],
        'szyja': [],
        'ramię': [],
        'ręka': [],
        'dłoń': [],
        'palec': [],
        'noga': [],
        'stopa': [],
        'klatka piersiowa': [],
        'brzuch': [],
        'serce': [],
        'płuco': [],
        'kość': [],
        'krew': [],
    }
    
    # Find exact matches only
    for code, polish in lp_entries.items():
        polish_clean = polish.lower().strip()
        if polish_clean in core_body_parts:
            core_body_parts[polish_clean].append((code, polish))
    
    print("\n### CORE BODY PARTS (exact matches only):\n")
    
    for part in sorted(core_body_parts.keys()):
        matches = core_body_parts[part]
        if matches:
            for code, polish in matches:
                print(f"  {part:25} → {code:15} ({polish})")
    
    print("\n" + "=" * 80)
    print("\n💡 ANALYSIS:")
    print("   These are the PRIMARY body parts we should organize")
    print("   Next step: Decide on semantic roots for each category")

if __name__ == "__main__":
    analyze_body_parts()
