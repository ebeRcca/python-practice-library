# Challenge 3 - right-angled triangle with 40-degree angle

# Calculate the area of this triangle
# Area of a triangle = 0.5 * base * height

# Dimensions available are: 
# angle degrees = 40 
# base = f

# calculate height using opposite = adjacent * angle 
# So height = f * tan(40degrees)

import math

print()

# User input base dimension = f
f = float(input("Enter the value of f: "))

print()

# Convert 40° to radians to calculate tan(40degrees)
angle_degrees = 40
angle_radians = math.radians(angle_degrees)

# Step 3: Calculate tan(40degrees) 
tan_value = math.tan(angle_radians)

print("tan_value is: ", tan_value, "\n")

# Use tan(40degrees) to calculate the height 
height = f * tan_value

print("height is: ", height, "\n")

# Use the triangle area formula to calcuate total_area
total_area = 0.5 * f * height

print("The total area of the triangle is: ", total_area, "\n")

# Assertion 1 for f = 12 > total area = 60.415 (approx)
# Assertion 2 for f = 3.3 > total area = 4.569 (approx)