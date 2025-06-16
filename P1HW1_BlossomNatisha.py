#Natisha Blossom
#June 16, 2025
#P1HW1
#This is a program designed to calculate mathematical expressions.

print('-----Calculating Exponents-----')


print("Enter an integer as the base value: ")
base_value = int(input())
print("Enter an integer as the exponent: ")
exponent = int(input())
new_value = base_value ** exponent

print(base_value, "raised to the power of ", exponent, " is ", new_value, " !!")


print('-----Addition and Subtraction-----')


print("Enter a starting integer: ")
starting_integer = int(input())
print("Enter an integer to add: ")
addition_integer = int(input())
print("Enter an integer to subtract: ")
subtraction_integer = int(input())
addSub_value = starting_integer + addition_integer - subtraction_integer

print(starting_integer , "+", addition_integer, "-", subtraction_integer, " is equal to ", addSub_value)
