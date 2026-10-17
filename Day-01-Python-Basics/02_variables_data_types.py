# Day 01: Lesson 2 - Variables & Data Types

# Variables store data values
student_name = "Hammad"          # str (String)
age = 18                         # int (Integer)
course_progress = 1.0            # float (Floating point number)
is_learning_active = True        # bool (Boolean)
dateofstart = "2026-10-16" 
print(student_name[1])
print(student_name[1:6:2]) # Slicing the string from index 1 to 6 with a step of 2


# Printing variables and their data types
print("Student Name:", student_name, "| Type:", type(student_name))
print("Age:", age, "| Type:", type(age))
print("Course Progress:", course_progress, "| Type:", type(course_progress))
print("Is Learning Active?", is_learning_active, "| Type:", type(is_learning_active))
print("Date of Start:", dateofstart, "| Type:", type(dateofstart))  

# Basic Type Casting (Conversion)
str_num = "50"
converted_num = int(str_num)
print("Converted to integer:", converted_num + 50)
b = 0
print(bool(b))  # False, because 0 is considered False
age_khan = 18 
print(str(age_khan))  # Converts integer to string
a = 13
a = str(a)
print((a), type(a))  # Converts integer to string and prints its type
 
name = "Hammad"
future_goals = "Becoming a Data Scientist"
semester = 3
print("Developer Name:", name,"|Type:", type(name))
print("Developer Goal:", future_goals,)
print("Current Semester:", semester, "|Type:", type(semester))
#age = 12 student_name = "Hammad" a = True course-progress = 1.0
