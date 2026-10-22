# Day 06: Lists and Tuples Practice Tasks

print("=" * 60)
print("DAY 06: LISTS AND TUPLES PRACTICE")
print("=" * 60)

# Task 1: Store and display student names
students = ["Ali", "Sara", "Hammad", "Ayesha"]
print("Students:", students)
print("First student:", students[0])
print("Last student:", students[-1])

# Task 2: Add and remove items
students.append("Usman")
students.remove("Sara")
print("Updated students:", students)

# Task 3: Calculate statistics
marks = [78, 92, 65, 88, 74]
print("Marks:", marks)
print("Total marks:", sum(marks))
print("Highest marks:", max(marks))
print("Lowest marks:", min(marks))
print("Average marks:", sum(marks) / len(marks))

# Task 4: Filter passing marks with list comprehension
passing_marks = [mark for mark in marks if mark >= 70]
print("Passing marks:", passing_marks)

# Task 5: Remove duplicate values
numbers = [1, 2, 2, 3, 4, 4, 5, 5]
unique_numbers = list(set(numbers))
unique_numbers.sort()
print("Unique numbers:", unique_numbers)

# Task 6: Count a value
colors = ["red", "blue", "green", "blue", "yellow", "blue"]
print("Blue appears:", colors.count("blue"), "times")

# Task 7: Tuple unpacking
person = ("Hammad", 18, "Pakistan")
person_name, person_age, country = person
print(f"{person_name} is {person_age} years old and lives in {country}.")

# Task 8: Shopping cart total
cart = [("Notebook", 250), ("Pen", 50), ("Bag", 1200)]
total = sum(price for item, price in cart)
print("Shopping cart total:", total)

print("\nDay 06 practice complete. Keep practicing lists and tuples!")
