# 📝 Day 06 Notes: Lists & Tuples

## 1. What is a List?
A list is an ordered and changeable collection of values.

```python
fruits = ["apple", "banana", "mango"]
```

Lists can contain strings, numbers, or mixed data types.

## 2. Indexing
Python list indexes start from `0`.

```python
items = ["a", "b", "c"]
print(items[0])   # a
print(items[-1])  # c
```

## 3. Updating List Values
Lists are mutable, which means their values can be changed.

```python
numbers = [10, 20, 30]
numbers[1] = 25
print(numbers)
```

## 4. Adding Items

```python
items.append("new")       # adds at the end
items.insert(1, "value")   # adds at a specific index
```

## 5. Removing Items

```python
items.remove("value")  # removes a matching value
items.pop()            # removes and returns the last item
items.pop(0)           # removes an item by index
```

## 6. Slicing
Slicing returns part of a list.

```python
numbers = [0, 1, 2, 3, 4]
print(numbers[1:4])  # [1, 2, 3]
print(numbers[:3])   # first three items
print(numbers[::2])  # every second item
```

## 7. Useful List Methods and Functions
- `len(list)` - number of items
- `sum(list)` - total of numeric values
- `min(list)` - smallest value
- `max(list)` - largest value
- `list.sort()` - sort in ascending order
- `list.reverse()` - reverse the list
- `list.count(value)` - count occurrences
- `list.index(value)` - find an item's index

## 8. Looping Through Lists

```python
for fruit in fruits:
    print(fruit)
```

Use `enumerate()` when you also need the position:

```python
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
```

## 9. List Comprehension
List comprehension creates a list in a short and readable way.

```python
squares = [number ** 2 for number in range(1, 6)]
evens = [number for number in range(10) if number % 2 == 0]
```

## 10. What is a Tuple?
A tuple is ordered like a list, but it is immutable. Its values cannot be changed after creation.

```python
coordinates = (24.86, 67.00)
```

Use tuples for fixed data such as coordinates, days of the week, or student records.

## 11. Tuple Unpacking

```python
student = ("Hammad", 18, "Python")
name, age, subject = student
```

## 12. List vs Tuple

| Feature | List | Tuple |
|---|---|---|
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` |
| Changeable | Yes | No |
| Best for | Data that changes | Fixed data |
| Methods | More methods | Fewer methods |

## 13. Day 06 Practice Goals
1. Create and index lists.
2. Add, update, and remove list values.
3. Use slicing and list methods.
4. Loop through lists with `for` and `enumerate()`.
5. Practice list comprehensions.
6. Create tuples and unpack their values.
7. Understand the difference between mutable and immutable data.
