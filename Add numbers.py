# Write a program with a while loop that computes the sum of the first n positive integers:

print()

# User input
n = int(input("Enter a number: "))

# Starting at 1
number = 1
total = 0

# Add by 1 up to n and calculate the total of all numbers
while number <= n:
    total = total + number
    number = number + 1

print("The sum is:", total)
print()

# Assertion 1 n = 6 (1 + 2 + 3 + 4 + 5 + 6) == 21
# Assertion 2 n = 10 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10) == 55
