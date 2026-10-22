# 📝 Day 06 Notes: Collections (List, Tuple, Set, Dictionary)

Python me collections ka use multiple values ko ek structure me store karne ke liye hota hai.
Aaj hum 4 core collection types cover kar rahe hain:
- List
- Tuple
- Set
- Dictionary

---

## 1. List
List ordered hoti hai, mutable hoti hai, aur duplicate values allow karti hai.

```python
fruits = ["apple", "banana", "mango"]
print(fruits[0])      # apple
print(fruits[-1])     # mango
print(fruits[0:2])    # ['apple', 'banana']

fruits.append("orange")
fruits[1] = "grapes"
```

Use list jab data ko change karna ho.

---

## 2. Tuple
Tuple ordered hoti hai lekin immutable hoti hai.

```python
colors = ("red", "green", "blue")
print(colors[1])

single = (5,)  # single value tuple
```

Tuple me item update nahi hota.

Use tuple jab fixed data store karna ho.

---

## 3. Set
Set unordered hoti hai, duplicates remove karti hai, aur mutable hoti hai.

```python
nums = {1, 2, 2, 3}
print(nums)  # {1, 2, 3}

set_a = {1, 2, 3}
set_b = {3, 4, 5}

print(set_a | set_b)  # union
print(set_a & set_b)  # intersection
print(set_a - set_b)  # difference
```

Use set jab unique values chahiye hon.

---

## 4. Dictionary
Dictionary key-value pairs me data store karti hai. Keys unique hoti hain.

```python
student = {
    "name": "Hammad",
    "age": 20,
}

print(student["name"])
student["city"] = "Lahore"
student["age"] = 21
```

Use dictionary jab labeled data store karna ho.

---

## 5. Important Difference (Quick View)

| Type | Ordered | Mutable | Duplicates | Syntax |
|---|---|---|---|---|
| List | ✅ Yes | ✅ Yes | ✅ Yes | `[]` |
| Tuple | ✅ Yes | ❌ No | ✅ Yes | `()` |
| Set | ❌ No | ✅ Yes | ❌ No | `{}` |
| Dictionary | ✅ Yes* | ✅ Yes | Keys ❌ / Values ✅ | `{key: value}` |


a* Python 3.7+ me dictionary insertion order preserve karti hai.

---

## 6. Common Methods

### List Methods
- `append()`
- `insert()`
- `remove()`
- `pop()`
- `sort()`

### Set Methods
- `add()`
- `remove()`
- `discard()`
- `union()`
- `intersection()`

### Dictionary Methods
- `get()`
- `keys()`
- `values()`
- `items()`
- `pop()`

---

## 7. Day 06 Practice Goals
Aaj ka focus yeh hai:

1. List indexing, slicing aur methods practice karo
2. Tuple immutability concept clear karo
3. Set operations (union/intersection/difference) solve karo
4. Dictionary key-value update aur access practice karo
5. Nested dictionary ko read karna seekho
6. Minimum 8-10 practical tasks run karo

---

## 8. Quick Summary
- List = ordered, mutable
- Tuple = ordered, immutable
- Set = unique items, unordered
- Dictionary = key-value structure

In 4 collections ko achi tarah samajh lena Python development ke liye bohat important hai.
