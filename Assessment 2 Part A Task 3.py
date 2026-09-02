# Scenario: Requisition System Prototype

# All functions need to be in the same file to run

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


def requisitions_total():
    date, staff_id, staff_name, requisition_id = staff_info()

    print("Enter items, including name and price.")
    print("Press Enter without an item name to finish.\n")

    total = 0 

    while True:
        item = input("Item name: ")
        if item == "":
            break 

        price = float(input(f"Price for {item}: $"))
        total += price # Total = total + price

    print(f"Total Cost: ${total:.2f}")

    return total, staff_id, requisition_id

# Task 3 makes approval decisions based on total cost
def requisition_approval():
    # Call values from requisitions_total() to be used in this function
    total, staff_id, requisition_id = requisitions_total()
    
    status = "Pending" # Set the default status for all requisitions
    approval_ref = "" # Stays empty unless approved

    if total < 500:
        status = "Approved"
        # requisition_id is created as an integer in staff_info(), but integers can't be broken up like strings.
        # It is converted to a string here to extract the last 3 digits for the approval reference.
        approval_ref = staff_id + str(requisition_id)[-3:] 

    print(f"Status: {status}")

    if approval_ref != "":
        print(f"Approval Reference Number: {approval_ref}")

    return status, approval_ref

requisition_approval()

def display_requisitions(date, requisition_id, staff_id, staff_name, total, status, approval_ref):
    print("\nPrinting Requisitions:")
    print(f"Date: {date}")
    print(f"Requisition ID: {requisition_id}")
    print(f"Staff ID: {staff_id}")
    print(f"Staff Name: {staff_name}")
    print(f"Total: ${total:.2f}")
    print(f"Status: {status}")

    if approval_ref != "":
        print(f"Approval Reference Number: {approval_ref}")

display_requisitions()


