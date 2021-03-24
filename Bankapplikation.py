# Planning :
# Imports 
# Functions
# Variabler 
saldo = 1000           # Saldot är 1000kr när programmet startar

# Main loop
# Input of text
# Write it in a file
# Read the file
# Complete the program 

while True:
    meny = ("\n#######################"
            "\n# Lilla banken"
            "\n# Meny"
            "\n#######################"
            "\n1. Visa saldo"
            "\n2. Gör en insättning"
            "\n3. Gör ett uttag"
            "\n0. Avsluta programmet"
            "\nGör ditt val: ")

    val = int(input(meny))

    if val == 0:
        break
    elif val == 1:
        print("Saldot är {}kr".format(saldo))
    elif val == 2:
        deposit = int(input("Ange hur mycket du vill sätta in: "))
        if deposit > 0:
            saldo += deposit
            print("Tack för din insättning på {}kr".format(deposit))
        else:
            print("En insättning måste vara större än 0.")      
    elif val == 3:
        withdraw = int(input("Ange hur mycket du vill ta ut: "))
        if withdraw <= saldo and withdraw >= 0:
            saldo -= withdraw
            print("Uttag goodkänt! Nytt saldo {}".format(saldo))
        elif withdraw < 0:
            print("Uttaget måste vara större än 0.")
        else:
            print("Uttaget får inte vara större än saldot. Uttag medgs ej")
    else:
        print("Felaktigt val !")
print("Tack för ditt besök, välkommen åter!")