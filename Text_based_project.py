# Autor: Josef Unčovský
# Vývoj: 2020-28-08 -
# Popis: Případ "ZLO PŘICHÁZÍ Z HOR" - Textová adventura

import os
import sys
import time
import random
import winsound
import json

#Objekty, které lze sebrat
zapalovac = 0
magnum = 0
guma = 0

#Inventář
inventar = []

#Zápisník
zapisnik = []
            
def Intro():
    print()
    print("----------------------")
    print("UPOZORNĚNÍ - NÁSLEDUJÍCÍ HRA OBSAHUJE VULGARISMY, RASISTICKÉ A ANTI-BALKÁNSKÉ MOTIVY A SEXUÁLNÍ MOTIVY.")
    print("NÁSLEDUJÍCÍ OBSAH JE NEPŘÍSTUPNÝ DĚTEM A MLÁDEŽI")
    print("----------------------")
    print()
    input("Stiskněte ENTER pro pokračování.")
#    x = upozorneni.center(20, "*")
#    y = upozorneni2.center(20, "*")
#    print(x)
#    print(y)
    print('"ZLO PŘICHÁZÍ Z HOR" - Josef Unčovský')
    #input("Stiskněte ENTER pro pokračování.")
    
    print("KAPITOLA 1")
    print("----------------------")
    print("Pondělí. Ranní káva vůbec nevoněla, a chutnala ještě hůř. Osvědčené znamení mizerného dne.")
    print("Cesta na pracoviště byla ještě otravnější, než jindy. Deštěm jsi celý promokl.")
    print("44tka pod tvým ramenem jakoby vážila víc, než kterýkoliv jiný den.")
    print("----------------------")
    winsound.PlaySound("dest", winsound.SND_FILENAME)
    input("")
    print("Hlavní dveře.")
    winsound.PlaySound("door_1", winsound.SND_FILENAME)
    input("")
    print("Výtah.")
    winsound.PlaySound("elevator", winsound.SND_FILENAME)
    input("")
    print("Chodbou do kanclu.")
    winsound.PlaySound("chuze", winsound.SND_FILENAME)
    input("")
    winsound.PlaySound("dvere_2", winsound.SND_FILENAME)
    print("Dveře kanclu.")
    input("")
    
    print("Kabát na věšák. Klobouk taky.")
    winsound.PlaySound("kabat", winsound.SND_FILENAME)
    input("")
    print("Vyčištěný a naolejovaný ruční kanón do šuplíku.")
    winsound.PlaySound("Suplik", winsound.SND_FILENAME)
    input("")
    winsound.PlaySound("Bourbon", winsound.SND_FILENAME)
    print("Sklenička. Led. Bourbon. A zapálit si.")
    winsound.PlaySound("Zapalovac", winsound.SND_FILENAME)
    winsound.PlaySound("Potahnuti", winsound.SND_FILENAME)
    input("")
    print("Jsi soukromý detektiv. Sedíš ve své ošuntělé, zaprášené kanceláři. Další zatracený pondělí.")
    print()
    print("Už měsíc nemůžeš zavadit o pořádnej případ.")
    input("")
    print("V jedné ruce cigareta, v druhé sklenička bourbonu.")
    input("")
    winsound.PlaySound("Piti", winsound.SND_FILENAME)
    print("Napiješ se bourbonu.")
    input("")
    #print('"CRRRRRRRRRRR! CRRRRRRRRRR!!!! CRRRRRR!"')
    winsound.PlaySound("telephone", winsound.SND_FILENAME)
    print("Telefon prořízne melancholické ticho tvého kanclu jako výbuch granátu.")
    input("")
def Prvni_Kontakt_Vseobecna():
    print("...")
    print("[VOLAJÍCÍ:]"+'"Je to Philip Marlowe?" ozve se z útrob děravého plastu.')
    input("")
    print()
    print("----------------------")
    print("(Zaregistuješ 4 věci: Volajícím je muž. Mladý muž. Sarkastický tón, vzhledem k otázce. Silně venkovský přízvuk, nejspíš oblast Salemu.)")
    print("----------------------")
    print()
    while True:
        print('A)"Ano. Co potřebujete?" B) "Néé, tady anglická královna." C) "Néé, tady princezna ze Sáby!" D) "Mami?!"')
        moznosti = input ('[A/B/C/D]: ')
        if moznosti in ['A','B', 'C', 'D']:
            break
    if moznosti == "B":
       print("[TY:]"+'"Néé, tady anglická královna." utrousíš, stejně sarkastickým tónem (ne-li více sarkastickým), do děravého kusu plastu.')
    if moznosti == "C":
        print("[TY:]"+'"Néé, tady princezna ze Sáby!" utrousíš, s důrazem na posměšný tón, do kulatého kusu plastu.')
    if moznosti == "D":
        print("[TY:]"+'"Mami?!" zahlaholíš pobaveně do telefonu. I když je pondělí, smysl pro humor tě neopustil.')
    if moznosti == "A":
        print("[TY:]"+'"Ano. Co potřebujete?" Odpovíš, nepodrážděn hloupou otázkou.')
def Prvni_Kontakt_Vseobecna_2():
    print("...")
    print()
    print("----------------------") 
    print('<Napadlo tě, jestli volající nezavěsil.>')
    print("----------------------")
    print()
    print("[VOLAJÍCÍ:]"+'"Bylo mi řečeno, že jste nejlepší soukromý detektiv na tomto kontinentu." Ozvalo se po chvíli z telefonu.')
    input("")
    print("----------------------") 
    print('(Hlas byl už serióznější. Ale nemůžeš se zbavit pocitu, že v něm slyšíš něco jako zklamání.)')
    print("----------------------")
    print()
    while True:
        print('A)"To rád slyším."  B) "Máte zájem o mé služby?" C) <mlčet>')
        moznosti = input ('[A/B/C]: ')
        if moznosti in ['A','B', 'C']:
            break
    if moznosti == "A":
       print("[TY:]"+'"To rád slyším." Odpovíš, s falešnou skromností.')
       
    if moznosti == "B":
        print("[TY:]"+'"Máte zájem o mé služby?" Odpovíš, dávajíc na vedomí, že chceš jít k věci.')
        
    if moznosti == "C":
        print("<mlčíš, čekáš>")
def Prvni_Kontakt_Vseobecna_3():
    print("----------------------")
    print("[VOLAJÍCÍ:]"+'"Mám pro vás práci." Ozve se z telefonu. (Hlas přešel do čistě profesionálního tónu)')
    print("----------------------")
    input("")
    while True:
        print('A)"O co se jedná?"  B) <z kapsy vytáhneš zápisník a propisku.> C) "Prosím, pokračujte."')
        moznosti = input ('[A/B/C]: ')
        if moznosti in ['A','B', 'C']:
            break
    if moznosti == "A":
       print("[TY:]"+'"O co se jedná?" Odpovíš, bez jakýchkoliv emocí v hlase. ')
       input("")
       Prvni_Kontakt_Detaily_A()
       Prvni_Kontakt_Detaily_2_Vseobecna()
       
    if moznosti == "B":
        winsound.PlaySound("Propiska", winsound.SND_FILENAME)
        print('<z kapsy vytáhneš zápisník a propisku.> Dáš si záležet, aby cvaknutí propisovačky bylo slyšet.')
        input("")
        Prvni_Kontakt_Detaily_B()
        Prvni_Kontakt_Detaily_2_Vseobecna()
    if moznosti == "C":
        print("[TY:]"+'"Prosím, pokračujte." Řekneš, předstírajíc profesní slušnost (Na kterou už dávno nevěříš).')
        input("")
        Prvni_Kontakt_Detaily_C()
        Prvni_Kontakt_Detaily_2_Vseobecna()
def Prvni_Kontakt_Detaily_A():
    print("[VOLAJÍCÍ:]"+"... <šustění papíru>")
    winsound.PlaySound("Susteni", winsound.SND_FILENAME)
    print("[VOLAJÍCÍ:]"+'"Vražda. Zločin se stal před 5ti lety. V Salemu." <svraštíš čelo>')
    print("[VOLAJÍCÍ:]"+'"Dnes je to už samozřejmě cold case(*), Policie skončila na mrtvém bodě."')
    input("")
    print('***"Cold case" -- v doslovném překladu "Chladný případ" značí případ, který není vyřešen a není aktivně vyšetřován policií***')
    print('"Co byl ten mrtvý bod?" Odvětíš, zatímco ti naděj na pořádnej případ nenápadně leze do mozku.')
    input("")
    print("...<další šustění papíru>")
    winsound.PlaySound("Susteni", winsound.SND_FILENAME)
    print("[VOLAJÍCÍ:]"+'"Údajný korunní svědek případu zmizel. Těsně před tím, než měl podat klíčovou výpověď." Odpovídá potenciální klient.')
    print("...")
    print("<začneš si nalévat ještě jednu sklenku.>")
    winsound.PlaySound("Bourbon", winsound.SND_FILENAME)
    input("")
    print("(je to přece úplně jasné. Někdo prostě nechtěl, aby ten svědek vypovídal. Takže ho zmizel.)")
    print('"Kdo byl ten korunní svědek, ve vztahu k oběti?" Zeptáš se, potlačujíc zívání.')
    input("")
    print("----------------------")
def Prvni_Kontakt_Detaily_B():
    winsound.PlaySound("Susteni", winsound.SND_FILENAME)
    print("[VOLAJÍCÍ:]"+"...<Otáčení stránky>")
    print()
    print("----------------------") 
    print("(Pochopil)")
    print("----------------------")
    print()
    print("[VOLAJÍCÍ:]"+'"Vražda. Zločin se stal před 5ti lety." <svraštíš čelo>')
    input("")
    print("[VOLAJÍCÍ:]"+'"Dnes je to už samozřejmě cold case(*), Policie skončila na mrtvém bodě."')
    print()
    print("----------------------") 
    print('***"Cold case" -- v doslovném překladu "Chladný případ" značí případ, který není vyřešen a není aktivně vyšetřován policií***')
    print("----------------------")
    print()
    print('"Co byl ten mrtvý bod?" Odvětíš, zatímco ti naděj na pořádnej případ nenápadně leze do mozku.')
    input("")
    print("[VOLAJÍCÍ:]"+"...<další otáčení stránky>")
    winsound.PlaySound("Susteni", winsound.SND_FILENAME)
    winsound.PlaySound("Susteni", winsound.SND_FILENAME)
    print("[VOLAJÍCÍ:]"+'"Údajný korunní svědek případu zmizel. Těsně před tím, než měl podat klíčovou výpověď." Odpovídá potenciální klient.')
    input("")
    print("...")
    print("<začneš si nalévat ještě jednu sklenku.>")
    winsound.PlaySound("Bourbon", winsound.SND_FILENAME)
    input("")
    print("(je to přece úplně jasné. Někdo prostě nechtěl, aby ten svědek vypovídal. Takže ho zmizel.)")
    print('"Kdo byl ten korunní svědek, ve vztahu k oběti?" Zeptáš se, potlačujíc zívání.')
def Prvni_Kontakt_Detaily_C():
    print("[VOLAJÍCÍ:]"+'"Jistě. Hned se k tomu dostanu." Odpovídá potenciální klient.')
    print("[VOLAJÍCÍ:]"+'"Vražda. Zločin se stal před 5ti lety." <svraštíš čelo>')
    print("[VOLAJÍCÍ:]"+'"Dnes je to už samozřejmě cold case(*), Policie skončila na mrtvém bodě."')
    input("")
    print()
    print("----------------------")
    print('***"Cold case" -- v doslovném překladu "Chladný případ" značí případ, který není vyřešen a není aktivně vyšetřován policií***')
    print("----------------------")
    print()
    print("[TY:]"+'"Co byl ten mrtvý bod?" Odvětíš, zatímco ti naděj na pořádnej případ nenápadně leze do mozku.')
    input("")
    print("...<další otáčení stránky>")
    winsound.PlaySound("Susteni", winsound.SND_FILENAME)
    winsound.PlaySound("Susteni", winsound.SND_FILENAME)
    print("[VOLAJÍCÍ:]"+'"Údajný korunní svědek případu zmizel. Těsně před tím, než měl podat klíčovou výpověď." Odpovídá potenciální klient.')
    input("")
    print("...")
    winsound.PlaySound("Bourbon", winsound.SND_FILENAME)
    print("<začneš si nalévat ještě jednu sklenku.>")
    input("")
    print("(Je to přece úplně jasné. Někdo prostě nechtěl, aby ten svědek vypovídal. Takže ho zmizel.)")
    print("[TY:]"+'"Kdo byl ten korunní svědek, ve vztahu k oběti?" Zeptáš se, potlačujíc zívání.')
    print("----------------------")
    input("")
def Prvni_Kontakt_Detaily_2_Vseobecna():
    print("[VOLAJÍCÍ:]"+'"Farář. Z její vesnice. Mimo toho, že byl jejím zpovědníkem, byli dobří přátelé. To říká spis."')
    print("<volnou rukou si mneš čelo. Poté do sebe otočíš i druhou sklenku>")
    input("")
    print("(Zaregistruješ 2 věci --> Ať už svědka umlčel kdokoliv, nemá problém sejmout muže víry. To značí nebezpečí.)")
    print("(A taky, že původní obětí je žena.)")
    input("")
    print("[TY:]"+'"A okolnosti té vraždy?"  Zeptáš se, teď už se skutečným zájmem a s opravdovou nadějí, že pořádnej případ je na světě.')
    print("[VOLAJÍCÍ:]"+'"To je právě to..." Odpovídá (teď už na půl jistý) klient.')
    print("[VOLAJÍCÍ:]"+'"Podle všeho byla otrávená."')
    input("")
    while True:
        print('A)"Arsenem?"  B) "Kyanidem?"')
        moznosti = input ('[A/B]: ')
        if moznosti in ['A','B']:
            break
    if moznosti == "A":
       print("[TY:]"+'"Arsenem?" Zeptáš se, s ledovým klidem v hlase.')
       Prvni_Kontakt_Detaily_2_A()
       Prvni_Kontakt_Detaily_3()
       Obet_1()
       
    if moznosti == "B":
        print("[TY:]"+'"Kyanidem?" Zeptáš se, s ledovým klidem v hlase.')
        Prvni_Kontakt_Detaily_2_B()
        Prvni_Kontakt_Detaily_3()
        Obet_1()
def Prvni_Kontakt_Detaily_2_A():
    print("[VOLAJÍCÍ:]"+'"Ne, arsenem ne." Odpovídá klient.')
    print("[VOLAJÍCÍ:]"+'"Pitevní zpráva říká, že jde o dosud neznámý druh jedu. Rozhodně to není nic běžného."')
    print("[VOLAJÍCÍ:]"+'"Už asi chápete, proč se z tohoto případu stal cold case."')
    print("...")
    input("")
    
    while True:
        print('A)"Ano, to chápu..."  B) "Další stopy nejsou?"')
        moznosti = input ('[A/B]:')
        if moznosti in ['A','B']:
            break
    if moznosti == "A":
       print("[TY:]"+'"Ano, to chápu..." Odpovídáš.')
       
    if moznosti == "B":
        print("[TY:]"+'"Další stopy nejsou?" Zeptáš se, klidně.')
def Prvni_Kontakt_Detaily_2_B():
    print("[VOLAJÍCÍ:]"+'"Ne, kyanidem ne." Odpovídá klient.')
    print("[VOLAJÍCÍ:]"+'"Pitevní zpráva říká, že jde o dosud neznámý druh jedu. Rozhodně to není nic běžného."')
    print("[VOLAJÍCÍ:]"+'"Už asi chápete, proč se z tohoto případu stal cold case."')
    print("...")
    input("")
    while True:
        print('A)"Ano, to chápu..."  B) "Další stopy nejsou?"')
        moznosti = input ('[A/B]: ')
        if moznosti in ['A','B']:
            break
    if moznosti == "A":
       print('"Ano, to chápu..." Odpovídáš.')
       
    if moznosti == "B":
        print('"Další stopy nejsou?" Zeptáš se, klidně.')
    
def Prvni_Kontakt_Detaily_3():
    winsound.PlaySound("Kychnuti", winsound.SND_FILENAME)
    print("[VOLAJÍCÍ:]"+"<Z telefonu se ozve kychnuti>")
    print("[VOLAJÍCÍ:]"+'"Korunní svědek zmizel a na místě činu, respektive na místě, kde oběť zemřela na otravu, se nic nenašlo." Odpovídá klient.')
    input("")
    print("[VOLAJÍCÍ:]"+'"Myslím, že..." Řekne klient, zastavujíc uprostřed věty.')
    winsound.PlaySound("SmrtelnyKasel", winsound.SND_FILENAME)
    winsound.PlaySound("Zaveseni", winsound.SND_FILENAME)
    print("<zaslechneš žuchnutí a zavěšení.>")
    input("")
    print("[TY:]"+'"Ale do prdele...!" Vyhrkneš.')
    print('Tvému potenciálnímu klientovi buď zaskočilo a udusil se, nebo ho někdo otrávil.')
    input("")
    print('Přesně na jednu vteřinu se zamyslíš, která možnost je pravděpodobnější.')
    print('Musíš zjistit, odkud ten člověk volal a zavolat záchranku.')
    print('...Možná spíš funebráky.')
def Obet_1():
    print("...")
    input("")
    while True:
        print('A)<Spojit se se záchrannou službou.>  B)<Vykašlat se na to.>')
        moznosti = input ('A/B]:')
        if moznosti in ['A','B']:
            break
    if moznosti == "A":
       print('<Začneš vytáčet číslo na záchrannou službu.>')
       input("")
       Obet_1_Telefon()
       
    if moznosti == "B":
        print('<Vykašleš se na to; mávneš rukou>')
        input("")
        Obet_1_Konec()

def Obet_1_Telefon():
    winsound.PlaySound("Policie_Telefon", winsound.SND_FILENAME)
    winsound.PlaySound("Policie_Telefon", winsound.SND_FILENAME)
    print("[DISPATCHER:]"+'"Záchranná služba." Ozve se na druhém konci telefonu.')
    input("")
    while True:
        print('A)"Dobrý den, s někým jsem právě mluvil a..."  B) "Někdo právě umírá a potřebuje pomoc!"')
        moznosti = input ('[A/B]:')
        if moznosti in ['A','B']:
            break
    if moznosti == "A":
       print("[TY:]"+'"Dobrý den, s někým jsem právě mluvil a..." (Postupně převyprávíš celý příběh).')
       input("")
       Obet_1_Telefon_A()
       
    if moznosti == "B":
        print("[TY:]"+'"Někdo právě umírá a potřebuje pomoc!" Řekneš, s větší panikou, než by sis od sebe představoval.')
        input("")
        Obet_1_Telefon_B()
    
def Obet_1_Konec():
    print("KONEC")
    time.sleep(2)
    sys.exit()

def Obet_1_Telefon_A():
    print("(Dispatcher si vyslechne všechno, co víš.)")
    input("")
    print("[DISPATCHER:]"+'"Takže jestli to správně chápu, nevíte, kdo ten člověk je ani kde je, mám pravdu?" Nakonec odpovídá, když domluvíš.')
    while True:
        print('A)"Vím, že mi představoval případ z městečka Salem, zněl trochu jako místní."  B) "Ano, to je pravda, bohužel."')
        moznosti = input ('[A/B]:')
        if moznosti in ['A','B']:
            break
    if moznosti == "A":
       print("[TY:]"+'"Vím, že mi představoval případ z městečka Salem, zněl trochu jako místní." Řekneš, vybavujíc si hlas klienta.')
       input("")
       Obet_1_Telefon_A_2_A()
       
    if moznosti == "B":
        print("[TY:]"+'"Ano, to je pravda, bohužel." Řekneš rezignovaně.')
        input("")
        Obet_1_Telefon_A_2_B()

def Obet_1_Telefon_A_2_A():
    print("[DISPATCHER:]"+'"Dobře, spojím se se Salemskou stanicí, ať se tam porozhlédnou."')
    print("[DISPATCHER:]"+'"Ale nejspíš budeme muset počkat, než někdo najde tělo." Odpovídá dispatcher kovovým hlasem.')
    print("[TY:]"+'"Dobře, děkuji vám." Odpovíš, pokládajíc telefon.')
    print("----------------------")
    input("")
    print("Vypadá to, že máš před sebou další případ.")
    print("Tentokrát před tebou stojí někdo, kdo si po sobě uklidí a nemá problém zavraždit každého, kdo po něm půjde.")
    print("Je načase odcestovat do Salemu. Třeba vrah něco přehlédl.")
    input("")
    print("<Vstaneš ze židle.>")
    global zapisnik
    zapisnik.append("Vrah (nebo vrahové?), má prozatím jen jednu potvrzenou oběť.")
    zapisnik.append("Prokázání skutečnosti, že potenciální klient byl otráven stejným jedem, by znamenalo druhou oběť.")
    zapisnik.append("Potvrzení tvé teorie, že korunní svěděk (farář) byl zavražděn stejným vrahem (nebo skupinou?), by potvrdilo oběť číslo 3.")
    zapisnik.append("Ať už je vrah jeden, nebo je jich více, jsou nepochybně extrémně nebezpeční.")
    zapisnik.append("A nemá/nemají rádi pozornost.")
    while True:
        print('Leží před tebou zapalovač. Vezmeš ho?')
        moznosti = input ('[Y/N]: ')
        if moznosti in ['Y','N']:
            break
    if moznosti == "Y":
       print('Sebral jsi zapalovač.')
       winsound.PlaySound("Item",winsound.SND_FILENAME)
       global zapalovac
       zapalovac = 1
       global inventar
       inventar.append("Zapalovač")
       Predmety_2()
       
    if moznosti == "N":
        print('Zapalovač necháš ležet. (Škoda, ten se ještě bude hodit. -_- )')
        Predmety_2()
def Obet_1_Telefon_A_2_B():
    print("[DISPATCHER:]"+'"Jste si jistý?" Zeptá se dispatcher.')
    print('"Počkat!" Zvoláš, vybavujíc si fakt, že místo vraždy (teď už nejspíš vražd) bylo městečko Salem.')
    print('"Vím, že mi představoval případ z městečka Salem, zněl trochu jako místní." Řekneš po chvíli.')
    input("")
    print("[DISPATCHER:]"+'"Dobře, spojím se se Salemskou stanicí, ať se tam porozhlédnou."')
    print("[DISPATCHER:]"+'"Ale nejspíš budeme muset počkat, než někdo najde tělo." Odpovídá dispatcher kovovým hlasem.')
    print('"Dobře, děkuji vám." Odpovíš, pokládajíc telefon.')
    print("----------------------")
    input("")
    print("Vypadá to, že máš před sebou další případ.")
    print("Tentokrát proti tobě stojí někdo, kdo si po sobě uklidí a nemá problém zavraždit každého, kdo po něm půjde.")
    print("Je načase odcestovat do Salemu. Třeba vrah něco přehlédl.")
    print("<Vstaneš ze židle.>")
    while True:
        print('Leží před tebou zapalovač. Vezmeš ho?')
        moznosti = input ('[Y/N]: ')
        if moznosti in ['Y','N']:
            break
    if moznosti == "Y":
       print('Sebral jsi zapalovač.')
       winsound.PlaySound("Item",winsound.SND_FILENAME)
       global zapalovac
       global inventar
       inventar.append("Zapalovač")
       zapalovac = 1
       
       input("")
       Predmety_2()
       
    if moznosti == "N":
        print('Zapalovač necháš ležet. (Škoda, ten se ještě bude hodit. -_- )')
        zapalovac = 0
        input("")
        Predmety_2()
def Obet_1_Telefon_B():
    print("[DISPATCHER]:"+'"Tak mluvte, krucinál!" Ozve se netrpělivě dispatcher, bojující o čas.')
    print("<řekneš mu vše, co víš.>")
    print("(Dispatcher si vyslechne všechno, co víš.)")
    input("")
    print("[DISPATCHER:]"+'"Takže jestli to správně chápu, nevíte, kdo ten člověk je ani kde je, mám pravdu?" Nakonec odpovídá, když domluvíš.')
    while True:
        print('A)"Vím, že mi představoval případ z městečka Salem, zněl trochu jako místní."  B) "Ano, to je pravda, bohužel."')
        moznosti = input ('[A/B]:')
        if moznosti in ['A','B']:
            break
    if moznosti == "A":
       print("[TY:]"+'"Vím, že mi představoval případ z městečka Salem, zněl trochu jako místní." Řekneš, vybavujíc si hlas klienta.')
       input("")
       Obet_1_Telefon_A_2_A()
       
    if moznosti == "B":
        print("[TY:]"+'"Ano, to je pravda, bohužel." Řekneš rezignovaně.')
        input("")
        Obet_1_Telefon_A_2_B()

def Predmety_2():
    while True:
        print('V šuplíku leží tvá věrná 44ka. Vezmeš ji?')
        moznosti = input ('[Y/N]:')
        if moznosti in ['Y','N']:
            break
    if moznosti == "Y":
       print('Sebral jsi ruční kanón.(*)')
       winsound.PlaySound("Item",winsound.SND_FILENAME)
       print('*** Revolveru 44. Magnum se přezdívá "Ruční kanón" díky jeho palebné síle, která dokáže zničit prakticky cokoliv.***')
       global magnum
       magnum = 1
       global inventar
       inventar.append("Magnum")
       #inventar_json = json.loads(inventar)
       input("")
       Odchod_Z_Kanclu()
       
    if moznosti == "N":
        print('44ku necháte v šuplíku. (To snad nemyslíte vážně... -_- )')
        magnum = 0
        input("")
        Odchod_Z_Kanclu()
def Odchod_Z_Kanclu():
    if magnum == 1 and zapalovac == 1:
        print("Připraven, obtěžkán oběma artefakty, odcházíš z kanclu.")
    elif magnum == 1 and zapalovac == 0:
        print("S 44kou pod ramenem vycházíš z kaclu.")
    elif magnum == 0 and zapalovac == 1:
        print("Neozbrojen (což je na na soukromého detektiva vyšetřující sériového vraha celkem bizarní) vycházíš z kanclu.")
    elif magnum == 0 and zapalovac == 0:
       print("Naprosto nevybaven jdeš vstříc nebezpečnému případu, jako by jsi šel na procházku do parku.")
    print("----------------------") 
    print("[INVENTÁŘ:]")
    print(*inventar, sep = ", ")
    input("")
    print("----------------------")    
    winsound.PlaySound("Zamek",winsound.SND_FILENAME)
    print("Na cestě ven zamkneš dveře.")
    input("")
    print("----------------------")
    print("KONEC 1. KAPITOLY")
    print("----------------------")
    input("")     
    
def Kapitola_2_Rvacka_Vyrecnost():
    print("Když tohle 4 gangsteři uslyšeli, strnuli.")
    print("Vypadali, jako by je napomenula učitelka ve škole.")
    input("")
    print("[BALKÁNSKÝ GANGSTER 1:]"+'"To je Phil Marlowe!" Zvolá pak zničehonic jeden z gangsterů.')
    print("[BALKÁNSKÝ GANGSTER 2:]"+'"Pičku materinu..." Na to reaguje druhý plešoun.')
    input("")
    print("[BALKÁNSKÝ GANGSTER 1:]"+'"Jsme si vás s někým spletli, šéfe." říká původní dotazující.')
    print("----------------------")
    print("(Po chvíli 2 z gangsterů poznáš. Jeden se jmenuje Milo a druhý Branko, řečený 'Laba'.)")
    print("(Před rokem jsi pomohl k uvěznění vůdce Albánských gangsterů, který byl současně i vraždící maniak.)")
    input("")
    print("(2 zmínění gangsteři ti v tom případu dost pomohli.)")
    print("(A díky tobě Albáncům bez vůdce Srbové natrhli prdel a vzali si jejich území.)")
    print("----------------------")
    input("")
    print("[TY:]"+'"Půjčím si vaše auto!"')
    print("<Laba ti podá klíčky a uhne ti z cesty, přitom nenamítá ani slovo>")
    input("")
    Kapitola_2_Cesta()
def Kapitola_2_Rvacka():
    while True:
        print('"A)Hele, chlapi. Nechci problémy!"<ustupuješ zpátky> B) <Zkusit mluvit Srbsky>. C)"Co chcete, buzeranti?" D)Vypsat inventář"')
        moznosti = input ('[A/B/C/D]:')
        if moznosti in ['A','B', 'C', 'D']:
            break
    if moznosti == "A":
        print("[TY:]"+'"Hele, chlapi. Nechci žádný problémy."')
        print("[TY:]"+'"Jen procházím."')
        input("")
        print("[BALKÁNSKÝ GANGSTER:]"+'"Tak se podíváme, co máš po kapsách, strejdo!"')
        print("Všichni 4 se tobě začnou blížit.")
        print("Budeš muset jednat.")
        input("")
        Kapitola_2_Rvacka_A()
    if moznosti == "B":
        print("[TY:]"+ '"Стварно сте га превели, зар не?!" Zařveš, autoritativním tónem.')
        print("Ještě, že jsi na střední vzal ten kurz srbštiny.")
        input("")
        Kapitola_2_Rvacka_Vyrecnost()
    if moznosti == "C":
        print("[Ty:]"+'"Co chcete, buzeranti?"')
        print("Opovržení a posměšek je ve tvém hlase zřetelný.")
        input("")
        print("[BALKÁNSKÝ GANGSTER 2:]"+'"Teď sis vo to řek, voe!"')
        print("Bitka je nevyhnutelná.")
        input("")
        Kapitola_2_Rvacka_A()
            
    if moznosti == "D":
        print("----------------------") 
        print("[INVENTÁŘ:]")
        print(*inventar, sep = ", ")
        while True:
            print('A)"Hele, chlapi. Nechci problémy!"<ustupuješ zpátky> B)<Zkusit mluvit Srbsky>. C)"Co chcete, buzeranti?"')
            moznosti = input ('[A/B/C]: ')
            if moznosti in ['A','B','C']:
                break
        if moznosti  == "A":
            print("[TY:]"+'"Hele, chlapi. Nechci žádný problémy."')
            print("[TY:]"+'"Jen procházím."')
            input("")
            print("[BALKÁNSKÝ GANGSTER:]"+'"Tak se podíváme, co máš po kapsách, strejdo!"')
            print("Všichni 4 se tobě začnou blížit.")
            print("Budeš muset jednat.")
            input("")
            Kapitola_2_Rvacka_A()
        if moznosti == "C":
            print("[Ty:]"+'"Co chcete, buzeranti?"')
            print("Opovržení a posměšek je ve tvém hlase zřetelný.")
            input("")
            print("[BALKÁNSKÝ GANGSTER 2:]"+'"Teď sis vo to řek, voe!"')
            print("Bitka je nevyhnutelná.")
            input("")
            Kapitola_2_Rvacka_A()
        if moznosti == "B":
            print("[TY:]"+ '"Стварно сте га превели, зар не?!" Zařveš, autoritativním tónem.')
            print("Ještě, že jsi na střední vzal ten kurz srbštiny.")
            input("")
            Kapitola_2_Rvacka_Vyrecnost()

def Kapitola_2_Rvacka_A():
    global magnum
    while True:
        print('A) <Sáhneš pro kanón> B) <Zkusit mluvit Srbsky>. C)"<hodit po jednom z nich zápisník>"')
        moznosti = input ('[A/B/C]: ')
        if moznosti in ['A','B', 'C']:
            break
    if moznosti == "A" and magnum == 1:
        print("Pohled na Phila Marlowa s 44. magnum v ruce má silný efekt.")
        print("Plešouni jsou pryč tak rychle, že po nich zůstaly jen klíčky od auta.")
        input("")
        print("[TY:]"+'"Hehehe." utrousíš, když klíčky zvedneš ze země.')
        print("Snad jim nebude vadit, když si to auto na chvíli půjčíš.")
        input("")
        Kapitola_2_Cesta()
    if moznosti == "A" and magnum == 0:
        print(" Sáhneš po magnum, ale není tam...")
        print("Po první ráně jsi v bezvědomí.")
        input("")
        print("KONEC")
        sys.exit()
    if moznosti == "B":
        print("[TY:]"+ '"Стварно сте га превели, зар не?!" Zařveš, autoritativním tónem.')
        print("Ještě, že jsi na střední vzal ten kurz srbštiny.")
        input("")
        Kapitola_2_Rvacka_Vyrecnost()
        
    if moznosti == "C":
        Kapitola_2_Bitka_1()
def Kapitola_2_Bitka_1():
    print("<Zápisník vyletí z tvé kapsy dost rychle>")
    print("<První nabíhající se na něj začne soustředit a chce ho chytit>")
    input("")
    print()
    print("----------------------")
    print("(To je ten nejstarší trik na světě, a stejně na něj každý skočí, usměješ se v duchu.)")
    print("(Je pořád lepší mít proti sobě 4 nepřátele, kteří se rvát neumí, než jednoho frajera, který to umí dobře.)")
    print("(A tohle očividně nejsou žádní profíci.)")
    print("----------------------")
    print()
    input("")
    print("Plešoun chytne zápisník, co mu přistál na prsou, oběma rukama.")
    print("<V tom už ale zasazuješ pecku ze zadní ruky.>")
    input("")
    winsound.PlaySound("Pestovka",winsound.SND_FILENAME)
    winsound.PlaySound("Prasknuti",winsound.SND_FILENAME)
    winsound.PlaySound("KO",winsound.SND_FILENAME)
    print("S příjemným zapraskáním plešoun padá k zemi.")
    input("")
    print("Víc zápisníků nemáš a zbytek gangsterů už je skoro u tebe.")
    print("Jeden už je na vzdálenot rukou.")
    while True:
        print('A)Hák B)Znovu zadní C)Přední')
        moznosti = input('[A/B/C]:')
        if moznosti in ['A','B','C']:
            break
    if moznosti == "A":
        Kapitola_2_Bitka_2()
    if moznosti == "B":
        print("Zadní je (bohužel) moc pomalá.")
        print("Mineš a jsi bit.")
        print("KONEC")
        time.sleep(3)
        sys.exit()
    if moznosti == "C":
        winsound.PlaySound("Predni",winsound.SND_FILENAME)
        print("Přední sice nabíhajícího na chvíli zdrží, ale tvoje zpráskání neodvrátí.")
        print()
        print("----------------------")
        print("Příště zkuste něco ráznějšího, než direkt.")
        print("----------------------")
        print()
        input("")
        print("3 gangsteři tě dobijí do bezvědomí.")
        print("KONEC")
        time.sleep(3)
        sys.exit()

def Kapitola_2_Bitka_2():
    winsound.PlaySound("Hak",winsound.SND_FILENAME)
    winsound.PlaySound("KO",winsound.SND_FILENAME)
    print("Přesný hák na bradu je víc, než tisíc slov.")
    print("Gangster padl na zem, jak pytel brambor.")
    input("")
    print("2 gangteři leží bezvládně na zemi, ale 2 pořád ještě stojí a řítí se na tebe.")
    print("Jeden doběhne a hned se po tobě rozmáchne přední rukou.")
    input("")
    print()
    print("----------------------")
    print("(Tenhle asi moc boxovat neumí, pomyslíš si, když sleduješ naprosto netechnickou a pomalou ránu, co se na tebe řítí.)")
    print("----------------------")
    print()
    input("")
#   print("----------------------")
#   print("***'Sidestep' je v boxu označení pro úhybný manévr, kde se boxer otočí na špičce přední nohy, čímž změní úhel.***")
#   print("***Na obranu před údery ze strany se moc nehodí.***")
#   print("----------------------")
#   print()
    while True:
        print('A) <duck(*)> B) <sidestep(*)> C)<ústup>')
        print("----------------------")
        print("***'Sidestep' je v boxu označení pro úhybný manévr, kde se boxer otočí na špičce přední nohy, čímž změní úhel.***")
        print("***Na obranu před údery ze strany se moc nehodí.***")
        print("----------------------")
        print()
        print("----------------------")
        print("***'Duck' neboli přikrčení/pokrčení je způsob obrany v boxu. Perfektně se hodí pro obranu před háky, protože obránce nijak neustupuje.***")
        print("----------------------")
        print()
        moznosti = input ('[A/B/C]:')
        if moznosti in ['A','B', 'C']:
            break
    if moznosti == "A":
        print("Uděláš duck (neboli se pokrčíš v kolenou) a úder ti prosviští nad hlavou.")
        input("")
        winsound.PlaySound("PredniZadniwav",winsound.SND_FILENAME)
        winsound.PlaySound("KO",winsound.SND_FILENAME)
        input("")
        print("Přední zadní posíláš třetího gangstera do říše snů.")
        Kapitola_2_Bitka_3()
    if moznosti == "B":
        print("Kdybyste četli pozorněji, nezvolili by jste tuto možnost! -_-")
        print("Sidestepem se postavíte přímo do rány.")
        input("")
        print("Padneš na zem a plešouni tě dokopou")
        print("KONEC")
        time.sleep(3)
        sys.exit()
    if moznosti == "C":
        print("Při ústupu uklouzneš po blitcích na chodníku.")
        input("")
        print("Plešouni tě domlátí na zemi.")
        print("KONEC")
        time.sleep(3)
        sys.exit()
def Kapitola_2_Bitka_3():
    global magnum
    print("Podařilo se ti vyrovnat počtovou převahu.")
    print("Poslední gangster vytáhne vystřelovák a podnikne výpad.")
    input("")
    print()
    print("----------------------")
    print("(Tenhle je z nich asi nejlepší. Alespoň chápe, jak se s takovým vystřelovákem zápasí.)")
    print("(Není to žádné sekání ani řezání. Jen rychlé a přesné bodavé výpady.)")
    print("----------------------")
    print()
    while True:
        print('A)<Prosit o milost> B)<Použít Krav Magu> C)<Vykopnout> D)<Vytáhnout magnum> E)Vypsat inventář')
        moznosti = input ('[A/B/C/D/E]:')
        if moznosti in ['A','B','C','D','E']:
            break
    if moznosti == "A":
            print("Tvoje škemrání nezastavilo plešouna, aby ti vrazil nůž do srdce.")
            print("KONEC")
            time.sleep(5)
            sys.exit()
    if moznosti == "B":
            print("Dobrý pokus, ale Krav Maga funguje jen ve filmech a ve hrách.")
            input("")
            print("...Ale tohle je dost realistická hra, takže máš smůlu!")
            print("Byl jsi pobodán.")
            input("")
            print("KONEC")
            time.sleep(5)
            sys.exit()
    if moznosti == "C":
            print("Než stačí plešoun podniknout druhý výpad, vykopneš.")
            winsound.PlaySound("Kop",winsound.SND_FILENAME)
            winsound.PlaySound("NuzPada",winsound.SND_FILENAME)
            input("")
            print("Štěstí stojí na tvé straně.")
            print("Podařilo se ti vykopnout vystřelovák z ruky plešouna.")
            input("")
            winsound.PlaySound("Pestovka",winsound.SND_FILENAME)
            winsound.PlaySound("KO",winsound.SND_FILENAME)
            input("")
            print("Jedna dobře mířená a je dobojováno.")
            Kapitola_2_Bitka_Vitezstvi()
    if moznosti == "D" and magnum == 1:
            print("Vytáhneš ruční kanón z pouzdra a bez míření vystřelíš.")
            print("Rychlejší, než tento proces, už je jen světlo.")
            input("")
            winsound.PlaySound("Magnum",winsound.SND_FILENAME)
            winsound.PlaySound("Nabojnice",winsound.SND_FILENAME)
            winsound.PlaySound("KO",winsound.SND_FILENAME)
            print("Rána z magnum probudila celou ulici.")
            input("")
            print("Z gangsterovy hlavy nezbylo...")
            print("No...")
            input("")
            print("Vůbec nic.")
            Kapitola_2_Bitka_Vitezstvi()
    if moznosti == "D" and magnum == 0:
            print("Sáhneš pro magnum, ale není tam.")
            print("Nůž se ti zabodne 20 čísel do prsou.")
            input("")
            print("KONEC")
            sys.exit()
    if moznosti == "E":
         print("[INVENTÁŘ:]")
         print()
         print("----------------------")
         print(*inventar, sep=", ")
         print("----------------------")
         print()
         while True:
            print('A)<Prosit o milost> B)<Použít Krav Magu> C)<Vykopnout> D)<Vytáhnout magnum>')
            moznosti = input ('[A/B/C/D]:')
            if moznosti in ['A','B','C','D']:
                break
         if moznosti == "A":
             print("Tvoje škemrání nezastavilo plešouna, aby ti vrazil nůž do srdce.")
             print("KONEC")
             time.sleep(5)
             sys.exit()
         if moznosti == "B":
             print("Dobrý pokus, ale Krav Maga funguje jen ve filmech a ve hrách.")
             input("")
             print("...Ale tohle je dost realistická hra, takže máš smůlu!")
             print("Byl jsi pobodán.")
             input("")
             print("KONEC")
             time.sleep(5)
             sys.exit()
         if moznosti == "C":
             print("Než stačí plešoun podniknout druhý výpad, vykopneš.")
             winsound.PlaySound("Kop",winsound.SND_FILENAME)
             winsound.PlaySound("NuzPada",winsound.SND_FILENAME)
             input("")
             print("Štěstí stojí na tvé straně.")
             print("Podařilo se ti vykopnout vystřelovák z ruky plešouna.")
             input("")
             winsound.PlaySound("Pestovka",winsound.SND_FILENAME)
             winsound.PlaySound("KO",winsound.SND_FILENAME)
             input("")
             print("Jedna dobře mířená a je dobojováno.")
             Kapitola_2_Bitka_Vitezstvi()
         if moznosti == "D" and magnum == 1:
             #global magnum
             winsound.PlaySound("Magnum",winsound.SND_FILENAME)
             winsound.PlaySound("KO",winsound.SND_FILENAME)
             print("Rána z magnum probudila celou ulici.")
             input("")
             print("Z gangsterovy hlavy nezbylo...")
             print("No...")
             input("")
             print("Vůbec nic.")
             Kapitola_2_Bitka_Vitezstvi()
         if moznosti == "D" and magnum == 0:
             #global magnum
             print("Sáhneš pro magnum, ale není tam.")
             print("Nůž se ti zabodne 20 čísel do prsou.")
             input("")
             print("KONEC")
             sys.exit()    
            
def Kapitola_2_Cesta():
    print("----------------------")
    print("To auto teda není zrovna v nejlepší stavu...")
    print("S odporem nastoupíš do rozvrzané, ojeté a oprýskané kraksny srbských gangsterů.")
    input("")
    print("Uvnitř to snad vypadá ještě hůř, než zvenčí.")
    input("")
    print("[TY:]"+'"Vypadá to tady, jak ve vopičárně..."')
    print("[TY:]"+"<čich>"+'"A taky to tak smrdí..."')
    input("")
    print("Nevíš, jestli se ti chce posadit do sedadla řidiče.")
    input("")
    print("Přeci jenom, tyhle kalhoty jsi včera pracně pral...")
    input("")
    print()
    print("----------------------")
    print("(Ještě jednou se zamyslíš nad kariérou faráře.)")
    print("----------------------")
    print()
    input("")
    print("Pak si sedneš.")
    print("Skoro lituješ, že jsi to nezkusil jít pěšky.")
    input("")
    print("I když, to by jsi asi umrzl v lese...")
    input("")
    print("<klíčky>")
    print("...")
    input("")
    print("Nechytá. Prostě nechytá.")
    print("<Rozhlédneš se>")
    input("")
    print("To auto je nemytý.")
    
    Kapitola_2_Cesta_2()
def Kapitola_2_PoNehode():
    global zapisnik
    print("----------------------")
    print("Co teď?")
    input("")
    while True:
        print("A)<Prohledat auto> B)<Prohledat řidiče> C)<Odejít> D)<Vypsat inventář>")
        moznosti = input("[A/B/C/D]:")
        if moznosti in ['A','B','C','D']:
            break
    if moznosti == "B":
        print("Řidič má rozšmelcovanou hlavu.")
        print("Malá nenápadná injekce se v tom fofru rozstříštila na podlaze auta.")
        input("")
        print("Ještě prohledáš kapsy řidiče.")
        winsound.PlaySound("Item", winsound.SND_FILENAME)
        print("Našel jsi u něj jen zmačkaný vzkaz, jeden další zmačkaný papír a zapalovač.")
        input("")
        print("[VZKAZ:]"+'"Někdo se znova pokusil čmuchat ohledně případu. Nejspíš je místní ze Salemu."')
        zapisnik.append("Ze vzkazu u kolemjedoucího řidiče je jasné, že máš co do činění s organizovanou skupinou vrahů.")
        input("")
        print("Na druhém zmačkaném papíru je tvoje podobizna...")
        print("Z druhé strany je tvé jméno. A taky další vzkaz.")
        input("")
        print("[VZKAZ 2:]"+'"Phil Marlowe. Soukromý detektiv. Extra třída. Do případu zatažen informátorem."')
        print("Nejspíš už je na cestě do Salemu. Sejmout a zakopat v horách.")
        input("")
        while True:
            print("A)<Prohledat auto> B)<Odejít> C)<Vypsat inventář>")
            input("[A/B/C]:")
            if moznosti in ['A', 'B', 'C']:
                break
            if moznosti == "C":
                print("Řidič má rozšmelcovanou hlavu.")
                print("Malá nenápadná injekce se v tom fofru rozstříštila na podlaze auta.")
                input("")
                print("Ještě prohledáš kapsy řidiče.")
                winsound.PlaySound("Item", winsound.SND_FILENAME)
                print("Našel jsi u něj jen zmačkaný vzkaz, jeden další zmačkaný papír a zapalovač.")
                input("")
                print("[VZKAZ:]" + '"Někdo se znova pokusil čmuchat ohledně případu. Nejspíš je místní ze Salemu."')
                zapisnik.append(
                    "Ze vzkazu u kolemjedoucího řidiče je jasné, že máš co do činění s organizovanou skupinou vrahů.")
                input("")
                print("Na druhém zmačkaném papíru je tvoje podobizna...")
                print("Z druhé strany je tvé jméno. A taky další vzkaz.")
                input("")
                print("[VZKAZ 2:]" + '"Phil Marlowe. Soukromý detektiv. Extra třída. Do případu zatažen informátorem."')
                print()
                print("----------------------")
                print("(Zamyslíš se, jak to mohli zjistit tak rychle.)")
                print("----------------------")
                print()
                print("Nejspíš už je na cestě do Salemu. Sejmout a zakopat v horách.")
                input("")
    if moznosti == "C":
        Kapitola_2_PoNehode2()
    if moznosti == "D":
        print()
        print("----------------------")
        print(*inventar, sep=", ")
        print("----------------------")
        print()
        input("")
        while True:
            print("A)<Prohledat auto> B)<Prohledat řidiče> C)<Odejít>")
            moznosti = input("[A/B/C]:")
            if moznosti in ['A', 'B', 'C']:
                break

    if moznosti == "A":
        print("Už předtím jsi zaznamenal, že auto je čisté a uklizené.")
        input("")
        print("Jenže to je tak asi všechno.")
        input("")
        print("Není tu vůbec nic. Všechen úložný prostor je prázdný.")
        input("")
        print("Vylezeš ven a podíváš se i do kufru.")
        print("Je v něm jen pytel na mrtvoly.")
        input("")
        print("[TY:]"+'"V té injekci asi neměl očkování proti chřipce."')
        print("Utrousíš.")
        input("")
        while True:
            print("A)<Prohledat řidiče> B)<Odejít> C)<Vypsat inventář>")
            moznosti = input("[A/B/C]:")
            if moznosti in ['A','B','C']:
                break
        if moznosti == "A":
            
            print("Řidič má rozšmelcovanou hlavu.")
            print("Malá nenápadná injekce se v tom fofru rozstříštila na podlaze auta.")
            input("")
            print("Ještě prohledáš kapsy řidiče.")
            winsound.PlaySound("Item", winsound.SND_FILENAME)
            print("Našel jsi u něj jen zmačkaný vzkaz, jeden další zmačkaný papír a zapalovač.")
            input("")
            print("[VZKAZ:]"+'"Někdo se znova pokusil čmuchat ohledně případu. Nejspíš je místní ze Salemu."')
            zapisnik.append("Ze vzkazu u kolemjedoucího řidiče je jasné, že máš co do činění s organizovanou skupinou vrahů.")
            input("")
            print("Na druhém zmačkaném papíru je tvoje podobizna...")
            print("Z druhé strany je tvé jméno. A taky další vzkaz.")
            input("")
            print("[VZKAZ 2:]"+'"Phil Marlowe. Soukromý detektiv. Extra třída. Do případu zatažen informátorem."')
            print("Nejspíš už je na cestě do Salemu. Sejmout a zakopat v horách.")
            input("")            
def Kapitola_2_Setkani_A_2():
    print("[TY:]"+"<povzdech>")
    print("Do Salemu se musíš dostat, a v tom lijáku tak možná zabloudíš.")
    input("")
    print("[TY:]"+'"Tak dobře. Jestli vám to teda nevadí, potřeboval bych svézt do Salemu!"')
    input("")
    print("[KOLEMJEDOUCÍ:]"+'"Dobře. Nasedejte."')
    print("Něco se ti na tom ale fakt nezdá...")
    input("")
    print("Nakonec ale do auta nasedneš.")
    input("")
    print("Tohle auto rozhodně není, jako ta kraksna srbských gangsterů.")
    print("Je tu uklizeno a čisto.")
    input("")
    print("Kolemjedoucí nasedne, a začne jet směrem, kterým přijel.")
    print("[KOLEMJEDOUCÍ:]"+'"A co v Salemu, pane? Omluvte mou upřímnost, ale je to zapadákov."')
    input("")
    while True:
        print('A)"Byznys." B)"Turistika" C)<všechno mu vyzvonit>')
        moznosti = input("[A/B/C]:")
        if moznosti in ['A','B','C']:
            break
    if moznosti == "C":    
        print("<Všechno jsi mu vyzvonil>")
        input("")
        print("Což se nedělá.")
        print("Bůh tě srazil bleskem spravedlnosti.")
        input("")
        print("KONEC")
        time.sleep(5)
        sys.exit()
    if moznosti == "B":
        print("[TY:]"+'"Turistika."')
        print("To je asi ta nejhorší výmluva, co jsi mohl říct.")
        input("")
        print("Postarší chlápek, co je cítít tabákem a bourbonem, má na sobě oblek, kabát a klobouk...")
        print("Nemá žádný batoh a navíc má na sobě boty k obleku.")
        print("Mimo to jde v tom největším dešti za poslední léta...")
        input("")
        print("Po silnici.")
        input("")
        print("Když ti dojde, jak špatnou výmluvu jsi právě řekl, umřeš trapností.")
        print("KONEC")
        time.sleep(5)
        sys.exit()
    if moznosti == "A":
        print("[TY:]"+'"Byznys."')
        print("Odpovíš stroze.")
        input("")
        print("[KOLEMJEDOUCÍ:]"+'"Nechcete žvýkačku?"')
        print("[TY:]"+'"Ano. Děkuji."')
        print("Žvýkačku by sis vážně dal.")
        input("")
        print("<Kolemjdoucí neohrabaně podává balíček žvýkaček při řízení.>")
        print("<Balíček mu vypadne z rukou a skončí pod tvým sedadlem.>")
        input("")
        print("[KOLEMJEDOUCÍ:]"+'"Aaa, zatraceně! Pardon. Natáhnete se tam?"')
        print("<Natáhneš se pro balíček pod sedadlo.>")
        input("")
        print("Tady něco nehraje... A asi tě napadlo, co.")
        print("Ten člověk jede opačným směrem, než je Salem.")
        input("")
        print("Jsi Phil Marlowe, posilněný bourbonem a ranní cigaretou.")
        print("Což znamená, že tvoje reflexy jsou v tuto chvíli na svém rychlostním maximu.")
        input("")
        print("<Když se natáhneš pod sedadlo, čas se zpomalí.>")
        input("")
        print("Cítíš, jak řidič natahuje ruku ke tvému krku, v rukávu má malou injekci.")
        while True:
            print("A)<Sklonit hlavu, vyhnou se jehle injekce> B)<Smířit se s osudem> C)<Prudce se zaklonit dozadu>")
            moznosti = input("[A/B/C]:")
            if moznosti in ['A', 'B','C']:
                break
        if moznosti == "B":
            print("Smířil ses s osudem.")
            print("Injekce ti probodne krkavici a vypustí tam 100 násobek smrtelné dávky batrachotoxinu(*).")
            print()
            print("----------------------")
            print("***Batrachotoxin je jedním z nejpotentnějších jedů na planetě, způsobuje svalovou paralýzu a zástavu srdce.***")
            print("***Smrtelná dávka je hmotnostně srovnatelná s 2mi zrnkami soli.***")
            print("***Při použití v injekci je účinek okamžitý a brutální.***")
            print("----------------------")
            print()
            input("")
            print("Jsi oběť číslo 4.")
            print("KONEC")
            time.sleep(5)
            sys.exit()
        if moznosti == "A":
            print("<Skloníš hlavu, řidičova ruka ti projede přímo nad hlavou.>")
            print("Z tohoto postavení však můžeš těžko zareagovat dál, takže řidič ti ve zlomku sekundy zabodne injekci do těla.")
            input("")
            print("Injekce ti probodne krkavici a vypustí tam 100 násobek smrtelné dávky batrachotoxinu(*).")
            print()
            print("----------------------")
            print("***Batrachotoxin je jedním z nejpotentnějších jedů na planetě, způsobuje svalovou paralýzu a zástavu srdce.***")
            print("***Smrtelná dávka je hmotnostně srovnatelná s 2mi zrnkami soli.***")
            print("***Při použití v injekci je účinek okamžitý a brutální.***")
            print("----------------------")
            print()
            input("")
            print("Jsi oběť číslo 4.")
            print("KONEC")
            time.sleep(5)
            sys.exit()
        if moznosti == "C":
            print("Zaklonil ses větší rychlostí, než kterou cestuje světlo.")
            print("Řidičova ruka ti projede přímo před hrudníkem.")
            input("")
            while True: 
                print("A)<Zvedák na bradu> B)<Chytit ruku v lokti>")
                moznosti = input("[A/B]:")
                if moznosti in ['A','B']:
                    break
            if moznosti == "A":
                print("<Levou ruku naúhluješ pod ruku s injekcí a pálíš přímo na bradu.>")
                winsound.PlaySound("Pestovka",winsound.SND_FILENAME)
                input("")
                print("Řidič na místě usnul.")
                print("Padne čelem na volant.")
                input("")
                print("Auto dostane smyk a narazí přímo do stromu podél silnice.")
                input("")
                winsound.PlaySound("Nehoda",winsound.SND_FILENAME)
                #winsound.PlaySound("Klakson",winsound.SND_LOOP|winsound.SND_ASYNC)
                print("Řidič leží s rozbitou hlavou na volantu.")
                input("")
                print("Cítíš se šťastný, že jeho hlava nepadla na klakson.")
                print("Mimo to se taky cítíš šťastný, že se ti nic nestalo.")
                #winsound.PlaySound(None,winsound.SND_ASYNC)
                Kapitola_2_PoNehode()
            if moznosti == "B":
                print("<Co nejrychleji zachytíš řidičovu ruku v lokti.>")
                print("To způsobí, že řidič se přestane dívat na cestu a začne se dívat na svou zachycenou ruku.")
                input("")
                winsound.PlaySound("Nehoda",winsound.SND_FILENAME)
                print("Srážka se stromem u silnice je smrtelná pro vás oba.")
                print("KONEC")
                time.sleep(5)
                sys.exit()
                    
       
       
       
def Kapitola_2_Setkani_B():
    print("[KOLEMJEDOUCÍ:]"+'"Heh. No, nechcete, abych vás svezl? V tomhle počasí dostanete tak možná zápal plic."')
    input("")
    print("Dobré samaritánství neznámeho kolemjedoucího ti připadá dost divné.")
    print("Na druhou stranu, toho sériového vraha (nebo vrahy?) asi těžko porazíš se zápalem plic...")
    Kapitola_2_Setkani_A_2()
def Kapitola_2_Setkani_C():
    print("Hned, jak to dořekneš, už stojíš přímo u kolemjedoucího.")
    print("<Ramenem ho odstrčíš stranou.>")
    input("")
    print("Kolemjedoucí tě při tom nenápadně bodne malou injekcí, ukrytou v rukávu.")
    input("")
    print("Smrtelná dávka batrachotoxinu(*) tě zabije na místě.")
    print()
    print("----------------------")
    print("***Batrachotoxin je jedním z nejpotentnějších jedů na planetě, způsobuje svalovou paralýzu a zástavu srdce.***")
    print("***Smrtelná dávka je hmotnostně srovnatelná s 2mi zrnkami soli.***")
    print("***Při použití v injekci je účinek okamžitý a brutální.***")
    print("----------------------")
    print()
    input("")
    print("Jsi oběť číslo 4.")
    print("KONEC")
    time.sleep(5)
    sys.exit()
def Kapitola_2_Setkani_A():
    print("[KOLEMJEDOUCÍ:]"+'"Hele, nic mi do toho není, ale proč jdete pěšky uprostřed toho lijáku?"')
    print("<Tázající rozhodí rukama v otevřeném gestu a postaví se ti přímo do cesty>")
    input("")
    while True:
        print('A)"Máte pravdu, nic vám do toho není." B)"Musím se někam dostat a musím se tam dostat co nejdřív." C)<Neodpovídat, odstrčit ho stranou>')
        moznosti = input("[A/B/C]:")
        if moznosti in ['A', 'B', 'C']:
            break
    if moznosti == "A":
        print("[TY:]"+'"Máte pravdu, nic vám do toho není."')
        print("Odpovíš, svým kovovým nekompromisním hlasem.")
        input("")
        print("[KOLEMJEDOUCÍ:]"+'"To je škoda, myslel jsem, že bych vás svezl..."')
        Kapitola_2_Setkani_A_2()
    if moznosti == "B":
        print("[TY:]"+'"Musím se někam dostat a musím se tam dostat co nejdřív."')
        print("Řekneš, nezmiňujíc nic konkrétnějšího.")
        input("")
        print("[KOLEMJEDOUCÍ:]"+'"Aha. A kam? Že bych vás svezl..."')
        Kapitola_2_Setkani_A_2()
    if moznosti == "C":
        print("<Pokusíš se kolemjedoucího odstrčit stranou.>")
        print("To se ti nakonec podaří, ale...")
        input("")
        print("Kolemjedoucí tě při tom nenápadně bodne malou injekcí, ukrytou v rukávu.")
        input("")
        print("Smrtelná dávka batrachotoxinu(*) tě zabije na místě.")
        print()
        print("----------------------")
        print("***Batrachotoxin je jedním z nejpotentnějších jedů na planetě, způsobuje svalovou paralýzu a zástavu srdce.***")
        print("***Smrtelná dávka je hmotnostně srovnatelná s 2mi zrnkami soli.***")
        print("***Při použití v injekci je účinek okamžitý a brutální.***")
        print("----------------------")
        print()
        input("")
        print("Jsi oběť číslo 4.")
        print("KONEC")
        time.sleep(5)
        sys.exit()
def Kapitola_2_Cesta_5():
    #winsound.PlaySound("dest", winsound.SND_ASYNC)
    print("----------------------")
    print("Déšť prostě nechce přestat.")
    input("")
    print("Pokračuješ vpřed.")
    print("...")
    input("")
    print("Po chvíli uslyšíš zvuk blížícího se auta.")
    input("")
    #winsound.PlaySound(None, winsound.SND_ASYNC)
    input("")
    print("Kdo by tudy proboha projížděl?")
    print("Zamyslíš se.")
    input("")
    print("Auto zastaví přímo před tebou.")
    input("")
    print("Vyleze z něj hubená postava. To je tak všechno, co přes liják dokážeš zaregistrovat.")
    print("[CIZINEC:]"+'"To je docelá blbá doba na procházku, pane!"')
    print()
    print("----------------------")
    print("(Přednesem jako by se snažil působit, jako vtipkující pohodář.)")
    print("----------------------")
    print()
    while True:
        print('A)<neodpovídat> B)"Ideální čas na procházku, vskutku!" C)"Nechcete mi uhnout z cesty? Spěchám!"')
        moznosti = input("[A/B/C]:")
        if moznosti in ['A','B','C']:
            break
    if moznosti == "A":
        print("<Neodpovídáš, hledíš si svého>")
        input("")
        print("<Do ničeho se nemontuješ>")
        input("")
        Kapitola_2_Setkani_A()
    if moznosti == "B":
        print("[TY:]"+'"Ideální čas na procházku, vskutku!"')
        print("Jeden musí obdivovat, že tě neopouští smysl pro humor i v těchto těžkých časech.")
        input("")
        Kapitola_2_Setkani_B()
    if moznosti == "C":
        print("[TY:]"+'"Nechcete mi uhnout z cesty?! Spěchám!"')
        print("Řekneš, podrážděně.")
        input("")
        Kapitola_2_Setkani_C()
        
def Kapitola_2_Cesta_4():
    #winsound.PlaySound("dest", winsound.SND_ASYNC)
    print("----------------------")
    print("Déšť ti znesnadňuje pohyb.")
    print("Který je už dost znesnadněn tím, že jdeš do kopce.")
    input("")
    print()
    print("----------------------")
    print("(Chvíli se obáváš, aby ti nenavlhnul kvér.)")
    print("----------------------")
    print()
    input("")
    print("Je tohle vůbec ten správný směr?")
    while True:
        print("A)Je. B)<Zaváhat> C)<začít panikařit>")
        moznosti = input("[A/B/C]:")
        if moznosti in['A', 'B', 'C']:
            break
    if moznosti == "A":
        print("Jasně, že je to správná cesta.")
        print("Je to jediná silnice, co tu kolem je.")
        input("")
        print("Ztěžka pokračuješ vpřed.")
        Kapitola_2_Cesta_5()
    if moznosti == "B":
        print('"Kdo zaváhá, je ztracen." - Autor neznámý.')
        print("Jsi ztracen.")
        input("")
        print("KONEC")
        time.sleep(5)
        sys.exit()
    if moznosti == "C":
        print("Zpanikaříš v domnění, že jsi se ztratil.")
        print("To ti přivodí infarkt.")
        input("")
        print("KONEC")
        time.sleep(5)
        sys.exit()
    #winsound.PlaySound(None, winsound.SND_ASYNC)  
def Kapitola_2_Cesta_3():
    print()
    print("Cesta do Salemu je dlouhá a nudná.")
    input("")
    print("A celou cestu musíš potlačovat nutkání zvracet z tohoto zaneřáděného vehiklu.")
    input("")
    print("Z nějakého důvodu dnes prostě nepřestává pršet.")
    input("")
    print("Projíždíš tou nejhorší čtvrtí města.")
    print("Ghetto.")
    print()
    print("----------------------")
    print("(V hlavě ti na chvíli začne hrát píseň 'In the Ghetto'.)")
    print("Tuto myšlenku hned zapudíš.")
    print("----------------------")
    print()
    input("")
    print("Gangsteři, dealeři, kurvy, pasáci. Nasilníci.")
    print("Doufáš, že jednou zaprší pořádně a všechnu tuhle pakáž to spláchne do kanálu, kam patří.")
    input("")
    print("...")
    print("Po chvíli už jsi venku z města.")
    print("Po silnici jedeš směrem do hor, tam, kde leží Salem.")
    print("Už jsi skoro překonal největší stoupání, když ti dojde palivo.")
    #SEM ZVUK
    input("")
    print("[TY:]"+'"No to si snad ze mě děláš..."')
    input("")
    print("Než to dořekneš, auto se úplně zastaví.")
    print("Sedíš ve smradlavé kraksně srbských gangsterů.")
    print("Kolem je ten největší liják v roce, jsi na úpatí velkého kopce a došel ti benzín.")
    input("")
    print("[TY:]"+ '"Jsem v hajzlu..."')
    print("Řekneš si, optimisticky.")
    input("")
    while True:
        print("A)<Vystoupit z auta, padnout na kolena a prosit boha o pomoc> B)<Počkat, až přestane pršet> C)<začít lamentovat>")
        moznosti = input("[A/B/C]:")
        if moznosti in ['A', 'B','C']:
            break
    if moznosti == "A":
        print("Dobrý nápad.")
        print("Ale bůh neodpovídá.")
        input("")
        print("Uklouzl jsi v dešti a skutálel se z kopce.")
        print("KONEC")
        time.sleep(6)
        sys.exit()
    if moznosti == "B":
        print("<Čekáš>")
        print("...")
        print("...")
        input("")
        print("Umřel jsi stářím.")
        print("KONEC")
        time.sleep(6)
        sys.exit()
    if moznosti == "C":
        print("[TY:]"+'"Kurvaa! Proč já do píčiii?!?!"')
        print("<další lamentování>")
        input("")
        print("Po chvíli se naštveš, vystoupíš a prostě odejdeš pěšky.")
        Kapitola_2_Cesta_4()
        
def Kapitola_2_Cesta_2():
    global guma
    global zapalovac
    global inventar
    while True:
        print("A)<Zkusit to znovu> B)<Poblít se z prostředí> C)<Praštit do palubní desky>")
        moznosti = input('[A/B/C]:')
        if moznosti in ['A','B', 'C']:
            break
    if moznosti == "A":
        winsound.PlaySound("Motor",winsound.SND_FILENAME)
        print("Motor nestartuje.")
        input("")
        while True:
            print("A)<Poblít se z prostředí> B)<Praštit do palubní desky> C)<Zkusit to ještě jednou>")
            moznosti = input('[A/B/C]:')
            if moznosti in ['A','B', 'C']:
                break
        if moznosti == "A":
            #SEM ZVUK
            print("Začal jsi blít.")
            input("")
            print("Za chvíli začneš blít krev.")
            input("")
            print("Praskl ti žaludeční vřed z chlastání, kouření a nadměrného stresu.")
            print("KONEC")
            time.sleep(3)
            sys.exit()
        if moznosti == "B":
            winsound.PlaySound("Pest_deska", winsound.SND_FILENAME)
            print("<Vší silou praštíš do palubní desky.>")
            input("")
            print("Zlámal sis zápěstí.")
            print("KONEC")
            time.sleep(3)
            sys.exit()
        if moznosti == "C":
            winsound.PlaySound("Motor",winsound.SND_FILENAME) 
            print("Motor nestartuje.")
            input("")
            print("...")
            print("Zkusíš to ještě jednou.")
            winsound.PlaySound("Motor",winsound.SND_FILENAME)
            print("A motor konečně naskočí!")
            print("[TY:]"+'"No sláva, kurva..."')
            print("Utrousíš.")
            input("")
            while True:
                print("A)<Jet do Salemu.> B)<Prohledat auto> C)<Zapálit si>")
                moznosti = input('[A/B/C]:')
                if moznosti in ['A','B', 'C']:
                    break
            if moznosti == "A":
                print("Opustíš bojiště a odjedeš do Salemu.")
                print("...")
                input("")
                Kapitola_2_Cesta_3()
            if moznosti == "C" and zapalovac == 1:
                winsound.PlaySound("Zapalovac", winsound.SND_FILENAME)
                winsound.PlaySound("Potahnuti", winsound.SND_FILENAME)
                print("Zapálil sis.")
                while True:
                    print("A)<Odjet do Salemu.> B)<Prohledat auto>")
                    moznosti = input("[A/B]:")
                    if moznosti in ['A', 'B']:
                        break
                if moznosti == "A":
                        print("Opustíš bojiště a odjedeš do Salemu.")
                        print("...")
                        input("")
                        Kapitola_2_Cesta_3()
                    
            if moznosti == "C" and zapalovac == 0:
                print("Zapálil by sis, ale nemáš zapalovač.")
                input("")
                while True:
                    print("A)<Odjet do Salemu.> B)<Prohledat auto>")
                    moznosti = input("[A/B]:")
                    if moznosti in ['A', 'B']:
                        break
                if moznosti == "A":
                    print("Opustíš bojiště a odjedeš do Salemu.")
                    print("...")
                    input("")
                    Kapitola_2_Cesta_3()
                if moznosti == "B":
                    global guma
                    print()
                    print("----------------------")
                    print("Napadně tě, jestli se v tom autě nepovaluje něco, co by se mohlo hodit.")
                    print("----------------------")
                    print()
                    input("")
                    #SEM ZVUK PROHLEDÁVÁNÍ
                    print("Auto obsahuje asi 10 prázdných flašek od Rakije.")
                    input("")
                    print("[TY:]"+'"Zasraný Srbové..."')
                    print("Utrousíš.")
                    input("")
                    print("Dále asi 15 prázdných krabiček od cigaret.")
                    print("A nezpočet vajglů.")
                    input("")
                    print("Pod sedadlem řidiče jsi našel nerozbalenou pánskou ochranu.")
                    print("S vůní.")
                    while True:
                        print("----------------------")
                        print("Vezmeš ji?")
                        moznosti = input("[Y/N]:")
                        if moznosti in ['Y', 'N']:
                            break
                    if moznosti == "Y":
                            winsound.PlaySound("Item",winsound.SND_FILENAME)
                            print("Sebral jsi prcgumu.")
                            guma = 1
                            global inventar
                            inventar.append("Pánská ochrana s vůní.")
                            input("")
                            while True:
                                print("A)<Odjet do Salemu>")
                                moznosti = input("[A]:")
                                if moznosti in ['A']:
                                    break
                            if moznosti == "A":
                                print("Opustíš bojiště a odjedeš do Salemu.")
                                print("...")
                                input("")
                                Kapitola_2_Cesta_3()
                    if moznosti == "N":
                        print("S odporem necháš šprcku ležet.")
                        input("")
                        while True:
                            print("A)<Odjet do Salemu>")
                            moznosti = input("[A]")
                            if moznosti in ['A']:
                                break
                        if moznosti == "A":
                            print("Opustíš bojiště a odjedeš do Salemu.")
                            print("...")
                            input("")
                            Kapitola_2_Cesta_3()
                        
                
            if moznosti == "B":
                print()
                print("----------------------")
                print("Napadně tě, jestli se v tom autě nepovaluje něco, co by se mohlo hodit.")
                print("----------------------")
                print()
                input("")
                #SEM ZVUK PROHLEDÁVÁNÍ
                print("Auto obsahuje asi 10 prázdných flašek od Rakije.")
                input("")
                print("[TY:]"+'"Zasraný Srbové..."')
                print("Utrousíš.")
                input("")
                print("Dále asi 15 prázdných krabiček od cigaret.")
                print("A nezpočet vajglů.")
                input("")
                print("Pod sedadlem řidiče jsi našel nerozbalenou pánskou ochranu.")
                print("S vůní.")
                while True:
                    print("----------------------")
                    print("Vezmeš ji?")
                    moznosti = input("[Y/N]:")
                    if moznosti in ['Y', 'N']:
                        break
                if moznosti == "Y":
                    winsound.PlaySound("Item",winsound.SND_FILENAME)
                    print("Sebral jsi prcgumu.")
                    #global guma
                    guma = 1
                    #global inventar
                    inventar.append("Pánská ochrana s vůní.")
                    input("")
                if moznosti == "N":
                    print("S odporem necháš šprcku ležet.")
                    input("")
                    
                while True:
                    #global zapalovac
                    print("A)<Odjet do Salemu.> B)<Zapálit si>")
                    moznosti = input("[A/B]:")
                    if moznosti in ['A', 'B']:
                        break
                if moznosti == "A":
                    print("Opustíš bojiště a odjedeš do Salemu.")
                    print("...")
                    input("")
                    Kapitola_2_Cesta_3()
                if moznosti == "B" and zapalovac == 1:
                    winsound.PlaySound("Zapalovac", winsound.SND_FILENAME)
                    winsound.PlaySound("Potahnuti", winsound.SND_FILENAME)
                    print("Zapálil sis. Podruhé.")
                    while True:
                        print("A)<Odjet do Salemu.>")
                        moznosti = input("[A]:")
                        if moznosti in ['A']:
                            break
                    if moznosti == "A":
                        print("Opustíš bojiště a odjedeš do Salemu.")
                        print("...")
                        input("")
                        Kapitola_2_Cesta_3()
                    
                if moznosti == "B" and zapalovac == 0:
                    print("Zapálil by sis, ale nemáš zapalovač.")
                    input("")
                    while True:
                        print("A)<Odjet do Salemu.>")
                        moznosti = input("[A]:")
                        if moznosti in ['A']:
                            break
                    if moznosti == "A":
                        print("Opustíš bojiště a odjedeš do Salemu.")
                        print("...")
                        input("")
                        Kapitola_2_Cesta_3()
            
            
    if moznosti == "B":
        print("Začal jsi blít.")
        input("")
        print("Za chvíli začneš blít krev.")
        input("")
        print("Praskl ti žaludeční vřed z chlastání, kouření a nadměrného stresu.")
        print("KONEC")
        time.sleep(3)
        sys.exit()
    if moznosti == "C":
        winsound.PlaySound("Pest_deska", winsound.SND_FILENAME)
        print("<Vší silou praštíš do palubní desky.>")
        input("")
        print("Zlámal sis zápěstí.")
        print("KONEC")
        time.sleep(3)
        sys.exit()
def Kapitola_2_Bitka_Vitezstvi():
    print()
    print("----------------------")
    print("(Kdyby šel zrovna někdo kolem, do konce života by tvrdil, že větší nakládačku jaktěživ neviděl.)")
    print("----------------------")
    print()
    print("Před tebou leží 4 bezvládná těla srbských gangsterů.")
    print("Co uděláš?")
    input("")
    while True:
        print('A)"KDO JE TADY ŠÉF, DO PÍČIIIIII?!?!??!!" B)<začít se mlátit do prsou a přitom vyřvávat možnost A)> C)<Sebrat zápisník a jít.>')
        moznosti = input ('[A/B/C]:')
        if moznosti in ['A','B', 'C']:
            break
    if moznosti == "A":
        print("Zařval jsi to tak nahlas, až ti zaskočilo a udusil ses.")
        input("")
        print("KONEC")
        time.sleep(5)
        sys.exit()
    if moznosti == "B":
        print("Tolik jsi se do toho vžil, že tě pátý gangster, co byl během rvačky za domem kvůli vykonání potřeby, uslyšel.")
        input("")
        print("Vzal tě zezadu po hlavě trubkou a na místě sejmul.")
        print("KONEC")
        time.sleep(5)
        sys.exit()
    if moznosti == "C":
        print("Radši by jsi měl jít.")
        input("")
        print("Máš jen 16 hodin, než se proberou.")
        print("Po cestě zakopneš o klíčky od auta.")
        print("Jednomu z gangsterů asi vypadly z kapsy, když se líbal s chodníkem.")
        input("")
        print("Snad nebude vadit, když si to auto na chvíli půjčíš.")
        Kapitola_2_Cesta()
        
        
def Kapitola_2_Auto():
    while True:
        print("A) Jít ke gangsterům. B) Zkusit to jít pěšky. C)<Nahlédnou do zápisníku>")
        moznosti = input ('[A/B/C]:')
        if moznosti in ['A','B', 'C']:
            break
    if moznosti == "A":
       print('Dobře víš, že v téhle části města žádné telefonní budky nejsou.')
       print("Procházíš kolem gangsterů, protože je to jediná cesta do lépe zařízené ulice.")
       input("")
       print("[BALKÁNSKÝ GANGSTER:]"+'"To čumíš na mě?"')
       print()
       print("----------------------") 
       print("(Zaregistruješ 5 věcí: Silný balkánský přízvuk, přesněji to ale neodhadneš. Dotazující má asi tak 90 kilo, a je asi o hlavu větší, než ty.)")
       print("(Má kolem sebe 3 kamarády. Všichni mají holé hlavy. A všichni jsou mladí, mezi 20-25.)")
       print("----------------------") 
       Kapitola_2_Rvacka()
    if moznosti == "B":
        print("S povzdechem vykročíš směrem do Salemu.")
        print("")
        print("Po cestě zabloudíš v lese a v noci umrzneš.")
        print("KONEC")
        input("")
        sys.exit()
    if moznosti == "C":
        print("----------------------")
        print("[ZÁPISNÍK:]")
        print(*zapisnik, sep = '// ')
        print("----------------------")
        while True:
            print("A) Jít ke gangsterům. B) Zkusit to jít pěšky.")
            moznosti = input ('[A/B]:')
            if moznosti in ['A','B']:
                break
        if moznosti == "A":
           print('Dobře víš, že v téhle části města žádné telefonní budky nejsou.')
           print("Procházíš kolem gangsterů, protože je to jediná cesta do lépe zařízené ulice.")
           input("")
           print("[BALKÁNSKÝ GANGSTER:]"+'"To čumíš na mě?"')
           print()
           print("----------------------") 
           print("(Zaregistruješ 5 věcí: Silný balkánský přízvuk, přesněji to ale neodhadneš. Dotazující má asi tak 90 kilo, a je asi o hlavu větší, než ty.)")
           print("(Má kolem sebe 3 kamarády. Všichni mají holé hlavy. A všichni jsou mladí, mezi 20-25.)")
           print("----------------------") 
           Kapitola_2_Rvacka()
        if moznosti == "B":
           print("S povzdechem vykročíš směrem do Salemu.")
           print("")
           print("Po cestě zabloudíš v lese a v noci umrzneš.")
           print("KONEC")
           input("")
           sys.exit()
def Kapitola_2_1():
    print("----------------------") 
    print("KAPITOLA 2")
    print("Tak zase rychle ven z kaclu. Dneska se tam nejspíš moc neohřeješ.")
    print("Na druhou stranu, kdo říká, že tohle je pohodlná profese?")
    input("")
    print('"Měl jsem jít na faráře..." Povzdechneš si.')
    print("...")
    print()
    print("Nacházíš se před kancelářkou budovou.")
    print("Což ti připomíná, že tvoje auto je zrovna v servisu.")
    input("")
    print("A Salem není zrovna v pěší vzdálenosti...")
    input("")
    while True:
        print('A)Najít nejbližší telefon a zavolat taxi. B)Zkusit to jít pěšky. C) Sednout si na obrubík, dát hlavu do dlaní a začít brečet. D)Vypsat inventář.')
        moznosti = input ('[A/B/C/D]:')
        if moznosti in ['A','B', 'C', 'D']:
            break
    if moznosti == "B":
        print("Vykročíš směrem k Salemu.")
        print("Po cestě zabloudíš v lese a v noci umrzneš.")
        input("")
        print("KONEC")
        time.sleep(3)
        sys.exit()    
    if moznosti == "C":
        print("Brečel jsi tak dlouho, až jsi umřel na dehydrataci.")
        print("KONEC")
        time.sleep(3)
        sys.exit()
    if moznosti == "A":
       print('Rozhlédneš se kolem sebe. Mimo zaneřáděnou silnici, poblitý chodník a pár gangsterů, co se baví u auta, nic zásadního nevidíš.')
       print("Rozhodně ne telefonní budku.")
       input("")
       Kapitola_2_Auto()
    if moznosti == "D":
        print("[INVENTÁŘ:]")
        print(*inventar, sep = ", ")
        while True:
            print('A)Najít nejbližší telefon a zavolat taxi. B)Zkusit to jít pěšky. C) Sednout si na obrubík, dát hlavu do dlaní a začít brečet.')
            moznosti = input ('[A/B/C]: ')
            if moznosti in ['A','B','C']:
                break
        if moznosti == "A":
           print('Rozhlédneš se kolem sebe. Mimo zaneřáděnou silnici, poblitý chodník a pár gangsterů, co se baví u auta, nic zásadního nevidíš.')
           print("Rozhodně ne telefonní budku.")
           input("")
           Kapitola_2_Auto()
        if moznosti == "B":
            print("Vykročíš směrem k Salemu.")
            print("Po cestě zabloudíš v lese a v noci umrzneš.")
            input("")
            print("KONEC")
            sys.exit()
        if moznosti == "C":
            print("Brečel jsi tak dlouho, až jsi umřel na dehydrataci.")
            print("KONEC")
            time.sleep(3)
            sys.exit()
def Vyber_Kapitol():
    while True:
        print("A)Kapitola 1 B) Kapitola 2")
        moznosti = input ('[A/B]:')
        print()
        if moznosti in ['A','B']:
            if moznosti == "A":
                Intro()                    
                print("----------------------")
                print("Zvedneš telefon?")
                odpoved = None 
                while odpoved not in ("Y", "N"):
                    odpoved = input("[Y/N]:")
                if odpoved == "Y":
                    print("S falešnou nadějí na pořádnej případ zvedneš sluchátko.")
                    print("[TY:]"+'"Phil Marlowe..." Mrzutým, rozespalým a napůl opilým hlasem řekneš do kulatého kusu plastu.')
                    print("V naději, že se z kusu plastu ozve odpověď.")
                    input("")
                    print("...")
                    print("...")
                    print("...")
                    while True:
                        moznosti = input ("A) Je tam někdo? B) To je fór? C) <mlčet> [A/B/C]? : ")
                        if moznosti in ['A','B', 'C']:
                            break
                    if moznosti == "A":
                        print("[TY:]"+'"Je tam někdo?" utrousíš, teď už spíš podrážděný než mrzutý, do děravého kusu plastu.')
                        Prvni_Kontakt_Vseobecna()
                        Prvni_Kontakt_Vseobecna_2()
                        Prvni_Kontakt_Vseobecna_3()
                        Kapitola_2_1()
                    if moznosti == "B":
                        print("[TY:]"+'"To je fór?"')
                        Prvni_Kontakt_Vseobecna()
                        Prvni_Kontakt_Vseobecna_2()
                        Prvni_Kontakt_Vseobecna_3()
                        Kapitola_2_1()
                    if moznosti == "C":
                        print("<mlčíš, čekáš>")
                        Prvni_Kontakt_Vseobecna()
                        Prvni_Kontakt_Vseobecna_2()
                        Prvni_Kontakt_Vseobecna_3()
                        Kapitola_2_1()
                    if odpoved == "N":
                        print("KONEC")
                        sys.exit()
            if moznosti == "B":
                global zapisnik
                zapisnik.append("Vrah (nebo vrahové?), má prozatím jen jednu potvrzenou oběť.")
                zapisnik.append("Prokázání skutečnosti, že potenciální klient byl otráven stejným jedem, by znamenalo druhou oběť.")
                zapisnik.append("Potvrzení tvé teorie, že korunní svěděk (farář) byl zavražděn stejným vrahem (nebo skupinou?), by potvrdilo oběť číslo 3.")
                zapisnik.append("Ať už je vrah jeden, nebo je jich více, jsou nepochybně extrémně nebezpeční.")
                zapisnik.append("A nemá/nemají rádi pozornost.")
                while True:
                    print('Než se teleportuješ do 2. kapitoly, máš možnost sebrat svou věrnou 44. magnum. Vezmeš ji?')
                    moznosti = input ('[Y/N]:')
                    if moznosti in ['Y','N']:
                        break
                if moznosti == "Y":
                   print('Sebral jsi ruční kanón.(*)')
                   winsound.PlaySound("Item",winsound.SND_FILENAME)
                   print('*** Revolveru 44. Magnum se přezdívá "Ruční kanón" díky jeho palebné síle, která dokáže zničit prakticky cokoliv.***')
                   global magnum
                   magnum = 1
                   global inventar
                   inventar.append("Magnum")
                   #inventar_json = json.loads(inventar)
                   input("")  
                if moznosti == "N":
                   print('44ku necháte v šuplíku. (To snad nemyslíte vážně... -_- )')
                   magnum = 0
                   input("")
                while True:
                    print("Než se teleportuješ do 2. kapitoly, máš také možnost sebrat zapalovač. Vezmeš ho?")
                    moznosti = input ('[Y/N]:')
                    if moznosti in ['Y','N']:
                        break
                if moznosti == "Y":
                    print("Sebral jsi zapalovač.")
                    winsound.PlaySound("Item",winsound.SND_FILENAME)
                    global zapalovac
                    zapalovac = 1
                    inventar.append("Zapalovač")
                    input("")
                Kapitola_2_1()
                Kapitola_2_Bitka_1()
Vyber_Kapitol()
#Intro()    
#print("----------------------")
#print("Zvedneš telefon?")
#odpoved = None 
#while odpoved not in ("Y", "N"):
#    odpoved = input("[Y/N]:")
#if odpoved == "Y":
#    print("S falešnou nadějí na pořádnej případ zvedneš sluchátko.")
#    print("[TY:]"+'"Phil Marlowe..." Mrzutým, rozespalým a napůl opilým hlasem řekneš do kulatého kusu plastu.')
#    print("V naději, že se z kusu plastu ozve odpověď.")
#    input("")
#    print("...")
##    print("...")
##    print("...")
##    while True:
##        moznosti = input ("A) Je tam někdo? B) To je fór? C) <mlčet> [A/B/C]? : ")
##        if moznosti in ['A','B', 'C']:
##            break
##    if moznosti == "A":
##       print("[TY:]"+'"Je tam někdo?" utrousíš, teď už spíš podrážděný než mrzutý, do děravého kusu plastu.')
##       Prvni_Kontakt_Vseobecna()
##       Prvni_Kontakt_Vseobecna_2()
##       Prvni_Kontakt_Vseobecna_3()
##       Kapitola_2_1()
##    if moznosti == "B":
##        print("[TY:]"+'"To je fór?"')
##        Prvni_Kontakt_Vseobecna()
##        Prvni_Kontakt_Vseobecna_2()
##        Prvni_Kontakt_Vseobecna_3()
##        Kapitola_2_1()
##    if moznosti == "C":
##        print("<mlčíš, čekáš>")
##        Prvni_Kontakt_Vseobecna()
##        Prvni_Kontakt_Vseobecna_2()
##        Prvni_Kontakt_Vseobecna_3()
##        Kapitola_2_1()
##if odpoved == "N":
##    print("KONEC")
##    sys.exit()
#else:
    #print("Prosím, zadejte ano nebo ne.")
    

