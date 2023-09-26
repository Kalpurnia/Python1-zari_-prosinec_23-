"""
Napiš program, který bude obsahovat jednu proměnnou jmeno. Tato proměnná bude obsahovat libovolné křestní jméno (třeba tvoje). Tvůj program vytvoří e-mailovou adresu na základě této proměnné, s doménou czechitas.cz a tuto e-mailovou adresu vypíše.

Tedy pokud bude hodnota proměnné jmeno například Jindřiška, pak program vypíše Jindřiška@czechitas.cz.
Nepovinný bonus:

Tuto část můžeš řešit, pokud už máš první část úkolu hotovou a chceš si ještě něco procvičit.

Napiš program, který bude obsahovat proměnnou jmeno_a_prijmeni. 
Obsah proměnné načti od uživatele pomocí funkce input. 
lkjjkTvůj program postupně vypíše několik způsobů formátování jména:

    všechna písmena velká (vypíše např. JANA MALÁ)
    všechna písmena malá (vypíše např. jana malá)
    standardní varianta - první písmeno velké, další malá (vypíše např. Jana Malá)
    iniciály (vypíše např. J. M.)
    křestní jméno zkrácené na první písmeno a příjmení, pokud je křestní jméno delší než 5 znaků. Jinak vypíše standardní variantu, tj. první písmeno velké, další malá (u vstupu Jarmila Malá by došlo ke zkrácení křestního jména, zatímco u vstupu Jana Malá nikoliv)

Zaexperimentuj s různými vstupy od uživatele (co třeba JaNA maLá?)"""

jmeno = "Olga"
domena = "czechitas.cz" 
adresa = jmeno+"@"+domena
print(f"moje emailová adresa je {adresa}")

name = input("Napiš své křestní jméno: ")
surname = input("Napiš své příjmení:  ")
if len(name)>5: 
    jmeno_a_prijmeni=(name[0]+". " + surname)          
else: 
    jmeno_a_prijmeni = name + " "+surname 


print(f"jak bylo zadáno: {jmeno_a_prijmeni}")
print(f"Všechna velká: {jmeno_a_prijmeni.upper()}")
print(f"Všechna malá: {jmeno_a_prijmeni.lower()}")
velka_pocatecni = (name[0].upper() + name[1:].lower()) + " " + (surname[0].upper() + surname[1:].lower())
print(f"Velká počáteční: {velka_pocatecni}")
inicialy = (name[0].upper())+ "." + (surname[0].upper() + ".")
print(f"Inicialy: {inicialy}")
