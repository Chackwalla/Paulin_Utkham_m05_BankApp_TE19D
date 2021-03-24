# Planning :
# Imports 
# Functions
from functions import *

# Variabler 
transactions.append(1000)   # Lägger till startbeloppet på 1000kr

# Main loop
# Input of text
# Write it in a file
# Read the file
# Complete the program 

while True:
    meny = ("\n#######################"
            "\n# Lilla banken"
            "\n# Meny"
            "\n# Saldo: {} kr"
            "\n#######################"
            "\n1. Visa saldo"
            "\n2. Gör en insättning"
            "\n3. Gör ett uttag"
            "\n0. Avsluta programmet"
            "\nGör ditt val: ".format(balance()))

    val = validate_int(meny, "Felaktig inmatning !")

    if val == 0:
        break
    elif val == 1:
        print(print_transactions())
        
    elif val == 2:
        deposit = validate_int("Ange hur mycket du vill sätta in: ", "Felaktig inmatning !")
        if deposit > 0:
            transactions.append(deposit)
            print("Tack för din insättning på {}kr".format(deposit))

        else:
            print("En insättning måste vara större än 0.")   

    elif val == 3:
        withdraw = validate_int("Ange hur mycket du vill ta ut: ", "Felaktig inmatning !")
        if withdraw <= balance() and withdraw >= 0:
            transactions.append(-withdraw)
            print("Uttag goodkänt! Nytt saldo {}".format(balance()))

        elif withdraw < 0:
            print("Uttaget måste vara större än 0.")

        else:
            print("Uttaget får inte vara större än saldot. Uttag medgs ej")

    else:
        print("Felaktigt val !")

print("Tack för ditt besök, välkommen åter!")