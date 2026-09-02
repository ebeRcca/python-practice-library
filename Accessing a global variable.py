# Author Rebecca Pene

# Create a funtion that accesses a global variable
# The function is called add_item to track the running total cost when adding items

total_cost = 0   

def add_item(price):
    global total_cost # Make total_cost global to allow access and updates outside the function

    total_cost += price
    print(f"The running total is: ${total_cost}")

# Call the function to show the functions running totals
add_item(3)
add_item(5)
add_item(8)

# Access the global variable total_cost to show the final total
print(f"The final total is: ${total_cost}")
