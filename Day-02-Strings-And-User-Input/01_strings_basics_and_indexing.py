# Day 02: Lesson 1 - String Basics, Indexing & Slicing

# 1. Defining Strings (Single, Double & Multi-line Triple Quotes)
single_quote = 'Python is amazing'
double_quote = "Python is powerful"
multi_line = """This is a multi-line string.
It can span multiple lines.
Great for documentation and paragraphs."""

print("--- String Types ---")
print(single_quote)
print(multi_line)

# 2. String Length
message = "Advance Python"
print("\n--- Length of String ---")
print("Text:", message)
print("Length:", len(message))

# 3. String Indexing (0-indexed)
# Positive:  0   1   2   3   4   5
#            P   y   t   h   o   n
# Negative: -6  -5  -4  -3  -2  -1
language = "Python"
print("\n--- Indexing ---")
print("First character [0]:", language[0])
print("Last character [-1]:", language[-1])
print("Second to last [-2]:", language[-2])

# 4. String Slicing [start:stop:step] (stop index is excluded)
text = "Artificial Intelligence"
print("\n--- Slicing ---")
print("First 10 chars [0:10]:", text[0:10])
print("From index 11 to end [11:]:", text[11:])
print("Every second character [::2]:", text[::2])
print("Reversed string [::-1]:", text[::-1])

# 5. Strings are Immutable (Cannot change a character directly)
# language[0] = "J"  <-- This would throw a TypeError!
# Instead, create a new string:
new_language = "J" + language[1:]
print("\nModified (new string):", new_language)
