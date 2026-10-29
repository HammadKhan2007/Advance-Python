# Day 08: File Handling Basics in Python

import os

print("=" * 60)
print("DAY 08: FILE HANDLING BASICS")
print("=" * 60)

file_path = "sample_notes.txt"

# 1. Writing to a file ('w' mode creates or overwrites the file)
print("\n--- 1. Writing to a File ('w' mode) ---")
with open(file_path, "w", encoding="utf-8") as file:
    file.write("Python Day 08: File Handling\n")
    file.write("Line 1: Files allow permanent data storage.\n")
    file.write("Line 2: The 'with' statement closes files automatically.\n")
print(f"Data successfully written to '{file_path}'.")

# 2. Reading from a file ('r' mode)
print("\n--- 2. Reading Full Content ('r' mode) ---")
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
    print("File Content:\n" + content.strip())

# 3. Reading line by line using readline() and loop
print("\n--- 3. Reading Line by Line ---")
with open(file_path, "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        print(f"Line {line_number}: {line.strip()}")

# 4. Appending to a file ('a' mode preserves existing content)
print("\n--- 4. Appending Data ('a' mode) ---")
with open(file_path, "a", encoding="utf-8") as file:
    file.write("Line 3: Appended content without deleting previous lines.\n")
print("New line appended successfully.")

# Verify appended content
with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()
    print(f"Total lines now in file: {len(lines)}")

# 5. Cleanup temporary file
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"\nTemporary file '{file_path}' cleaned up.")
