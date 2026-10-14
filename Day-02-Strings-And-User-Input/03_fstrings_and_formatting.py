# Day 02: Lesson 3 - Modern String Formatting with f-strings

developer_name = "Muhammad Hammad"
experience_days = 2
course = "Advance Python"
rating = 4.9856
wallet_balance = 150000

# 1. Basic f-string (Python 3.6+)
intro = f"Hi, I am {developer_name}. Today is Day {experience_days} of {course}."
print(intro)

# 2. Arithmetic expressions inside f-strings
print(f"In 30 days, I will be at Day {experience_days + 28}!")

# 3. Formatting floating point numbers (rounding to 2 decimals)
print(f"Course rating: {rating:.2f} / 5.00")

# 4. Currency and large number formatting with commas
print(f"Monthly Target Salary: PKR {wallet_balance:,}")

# 5. Padding and Text Alignment
print("\n--- Alignment Examples ---")
print(f"{'Left Aligned':<20} | {'Center':^15} | {'Right':>10}")
print("-" * 52)
print(f"{'Python':<20} | {'Awesome':^15} | {'100%':>10}")
print(f"{'JavaScript':<20} | {'Good':^15} | {'90%':>10}")
