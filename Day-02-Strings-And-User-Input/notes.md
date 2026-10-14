# 📝 Day 02 Notes: Strings Manipulation & User Input

## 1. Strings Indexing & Slicing
- **Indexing**: String ke har character ka ek index number hota hai jo `0` se start hota hai.
  - Positive index: `0, 1, 2, ...` (Left to Right)
  - Negative index: `-1, -2, -3, ...` (Right to Left)
- **Slicing Syntax**: `string[start:stop:step]`
  - `start`: Jahan se shuru karna hai (inclusive).
  - `stop`: Jahan tak jana hai (yeh index include nahi hota).
  - `step`: Kitne steps ka jump lena hai.
  - Reversing a string trick: `string[::-1]`

## 2. Key String Methods
- `.upper()` / `.lower()`: Case conversion.
- `.strip()`: Shuru aur aakhir ke faltu spaces hatata hai.
- `.replace(old, new)`: Text ke kisi hisse ko tabdeel karta hai.
- `.split(separator)`: String ko list mein convert karta hai.
- `.join(iterable)`: List ke items ko string mein jodta hai.
- `.startswith()` / `.endswith()`: Boolean check return karta hai (`True`/`False`).

## 3. Modern f-strings (Formatted String Literals)
- String ke shuru mein `f` lagaya jata hai: `f"Hello, {name}"`
- Curly brackets `{}` ke andar Python expressions aur variables likhe ja sakte hain.
- Float formatting: `{price:.2f}` (2 decimal places tak round karta hai).
- Number comma formatting: `{1000000:,}` -> `1,000,000`.

## 4. User Input (`input()`)
- `input()` user se terminal par value leta hai.
- **Hamesha string return karta hai**, chahe user number hi kyun na type kare.
- Number operations ke liye type casting lazmi hai:
  - `int(input("Enter number: "))`
  - `float(input("Enter price: "))`
