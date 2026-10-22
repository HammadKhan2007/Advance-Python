# Day 06: Collections Practice Tasks

print("=" * 60)
print("DAY 06: COLLECTIONS PRACTICE")
print("=" * 60)

# ---------------------------------------------------
# Task 1: Create and print a list
# ---------------------------------------------------
print("\n--- Task 1: List Creation ---")
cities = ["Lahore", "Karachi", "Islamabad"]
print(cities)

# ---------------------------------------------------
# Task 2: List indexing and slicing
# ---------------------------------------------------
print("\n--- Task 2: List Indexing & Slicing ---")
print("First city:", cities[0])
print("Last city:", cities[-1])
print("First two cities:", cities[:2])

# ---------------------------------------------------
# Task 3: Update list and use methods
# ---------------------------------------------------
print("\n--- Task 3: List Update & Methods ---")
cities.append("Peshawar")
cities.insert(1, "Multan")
print("After append/insert:", cities)
cities.remove("Karachi")
print("After remove:", cities)

# ---------------------------------------------------
# Task 4: Tuple basics
# ---------------------------------------------------
print("\n--- Task 4: Tuple Basics ---")
months = ("Jan", "Feb", "Mar", "Apr")
print("Months tuple:", months)
print("Second month:", months[1])

# ---------------------------------------------------
# Task 5: Convert tuple to list and back
# ---------------------------------------------------
print("\n--- Task 5: Tuple to List Conversion ---")
months_list = list(months)
months_list.append("May")
months = tuple(months_list)
print("Updated months tuple:", months)

# ---------------------------------------------------
# Task 6: Set uniqueness
# ---------------------------------------------------
print("\n--- Task 6: Set Uniqueness ---")
roll_numbers = {101, 102, 102, 103, 104, 104}
print("Unique roll numbers:", roll_numbers)

# ---------------------------------------------------
# Task 7: Set operations
# ---------------------------------------------------
print("\n--- Task 7: Set Operations ---")
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference (a-b):", a - b)

# ---------------------------------------------------
# Task 8: Dictionary create and access
# ---------------------------------------------------
print("\n--- Task 8: Dictionary Access ---")
book = {
    "title": "Python Basics",
    "author": "Hammad",
    "price": 500,
}
print("Title:", book["title"])
print("Author:", book.get("author"))

# ---------------------------------------------------
# Task 9: Dictionary update and iteration
# ---------------------------------------------------
print("\n--- Task 9: Dictionary Update & Loop ---")
book["price"] = 550
book["edition"] = "2nd"
for key, value in book.items():
    print(f"{key}: {value}")

# ---------------------------------------------------
# Task 10: Nested dictionary
# ---------------------------------------------------
print("\n--- Task 10: Nested Dictionary ---")
school = {
    "class_1": {"teacher": "Ali", "students": 30},
    "class_2": {"teacher": "Sara", "students": 28},
}
print("Class 1 teacher:", school["class_1"]["teacher"])
print("Class 2 students:", school["class_2"]["students"])

print("\n" + "=" * 60)
print("Day 06 practice complete. Great work on collections!")
print("=" * 60)
