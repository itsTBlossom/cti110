#Natisha Blossom
#June 16, 2025
#P1HW2
#This is a program for budgeting and to calculate expenses.

print("This program calculates and displays travel expenses")
#Enter a starting budget value
print("Enter Budget: ")
budget = int(input())
#Enter desired travel destination
print("Enter your travel destination: ")
travel_destination = input()
#Enter estimated amount for gas
print("How much do you think you will spend on gas? ")
gas = int(input())
#Enter estimated amount for a hotel
print("Approximately, how much will you need for accomodation/hotel? ")
hotel = int(input())
#Enter estimated amount for food
print("Last, how much do you need for food? ")
food = int(input())
#Addition of entered expenses
expenses = gas + hotel + food
#Calculating the remaining balance after subtracting expenses from budget
remaining_balance = budget - expenses

print('-----Travel Expenses-----')
print("Location: ", travel_destination)
print("Initial Budget: ", budget)
#Expenses
print("Fuel: ", gas)
print("Accomodation: ", hotel)
print("Food: ", food)
#Remaining Balance
print("Remaining Balance: ", remaining_balance)

