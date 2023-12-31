import re
# I. data
expression = re.compile(r"(\d{1,2}[./] ?){2}\d{4}")
data =["2.2.2022",
"13. 8. 1999",
"4/5/2001",
"5.123.458.91"
"21.4",
"8./9"]
valid=[]
for datum in data:
    if  expression.fullmatch(datum):
        valid.append(datum)
print(valid)



# II PSČ a město 

text = """Běžná poštovní adresa zásilky
adresované fyzické osobě
Poštovní adresa zásilky adresované
právnické osobě
Paní
Božena Novotná
Stavbařů 4211
190 16 PRAHA 916
MOTOSPORT, a. s.
do rukou p. Ptáčka
Plantážníků 421
378 08 DVORY NAD LUŽNICÍ
Poštovní adresa zásilky adresované
fyzické osobě do vlastních rukou,
doplněná datem narození Poštovní adresa zásilky adresované
fyzické osobě k dodání
prostřednictvím právnické osoby
Paní
Božena Novotná
nar. 1. 4. 1946
Stavbařů 4211
190 16 PRAHA 916
Pan
Václav Ptáček
MOTOSPORT, a. s.
Plantážníků 421
378 08 DVORY NAD LUŽNICÍ
Poštovní adresa zásilky adresované
fyzické osobě k dodání
prostřednictvím jiné osoby  Poštovní adresa zásilky adresované
ústavnímu činiteli, která má být
dodána jako právnické osobě
Slečna
Kamila Zelená
u p. T. Červeného
Borovského 33
186 00 PRAHA 86
Vážená paní
Václava Kroupová, senátorka PČR
Valdštejnské náměstí 17/4
118 00 PRAHA 011
Poštovní adresa zásilky adresované
fyzické osobě poste restante
Běžná poštovní adresa zásilky adresované
právnické osobě
Vážený pan
MUDr. Matěj Kopecký
poste restante
397 04 PÍSEK 4  OKNOPLAST, a. s.
nám. Svobody 45
460 15 LIBEREC 15
Poštovní adresa zásilky adresované
právnické osobě (přesné označení je
důležité pro vyloučení záměny
s fyzickou osobou)  Poštovní adresa zásilky adresované
daňovému poradci, advokátovi,
soudnímu exekutorovi, notáři, nebo
patentovému zástupci, která má být
dodána jako právnické osobě
Firma
Vojtěch Pavlát, s. r. o.
Truhlářská 7
623 00 BRNO 23
Mgr. Eva Hásková
daňová poradkyně
Věnceslava Metelky 114
512 11 VYSOKÉ NAD JIZEROU
Poštovní adresa zásilky adresované
několika osobám do místa, kde není
používán systém ulic
Poštovní adresa zásilky adresované
podnikateli, který je fyzickou osobou,
která má být dodána jako právnické
osobě
Sourozenci
Karel a Bedřich Weberovi
č. p. 8
378 07 RAPŠACH
Pan
Josef Novák, podnikatel
Hlavní 1234
130 00 PRAHA 3
Poštovní adresa zásilky adresované
do poštovní přihrádky
Poštovní adresa zásilky adresované
do obce, ve které nesídlí adresní pošta
Pan
František Koucký
poštovní přihrádka 72
273 01 KAMENNÉ ŽEHROVICE
Vážená paní
Marie Kousalová
Roprachtice 129
513 01 SEMILY
Poštovní adresa zásilky adresované
do dodávací schrány Poštovní adresa zásilky Balík Na Poštu
Pan
Bohumil Frkal
dodávací schrána B/52
398 11 PROTIVÍN
Eva Drobná
NA POŠTU
742 45 FULNEK
+420 777 123 456
(vždy uveďte mob. tel. číslo)
Poštovní adresa zásilky adresované fyzické osobě,
jejíž zdravotní stav nedovoluje vyzvednutí,
k dodání prostřednictvím právnické osoby
Poštovní adresa zásilky adresované fyzické osobě,
jejíž omezení pohybu nedovoluje vyzvednutí,
k dodání prostřednictvím právnické osoby
Paní
Jamila Nováková, 5. 8. 1982
Fakultní nemocnice v Motole
I. ortopedická klinika, 2. lůžkové oddělení
V Úvalu 84
150 06  PRAHA 5
Pan
Jan Novák, 28. 2. 1956
Věznice Valdice
Nám. Míru 55
507 11  VALDICE"""
expression_2= re.compile(r"(\d{3} \d{2} +(\w* ?)\d.*)")
 
zip_town = expression_2.findall(text)
for zip in zip_town:
    print(zip[0])    


# III, emaily


regular_username = re.compile(r"[a-zA-Z]{6,10}")
regular_password = re.compile(r"[\w+.=-]{12,30}")
regular_email = re.compile(r"[\w]+[\w_%+-.]*@[A-Za-z0-9.]+\.[a-zA-Z]{2,4}")# toto mi na vzorové adresy funguje tak ze 75% max., ale víc to neumím vylepšit 

username = input("Zadejte uživatelské jméno: ")
validation_username=regular_username.fullmatch(username)
if validation_username:
    password = input("Vaše uživatelské jméno je v pořádku. Zadejte heslo: ")
    validation_password = regular_password.fullmatch(password)
    if validation_password: 
        email = input("Zvolené heslo je v pořádku. Zadejte e-mailovou adresu: ")
        validation_email = regular_email.fullmatch(email)
        if validation_email: 
            print("Váš email je v pořádku. Nyní máte uživatelské jméno, heslo a email tak hajdy do práce!!!")
        else: 
            print ("Zadali jsem neplatný email")
            
    else: 
        print("Zadali jste neplatné heslo")
        
else: 
    print("Zadali jste nepovolené uživatelské jméno")    
    

        



