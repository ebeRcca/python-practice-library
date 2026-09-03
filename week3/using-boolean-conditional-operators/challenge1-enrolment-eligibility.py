# Challenge 1 – Enrolment Eligibility

# User input
distance_from_school = float(input("How far does the student live from the school (in km)? "))
age = int(input("What is the age of the student? "))
right_to_stay = input("Does the student have the right to stay in NZ? (yes/no): ")
international_fees = input("Will the student pay international fees? (yes/no): ")

# Student meets criteria
if distance_from_school < 4 and age < 18 and right_to_stay == "yes":
    eligible = True

# Exception 
elif age < 18 and international_fees == "yes":
    eligible = True

# Student does not meet the critera 
else:
    eligible = False

print("Eligible to enrol:", eligible)

# Assertion 1:
# distance_from_school = 3, age = 17, right_to_stay = yes, intl_fees = no
# Expected eligiblility = True

# Assertion 2:
# distance_from_school = 10, age = 16, right_to_stay = no, intl_fees = yes
# Expected eligibility = True   (because international fees override)

# Assertion 3:
# distance_from_school = 5, age = 17, right_to_stay = no, intl_fees = no
# Expected eligibility = False

