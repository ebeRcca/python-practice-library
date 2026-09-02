# Challenge 1 - rectangle with cut-out

# What is the area of this shape?
# Area = (rectangle) length * width - (cut-out) length * width

# rectangle length = s, width = g
# cutout length = q, width = w

print()

# User input for dimensions:
s = float(input("Enter length s: "))
g = float(input("Enter width g: "))
q = float(input("Enter length q: "))
w = float(input("Enter width w: "))

total_area = (s * g) - (q * w)

print("\nThe total area of this shape is", total_area, "\n")

# Assertion 1: s = 20, g = 10, q = 14, w = 6 > area = 116
# Assertion 2: s = 8, g = 4, q = 4.5, w = 2.5 > area = 20.75
