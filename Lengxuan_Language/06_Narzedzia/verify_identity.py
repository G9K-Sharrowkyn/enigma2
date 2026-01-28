# -*- coding: utf-8 -*-
"""
VERIFY DICTIONARY IDENTITY - LENGXUAN

Ensures both dictionaries (Lengxuan→Polski and Polski→Lengxuan) contain
identical (code, meaning) pairs, just in different sort orders.

Requirements:
- Both dictionaries must have same number of entries
- Each (code, polish) pair in L→P must exist in P→L
- No duplicates in either dictionary
"""

import re
from collections import defaultdict

def load_dict_entries(file_path, dict_type):
    """Load dictionary entries"""
    entries = []
    duplicates = defaultdict(list)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        for i, line in enumerate(lines, 1):
            line = line.strip()
            if line.startswith('- '):
                # Use rsplit to handle " - " in descriptions
                parts = line[2:].rsplit(' - ', 1)
                
                if len(parts) == 2:
                    if dict_type == 'lengxuan_polish':
                        code, polish = parts
                        entries.append((code.strip(), polish.strip()))
                    else:  # polish_lengxuan
                        polish, code = parts
                        entries.append((code.strip(), polish.strip()))
                    
                    # Check for duplicates
                    key = (parts[0].strip(), parts[1].strip())
                    duplicates[key].append(i)
                else:
                    print(f"[WARNING] Line {i}: Could not parse: {line}")
        
        return entries, duplicates
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        return [], {}

def verify_identity(lp_entries, pl_entries):
    """Verify both dictionaries contain identical pairs"""
    lp_set = set(lp_entries)
    pl_set = set(pl_entries)
    
    # Check for entries in L→P but not in P→L
    only_in_lp = lp_set - pl_set
    
    # Check for entries in P→L but not in L→P
    only_in_pl = pl_set - lp_set
    
    return only_in_lp, only_in_pl

def check_duplicates(duplicates):
    """Check for duplicate entries"""
    actual_duplicates = {}
    
    for key, line_numbers in duplicates.items():
        if len(line_numbers) > 1:
            actual_duplicates[key] = line_numbers
    
    return actual_duplicates

def print_report(lp_entries, pl_entries, lp_dups, pl_dups, only_in_lp, only_in_pl):
    """Print verification report"""
    print("=" * 80)
    print("DICTIONARY IDENTITY VERIFICATION - LENGXUAN")
    print("=" * 80)
    
    print(f"\n[INFO] Lengxuan→Polski entries: {len(lp_entries)}")
    print(f"[INFO] Polski→Lengxuan entries: {len(pl_entries)}")
    
    # Check count
    print("\n" + "=" * 80)
    print("1. ENTRY COUNT VERIFICATION")
    print("=" * 80)
    
    if len(lp_entries) == len(pl_entries):
        print(f"\n✓ PASS: Both dictionaries have {len(lp_entries)} entries")
    else:
        print(f"\n✗ FAIL: Entry count mismatch!")
        print(f"  Lengxuan→Polski: {len(lp_entries)}")
        print(f"  Polski→Lengxuan: {len(pl_entries)}")
        print(f"  Difference: {abs(len(lp_entries) - len(pl_entries))}")
    
    # Check duplicates
    print("\n" + "=" * 80)
    print("2. DUPLICATE CHECK")
    print("=" * 80)
    
    lp_actual_dups = check_duplicates(lp_dups)
    pl_actual_dups = check_duplicates(pl_dups)
    
    if not lp_actual_dups and not pl_actual_dups:
        print("\n✓ PASS: No duplicates found in either dictionary")
    else:
        if lp_actual_dups:
            print(f"\n✗ FAIL: Found {len(lp_actual_dups)} duplicates in Lengxuan→Polski:")
            for key, lines in list(lp_actual_dups.items())[:10]:
                print(f"  {key[0]} - {key[1]} (lines: {lines})")
            if len(lp_actual_dups) > 10:
                print(f"  ... and {len(lp_actual_dups) - 10} more")
        
        if pl_actual_dups:
            print(f"\n✗ FAIL: Found {len(pl_actual_dups)} duplicates in Polski→Lengxuan:")
            for key, lines in list(pl_actual_dups.items())[:10]:
                print(f"  {key[0]} - {key[1]} (lines: {lines})")
            if len(pl_actual_dups) > 10:
                print(f"  ... and {len(pl_actual_dups) - 10} more")
    
    # Check identity
    print("\n" + "=" * 80)
    print("3. IDENTITY VERIFICATION")
    print("=" * 80)
    
    if not only_in_lp and not only_in_pl:
        print("\n✓ PASS: Both dictionaries contain identical (code, polish) pairs")
    else:
        if only_in_lp:
            print(f"\n✗ FAIL: Found {len(only_in_lp)} entries only in Lengxuan→Polski:")
            for code, polish in list(only_in_lp)[:10]:
                print(f"  {code} - {polish}")
            if len(only_in_lp) > 10:
                print(f"  ... and {len(only_in_lp) - 10} more")
        
        if only_in_pl:
            print(f"\n✗ FAIL: Found {len(only_in_pl)} entries only in Polski→Lengxuan:")
            for code, polish in list(only_in_pl)[:10]:
                print(f"  {code} - {polish}")
            if len(only_in_pl) > 10:
                print(f"  ... and {len(only_in_pl) - 10} more")
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    
    issues = []
    if len(lp_entries) != len(pl_entries):
        issues.append("Entry count mismatch")
    if lp_actual_dups or pl_actual_dups:
        issues.append("Duplicates found")
    if only_in_lp or only_in_pl:
        issues.append("Identity mismatch")
    
    if issues:
        print("\n✗ VERIFICATION FAILED")
        print("\nIssues found:")
        for issue in issues:
            print(f"  • {issue}")
        print("\nSTATUS: DICTIONARIES NEED SYNCHRONIZATION")
    else:
        print("\n✓ VERIFICATION PASSED")
        print("\nSTATUS: DICTIONARIES ARE SYNCHRONIZED")
        print("Both dictionaries contain identical (code, polish) pairs.")
    
    print("\n" + "=" * 80)

def save_report(lp_entries, pl_entries, only_in_lp, only_in_pl, output_path):
    """Save verification report"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("DICTIONARY IDENTITY VERIFICATION - LENGXUAN\n")
        f.write("=" * 80 + "\n\n")
        
        f.write(f"Date: 2026-01-28\n")
        f.write(f"Lengxuan→Polski entries: {len(lp_entries)}\n")
        f.write(f"Polski→Lengxuan entries: {len(pl_entries)}\n\n")
        
        if len(lp_entries) == len(pl_entries):
            f.write("Entry count: PASS\n")
        else:
            f.write(f"Entry count: FAIL (difference: {abs(len(lp_entries) - len(pl_entries))})\n")
        
        if not only_in_lp and not only_in_pl:
            f.write("Identity: PASS\n")
        else:
            f.write("Identity: FAIL\n\n")
            
            if only_in_lp:
                f.write(f"\nOnly in Lengxuan→Polski ({len(only_in_lp)}):\n")
                for code, polish in only_in_lp:
                    f.write(f"  {code} - {polish}\n")
            
            if only_in_pl:
                f.write(f"\nOnly in Polski→Lengxuan ({len(only_in_pl)}):\n")
                for code, polish in only_in_pl:
                    f.write(f"  {code} - {polish}\n")

def main():
    lp_path = "../03_Slownik/slownik_lengxuan_polski.new.md"
    pl_path = "../03_Slownik/slownik_polski_lengxuan.new.md"
    report_path = "../05_Dokumentacja/raport_identity.txt"
    
    print("Loading Lengxuan→Polski dictionary...")
    lp_entries, lp_dups = load_dict_entries(lp_path, 'lengxuan_polish')
    
    print("Loading Polski→Lengxuan dictionary...")
    pl_entries, pl_dups = load_dict_entries(pl_path, 'polish_lengxuan')
    
    if not lp_entries or not pl_entries:
        print("ERROR: Could not load dictionaries!")
        return
    
    print(f"\nVerifying identity...\n")
    
    only_in_lp, only_in_pl = verify_identity(lp_entries, pl_entries)
    
    # Print report
    print_report(lp_entries, pl_entries, lp_dups, pl_dups, only_in_lp, only_in_pl)
    
    # Save report
    save_report(lp_entries, pl_entries, only_in_lp, only_in_pl, report_path)
    print(f"\nReport saved to: {report_path}")

if __name__ == "__main__":
    main()
