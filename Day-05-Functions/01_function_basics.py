# Day 05: Function Basics

print("=" * 55)
print("LESSON 1: FUNCTIONS & SCOPE")
print("=" * 55)

# 1. Simple function
print("\n--- 1. Simple Function ---")

def greet(name):
    print(f"Hello, {name}!")

greet("Python")

def add(a, b):
    return a + b

print(f"Sum = {add(5, 7)}")

# 2. Default parameter
print("\n--- 2. Default Parameter ---")

def welcome(name="User"):
    print(f"Welcome, {name}!")

welcome()
welcome("Hammad")

# 3. Scope example
print("\n--- 3. Scope Example ---")

global_var = "I am global"

def show_scope():
    local_var = "I am local"
    print(global_var)
    print(local_var)

show_scope()

# 4. Function with loop
print("\n--- 4. Function with Loop ---")

def print_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

print_table(3)
