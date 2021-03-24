# Planning :
# Imports 
# Functions
# Variabler 
saldo = 1000                # Saldot är 1000kr när programmet startar
transactions = []           # Listan lagrar alla transaktioner
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
            "\nGör ditt val: ".format(saldo))

    val = int(input(meny))

    if val == 0:
        break
    elif val == 1:
        line = 0
        sum = 0
        head = ("\nAlla transaktioner:"
                "\n{:>3} {:>12} {:>12}"
                "\n---------------------------------").format("Nr", "Händelser", "Saldo")
        print(head)
        for t in transactions:
            line += 1
            sum += t
            print("{:>2}. {:>9} kr".format(line, t, sum))

    elif val == 2:
        deposit = int(input("Ange hur mycket du vill sätta in: "))
        if deposit > 0:
            saldo += deposit
            transactions.append(deposit)
            print("Tack för din insättning på {}kr".format(deposit))

        else:
            print("En insättning måste vara större än 0.")   

    elif val == 3:
        withdraw = int(input("Ange hur mycket du vill ta ut: "))
        if withdraw <= saldo and withdraw >= 0:
            saldo -= withdraw
            transactions.append(-withdraw)
            print("Uttag goodkänt! Nytt saldo {}".format(saldo))

        elif withdraw < 0:
            print("Uttaget måste vara större än 0.")

        else:
            print("Uttaget får inte vara större än saldot. Uttag medgs ej")

    else:
        print("Felaktigt val !")

print("Tack för ditt besök, välkommen åter!")