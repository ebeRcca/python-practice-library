# Scenario: Requisition System Prototype

# Counter to generate requisition IDs. 
# The counter is global as it needs to remember its value every time the function runs.
counter = 10001

# Task 1 generates unique ID and collects staff information
def staff_info():
    global counter
    print("About to ask for inputs")

    # Staff information required:
    date = input("Enter date (DD/MM/YYYY): ")
    staff_id = input("Enter Staff ID: ")
    staff_name = input("Enter Staff Name: ")

    # Generate unique ID using counter + 10000
    requisition_id = counter
    counter += 1  # Counter = counter + 1 -> increases the counter by 1 for the next requisition

    # Print the information in the format given
    print("\nStaff Information:")
    print("Date:", date)
    print("Staff ID:", staff_id)
    print("Staff Name:", staff_name)
    print("Requisition ID:", requisition_id, "\n")

    # Return all values for later tasks
    return date, staff_id, staff_name, requisition_id

# Call the function multiple times to check the counter is increasing
staff_info()
staff_info()
staff_info()





    


    