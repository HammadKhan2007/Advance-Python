# 📝 Day 08 Notes: File Handling & Exception Handling

## 1. File Handling Modes
Python mein `open(filename, mode)` use hota hai:

| Mode | Name | Description |
|:---:|:---|:---|
| `'r'` | Read | File read karne ke liye (File ka hona lazmi hai, warna `FileNotFoundError` aata hai). |
| `'w'` | Write | Nayi file banata hai ya purani file ka data overwrite kar deta hai. |
| `'a'` | Append | Purani file ke aakhir mein naya data add karta hai (overwrite nahi karta). |
| `'r+'`| Read & Write | Dono operations ek sath karne ke liye. |

## 2. Why use the `with` statement?
`with open(...) as f:` use karne se file automatically close ho jati hai, chahe code ke dauran koi error hi kyun na aa jaye. File close karna memory aur OS lock issues se bachata hai.

## 3. Working with JSON
- JSON (JavaScript Object Notation) structured data store aur exchange karne ka standard format hai.
- **`json.dump(obj, file)`**: Python dictionary ko direct JSON file mein save karta hai.
- **`json.load(file)`**: JSON file se data read kar ke Python dictionary banata hai.
- **`json.dumps(obj)`**: Dictionary ko JSON string banata hai.
- **`json.loads(string)`**: JSON string ko dictionary banata hai.

## 4. Exception Handling Structure
```python
try:
    # Wo code jahan error aane ka chance ho
    result = 10 / 0
except ZeroDivisionError as e:
    # Error aane par yeh block chalega
    print("Cannot divide by zero!")
else:
    # Agar try mein koi error NA aaye to yeh chalega
    print("Execution successful!")
finally:
    # Yeh block HAMESHA chalega (cleanup ke liye)
    print("Execution complete.")
```

## 5. Common Python Exceptions
- **`FileNotFoundError`**: Jab file disk par maujood na ho.
- **`ZeroDivisionError`**: Kisi number ko 0 se divide karne par.
- **`ValueError`**: Galat data type convert karne par (e.g. `int("abc")`).
- **`KeyError`**: Dictionary mein non-existent key access karne par.
- **`IndexError`**: List ki limit se bahar index access karne par.
