# Vowel or consonant

print()

# User input
letter = input("Enter a letter (in lowercase): ")

# Vowel or consonant
if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("The letter", letter, "is a vowel")

elif letter == "y":
    print("The letter y is sometimes a vowel and sometimes a consonant")

else:
    print("The letter", letter, "is a consonant")

print()



