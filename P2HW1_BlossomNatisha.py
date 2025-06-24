#Natisha Blossom
#June 23, 2025
#P2HW1
#This is a program for budgeting and to calculate expenses.

print("This program calculates and displays travel expenses")
#Enter a starting budget value
print("Enter Budget: ")
budget = float(input())
#Enter desired travel destination
print("Enter your travel destination: ")
travel_destination = input()
#Enter estimated amount for gas
print("How much do you think you will spend on gas? ")
gas = float(input())
#Enter estimated amount for a hotel
print("Approximately, how much will you need for accomodation/hotel? ")
hotel = float(input())
#Enter estimated amount for food
print("Last, how much do you need for food? ")
food = float(input())
#Addition of entered expenses
expenses = gas + hotel + food
#Calculating the remaining balance after subtracting expenses from budget
remaining_balance = budget - expenses

print('------------Travel Expenses------------')
print(f"{'Location: ':<20}{travel_destination}")
print(f"{'Initial Budget: ' :<20}${budget:.2f}")
#Expenses
print(f"{'Fuel: ':<20}${gas:.2f}")
print(f"{'Accomodation: ':<20}${hotel:.2f}")
print(f"{'Food: ' :<20}${food:.2f}")
print('---------------------------------------')

#Remaining Balance
print(f"{'Remaining Balance: ':<20}${remaining_balance:.2f}")

