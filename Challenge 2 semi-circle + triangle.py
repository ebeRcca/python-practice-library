# Challenge 2 semi-circle + triangle

# What is the area of this shape?
# Total area = area of semi-circle + area of triangle 

# Area of semi-circle = 0.5 * pi * radius ** 2
# Area of triangle = 0.5 * base * height

# e = radius of semi-circle
# f = base of triangle
# g = height of triangle

import math

print()

# User input for dimensions:
e = float(input("Enter radius of semi-circle: "))
f = float(input("Enter base of triangle: "))
g = float(input("Enter height of triangle: "))

total_area = 0.5 * math.pi * (e ** 2) + 0.5 * f * g

print("\nThe total area of this shape is", total_area, "\n")

# Assertion 1: e = 2, f = 6, g = 5.5  > area = 22.78 (approx)
# Assertion 2: e = 3, f = 9, g = 8 > area = 50.13 (approx)