#Natisha Blossom
#July 8, 2025
#P4LAB2
#Program to show a user a multiplication table for 1-12.

#While loop to keep program running until user says "no".
while True:
    print("Enter an integer: ")
    integer = int(input())

    if integer < 0:
        print("This program does not handle negative numbers.")
    else:
        for i in range(1,13):
            print(f"{integer} * {i} = {integer * i}")

    while True:
        print("Would you like to run the program again? ")
        run_again = input()

        if run_again == "yes":
            break
        elif run_again == "no":
            print("Exiting program... ")
            exit()
        else:
            print("Please type 'yes' or 'no'")
