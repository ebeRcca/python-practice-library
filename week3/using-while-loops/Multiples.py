# Write a program that prints multiples of p from 10 until the value of q (inclusive).
# Examples: the user enters: p = 4 and q = 29 
# Answer: 12, 16, 20, 24, 28,
print()

# User input
p = int(input("Enter p: "))
q = int(input("Enter q: "))

# Starting from 10, check each number up to q.
# If number % p == 0 (divisible with no remainder), print it.
# Add 1 each loop so every number from 10 to q is checked.
number = 10
while number <= q:
    if number % p == 0:
        print(number)
    number = number + 1

print()

# Assertion 1: p = 3, q = 18 > 12, 15, 18
# Assertion 2: p = 8, q = 42 > 16, 24, 32, 40
