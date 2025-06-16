#Natisha Blossom
#June 16, 2025
#P1HW2
#This is a program for budgeting and to calculate expenses.

print("This program calculates and displays travel expenses")
print("Enter Budget: ")
budget = int(input())
print("Enter your travel destination: ")
travel_destination = input()
print("How much do you think you will spend on gas? ")
gas = int(input())
print("Approximately, how much will you need for accomodation/hotel? ")
hotel = int(input())
print("Last, how much do you need for food? ")
food = int(input())
expenses = gas + hotel + food
remaining_balance = budget - expenses

print('-----Travel Expenses-----')
print("Location: ", travel_destination)
print("Initial Budget: ", budget)

print("Fuel: ", gas)
print("Accomodation: ", hotel)
print("Food: ", food)

print("Remaining Balance: ", remaining_balance)

