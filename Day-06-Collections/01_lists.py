# Day 06: Lists in Python

print("=" * 60)
print("DAY 06 - LESSON 1: LISTS")
print("=" * 60)

# 1. List creation
print("\n--- 1. List Creation ---")
fruits = ["apple", "banana", "mango", "orange"]
print("Fruits list:", fruits)

numbers = [10, 20, 30, 40, 50]
print("Numbers list:", numbers)

# 2. Indexing
print("\n--- 2. Indexing ---")
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# 3. Slicing
print("\n--- 3. Slicing ---")
print("First 3 numbers:", numbers[:3])
print("Middle numbers:", numbers[1:4])

# 4. Updating list values
print("\n--- 4. Update List ---")
fruits[1] = "grapes"
print("Updated fruits:", fruits)

# 5. Common list methods
print("\n--- 5. List Methods ---")
fruits.append("peach")
print("After append:", fruits)

fruits.insert(1, "kiwi")
print("After insert:", fruits)

fruits.remove("mango")
print("After remove:", fruits)

removed_item = fruits.pop()
print("Popped item:", removed_item)
print("After pop:", fruits)

print("Length of fruits list:", len(fruits))

# 6. Iteration
print("\n--- 6. Iterating Over List ---")
for item in fruits:
    print("Fruit:", item)

print("\nList lesson complete!")
print("=" * 60)
