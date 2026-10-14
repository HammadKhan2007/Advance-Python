# Day 02: Practical Exercises & Mini Projects

print("=" * 50)
print("DAY 02: PRACTICE TASKS & MINI PROJECTS")
print("=" * 50)

# -----------------------------------------------------------
# Task 1: Smart Email Parser & Username Generator
# -----------------------------------------------------------
print("\n--- Task 1: Smart Email Parser ---")
raw_email = "   HammadKhan2007@gmail.COM   "
clean_email = raw_email.strip().lower()

# Extract username (before @) and domain (after @)
username, domain = clean_email.split("@")
is_valid_gmail = clean_email.endswith("gmail.com")

print(f"Cleaned Email : {clean_email}")
print(f"Username      : {username}")
print(f"Domain        : {domain}")
print(f"Is Gmail?     : {is_valid_gmail}")

# -----------------------------------------------------------
# Task 2: Restaurant Bill & Tip Split Calculator
# -----------------------------------------------------------
print("\n--- Task 2: Restaurant Bill Splitter ---")
total_bill = 4500.00
tip_percentage = 10.0      # 10% tip
number_of_friends = 3

tip_amount = (total_bill * tip_percentage) / 100
final_bill = total_bill + tip_amount
each_person_share = final_bill / number_of_friends

print(f"Original Bill : PKR {total_bill:,.2f}")
print(f"Tip ({tip_percentage}%)  : PKR {tip_amount:,.2f}")
print(f"Total Amount  : PKR {final_bill:,.2f}")
print(f"Each Person   : PKR {each_person_share:,.2f}")

# -----------------------------------------------------------
# Task 3: Palindrome Checker (Using Slicing)
# -----------------------------------------------------------
print("\n--- Task 3: Palindrome Checker ---")
word = "Radar"
# Clean and normalize: lowercase
normalized_word = word.lower()
reversed_word = normalized_word[::-1]
is_palindrome = normalized_word == reversed_word

print(f"Original Word : '{word}'")
print(f"Reversed Word : '{reversed_word}'")
print(f"Is Palindrome?: {is_palindrome}")
