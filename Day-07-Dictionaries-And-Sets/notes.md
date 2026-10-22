# 📝 Day 07 Notes: Dictionaries & Sets

## 1. What is a Dictionary?
A dictionary stores data in `key: value` pairs.

```python
student = {
    "name": "Hammad",
    "age": 18,
}
```

Dictionaries are mutable, so values can be added, changed, or removed.

## 2. Accessing Values

```python
print(student["name"])
print(student.get("age"))
print(student.get("phone", "Not available"))
```

Using `.get()` is safer when a key might not exist.

## 3. Adding and Updating Values

```python
student["city"] = "Karachi"  # add a new key
student["age"] = 19          # update an existing key
```

## 4. Removing Values

```python
student.pop("age")
del student["city"]
student.clear()
```

## 5. Useful Dictionary Methods
- `dict.keys()` - returns all keys
- `dict.values()` - returns all values
- `dict.items()` - returns key-value pairs
- `dict.get(key)` - safely gets a value
- `dict.update(other)` - adds or updates multiple values

## 6. Looping Through Dictionaries

```python
for key, value in student.items():
    print(key, value)
```

## 7. Nested Dictionaries
A dictionary can contain another dictionary.

```python
students = {
    "student_1": {"name": "Ali", "marks": 82},
    "student_2": {"name": "Sara", "marks": 91},
}
print(students["student_1"]["marks"])
```

## 8. What is a Set?
A set is an unordered collection that stores only unique values.

```python
numbers = {1, 2, 2, 3}
print(numbers)  # {1, 2, 3}
```

Sets are useful for removing duplicates and comparing groups of values.

## 9. Set Methods

```python
values.add(10)
values.remove(10)   # raises an error if missing
values.discard(10)  # does not raise an error if missing
```

## 10. Set Operations

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # union
print(a & b)  # intersection
print(a - b)  # difference
print(a ^ b)  # symmetric difference
```

## 11. Dictionary vs Set

| Feature | Dictionary | Set |
|---|---|---|
| Stores | Key-value pairs | Unique values |
| Syntax | `{"key": "value"}` | `{1, 2, 3}` |
| Duplicate values | Keys must be unique | All values are unique |
| Common use | Structured records | Membership and comparisons |

## 12. Day 07 Practice Goals
1. Create and access dictionaries.
2. Add, update, and remove dictionary values.
3. Use dictionary methods and loops.
4. Practice nested dictionaries.
5. Create sets and remove duplicates.
6. Use union, intersection, difference, and symmetric difference.
