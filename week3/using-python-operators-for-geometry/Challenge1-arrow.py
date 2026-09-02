# Challenge 1 - arrow

# What is the area of the arrow?
# Area of the arrow = triangle (1/2 * base * height) +  rectangle (length * width)
# n = triangle height
# n = triangle base
# m = rectangle length
# u = rectangle width

print()

# User input for dimensions:
n = float(input("Enter the height of triangle: "))
n = float(input("Enter the base of triangle: "))
m = float(input("Enter the length of rectangle: "))
u = float(input("Enter the width of rectangle: "))

total_area = (0.5 * n * n) + (m * u)

print("\nThe total area of the arrow is", total_area, "\n")

# Assertion 1: n = 6, m = 4, u = 6 > area = 42
# Assertion 2: n = 2.5, m = 1.5, u = 2.5 > area = 6.875
