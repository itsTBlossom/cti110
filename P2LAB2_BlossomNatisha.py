#Natisha Blossom
#June 23, 2025
#P2LAB2
#Using a dictionary to store input and display the output

#Dictionary creation with keys and values
vehicles = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}
keys = vehicles.keys()
print(keys)

#Vehicle and mileage 
print("Enter a vehicle to see it's mpg: ")
vehicle = input()
mpg = vehicles[vehicle]
print(f"The {vehicle} gets {mpg} mpg.")

#Gas needed based on miles driven
print(f"How many miles will you drive the {vehicle}?")
miles_to_drive = float(input())
gas_needed = miles_to_drive / mpg
print(f"{gas_needed:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles_to_drive} miles.")
