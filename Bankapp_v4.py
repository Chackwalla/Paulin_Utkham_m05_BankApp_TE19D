#Will continue tomorrow at '8.4 Skriv transaktioner till filen'
# Planning :
# Imports 
from functions import *

# Functions
check_file_exists()
read_file()

# Variabler 

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
            "\n4. Nollställ kontot"
            "\n0. Avsluta programmet"
            "\nGör ditt val: ".format(balance()))

    val = validate_int(meny, "Felaktig inmatning !")

# Val 0
    if val == 0:
        break

#Val 1
    elif val == 1:
        print(print_transactions())
        
# Val 2
    elif val == 2:
        deposit = validate_int("Ange hur mycket du vill sätta in: ", "Felaktig inmatning !")
        if deposit > 0:
            add_transaction(deposit, True)
            print("Tack för din insättning på {}kr".format(deposit))

        else:
            print("En insättning måste vara större än 0.")   

# Val 3
    elif val == 3:
        withdraw = validate_int("Ange hur mycket du vill ta ut: ", "Felaktig inmatning !")
        if withdraw <= balance() and withdraw >= 0:
            add_transaction(-withdraw, True)
            print("Uttag goodkänt! Nytt saldo {}".format(balance()))

        elif withdraw < 0:
            print("Uttaget måste vara större än 0.")

        else:
            print("Uttaget får inte vara större än saldot. Uttag medgs ej")

# Val 4
    elif val == 4:
        os.remove(filename)                      # Tar bort filen
        transactions.clear()                     # Töm listan
        read_file()                              # Skapa filen och läs in den

    else:
        print("Felaktigt val !")

print("Tack för ditt besök, välkommen åter!")