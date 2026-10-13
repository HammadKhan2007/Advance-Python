# Day 01: Lesson 2 - Variables & Data Types

# Variables store data values
student_name = "Hammad"          # str (String)
age = 18                         # int (Integer)
course_progress = 1.0            # float (Floating point number)
is_learning_active = True        # bool (Boolean)

# Printing variables and their data types
print("Student Name:", student_name, "| Type:", type(student_name))
print("Age:", age, "| Type:", type(age))
print("Course Progress:", course_progress, "| Type:", type(course_progress))
print("Is Learning Active?", is_learning_active, "| Type:", type(is_learning_active))

# Basic Type Casting (Conversion)
str_num = "50"
converted_num = int(str_num)
print("Converted to integer:", converted_num + 50)
