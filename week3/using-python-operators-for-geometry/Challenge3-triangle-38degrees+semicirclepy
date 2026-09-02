# Challenge 3 - triangle + rectangle + semicircle 

# This shape is made up of:
# - a right-angle triangle
# - a rectangle
# - a semicircle

# Area formulas:
# Triangle area = 0.5 * base * height
# Rectangle area = length * width
# Semicircle area = 0.5 * pi * (radius ** 2)

# Dimensions for rectangle:
# e = length
# g = width

# Dimensions for triangle:
# angle = 38 degrees
# g = height

# Dimensions for semicircle:
# diameter = g
# radius = g / 2

import math

print()

e = float(input("Enter the value of e: "))
g = float(input("Enter the value of g: "))

# Calculate area of rectangle
rectangle_area = e * g

print("\nThe area of the rectangle is: ", rectangle_area, "\n")

# Calculate area of triangle
angle_degrees = 38
angle_radians = math.radians(angle_degrees)
tan_value = math.tan(angle_radians)
base = g * tan_value
triangle_area = 0.5 * base * g

print("The area of the triangle is: ", triangle_area, "\n")

#Calclulate the area of the semicircle
semicircle_area = 0.5 * math.pi * ((g/2) ** 2)

print("The area of the semicircle is: ", semicircle_area, "\n")

total_area = rectangle_area + triangle_area + semicircle_area

print("The total area of this shape is: ", total_area, "\n")

# Assertion 1 e = 2, g = 6 > total area = 40.17 (approx)
# Assertion 2 e = 3.5, g = 10.5 > total area = 123.088 (approx)

