class Auto: 
    def __init__(self, registracni_znacka, typ_vozidla, najete_km, dostupne=True):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne =dostupne 

    def pujc_auto(self): 
        if self.dostupne==True: 
            self.dostupne=False
            return "Potvrzuji zapůjčení vozidla"
        else: 
            return "Vozidlo není k dispozici"
        
    def get_info (self): 
        return f"Vozidlo {self.registracni_znacka},  typ {self.typ_vozidla}, {self.dostupne}" 

    def vrat_auto(self, tachometr, pocet_dni):
        self.najete_km = tachometr
        self.dostupne=True 
        if pocet_dni < 7: 
           cena =  pocet_dni * 400
        else: 
            cena =  pocet_dni * 300

        return f"Cena za zapůjčení vozu je {cena}"
           

vozidlo_1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534 )
vozidlo_2 = Auto("1P3 4747","Škoda Octavia", 41253)


reguest = input("Přejete si zapůjčit vozidlo Peugeot nebo vozidlo Octavia?").strip()
if reguest =="Peugeot":
    print(vozidlo_1.get_info())
    print(vozidlo_1.pujc_auto())
else: 
    print(vozidlo_2.get_info())
    print(vozidlo_2.pujc_auto())

# konstrola zmeny parametru dostupne z True na False, podle toho, které auto jsem půjčila. Tady to ještě funguje. 
print (vozidlo_1.get_info())
print (vozidlo_2.get_info())


print (vozidlo_1.vrat_auto(47900, 2))
print(vozidlo_1.get_info())

print(vozidlo_2.vrat_auto(55000, 9))
print(vozidlo_2.get_info())