# Day 08: Practice Tasks & Mini Projects

import json
import os

print("=" * 60)
print("DAY 08: PRACTICE TASKS & REAL-WORLD SCENARIOS")
print("=" * 60)

# -------------------------------------------------------------
# Task 1: Safe File Reader with Exception Handling
# -------------------------------------------------------------
print("\n--- Task 1: Safe File Reader Function ---")

def read_file_safely(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return f"[Error] File '{filename}' was not found on disk."
    except Exception as e:
        return f"[Unexpected Error] {e}"

print(read_file_safely("non_existent_file.txt"))

# -------------------------------------------------------------
# Task 2: Student Grade Logger (File Append + Read)
# -------------------------------------------------------------
print("\n--- Task 2: Student Score Logger ---")
log_filename = "student_records.txt"

students_scores = [
    ("Hammad", 95),
    ("Ali", 88),
    ("Sara", 92)
]

# Write records
with open(log_filename, "w", encoding="utf-8") as f:
    for name, score in students_scores:
        f.write(f"Student: {name} | Score: {score} | Status: Pass\n")

# Read and print records
with open(log_filename, "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# Clean up
if os.path.exists(log_filename):
    os.remove(log_filename)

# -------------------------------------------------------------
# Task 3: JSON Todo / Task Persistence Manager
# -------------------------------------------------------------
print("\n--- Task 3: JSON Task Persistence Manager ---")
todo_file = "tasks.json"

tasks_data = {
    "user": "Hammad",
    "tasks": [
        {"id": 1, "title": "Complete Python Day 08", "done": True},
        {"id": 2, "title": "Push Day 08 code via GitHub Desktop", "done": False},
        {"id": 3, "title": "Review OOP basics for Day 09", "done": False}
    ]
}

# Save to JSON
with open(todo_file, "w", encoding="utf-8") as f:
    json.dump(tasks_data, f, indent=4)

# Load and display from JSON
with open(todo_file, "r", encoding="utf-8") as f:
    loaded_tasks = json.load(f)

print(f"Todo List for {loaded_tasks['user']}:")
for item in loaded_tasks["tasks"]:
    status_icon = "[x]" if item["done"] else "[ ]"
    print(f"  {status_icon} Task #{item['id']}: {item['title']}")

# Clean up
if os.path.exists(todo_file):
    os.remove(todo_file)
