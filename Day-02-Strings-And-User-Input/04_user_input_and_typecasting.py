# Day 02: Lesson 4 - User Input and Typecasting

# Note: The input() function always returns data as a 'str' (string).

print("=== User Greeting & Info Demo ===")

# Example: Static simulated inputs for automated testing, with interactive structure explained
# In interactive mode:
# user_name = input("Enter your full name: ").strip().title()
# birth_year = int(input("Enter your birth year: "))

# Simulated values for demonstration:
sample_raw_input_name = "  hammad khan  "
clean_user_name = sample_raw_input_name.strip().title()
sample_birth_year_str = "2007"
birth_year = int(sample_birth_year_str)
current_year = 2026
calculated_age = current_year - birth_year

print(f"Original Input Name: '{sample_raw_input_name}'")
print(f"Cleaned & Formatted Name: '{clean_user_name}'")
print(f"Calculated Age for {clean_user_name}: {calculated_age} years old")

print("\n--- How to take inputs interactively in your own scripts ---")
print("""
# 1. Taking string input:
name = input("What is your name? ")

# 2. Taking integer input:
age = int(input("How old are you? "))

# 3. Taking float input:
height = float(input("Enter your height in feet: "))
""")
