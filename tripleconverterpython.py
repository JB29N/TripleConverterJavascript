# TRIPLE CONVERTER PYTHON

# Convertion Fonctions

def eurotochf(eur):
    return eur * 1.08

def kilotopound(kilo):
    return kilo * 0.4

def litertom3(liter):
    return liter / 1000

# Asking Functions

def askcontinue():
    answer = input("Do you want to convert a value? (yes/no)")
    if answer == "yes":
        return True
    else:
        return False

def askkindofvalue():
   answer = input("Which value do you want to convert? (eur, kilo, liter) ")
   return answer

def askvalue():
    value = float(input("Enter a value: "))
    return value

# MAIN

while askcontinue():
    kindofvalue = askkindofvalue()
    value = askvalue()
    if kindofvalue == "eur":
        print("The result is " + str(eurotochf(value)))
    elif kindofvalue == "kilo":
        print("The result is " + str(kilotopound(value)))
    elif kindofvalue == "liter":
        print("The result is " + str(litertom3(value)))
    else: print("I can't do this conversion.")