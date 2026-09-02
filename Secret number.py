# Write a guessing game where the user has to guess a stored secret number. 
# After every guess, the program tells the user whether their number was too large or too small. 
# At the end, the number of tries needed should be printed. 
# It counts only as one try if they input the same number multiple times consecutively. 

print()
print("Guess the secret number!")

secret_number = 12

# previous_guess starts as None so we can compare it to the first guess
tries = 0
previous_guess = None

# Use while True here so the loop can start without needing an initial guess value
while True:
    guess = int(input("Enter your guess: "))

    # If this guess is different from the last one, count it as a new try
    if guess != previous_guess:
        tries = tries + 1

    # Update previous_guess so we can compare it next time
    previous_guess = guess

    # Tell the user if it's too small, too large, or correct
    # break stops the loop when the guess is correct

    if guess < secret_number:
        print("Too small.")
    elif guess > secret_number:
        print("Too large.")
    else:
        print("Correct!")
        break

print("You needed", tries, "tries.")





