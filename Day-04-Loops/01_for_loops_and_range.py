# Day 04: Lesson 1 - For Loops, Range & Iteration

# A 'for' loop is used for iterating over a sequence (list, tuple, string, or range).

print("=" * 55)
print("LESSON 1: FOR LOOPS & RANGE FUNCTION")
print("=" * 55)

# 1. Iterating through a List
fruits = ["Apple", "Mango", "Banana", "Cherry"]
print("\n--- 1. Iterating Over a List ---")
for fruit in fruits:
    print(f"Fresh Fruit: {fruit}")

# 2. Iterating through a String (character by character)
print("\n--- 2. Iterating Over a String ---")
word = "PYTHON"
for char in word:
    print(f"Letter: {char}")

# 3. The range() Function: range(start, stop, step)
# Note: 'stop' is always excluded.

# A) range(stop) -> starts at 0, goes up to stop-1
print("\n--- 3A. range(5) ---")
for i in range(5):
    print(f"Count: {i}")

# B) range(start, stop) -> from start to stop-1
print("\n--- 3B. range(1, 6) ---")
for num in range(1, 6):
    print(f"Number: {num}")

# C) range(start, stop, step) -> skips by step value
print("\n--- 3C. Even Numbers from 2 to 10 (step=2) ---")
for even in range(2, 11, 2):
    print(f"Even: {even}")

# D) Counting Backwards (negative step)
print("\n--- 3D. Countdown from 5 to 1 ---")
for count in range(5, 0, -1):
    print(f"Countdown: {count}...")
print("Liftoff! [Success]")

# 4. Practical Example: Sum of Numbers from 1 to 100
total_sum = 0
for n in range(1, 101):
    total_sum += n
print(f"\nTotal Sum of numbers from 1 to 100 = {total_sum}")

# 5. Using enumerate() to get both Index and Value
print("\n--- 5. Using enumerate() ---")
technologies = ["Python", "FastAPI", "Pandas", "PyTorch"]
for index, tech in enumerate(technologies, start=1):
    print(f"{index}. {tech}")
