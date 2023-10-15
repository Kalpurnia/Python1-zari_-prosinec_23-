def verify_number (number:str)->bool: 

    if len(number) == 9: 
        return True 
    if len (number)==13: 
        if number[0:4]=="+420":
            return True 
    else: 
        return False 
    
def replacement (number:str)->str: 
        for i in number: 
            your_number = number.replace(" ","") 
        return your_number

def SMS_price(length:int)->int: 
    if length <= 180: 
        price = 3 
    elif length  > 180 and length % 180 >0:
        price = ((length//180) *3) +3
    else: 
        price = ((length/180) *3)

    return price 


    
    



phone_number =input("Zadej telefonni číslo:")
phone_number_fixed = (replacement(phone_number))
#print (phone_number_fixed)
#print (len(phone_number_fixed))
if (verify_number(phone_number_fixed))==True: 
    text = len(input("Zadej text SMS: "))
    print (f"Cena zprávy je {SMS_price(text)} Kč.")
else: 
    print("Zadejte telefonní číslo správně.")


