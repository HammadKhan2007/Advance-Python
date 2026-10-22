# Day 07: Dictionaries and Sets

print("=" * 60)
print("DAY 07: DICTIONARIES AND SETS")
print("=" * 60)

# 1. Creating a dictionary
print("\n--- 1. Creating a Dictionary ---")
student = {
    "name": "Hammad",
    "age": 18,
    "course": "Python",
}
print(student)
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")

# 2. Adding and updating values
print("\n--- 2. Adding and Updating Values ---")
student["city"] = "Karachi"
student["age"] = 19
print(student)

# 3. Dictionary methods
print("\n--- 3. Dictionary Methods ---")
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:", list(student.items()))
print("Phone:", student.get("phone", "Not available"))

# 4. Looping through a dictionary
print("\n--- 4. Looping Through a Dictionary ---")
for key, value in student.items():
    print(f"{key}: {value}")

# 5. Nested dictionaries
print("\n--- 5. Nested Dictionaries ---")
classroom = {
    "student_1": {"name": "Ali", "marks": 82},
    "student_2": {"name": "Sara", "marks": 91},
}
print(f"Student 1: {classroom['student_1']['name']}")
print(f"Student 2 marks: {classroom['student_2']['marks']}")

# 6. Creating a set
print("\n--- 6. Creating a Set ---")
numbers = {1, 2, 3, 3, 4, 4, 5}
print("Duplicate values are removed:", numbers)

# 7. Set operations
print("\n--- 7. Set Operations ---")
python_students = {"Ali", "Hammad", "Sara"}
java_students = {"Sara", "Usman", "Hammad"}
print("Union:", python_students | java_students)
print("Intersection:", python_students & java_students)
print("Only Python:", python_students - java_students)
print("Different students:", python_students ^ java_students)

# 8. Adding and removing set values
print("\n--- 8. Updating a Set ---")
python_students.add("Ayesha")
python_students.discard("Ali")
print(python_students)

print("\n" + "=" * 60)
print("Day 07 lesson complete!")
print("=" * 60)
