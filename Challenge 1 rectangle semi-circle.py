# Challenge 1 - rectangle with semi-circle added and semi-circle cut-out

# What is the area of this shape?
# The semi-circles have the same diameter, so cancel each other out
# Area = (rectangle) length * width


# rectangle length = y, width = x


print()

# User input for dimensions:
y = float(input("Enter length y: "))
x = float(input("Enter width x: "))

total_area = y * x

print("\nThe total area of this shape is", total_area, "\n")

# Assertion 1: y = 12, x = 8 > area = 96
# Assertion 2: y = 5.5, x = 2.5 > area = 13.75
