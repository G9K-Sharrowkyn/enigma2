#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Manual Lengxuan translations of Ryujin dialogues
Using dictionary + creating necessary grammatical forms
"""

translations = {
    # 1
    "Nie przyjmuję uczniów, od dawna. Wracaj skąd przybyłeś i nie zawracaj mi więcej głowy.":
    "Nai xue-ren, geng-lao. Cu-lai geng-wo lun nai fan-luo nio shun-qin.",
    # Translation: NEG accept-student, from-old. Return from-you and NEG bother I head.
    
    # 2
    "Odejdź! Nic cię tu nie czeka!":
    "Deo! Wuo nio kan nai pen!",
    # Translation: Go-away! Nothing you here NEG wait!
    
    # 3
    "No trudno. Wejdź. Za godzinę przyjdzie tłumacz. Może on ci wyjaśni, że masz wracać do domu.":
    "Duo-ran. Lai-nei. Zai shi-qian lai nei-he-ren. Meno tao xue-ma nio, nio cu-lai dao qin-ze.",
    # Translation: Difficult-but. Enter-inside. At hour come translator. Maybe he explain you, you return to house.
    
    # 4
    "Wejdź":
    "Lai-nei",
    # Translation: Come-inside
    
    # 5
    "Mistrzu, jesteś tu?":
    "Shi-fu-ren, ai kan?",
    # Translation: Master, be here?
    
    # 6
    "Wejdź, Chen-Lu.":
    "Lai-nei, Chen-Lu.",
    # Translation: Come-inside, Chen-Lu.
    
    # 7
    "Wzywałeś mnie, Mistrzu Lao?":
    "Hu-jiao nio, Shi-fu Lao?",
    # Translation: Call I, Master Lao?
    
    # 8
    "Tak. Posłuchaj mnie. Ten chłopiec pojawił się tu niedawno. Wygląda na to, że przybył z Askikagamy. Powiedz mu, żeby wracał skąd przyszedł. Nie przyjmuję już uczniów.":
    "En. Ting-jian nio. Chai-cen lai kan jin-lao. Kan-lai tao, tao lai geng Ashikagama. Shuo-ma tao, tao cu-lai geng-wo. Nai xue-ren jin-wo.",
    # Translation: Yes. Listen I. Boy come here near-old. Look-come he, he come from Ashikagama. Speak-teach he, he return from-you. NEG student now-I.
    
    # 9
    "Jak sobie życzysz, mistrzu.":
    "Yuan-zhi nio, shi-fu.",
    # Translation: Wish you, master.
    
    # 10
    "Zapytaj go, czy wie dlaczego go tu wpuściłem.":
    "Wen-ma tao, jie tao xiaoo-na-shu nio kai-men tao kan.",
    # Translation: Ask-teach he, know he why I open-door he here.
    
    # 11
    "Pamiętam Heijiro. Dobry wojownik. Honorowy człowiekiem. Ale to nie znaczy, że zostaniesz tu przyjęty jako uczeń.":
    "Ji-yi nio Heijiro. Hao chai-hun. Rongo-cao ren-yuan. Tan chai nai yi-si, nio wo kan xue-ren.",
    # Translation: Remember I Heijiro. Good warrior. Honor person. But this NEG meaning, you stay here student.
    
    # 12
    "Przed laty szkoliłem wielu uczniów. Jeden z nich nazywał się Lianyu. Zdradził on moje zaufanie i nauki. Zamknąłem swoją szkołę i przyrzekłem sobie nie trenować nikogo więcej.":
    "Qian-nian nio ma-jiao duo xue-ren. Cou-chang geng tao ming Lianyu. Bei-pan tao nio bie-keng lun ma-jiao. Guan-bi nio xue-yuan lun ba-zheng nio nai lian-xi wuo-ren shun-qin.",
    # Translation: Before-year I teach many student. One from he name Lianyu. Betray he I trust and teaching. Close-shut I school and promise I NEG train nobody more.
    
    # 13
    "Zatem przybyłeś tu, by się zemścić?":
    "Zai-ci nio lai kan, bao-fu wei?",
    # Translation: So you come here, revenge for?
    
    # 14
    "Heijiro ocalił moje życie, dawno temu. Uhonoruję jego pamięć dając ci szansę. Pozwolę Ci przystąpić do prób. Jeśli sobie z nimi poradzisz, będziesz mógł tu zostać. O zasadach obowiązujących w tym miejscu dowiesz się, jeśli zdasz testy... Ale jeśli nie okażesz się dość silny, odejdziesz stąd i nigdy nie wrócisz.":
    "Heijiro jiu nio sheng-ming, qian-shi. Rongo-cao nio ji-yi tao gei nio ji-hui. Rang nio kai-shi dao kao-shi. Jiao nio cheng-gong, nio neng wo kan. Guan gui-ze kan chai deo, jiao nio cheng kao-shi... Tan jiao nai xian-shi nio run-zhao, nio deo geng-kan lun mie nai hui-lai.",
    # Translation: Heijiro save I life, before-time. Honor I memory he give you opportunity. Allow you start to test. If you succeed, you can stay here. About rules here this place, if you pass test... But if NEG show you strong, you go from-here and never NEG return.
    
    # 15
    "Dziękuję.":
    "Poye."
    # Translation: Thank.
}

def main():
    print("LENGXUAN TRANSLATIONS FOR RYUJIN.HTML\n")
    print("=" * 80)
    
    for i, (polish, lengxuan) in enumerate(translations.items(), 1):
        print(f"\n{i}.")
        print(f"PL: {polish}")
        print(f"LX: {lengxuan}")
        print()
    
    print("=" * 80)
    print("\nTotal translations: 15 dialogues")

if __name__ == "__main__":
    main()
