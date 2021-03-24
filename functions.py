from config import *

# Funktioner
def balance():
    """ Beräknar saldot på kontot

    :return: saldot
    """
    balance = 0
    for t in transactions:
        balance += t
    return balance

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