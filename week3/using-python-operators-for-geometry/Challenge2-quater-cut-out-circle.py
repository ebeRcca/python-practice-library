# Challenge 2 - 3/4 circle

# What is the area of this shape?

# Area of a circle = pi * radius ** 2
# Area of 3/4 circle = 0.75 * pi * radius ** 2
# Radius of circle = c

import math

print()

# User input for dimensions:
c = float(input("Enter radius: "))

# Calculate the area of the 3/4 circle
total_area = 0.75 * math.pi * (c ** 2)

print("\nThe total area of the 3/4 circle is", total_area, "\n")

# Assertion 1: c = 5 > area = 58.875 (approx)
# Assertion 2: c = 11 > area = 284.955 (approx)
