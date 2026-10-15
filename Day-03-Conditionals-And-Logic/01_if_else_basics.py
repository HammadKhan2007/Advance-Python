# Day 03: Lesson 1 - If-Else Basics & Comparison Operators

# In Python, indentation (4 spaces) defines the code block inside if/else.

# 1. Comparison Operators:
# == (Equal to)
# != (Not equal to)
# >  (Greater than)
# <  (Less than)
# >= (Greater than or equal to)
# <= (Less than or equal to)

score = 78
passing_marks = 50

print("--- 1. Basic If-Else Statement ---")
if score >= passing_marks:
    print(f"Congratulations! You passed with {score} marks.")
else:
    print(f"Unfortunately, you did not pass. Required: {passing_marks}, Your score: {score}")

# 2. Checking Even or Odd (Using Modulo operator %)
number = 27
print("\n--- 2. Even or Odd Checker ---")
if number % 2 == 0:
    print(f"{number} is an EVEN number.")
else:
    print(f"{number} is an ODD number.")

# 3. Truthy and Falsy Values in Python
# Falsy values: 0, 0.0, "", None, [], (), {}
# Everything else is considered Truthy!
print("\n--- 3. Truthy & Falsy Demonstration ---")
username_input = "hammad_dev"  # Non-empty string = Truthy

if username_input:
    print(f"Welcome back, {username_input}!")
else:
    print("Username cannot be empty!")

empty_wallet = 0
if not empty_wallet:
    print("Wallet is currently empty ($0).")
