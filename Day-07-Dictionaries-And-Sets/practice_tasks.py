# Day 07: Dictionaries and Sets Practice Tasks

print("=" * 60)
print("DAY 07: DICTIONARIES AND SETS PRACTICE")
print("=" * 60)

# Task 1: Student record
student = {
    "name": "Hammad",
    "age": 18,
    "marks": 88,
}
print("Student:", student)
student["grade"] = "A"
print("Updated student:", student)

# Task 2: Count word frequency
sentence = "python is easy and python is powerful"
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print("Word count:", word_count)

# Task 3: Product prices
products = {
    "laptop": 85000,
    "mouse": 2500,
    "keyboard": 4500,
}
total = sum(products.values())
print("Product total:", total)
print("Most expensive product:", max(products, key=products.get))

# Task 4: Remove duplicate numbers
numbers = [4, 2, 4, 7, 2, 9, 7, 1]
unique_numbers = set(numbers)
print("Unique numbers:", unique_numbers)

# Task 5: Set relationships
sports = {"cricket", "football", "tennis"}
indoor_games = {"chess", "tennis", "table tennis"}
print("All activities:", sports | indoor_games)
print("Common activities:", sports & indoor_games)

# Task 6: Contact book
contacts = {
    "Ali": "0300-1111111",
    "Sara": "0300-2222222",
}
name = "Sara"
print(f"{name}'s number:", contacts.get(name, "Contact not found"))

print("\nDay 07 practice complete. Keep practicing dictionaries and sets!")
