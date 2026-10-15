# Day 03: Lesson 2 - Elif Chains & Logical Operators (and, or, not)

# 1. Elif Ladder: Grading System
marks = 86

print("--- 1. Grading System with Elif ---")
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F (Fail)"

print(f"Obtained Marks: {marks} | Final Grade: {grade}")

# 2. Logical Operators:
# 'and' : Both conditions must be True
# 'or'  : At least one condition must be True
# 'not' : Inverts the boolean value (True becomes False, False becomes True)

print("\n--- 2. Job Candidate Eligibility Check ---")
has_python_skills = True
experience_years = 2
has_portfolio = True
is_student = False

# Condition using 'and' & 'or'
if (has_python_skills and experience_years >= 1) or has_portfolio:
    print("Candidate is eligible for the Developer Interview!")
else:
    print("Candidate does not meet the basic criteria yet.")

# Example with 'not'
is_banned = False
if not is_banned:
    print("Account Status: Active & in good standing.")
else:
    print("Account Status: Suspended!")
