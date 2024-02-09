"""
Program that prints the equivalent number of Joules as an integer.
"""

kgs = int(input("Enter mass in kg's (as a number): "))

lightSpeed = 3 * 10**8  # Declaring speed of light.
joules = kgs * (lightSpeed**2)  # Energy formula E = mc^2.
print(joules)
