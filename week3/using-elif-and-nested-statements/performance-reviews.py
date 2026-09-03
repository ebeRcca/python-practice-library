# Performance Reviews

print()

# User input
employee_rating = float(input("Enter the employee's rating: "))

# Calculate bonus based on rating
if employee_rating == 0.0:
    print("Unacceptable performance")
    print("Raise: $0.00")

elif employee_rating == 0.4:
    print("Acceptable performance")
    print("Raise: $", 2400.00 * employee_rating)

elif employee_rating >= 0.6:
    print("Meritorious performance")
    print("Raise: $", 2400.00 *employee_rating)

else:
    print("Error: Invalid rating number entered.")

print()

