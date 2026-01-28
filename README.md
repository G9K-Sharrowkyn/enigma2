# Lengxuan Language Project

**Lengxuan** is a fictional constructed language (conlang) inspired by ancient Chinese, designed for use in a novel. The language aims to sound authentically Chinese while using NO actual Chinese words or direct borrowings.

## Core Principle

> **"Sound Chinese, but BE original"**

For example:
- Chinese: 谢谢 (xiè xie) = "thank you"  
- Lengxuan: **poye** = "thank you"

**CRITICAL RULE**: No Lengxuan word should be identical or similar to actual Chinese words. The language must maintain phonological authenticity while being semantically independent.

---

## Project Status

### Current State
- **2,718 dictionary entries** (bidirectional: Lengxuan ↔ Polish)
- **750+ semantic corrections applied**
- **23 semantic groups** reorganized for consistency
- **8 color families** unified with shared roots
- Zero homonymy (1:1 word mapping guaranteed)

### Completed Improvements
✅ Capitalization standardization (634 fixes)  
✅ Professional suffixes (-ren for occupations: 11 fixes)  
✅ Semantic root consistency (66 changes across 23 groups)  
✅ Color families unified (20 changes across 8 color groups)  
✅ Duplicate removal and cleanup (17 malformed entries)  
✅ Problematic entries removed (2 non-Chinese terms)

---

## Semantic System

Lengxuan uses **semantic roots** - related concepts share common root morphemes:

### Examples of Semantic Families

#### Colors (8 families)
- **nan** (green): nan, nan-liu (green grass), nan-qie (green vegetables), nan-tun (bright green)
- **mao** (red): mao, mao-ban (red bird), mao-chuang (bright red), mao-gen (dark red)
- **mei** (black): mei, mei-da (black warrior), mei-pei (black bear), mei-bu (black crow)
- **nou** (yellow/gold): nou, nou-gang (earthy yellow), nou-chou (golden-yellow)

#### Actions (15 families)
- **tao** (laugh): tao-pin (laugh), tao-mai (laugh joyfully), tao-bin (smile)
- **mou** (cook): mou-wen (cook), mou-kang (steamed), mou-dan (steam), mou-jing (cook rice)
- **ma** (teach/learn): ma (teach), ma-ren (teacher), ma-cha (student), ma-lu (study)
- **mu** (write): mu (write), mu-ren (writer), mu-pei (write letter)

#### Professions (-ren suffix)
All occupations use the **-ren** (person) suffix:
- yue-ren (musician), zhe-ren (philosopher), shi-ren (historian), hua-ren (painter)

---

## Known Issues & Quality Concerns

### 1. **Chinese Word Contamination** ⚠️
**PRIORITY**: Verify that NO Lengxuan words match actual Chinese.

**How to check:**
- Cross-reference with Mandarin, Cantonese, and Classical Chinese dictionaries
- Use pinyin romanization comparison tools
- Check for phonological similarity (not just exact matches)

**Tools needed:**
```python
# Compare against Chinese dictionary API
# Flag words with >70% phonetic similarity
# Manual review for borderline cases
```

### 2. **Remaining Semantic Inconsistencies**
**Status**: 8 groups identified but NOT yet fixed:

#### A. Direction/Geography (16 words, 16 different roots)
- Issue: Cardinal directions (east, west, north, south) don't share roots
- Example: `chao-mo` (east), `gou-ka` (west), `mao-chi` (northeast)
- **Fix needed**: Unify under directional root system (e.g., fang-dong, fang-xi)

#### B. Food/Eating (mixed roots)
- Issue: Cooking methods scattered across unrelated roots
- Already fixed: `mou-*` (general cooking), `da-*` (frying)
- Still needs: Baking, roasting, boiling subcategories

#### C. Medical/Body Terms (no systematic root)
- Issue: Body parts, illnesses, treatments use random codes
- **Fix needed**: Establish anatomical root system

#### D. Nature/Weather (partially organized)
- Fixed: Some weather terms
- Needs: Plants, animals, geological features

### 3. **Long Compound Codes** ⚠️
**Issue**: Some codes are excessively long (>25 characters)

Examples:
- `xiu-ken-guan` (swimming in wind and waves)
- `piao-pa-nie` (cannot stop 10,000 people - idiom)

**Recommendation**: 
- Compound codes should be max 3-4 syllables
- Idioms might need abbreviated forms

### 4. **Derivative Coverage**
**Status**: ~1,800 words still use non-semantic roots

**Target**: 
- Base roots: 300 (✅ complete)
- Semantic derivatives: 535 (✅ complete)
- **Remaining**: 1,883 words need semantic mapping or simplification

---

## Quality Assurance Checklist

### Before Accepting New Words:

- [ ] **Phonological Check**: Does it sound Chinese? (use syllable structure rules)
- [ ] **Uniqueness Check**: Is it different from actual Chinese words?
- [ ] **Semantic Check**: Does it fit into an existing semantic family?
- [ ] **Homonymy Check**: Is the (code, meaning) pair unique?
- [ ] **Root Consistency**: If related word exists, does it share the root?
- [ ] **Length Check**: Is the code ≤20 characters?

### Automated Tools Available:

1. **`verify_identity.py`** ✅ - Check dictionary synchronization
2. **`check_chinese_contamination.py`** ✅ - Verify no overlap with Chinese words
3. **`analyze_code_lengths.py`** ✅ - Check code length limits
4. **`find_semantic_inconsistencies.py`** ✅ - Find words that should share roots
5. **`find_color_inconsistencies.py`** 🔜 - Verify color family consistency
6. **`apply_all_semantic_fixes.py`** 🔜 - Apply systematic corrections
7. **`fix_all_colors.py`** 🔜 - Unify color families

✅ = Available now | 🔜 = Planned

---

## Roadmap to Perfection

### Phase 1: Verification (HIGH PRIORITY)
- [ ] **Chinese contamination scan** - Verify zero overlap with Mandarin/Cantonese
- [ ] Cross-check with Wade-Giles, Pinyin, and Zhuyin romanization systems
- [ ] Flag phonologically similar words (>70% match threshold)

### Phase 2: Complete Semantic Mapping
- [ ] Directions/Geography family (16 words)
- [ ] Medical/Anatomy family (~50 words)
- [ ] Nature/Plants family (~80 words)
- [ ] Animals family (~60 words)
- [ ] Food/Cooking completion (~40 words)
- [ ] Emotions/States (~35 words)

### Phase 3: Code Optimization
- [ ] Shorten compound codes (target: max 20 chars)
- [ ] Create abbreviated idiom forms
- [ ] Establish 2-syllable base + 1-2 syllable modifier pattern

### Phase 4: Grammar Integration
- [ ] Verify all particles have unique codes
- [ ] Ensure measure words follow systematic pattern
- [ ] Check aspect markers for consistency

### Phase 5: Final Audit
- [ ] Professional linguist review (Chinese language expert)
- [ ] Native Chinese speaker phonetic test
- [ ] Conlang community peer review
- [ ] Automated clash detection (run against Chinese corpora)

---

## Contributing Guidelines

### When Adding New Words:

1. **Research**: Check if similar meaning exists (might be derivative)
2. **Root Selection**: Use existing root if semantic relationship exists
3. **Phonology**: Follow syllable structure rules (see `01_Fonologia/`)
4. **Testing**: Run all verification scripts before committing
5. **Documentation**: Add entry to changelog with justification

### When Modifying Existing Words:

1. **Impact Analysis**: Check how many related words affected
2. **Consistency**: Update entire semantic family together
3. **Backup**: Scripts automatically backup to `in case/` folder
4. **Verification**: Run `verify_identity.py` after changes

---

## File Structure

```
Lengxuan_Language/
├── 01_Fonologia/          # Phonology & transcription rules
├── 02_Gramatyka/          # Grammar & syntax
├── 03_Slownik/            # Dictionaries (main files)
│   ├── slownik_lengxuan_polski.new.md (L→PL, 2718 entries)
│   └── slownik_polski_lengxuan.new.md (PL→L, 2718 entries)
├── 04_Przyklady/          # Example dialogues
├── 05_Dokumentacja/       # Reports & changelogs
└── 06_Narzedzia/          # Python tools for maintenance

in case/                   # Automatic backups
```

---

## Technical Notes

### Dictionary Format
```markdown
- code - polish description
```

### Parsing Rules
- Use `rsplit(' - ', 1)` to split (handles idioms with " - " in description)
- Both dictionaries must contain identical (code, polish) pairs
- Sort order: Lengxuan→Polski by code, Polski→Lengxuan by Polish (case-insensitive)

### Known Parsing Issues
- Terminal wrapping can break long idiom descriptions
- ~~Fixed by removing lines where code contains `(idiom` or uppercase letters~~
- **✅ VERIFIED**: No codes contain `(idiom` or uppercase letters (except 2 proper names)
- All dictionary entries are properly formatted

---

## Quality Reports

### Comprehensive Analysis (Jan 28, 2026)

📊 **[Read Full Quality Report](Lengxuan_Language/05_Dokumentacja/comprehensive_quality_report.md)**

**Key Findings:**
- ✅ **Dictionary Sync**: 100% - Perfect synchronization (2,718 entries)
- ✅ **Code Lengths**: 100% - All codes within optimal limits (max 15 chars)
- ✅ **Homonymy**: 100% - Zero duplicates maintained
- ⚠️ **Chinese Overlap**: 76 single-syllable matches with Chinese - needs policy decision
- ⚠️ **Semantic Consistency**: 65% - 293 words need semantic organization (8 groups)

**Overall Quality Score: 85%**

### Individual Reports Available:
- `raport_identity.txt` - Dictionary synchronization verification
- `raport_code_lengths.txt` - Length and syllable analysis
- `raport_chinese_contamination.txt` - Chinese word overlap analysis
- `raport_semantic_inconsistencies.txt` - Semantic family consistency check

---

## Credits

**Language Design**: G9K-Sharrowkyn  
**Semantic Consistency System**: Developed through iterative refinement (Jan 2026)  
**Tools**: Python 3.x automation scripts  

---

## License

This is a fictional language created for literary purposes. Free to use for non-commercial creative works with attribution.

---

## Quick Start

### For Dictionary Maintenance:
```bash
cd Lengxuan_Language/06_Narzedzia/

# Verify both dictionaries are identical
python3 verify_identity.py

# Check for Chinese word contamination
python3 check_chinese_contamination.py

# Analyze code lengths
python3 analyze_code_lengths.py

# Find semantic inconsistencies
python3 find_semantic_inconsistencies.py
```

### For Adding New Words:
```bash
cd Lengxuan_Language/06_Narzedzia/

# 1. Check if semantic family exists
python3 find_semantic_inconsistencies.py

# 2. Add to both dictionaries manually
# Edit: 03_Slownik/slownik_lengxuan_polski.new.md
# Edit: 03_Slownik/slownik_polski_lengxuan.new.md

# 3. Run verification
python3 verify_identity.py
```

---

## Status: 🟡 In Development

**Current Quality**: 85% complete  
**Remaining Work**: Chinese contamination verification, final semantic mapping (1,800 words)  

**Last Updated**: January 28, 2026  
**Dictionary Version**: 2718 entries (synchronized)
