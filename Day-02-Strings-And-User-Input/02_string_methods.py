# Day 02: Lesson 2 - Built-in String Methods

sample_text = "   hello, Python programmers! Welcome to day 02.   "

print("Original text:", repr(sample_text))

# 1. Case Conversions
print("\n--- Case Conversions ---")
print("upper():", sample_text.upper())
print("lower():", sample_text.lower())
print("title():", sample_text.title())
print("capitalize():", sample_text.strip().capitalize())

# 2. Removing Whitespace (strip, lstrip, rstrip)
print("\n--- Stripping Whitespace ---")
clean_text = sample_text.strip()
print("strip():", repr(clean_text))
print("lstrip():", repr(sample_text.lstrip()))
print("rstrip():", repr(sample_text.rstrip()))

# 3. Search and Count
sentence = "python is easy to learn. python is widely used."
print("\n--- Search and Count ---")
print("count('python'):", sentence.count("python"))
print("find('easy'):", sentence.find("easy"))          # returns starting index
print("find('java'):", sentence.find("java"))          # returns -1 if not found
print("startswith('python'):", sentence.startswith("python"))
print("endswith('used.'):", sentence.endswith("used."))

# 4. Replacement
print("\n--- Replace ---")
updated_sentence = sentence.replace("python", "Python 3")
print("replace():", updated_sentence)

# 5. Split and Join
print("\n--- Split and Join ---")
csv_data = "hammad,python,developer,karachi"
words_list = csv_data.split(",")
print("split(','):", words_list)

joined_text = " | ".join(words_list)
print("join(' | '):", joined_text)
