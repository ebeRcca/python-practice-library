# Challenge 3 - right-angled triangle

# Calculate the area of this right-angled triangle
# Area of a triangle = 0.5 * base * height

# Dimensions available are base and hypotenuse
# hypotenuse = e
# base = d

import math

print()

# User inputs
e = float(input("Enter the value for e (hypotenuse): "))
d = float(input("Enter the value for d (base): "))

# Calculate the missing height using Pythagoras
height = math.sqrt(e**2 - d**2)
print("\nThe height of the triangle is:", height, "\n")

# Calculate the area of the triangle
total_area = 0.5 * d * height

print("The area of the triangle is:", total_area)

print()

# Aseertion 1 e = 11, d = 10 > total_area = 22.9 (approx)
# Aseertion 2 e = 6, d = 5.5 > total_area = 6.6 (approx)

