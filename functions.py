from config import *

# Funktioner

# Balance
def balance():
    """ Beräknar saldot på kontot

    :return: saldot
    """
    balance = 0
    for t in transactions:
        balance += t
    return balance


# Validate_int
def validate_int(output, error_mess):
    """Validerar inmatat värde

    :param output: Text som skrivs till anändaren
    :param erro_mess: Text som skrics om inmatning är felaktig
    :return: validerat värde
    """
    while True:
        try:
            value = int(input(output))
            break
        except:
            print(error_mess)
    return value


# Print_Transactions
def print_transactions():
    """ Skapar utskrift av alla transaktioner

    :return: sträng med hela utskriften
    """
    line = 0
    balance = 0
    output = ("\nAlla transaktioner:"
              "\n{:>3} {:>12} {:>12}"
              "\n---------------------------------").format("Nr", "Händelser", "Saldo")
    for t in transactions:
        line += 1
        balance += t
        output += ("\n{:>2}. {:>9} kr".format(line, t, balance))

    return output


# Check_FIle_Exists
def check_file_exists():
    """Om filen inte finns så skapas den och sedan läggs en transaktion till
       Eftersom "x" returnerar ett error om filen finns kan vi utnyttja detta.
    :return: None
    """
    try:
        with open(filename, "x"):
            print("Filen skapades")

        with open(filename, "a") as f:
            f.write("{}\n".format(1000))
    except:
        return


# Read_File
def read_file():
    """Läser in filens innehåll till transaktionslistan

    :return: none
    """
    check_file_exists()                                        # Kollar om filen finns, annars skapas den

    with open(filename) as f:
        for rad in f:
            if len(rad) > 0:
                transactions.append(int(rad))


# Add_Transactions
def add_transaction(transaction, toFile = False):
    """ Lagrar transaktioner i transaktionslistan och eventuellt till filen

    :param transaction: transaktionen
    :param toFile: True - lagra också till filen, False är förvalt
    :return: None
    """ 
    transactions.append(transaction)
    if toFile:
        write_transaction_to_file(transaction)
    
    
# Write_Transaction_To_File
def write_transaction_to_file(transaction):
    """ Skriver en transaktion till filen

    :param transaction: transaktionen
    :return: None
    """
    with open(filename, "a") as f:
        f.write("{}\n".format(transaction))