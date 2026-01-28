#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from collections import defaultdict

def analyze_dictionary():
    """Analizuje słownik i znajduje grupy semantyczne bez spójności fonetycznej"""
    
    with open('Lengxuan_Language/03_Slownik/slownik_polski_lengxuan.new.md', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Zbierz wszystkie wpisy
    entries = []
    for line in lines:
        if line.startswith('- '):
            match = re.match(r'- ([^-]+) - (.+)', line)
            if match:
                polish = match.group(1).strip()
                lengxuan = match.group(2).strip()
                entries.append((polish.lower(), lengxuan, polish))
    
    # Definicje grup semantycznych do sprawdzenia
    semantic_groups = {
        'słodki': ['słodki', 'słodko-kwaśny', 'słodko-kwaśne', 'słodki sos'],
        'taoizm': ['taoizm', 'taoistyczny', 'tao'],
        'budda': ['budda', 'buddyzm', 'buddyjski'],
        'mistrz': ['mistrz', 'mistrzowski', 'mistrzostwo'],
        'uczeń': ['uczeń', 'uczennica', 'uczenie'],
        'ojciec': ['ojciec', 'ojczyzna'],
        'matka': ['matka', 'macierzyństwo'],
        'brat': ['brat', 'braterski', 'braterstwo'],
        'siostra': ['siostra', 'siostrzany'],
        'czerwony': ['czerwony', 'czerwień'],
        'biały': ['biały', 'biel'],
        'czarny': ['czarny', 'czerń'],
        'zielony': ['zielony', 'zieleń'],
        'niebieski': ['niebieski', 'błękit'],
        'żółty': ['żółty', 'żółć'],
        'góra': ['góra', 'górski', 'góral'],
        'rzeka': ['rzeka', 'rzeczny'],
        'morze': ['morze', 'morski'],
        'jezioro': ['jezioro', 'jeziorny'],
        'las': ['las', 'leśny'],
        'ogień': ['ogień', 'ognisty', 'ognisko'],
        'woda': ['woda', 'wodny'],
        'ziemia': ['ziemia', 'ziemski'],
        'wiatr': ['wiatr', 'wietrzny'],
        'deszcz': ['deszcz', 'deszczowy'],
        'śnieg': ['śnieg', 'śnieżny'],
        'miecz': ['miecz', 'miecznik', 'szermierz'],
        'nóż': ['nóż', 'nożownik'],
        'łuk': ['łuk', 'łucznik', 'łuczniczy'],
        'strzała': ['strzała', 'strzałka'],
        'pięść': ['pięść', 'pięściarz'],
        'wojownik': ['wojownik', 'wojenny', 'wojna', 'walczyć', 'walka'],
        'król': ['król', 'królewski', 'królestwo', 'królowa'],
        'cesarz': ['cesarz', 'cesarski', 'cesarstwo', 'cesarzowa'],
        'książę': ['książę', 'książęcy'],
        'generał': ['generał', 'generalski'],
        'żołnierz': ['żołnierz', 'żołnierski'],
        'mnich': ['mnich', 'mnisi', 'mniszka'],
        'kapłan': ['kapłan', 'kapłanka', 'kapłański'],
        'świątynia': ['świątynia', 'świątynny'],
        'klasztor': ['klasztor', 'klasztorny'],
        'książka': ['książka', 'księga', 'książkowy'],
        'pisać': ['pisać', 'pismo', 'pisarz', 'pisanie'],
        'czytać': ['czytać', 'czytanie', 'czytelnik'],
        'uczyć': ['uczyć', 'uczyć się', 'nauczyciel', 'nauka', 'nauczyć'],
        'mówić': ['mówić', 'mowa', 'mówca', 'powiedzieć'],
        'słuchać': ['słuchać', 'słyszeć', 'słuch'],
        'widzieć': ['widzieć', 'widok', 'widzenie', 'patrzeć'],
        'jeść': ['jeść', 'jedzenie', 'jadło'],
        'pić': ['pić', 'picie', 'napój'],
        'spać': ['spać', 'sen', 'śpiący'],
        'budzić': ['budzić', 'obudzić się', 'budzenie'],
        'żyć': ['żyć', 'życie', 'żywy'],
        'umrzeć': ['umrzeć', 'śmierć', 'martwy'],
        'kochać': ['kochać', 'miłość', 'ukochany'],
        'nienawidzić': ['nienawidzić', 'nienawiść'],
        'bać się': ['bać się', 'strach', 'bojaźliwy'],
        'silny': ['silny', 'siła', 'siłacz', 'mocny'],
        'słaby': ['słaby', 'słabość'],
        'dobry': ['dobry', 'dobro', 'dobroć'],
        'zły': ['zły', 'zło', 'złość'],
        'wielki': ['wielki', 'wielkość'],
        'mały': ['mały', 'małość'],
        'długi': ['długi', 'długość'],
        'krótki': ['krótki', 'krótkość'],
        'wysoki': ['wysoki', 'wysokość'],
        'niski': ['niski', 'niskość'],
    }
    
    # Znajdź niezgodności
    print("="*80)
    print("ANALIZA SPÓJNOŚCI SEMANTYCZNEJ SŁOWNIKA LENGXUAN")
    print("="*80)
    print()
    
    inconsistencies = []
    
    for base_concept, related_words in semantic_groups.items():
        # Znajdź wpisy w słowniku
        found_entries = []
        for search_word in related_words:
            for polish, lengxuan, original_polish in entries:
                if polish == search_word:
                    found_entries.append((original_polish, lengxuan))
        
        if len(found_entries) >= 2:
            # Sprawdź czy mają wspólny rdzeń
            codes = [entry[1] for entry in found_entries]
            
            # Wyciągnij sylaby
            def get_syllables(code):
                return set(code.split('-'))
            
            all_syllables = [get_syllables(code) for code in codes]
            
            # Sprawdź czy jakieś sylaby są wspólne
            common = all_syllables[0]
            for syllables in all_syllables[1:]:
                common = common & syllables
            
            if not common:
                inconsistencies.append({
                    'group': base_concept,
                    'entries': found_entries
                })
    
    # Raportuj
    print(f"Znaleziono {len(inconsistencies)} grup semantycznych BEZ wspólnego rdzenia:\n")
    
    for item in inconsistencies[:50]:  # Pierwsze 50
        print(f"📍 Grupa: {item['group'].upper()}")
        for polish, lengxuan in item['entries']:
            print(f"   - {polish} → {lengxuan}")
        print()
    
    print("="*80)
    print(f"PODSUMOWANIE: {len(inconsistencies)} niezgodności wymaga poprawy")
    print("="*80)
    
    return inconsistencies

if __name__ == '__main__':
    analyze_dictionary()
