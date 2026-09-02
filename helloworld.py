# Create greet function
def greet():
    name = input("Enter your name: ")
    print(f"Hello, {name}")
    

# Create add_numbers function
def add_numbers():
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    total = x + y
    print(f"The sum is: {total}")

# Call the functions
greet()
add_numbers()


