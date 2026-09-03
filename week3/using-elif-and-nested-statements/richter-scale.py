# Challenge 1 – Richter Scale 

print()

#User input
magnitude = float(input("Enter the earthquake magnitude: "))

if magnitude < 2.0:
    descriptor = "Micro"
elif magnitude < 3.0:
    descriptor = "Very minor"
elif magnitude < 4.0:
    descriptor = "Minor"
elif magnitude < 5.0:
    descriptor = "Light"
elif magnitude < 6.0:
    descriptor = "Moderate"
elif magnitude < 7.0:
    descriptor = "Strong"
elif magnitude < 8.0:
    descriptor = "Major"
elif magnitude < 10.0:
    descriptor = "Great"
else:
    descriptor = "Meteoric"

print(f"A magnitude {magnitude} earthquake is considered a {descriptor} earthquake.", "\n")

# Assertion 1:
# Magnitude = 5.5 > descriptor = Moderate

# Assertion 2:
# Magnitude = 7.2 > descriptor = Major
