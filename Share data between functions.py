# Author Rebecca Pene

# Create a funtion that uses global variables to share data between functions
# Utilising add_item function

total_cost = 0   

def add_item(price):
    global total_cost
    total_cost += price
    print(f"The running total is: ${total_cost}")

# Function 2, final_total, displays the global total_cost updated by add_item
def final_total():
    print(f"The final total is: ${total_cost}")

# Call the functions to show running and final totals
add_item(3)
add_item(5)
add_item(8)
final_total()





