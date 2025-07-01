#Natisha Blossom
#June 30, 2025
#P3LAB
#A program to list least amount of currency denominations needed to equal amount entered.


#Have a dollar amount entered for denomination calculation
print("Enter the amount of money as a float: ")
amount = float(input())

#How denominations are calculated
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

#Output of calculations
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
