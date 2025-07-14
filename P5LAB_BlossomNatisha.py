#Natisha Blossom
#July 11, 2025
#P5LAB
#Simulating change due from a self-checkout machine using random input.

#To generate random amounts
import random

#How denominations are calculated
def disperse_change(amount):
    cents = int(round(amount * 100))

    dollars = cents // 100
    cents = cents % 100

    quarters = cents // 25
    cents = cents % 25

    dimes = cents // 10
    cents = cents % 10

    nickels = cents // 5
    cents = cents % 5

    pennies = cents

    if dollars > 0:
        if dollars == 1:
            print(f"{dollars} Dollar")
        elif dollars != 1:
            print(f"{dollars} Dollars")
        else:
            print('')

    if quarters > 0:
        if quarters == 1:
            print(f"{quarters} Quarter")
        elif quarters != 1:
             print(f"{quarters} Quarters")
        else:
            print('')

    if dimes > 0:  
        if dimes == 1:
            print(f"{dimes} Dime")
        elif dimes != 1:
            print(f"{dimes} Dimes")
        else:
            print('')

    if nickels > 0:
        if nickels == 1:
            print(f"{nickels} Nickel")
        elif nickels != 1:
            print(f"{nickels} Nickels")
        else:
            print('')

    if pennies > 0:
        if pennies == 1:
            print(f"{pennies} Penny")
        elif pennies != 1:
            print(f"{pennies} Pennies")
        else:
            print('')

    if dollars == 0 and quarters == 0 and dimes == 0 and nickels == 0 and pennies == 0:
        print("No change")

#Main logic
def main_logic():
    balance_due = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${balance_due}")

    cash_tendered = float(input("How much cash will you put in the self-checkout? "))

    change_due = round(cash_tendered - balance_due, 2)
    print(f"Change is: ${change_due}")

    disperse_change(change_due)
main_logic()
