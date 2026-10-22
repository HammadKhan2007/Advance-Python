# Day 06: Lists and Tuples

print("=" * 60)
print("DAY 06: LISTS AND TUPLES")
print("=" * 60)

# 1. Creating lists
print("\n--- 1. Creating Lists ---")
fruits = ["apple", "banana", "mango"]
print(fruits)
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# 2. Updating list items
print("\n--- 2. Updating List Items ---")
fruits[1] = "orange"
print(fruits)

# 3. Adding and removing items
print("\n--- 3. Add and Remove Items ---")
fruits.append("grapes")
fruits.insert(1, "banana")
print(f"After adding: {fruits}")

fruits.remove("orange")
removed_fruit = fruits.pop()
print(f"After removing orange: {fruits}")
print(f"Popped fruit: {removed_fruit}")

# 4. Slicing and useful list functions
print("\n--- 4. Slicing and List Functions ---")
numbers = [5, 2, 9, 1, 7]
print(f"First three: {numbers[:3]}")
print(f"Length: {len(numbers)}")
print(f"Minimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Total: {sum(numbers)}")

numbers.sort()
print(f"Sorted: {numbers}")
numbers.reverse()
print(f"Reversed: {numbers}")

# 5. Loop through a list
print("\n--- 5. Loop Through a List ---")
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# 6. List comprehension
print("\n--- 6. List Comprehension ---")
squares = [number ** 2 for number in range(1, 6)]
even_numbers = [number for number in range(1, 11) if number % 2 == 0]
print(f"Squares: {squares}")
print(f"Even numbers: {even_numbers}")

# 7. Tuples
print("\n--- 7. Tuples ---")
coordinates = ( Karachi", 24.8607, 67.0011)
print(coordinates)
print(f"City: {coordinates[0]}")
print(f"Tuple length: {len(coordinates)}")

# Tuples are immutable, so their values cannot be changed after creation.
student = ("Hammad", 18, "Python")
name, age, subject = student
print(f"Name: {name}, Age: {age}, Subject: {subject}")

print("\n" + "=" * 60)
print("Day 06 lesson complete!")
print("=" * 60)
