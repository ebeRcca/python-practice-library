secret = 17
tries = 0
previous_guess = None

while True:
    guess = int(input("Enter your guess: "))

    if guess != previous_guess:
        tries = tries + 1

    previous_guess = guess

    if guess < secret:
        print("Too small.")
    elif guess > secret:
        print("Too large.")
    else:
        print("Correct!")
        break

print("You needed", tries, "tries.")
