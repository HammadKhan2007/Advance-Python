# Day 08: Exception Handling in Python (try, except, else, finally)

print("=" * 60)
print("DAY 08: EXCEPTION HANDLING")
print("=" * 60)

# 1. Basic try-except (Handling ZeroDivisionError)
print("\n--- 1. Handling ZeroDivisionError ---")
try:
    numerator = 100
    denominator = 0
    result = numerator / denominator
    print(f"Result: {result}")
except ZeroDivisionError as error:
    print(f"Caught Error: Cannot divide by zero! ({error})")

# 2. Handling multiple specific exceptions
print("\n--- 2. Handling Multiple Exceptions ---")
sample_data = {"name": "Hammad", "age": "19"}

try:
    # Converting string to int
    age_number = int(sample_data["age"])
    print(f"Valid Age: {age_number}")
    
    # Trying to access non-existent key
    email = sample_data["email"]
except ValueError:
    print("Error: Could not convert value to integer!")
except KeyError as key_err:
    print(f"Caught KeyError: Missing key {key_err} in dictionary!")

# 3. Full try-except-else-finally block
print("\n--- 3. Full try-except-else-finally Pattern ---")
try:
    num1 = 50
    num2 = 5
    ans = num1 / num2
except ZeroDivisionError:
    print("Exception occurred during division!")
else:
    # Runs ONLY if no exceptions were raised
    print(f"Else block: Calculation succeeded! Answer = {ans}")
finally:
    # Runs ALWAYS, regardless of exceptions (ideal for closing files / DB connections)
    print("Finally block: Operation completed safely.")

# 4. Raising Custom Exceptions with 'raise'
print("\n--- 4. Raising Custom Exceptions ---")
def validate_age(user_age):
    if user_age < 0:
        raise ValueError("Age cannot be negative!")
    return f"Valid age provided: {user_age}"

try:
    print(validate_age(19))
    print(validate_age(-5))
except ValueError as val_err:
    print(f"Custom validation caught: {val_err}")
