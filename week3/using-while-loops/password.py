# Write a password program that prompts the user for a password and gives them just 3 attempts.
# If the user types exit when prompted for the password, then the program should terminate.

# What is the password?
correct_password = "youguessedit"

# User has 3 attempts
attempts = 3
print()

while attempts > 0:
    password = input("Enter password (or type 'exit' to quit): ")

    # If user wants to exit
    if password == "exit":
        print("Program terminated.")
        break

    # If password is correct
    if password == correct_password:
        print("Password is correct.")

        break

    # If password is wrong
    attempts = attempts - 1
    print("Incorrect password. Attempts left:", attempts)

# If attempts run out
if attempts == 0:
    print("Too many attempts. Program terminated.")

print()
