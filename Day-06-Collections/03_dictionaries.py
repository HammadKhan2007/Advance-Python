# Day 06: Dictionaries in Python

print("=" * 60)
print("DAY 06 - LESSON 3: DICTIONARIES")
print("=" * 60)

# 1. Dictionary creation
print("\n--- 1. Dictionary Creation ---")
student = {
    "name": "Hammad",
    "age": 20,
    "course": "Python",
}
print("Student dictionary:", student)

# 2. Accessing values
print("\n--- 2. Accessing Key/Value ---")
print("Name:", student["name"])
print("Age using get():", student.get("age"))
print("City using get() with default:", student.get("city", "Not provided"))

# 3. Updating dictionary
print("\n--- 3. Updating Dictionary ---")
student["age"] = 21
student["city"] = "Lahore"
print("Updated student:", student)

# 4. Common dictionary methods
print("\n--- 4. Dictionary Methods ---")
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

removed_course = student.pop("course")
print("Removed course:", removed_course)
print("After pop:", student)

# 5. Iteration in dictionary
print("\n--- 5. Dictionary Iteration ---")
for key, value in student.items():
    print(f"{key} -> {value}")

# 6. Nested dictionaries
print("\n--- 6. Nested Dictionary ---")
classroom = {
    "student_1": {"name": "Ali", "marks": 88},
    "student_2": {"name": "Sara", "marks": 92},
}

print("Classroom data:", classroom)
print("Student 2 name:", classroom["student_2"]["name"])

print("\nDictionary lesson complete!")
print("=" * 60)
