"""Soubor body.json je JSON, který obsahuje informace o získaných bodech z písemky.

    Soubor si ulož a načti do slovníku.

    Z písemky nebude známka, ale jen Pass/Fail hodnocení neboli prospěl(a)/neprospěl(a). Vytvoř nový slovník. Jeho klíče budou opět jména žáků, a hodnotou bude řetězec "Pass", pokud má jednotlivec alespoň než 60 bodů. Pokud má méně než 60, hodnota bude "Fail".

    Výsledný slovník ulož jako JSON do souboru prospech.json."""


import json
with open("body.json", mode="r", encoding="utf-8") as file: 
    test_results=json.load(file)

result ={}
for key, value in test_results.items(): 
    if value >=60: 
        result[key]=["Pass"]
    else: 
        result[key]=["Fail"]

#print(result)

with open("prospech.json", mode="w", encoding="utf-8") as output_file: 
    json.dump(result, output_file, ensure_ascii=False )

#bonus - sečíst body 
"""
Tvým úkolem je žákům přiřadit známky na základě součtu bodů 
z písemky a bonusových bodů. Bodová rozhraní (vztahují se na součet) najdeš zde:

1: 90 a více
2: 70-89
3: 50-69
4: 30-49
5: 29 a méně

    Výsledný slovník ulož jako JSON do souboru znamky.json.

"""

points={}

with open("bonusy.json", mode="r", encoding="utf-8") as file: 
    bonus_points=json.load(file)

#print(bonus_points)

for key, value in test_results.items(): 
    if key in bonus_points: 
        points[key]=value+bonus_points[key]
               
    else: 
        points[key]=value
#print(points)

grades= {}
for key, value in points.items(): 
    
    if value > 90: 
        grades[key]="1"
    elif (value < 90) and (value>69):
        grades[key] = "2"
    elif (value>49) and (value<70):
        grades[key]="3"
    elif (value>29) and (value<50):
        grades[key]="4"
    else: 
        grades[key]="5"

#print(grades)
with open("znamky.json", mode="w", encoding="utf-8") as output_file: 
    json.dump(grades, output_file, ensure_ascii=False )