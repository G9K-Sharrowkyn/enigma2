#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translate Polish dialogues to Lengxuan
"""

def load_dictionary():
    """Load PL->Lengxuan dictionary"""
    pl_path = 'Lengxuan_Language/03_Slownik/slownik_polski_lengxuan.md'
    dictionary = {}
    
    with open(pl_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('- '):
                parts = line.strip().rsplit(' - ', 1)
                if len(parts) == 2:
                    polish, code = parts[0][2:], parts[1]
                    dictionary[polish.lower()] = code
    
    return dictionary

def translate_text(text, dictionary):
    """Translate Polish text to Lengxuan"""
    words = text.split()
    translated = []
    
    for word in words:
        # Remove punctuation for lookup
        clean_word = word.strip('.,!?:;').lower()
        
        if clean_word in dictionary:
            translated.append(dictionary[clean_word])
        else:
            # Try to find partial matches or keep original
            translated.append(f"[{word}]")
    
    return ' '.join(translated)

def main():
    print("Loading dictionary...")
    dictionary = load_dictionary()
    print(f"Loaded {len(dictionary)} entries\n")
    
    dialogues = [
        "Nie przyjmuję uczniów, od dawna. Wracaj skąd przybyłeś i nie zawracaj mi więcej głowy.",
        "Odejdź! Nic cię tu nie czeka!",
        "No trudno. Wejdź. Za godzinę przyjdzie tłumacz. Może on ci wyjaśni, że masz wracać do domu.",
        "Wejdź",
        "Mistrzu, jesteś tu?",
        "Wejdź, Chen-Lu.",
        "Wzywałeś mnie, Mistrzu Lao?",
        "Tak. Posłuchaj mnie. Ten chłopiec pojawił się tu niedawno. Wygląda na to, że przybył z Askikagamy. Powiedz mu, żeby wracał skąd przyszedł. Nie przyjmuję już uczniów.",
        "Jak sobie życzysz, mistrzu.",
        "Zapytaj go, czy wie dlaczego go tu wpuściłem.",
        "Pamiętam Heijiro. Dobry wojownik. Honorowy człowiekiem. Ale to nie znaczy, że zostaniesz tu przyjęty jako uczeń.",
        "Przed laty szkoliłem wielu uczniów. Jeden z nich nazywał się Lianyu. Zdradził on moje zaufanie i nauki. Zamknąłem swoją szkołę i przyrzekłem sobie nie trenować nikogo więcej.",
        "Zatem przybyłeś tu, by się zemścić?",
        "Heijiro ocalił moje życie, dawno temu. Uhonoruję jego pamięć dając ci szansę. Pozwolę Ci przystąpić do prób. Jeśli sobie z nimi poradzisz, będziesz mógł tu zostać. O zasadach obowiązujących w tym miejscu dowiesz się, jeśli zdasz testy... Ale jeśli nie okażesz się dość silny, odejdziesz stąd i nigdy nie wrócisz.",
        "Dziękuję."
    ]
    
    print("TRANSLATING DIALOGUES:\n")
    print("=" * 80)
    
    for i, dialogue in enumerate(dialogues, 1):
        print(f"\n{i}. PL: {dialogue}")
        translation = translate_text(dialogue, dictionary)
        print(f"   LX: {translation}")
    
    # Show which words are missing
    print("\n" + "=" * 80)
    print("\nMISSING WORDS (need manual translation):\n")
    
    all_words = set()
    for dialogue in dialogues:
        words = dialogue.split()
        for word in words:
            clean = word.strip('.,!?:;').lower()
            if clean and clean not in dictionary:
                all_words.add(clean)
    
    for word in sorted(all_words):
        print(f"  - {word}")

if __name__ == "__main__":
    main()
