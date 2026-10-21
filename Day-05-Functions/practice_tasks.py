# Day 05: Functions Practice Tasks

print("=" * 60)
print("DAY 05: FUNCTIONS & SCOPE PRACTICE")
print("=" * 60)

# ---------------------------------------------------
# Task 1: Simple greeting function
# ---------------------------------------------------
print("\n--- Task 1: Greeting Function ---")

def greet(name):
    return f"Hello, {name}!"

print(greet("Hammad"))

# ---------------------------------------------------
# Task 2: Add two numbers
# ---------------------------------------------------
print("\n--- Task 2: Sum Function ---")

def add(a, b):
    return a + b

print(add(10, 25))

# ---------------------------------------------------
# Task 3: Check even or odd
# ---------------------------------------------------
print("\n--- Task 3: Even / Odd Checker ---")

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    return "Odd"

print(check_even_odd(9))
print(check_even_odd(12))

# ---------------------------------------------------
# Task 4: Default parameter example
# ---------------------------------------------------
print("\n--- Task 4: Default Parameter ---")

def greet_user(name="User"):
    return f"Welcome, {name}!"

print(greet_user())
print(greet_user("Ali"))

# ---------------------------------------------------
# Task 5: Area of rectangle
# ---------------------------------------------------
print("\n--- Task 5: Area Function ---")

def rectangle_area(length, width):
    return length * width

print(rectangle_area(5, 7))

# ---------------------------------------------------
# Task 6: Factorial function
# ---------------------------------------------------
print("\n--- Task 6: Factorial Function ---")

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))

# ---------------------------------------------------
# Task 7: Global vs Local variable
# ---------------------------------------------------
print("\n--- Task 7: Scope Example ---")

global_value = 50

def update_value():
    local_value = 20
    print(f"Local value = {local_value}")
    print(f"Global value = {global_value}")

update_value()

# ---------------------------------------------------
# Task 8: Calculator function
# ---------------------------------------------------
print("\n--- Task 8: Calculator ---")

def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    else:
        return "Invalid operation"

print(calculator(8, 4, "+"))
print(calculator(8, 4, "*"))

# ---------------------------------------------------
# Task 9: Simple loop inside function
# ---------------------------------------------------
print("\n--- Task 9: Function With Loop ---")

def print_numbers(limit):
    for i in range(1, limit + 1):
        print(i, end=" ")
    print()

print_numbers(10)

# ---------------------------------------------------
# Task 10: Challenge - Password checker
# ---------------------------------------------------
print("\n--- Task 10: Password Checker ---")

def password_check(password):
    correct_password = "python123"
    if password == correct_password:
        return "Access granted"
    return "Access denied"

print(password_check("python123"))
print(password_check("wrongpass"))

print("\n" + "=" * 60)
print("Day 05 practice complete. Keep mastering Python functions!")
print("=" * 60)
