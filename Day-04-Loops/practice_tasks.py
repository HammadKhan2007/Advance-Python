# Day 04: Loops Practice Tasks

print("=" * 60)
print("DAY 04: LOOPS & ITERATION PRACTICE")
print("=" * 60)

# ---------------------------------------------------
# Task 1: Print numbers from 1 to 10 using for loop
# ---------------------------------------------------
print("\n--- Task 1: Numbers 1 to 10 ---")
for num in range(1, 11):
    print(num, end=" ")
print()

# ---------------------------------------------------
# Task 2: Print even numbers from 2 to 20
# ---------------------------------------------------
print("\n--- Task 2: Even Numbers ---")
for even in range(2, 21, 2):
    print(even, end=" ")
print()

# ---------------------------------------------------
# Task 3: Sum of numbers from 1 to 100
# ---------------------------------------------------
print("\n--- Task 3: Sum from 1 to 100 ---")
total = 0
for n in range(1, 101):
    total += n
print(f"Total = {total}")

# ---------------------------------------------------
# Task 4: Countdown using while loop
# ---------------------------------------------------
print("\n--- Task 4: Countdown ---")
count = 5
while count >= 1:
    print(f"Countdown: {count}")
    count -= 1
print("Liftoff!")

# ---------------------------------------------------
# Task 5: Skip numbers divisible by 3 using continue
# ---------------------------------------------------
print("\n--- Task 5: Continue Example ---")
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()

# ---------------------------------------------------
# Task 6: Stop at 7 using break
# ---------------------------------------------------
print("\n--- Task 6: Break Example ---")
for i in range(1, 11):
    if i == 7:
        print("Stopped at 7")
        break
    print(i, end=" ")
print()

# ---------------------------------------------------
# Task 7: Multiplication table of 5
# ---------------------------------------------------
print("\n--- Task 7: Multiplication Table ---")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# ---------------------------------------------------
# Task 8: Nested loop example
# ---------------------------------------------------
print("\n--- Task 8: Nested Loop Example ---")
for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row}, {col})", end=" ")
    print()

# ---------------------------------------------------
# Task 9: Mini project - Password attempt loop
# ---------------------------------------------------
print("\n--- Task 9: Password Attempt Example ---")
correct_password = "python123"
attempts = 0
while attempts < 3:
    user_input = input("Enter password: ")
    if user_input == correct_password:
        print("Access granted!")
        break
    else:
        attempts += 1
        print(f"Wrong password. Attempts left: {3 - attempts}")
else:
    print("Account locked. Try again later.")

# ---------------------------------------------------
# Task 10: Loop challenge - Factorial calculation
# ---------------------------------------------------
print("\n--- Task 10: Factorial Challenge ---")
number = 5
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"Factorial of {number} is {factorial}")

print("\n" + "=" * 60)
print("Day 04 practice complete. Keep practicing loops!")
print("=" * 60)
