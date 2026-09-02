# Initialize a global counter
registration_counter = 50000

def student_registration():
    global registration_counter  # Use the global counter

    # Generate the Registration ID using the current counter value
    registration_id = registration_counter
    registration_counter += 1  # Increment the counter for the next registration

    date = input("Enter the registration date (dd/mm/yyyy): ")
    student_id = input("Enter the Student ID: ")
    student_name = input("Enter the Student Name: ")
    course_name = input("Enter the Course Name: ")

    # Display the information
    print("\nPrinting Student Registration Information:")
    print(f"Date: {date}")
    print(f"Student ID: {student_id}")
    print(f"Student Name: {student_name}")
    print(f"Course Name: {course_name}")
    print(f"Registration ID: {registration_id}")

# call the function:
student_registration()
