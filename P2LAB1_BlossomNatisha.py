#Natisha Blossom
#June 23, 2025
#P2LAB1
#Program to perform calculations for a circle

#Value to be entered for radius
print("What is the radius of the circle? ")
radius = float(input())

#Calculations based off value for radius
import math
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius**2

#Values for calculations
print(f"{'The diameter of the circle is '}{diameter:.1f}")
print(f"{'The circumference of the circle is '}{circumference:.2f}")
print(f"{'The area of the circle is '}{area:.3f}")
