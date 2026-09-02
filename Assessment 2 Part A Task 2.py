# Scenario: Requisition System Prototype

counter = 1

def staff_info():
    global counter

    date = input("Enter date (DD/MM/YYYY): ")
    staff_id = input("Enter Staff ID: ")
    staff_name = input("Enter Staff Name: ")

    requisition_id = 10000 + counter
    counter += 1

    print("\nStaff Information:")
    print("Date:", date)
    print("Staff ID:", staff_id)
    print("Staff Name:", staff_name)
    print("Requisition ID:", requisition_id, "\n")

    return date, staff_id, staff_name, requisition_id

# Task 2 calculates the total cost of requistion items
def requisitions_total():
    # Call values in staff_info() to be used in this function
    date, staff_id, staff_name, requisition_id = staff_info()

    # Give instructions for entering items
    print("Enter items, including name and price.")
    print("Press Enter without an item name to finish.\n")

    total = 0 

    # Create a loop to add multiple items
    while True:
        item = input("Item name: ")
        if item == "":
            break # Stops the loop when all items have been added

        # The price of each item is added to the total
        price = float(input(f"Price for {item}: $"))
        total += price # Total = total + price

    # Print the total cost with 2 decimal places for $
    print(f"Total Cost: ${total:.2f}")

    # Return the total for task 3
    return total

# Call the function to run it
requisitions_total()

