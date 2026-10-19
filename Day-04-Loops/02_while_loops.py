# Day 04: Lesson 2 - While Loops

# 'while' loop tab tak chalta rehta hai jab tak condition True ho.

print("=" * 55)
print("LESSON 2: WHILE LOOPS")
print("=" * 55)

# 1. Basic While Loop
print("\n--- 1. Basic While Loop ---")
count = 1
while count <= 5:
    print(f"Count is: {count}")
    count += 1  # Very important: counter increment karna!
print("Loop finished!")

# 2. While loop with User-like Input Simulation
print("\n--- 2. Password Attempt Simulator ---")
correct_password = "python123"
attempts_left = 3
entered_password = "wrong"   # simulated wrong attempt

while attempts_left > 0 and entered_password != correct_password:
    print(f"Wrong password! Attempts remaining: {attempts_left}")
    attempts_left -= 1
    if attempts_left == 0:
        entered_password = "python123"  # simulate correct on last try

if entered_password == correct_password:
    print("Access Granted! Welcome back.")
else:
    print("Account locked due to too many failed attempts.")

# 3. While loop as a running counter
print("\n--- 3. Multiplication Table Generator ---")
number = 7
multiplier = 1
while multiplier <= 10:
    result = number * multiplier
    print(f"{number} x {multiplier:>2} = {result:>3}")
    multiplier += 1
